from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load preprocessed data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))              # Pivot table for similarity
books = pickle.load(open('books.pkl', 'rb'))        # Full book details
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))  # Precomputed similarity

@app.route('/')
def index():
    popular_df['avg_rating'] = popular_df['avg_rating'].round(2)

    return render_template(
        'home.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=list(popular_df['avg_rating'].values)
    )

@app.route('/recommend', methods=['GET', 'POST'])
def recommend_ui():
    recommended_books = []
    query = None

    if request.method == 'POST':
        query = request.form.get('user_input')

        if query in pt.index:
            index = pt.index.get_loc(query)
            sim_scores = list(enumerate(similarity_scores[index]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]  # top 5

            for i in sim_scores:
                book_title = pt.index[i[0]]
                temp_df = books[books['Book-Title'] == book_title].iloc[0]
                recommended_books.append({
                    'title': temp_df['Book-Title'],
                    'author': temp_df['Book-Author'],
                    'image': temp_df['Image-URL-M'],
                })
        else:
            recommended_books = None

    return render_template(
        'recommend.html',
        query=query,
        recommended_books=recommended_books
    )

if __name__ == '__main__':
    app.run(debug=True)
