import streamlit as st
import pickle

from get_prediction import get_classification

# Load the trained model
with open("random_forest_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)


# Predict function
def predict_message(message):
    features = get_classification(message)
    prediction = loaded_model.predict([features])[0]
    return prediction

# Streamlit App Interface
st.title("Spam Classification Demo")
st.write("Enter a message to classify it as Spam or Ham.")

# Input
user_input = st.text_area("Message", placeholder="Type your message here...")

# Predict and Display
if st.button("Classify"):
    if user_input.strip():
        prediction = predict_message(user_input)
        label = "Spam" if prediction == "spam" else "Ham"
        st.write(f"The message is classified as: **{label}**")
    else:
        st.error("Please enter a valid message!")
