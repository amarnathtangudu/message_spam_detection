import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def gf_classify(message):
    # Load the model and vectorizer
    with open("models/gift_card_classifier_model.pkl", "rb") as file:
        loaded_data = pickle.load(file)

    loaded_classifier = loaded_data["classifier"]
    loaded_vectorizer = loaded_data["vectorizer"]

    # Example test messages
    # test_messages = [
    #     "Claim your $100 gift card now!",
    #     "Your order is on the way.",
    #     "Congratulations! You have won a $50 gift card.",
    #     "Please remember to attend the meeting tomorrow.",
    #     "Get a free gift card with your purchase.",
    # ]
    test_messages = [message]

    # Vectorize the test messages
    test_vectorized = loaded_vectorizer.transform(test_messages)

    # Predict and get confidence scores
    predictions = loaded_classifier.predict(test_vectorized)
    confidence_scores = loaded_classifier.predict_proba(test_vectorized)

    # Print results with confidence scores
    for message, prediction, confidence in zip(
        test_messages, predictions, confidence_scores
    ):
        label = "Gift Card Offer" if prediction == 1 else "Not a Gift Card Offer"
        confidence_score = max(confidence)  # Get the confidence for the predicted class
        print(
            f"Message: {message}\nPredicted Label: {label}\nConfidence Score: {confidence_score:.2f}\n"
        )
