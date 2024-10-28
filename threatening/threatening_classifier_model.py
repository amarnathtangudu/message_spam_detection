import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from constants import models_folder_path


def train_threatening_classifier():
    os.makedirs(models_folder_path, exist_ok=True)
    # Load data from CSV file
    df = pd.read_csv("datasets/threatening_messages_test_data.csv")

    # Separate the data into texts and labels
    texts = df["message"].values
    labels = df["label"].values

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    X_train, X_test, y_train, y_test = train_test_split(
        X, labels, test_size=0.2, random_state=42
    )

    # Train the Logistic Regression classifier
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)

    # Evaluate the classifier
    y_pred = classifier.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save the model and vectorizer to a pickle file
    import pickle

    with open(os.path.join(models_folder_path,"threat_classifier_model.pkl"), "wb") as file:
        pickle.dump({"classifier": classifier, "vectorizer": vectorizer}, file)
    print("Model saved as 'threat_classifier_model.pkl'.")
