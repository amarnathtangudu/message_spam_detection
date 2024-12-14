import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def rm_classify(message):
    # Load the model and vectorizer
    with open("models/money_request_classifier_model.pkl", "rb") as file:
        loaded_data = pickle.load(file)

    loaded_classifier = loaded_data["classifier"]
    loaded_vectorizer = loaded_data["vectorizer"]

    # Example test messages
    # test_messages = [
    #     "Please transfer the amount by tomorrow.",
    #     "Hope you're doing well!",
    #     "Send the payment via bank transfer.",
    #     "Let's catch up later this week.",
    #     "I need the funds for the project as soon as possible.",
    # ]
    test_messages = [message]

    # Vectorize the test messages
    test_vectorized = loaded_vectorizer.transform(test_messages)

    # Predict and get confidence scores
    predictions = loaded_classifier.predict(test_vectorized)
    confidence_scores = loaded_classifier.predict_proba(test_vectorized)
    label = ""
    confidence_score = 0
    # Print results with confidence scores
    for message, prediction, confidence in zip(
        test_messages, predictions, confidence_scores
    ):
        label = prediction == 1
        confidence_score = max(confidence)  # Get the confidence for the predicted class

    result = {
        "Predicted label": label,
        "Confidence score": f"{confidence_score:.2f}"
    }
    return result