
# 📰 Fake News Detection System

## 📌 Overview
In today’s digital world, misinformation spreads very quickly. This project aims to detect whether a news article is real or fake using Machine Learning techniques in Python.

The system takes news text as input and predicts whether it is REAL 🟢 or FAKE 🔴.


## 🎯 Objective
The objective of this project is to build a simple and effective model that can identify fake news using Natural Language Processing (NLP).


## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression


## 📚 References
- Kaggle Fake News Dataset  
- Scikit-learn Documentation  
- Pandas Documentation

## 📂 Dataset
The dataset used in this project is taken from Kaggle:

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

⚠️ Note: Due to file size limitations on GitHub, the dataset is not included in this repositor.
This project uses two datasets:
- Fake.csv → contains fake news articles
- True.csv → contains real news articles


## ⚙️ How It Works
1. Load datasets
2. Add labels (Fake = 0, Real = 1)
3. Combine and shuffle data
4. Convert text into numerical form using TF-IDF
5. Train model using Logistic Regression
6. Predict output based on user input


## ▶️ How to Run
1. Download the dataset from the link above
2.	Extract the files
3.	Place Fake.csv and True.csv in the same folder as main.py
4. Download repository 
5. Open terminal in the project folder  
6. Install dependencies:
   pip install -r requirements.txt
7. Run the program:
   python main.py
8. Enter any news text  
9. The system will predict whether it is REAL or FAKE


## 📊 Output Example

Input:
"Scientists confirm aliens landed in India"

Output:
🔴 This news is likely FAKE


## 🚀 Future Improvements
- Use advanced models like LSTM or BERT
- Improve accuracy with better datasets
- Build a web interface


## 🙋‍♀️ Author
This project was created as part of the BYOP submission.

## 📄 Project Report
The detailed project report is available in this repository as `Project_Report.docx`.