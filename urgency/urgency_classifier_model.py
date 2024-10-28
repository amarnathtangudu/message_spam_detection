import os

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
from constants import models_folder_path


def train_urgency_classifier():
    os.makedirs(models_folder_path, exist_ok=True)
    # Load data from CSV
    df = pd.read_csv("datasets/urgency_dataset.csv")

    # Separate features and labels
    texts = df["text"].values
    labels = df["label"].values  # Assuming 1 for urgent, 0 for non-urgent

    # Vectorize text data
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, labels, test_size=0.2, random_state=42
    )

    # Train the classifier
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)

    # Evaluate the classifier
    y_pred = classifier.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save the classifier and vectorizer to a .pkl file
    with open(os.path.join(models_folder_path,"urgency_classifier_model.pkl"), "wb") as file:
        pickle.dump({"classifier": classifier, "vectorizer": vectorizer}, file)

    print("Model and vectorizer saved to 'urgency_classifier_model.pkl'.")
