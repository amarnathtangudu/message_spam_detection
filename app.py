import streamlit as st
import pickle
import numpy as np

from get_prediction import get_classification


def preprocess_prediction_data(predictions_dict):
    """
    Convert the predictions dictionary into a list of features for the model.
    """
    features = []
    for key in [
        "urgency_result", "threatening_result",
        "requesting_personal_information_result", "gift_card_offer_result",
        "requesting_money_result", "update_bill_result",
        "prior_activity_result"
    ]:
        label = float(predictions_dict[key]["Predicted label"])
        score = float(predictions_dict[key]["Confidence score"])
        features.extend([label, score])
    return np.array(features).reshape(1, -1)


def predict_spam(message, predictions_dict, model):
    """
    Predict whether the message is spam or ham based on predictions.
    """
    # Preprocess the data
    input_features = preprocess_prediction_data(predictions_dict)

    # Predict using the model
    prediction = model.predict(input_features)
    confidence = max(model.predict_proba(input_features)[0])

    return ("spam" if prediction[0] == 1 else "ham", confidence)


def format_positive_predictions(predictions_dict):
    """
    Format the positive predictions (where label is True/1.0) into a useful message.
    """
    messages = []
    for key, value in predictions_dict.items():
        if value["Predicted label"] in [True, 1.0]:
            messages.append(f"{key.replace('_', ' ').title()}: Confidence Score: {value['Confidence score']}")
    return messages


# Load the trained Random Forest model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app UI
st.title("Spam Message Classifier")
st.write("This app classifies a message as Spam or Ham based on its content.")

# Input text box for the message
message = st.text_area("Enter the message you want to classify:")

if st.button("Classify"):
    if message.strip():
        # Generate predictions dictionary
        predictions_dict = get_classification(message)

        # Format and display positive predictions
        positive_predictions = format_positive_predictions(predictions_dict)

        if positive_predictions:
            st.subheader("Key Indicators (Positive Predictions):")
            for msg in positive_predictions:
                st.write(f"- {msg}")
        else:
            st.write("No significant indicators found.")

        # Classify the message
        result, confidence = predict_spam(message, predictions_dict, model)

        # Display the result
        st.subheader("Classification Result:")
        st.write(f"The message is classified as: **{result.upper()}**")
        st.write(f"Confidence Score: **{confidence:.2f}**")
    else:
        st.warning("Please enter a message to classify.")
