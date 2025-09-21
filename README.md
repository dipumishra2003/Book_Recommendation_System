# 📚 Book Recommendation System

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/) 
[![Flask](https://img.shields.io/badge/Flask-2.3-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-red)](LICENSE)

---

## 🌟 Overview
Welcome to **Book Recommendation System**, an intelligent platform that helps users discover new books based on their favorite reads. Powered by **Python**, **Machine Learning**, and **Flask**, this app provides personalized recommendations with a sleek **dark-themed UI**.  

**Features:**
- Top 50 trending books displayed on the homepage 🏆  
- Personalized book recommendations based on user input 🔍  
- Fully responsive, modern dark-themed UI 🌑  
- Powered by a pre-trained similarity model using **Pickle files** 🧠  

---

## 🛠 Technologies Used
- Python 3.10  
- Flask Web Framework  
- Pandas & NumPy for data handling  
- Pickle for pre-trained models  
- Bootstrap 5 for UI design  

---

## 🚀 Demo
You can see the app in action:

**Home Page:**  
![Home Page](screenshots/home_page.png)  

**Recommendation Page:**  
![Recommendation Page](screenshots/recommend_page.png)  

---

## ⚡ How to Run Locally
1. **Clone the repository**
```
git clone https://github.com/yourusername/Book_Recommendation_System.git
cd Book_Recommendation_System
```

Create a virtual environment
```
python -m venv .venv
```

Activate the virtual environment

Windows:
```
.venv\Scripts\activate
```

macOS/Linux:
```
source .venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

Run the Flask app
```
python app.py
```

Open http://127.0.0.1:5000 in your browser.

.

📂 Repository Structure
```
Book_Recommendation_System/
│
├─ app.py               # Flask application
├─ popular.pkl          # Preprocessed top books data
├─ pt.pkl               # Pivot table for recommendations
├─ books.pkl            # Books metadata
├─ similarity_scores.pkl# Precomputed similarity matrix
├─ templates/           # HTML templates
│   ├─ home.html
│   └─ recommend.html
├─ static/              # CSS, images (optional)
├─ requirements.txt
└─ README.md
```

💡 Future Improvements

Add user login system for personalized profiles

Integrate real-time ratings from external APIs

Use Deep Learning models for better recommendation accuracy

Add pagination and search filters for books

❤️ Author

Dipu Mishra – Passionate about AI/ML and building helpful applications.
Feel free to connect: https://www.linkedin.com/in/dipu-mishra
