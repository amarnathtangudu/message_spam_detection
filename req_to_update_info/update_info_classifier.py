import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

def train_update_info_model():
    # Load dataset
    df = pd.read_csv("datasets/bill_update_requests.csv")
    texts = df["message"].values
    labels = df["label"].values  # 1 for bill update request, 0 for non-request

    # Vectorize text data
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

    # Train the classifier
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)

    # Evaluate the classifier
    y_pred = classifier.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save the classifier and vectorizer to a .pkl file in a folder
    folder_path = "models"
    os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

    with open(os.path.join(folder_path, "bill_update_classifier_model.pkl"), "wb") as file:
        pickle.dump({'classifier': classifier, 'vectorizer': vectorizer}, file)

    print(f"Model and vectorizer saved to '{folder_path}/bill_update_classifier_model.pkl'.")
