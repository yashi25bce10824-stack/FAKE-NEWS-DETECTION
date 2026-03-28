# Fake News Detection System

# importing libraries
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# STEP 1: Check files in folder
print("Files in folder:", os.listdir())


# STEP 2: Load dataset
df_fake = pd.read_csv("Fake.csv")
df_true = pd.read_csv("True.csv")

print("Datasets loaded successfully!")


# STEP 3: Add labels
df_fake['label'] = 0   # fake
df_true['label'] = 1   # real


# STEP 4: Combine datasets
data = pd.concat([df_fake, df_true])


# STEP 5: Shuffle data
data = data.sample(frac=1).reset_index(drop=True)


# STEP 6: Create content column (title + text)
data['content'] = data['title'] + " " + data['text']


# STEP 7: Define input and output
X = data['content']
y = data['label']


# STEP 8: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# STEP 9: Convert text into numbers
vectorizer = TfidfVectorizer(stop_words='english')

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)



# STEP 10: Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model trained successfully!")


# STEP 11: Check accuracy
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))


# STEP 12: User input loop
while True:
    print("\nEnter news text (or type 'exit' to quit):")
    user_input = input()

    if user_input.lower() == "exit":
        print("Exiting program...")
        break

    # convert input
    input_vector = vectorizer.transform([user_input])

    # predict
    prediction = model.predict(input_vector)

    # output
    if prediction[0] == 1:
        print("🟢 This news is likely REAL.")
    else:
        print("🔴 This news is likely FAKE.")