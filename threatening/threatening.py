import pickle
from constants import models_folder_path
import os

def get_threatening_classification(message):
    # Load the model and vectorizer
    with open(os.path.join(models_folder_path, "threat_classifier_model.pkl"), "rb") as file:
        loaded_data = pickle.load(file)

    loaded_classifier = loaded_data["classifier"]
    loaded_vectorizer = loaded_data["vectorizer"]

    # # Example test messages for prediction
    # test_messages = [
    #     "If you don't pay by tomorrow, there will be consequences.",
    #     "Please provide your response when you are ready.",
    #     "Failure to submit the documents will lead to legal actions.",
    # ]

    # Predict and display results for each test message
    # for message in test_messages:
    test_vectorized = loaded_vectorizer.transform([message])
    prediction = loaded_classifier.predict(test_vectorized)
    confidence_scores = loaded_classifier.predict_proba(test_vectorized)

    # Get confidence score for the predicted class
    predicted_label = prediction[0] == 1
    confidence_score = confidence_scores[0][prediction[0]]

    result = {
        "Predicted label": predicted_label,
        "Confidence score": f"{confidence_score:.2f}"
    }
    return result
