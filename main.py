import pickle
import numpy as np

from get_prediction import get_classification

# Load the saved model
model_file = 'random_forest_model.pkl'
with open(model_file, 'rb') as file:
    loaded_model = pickle.load(file)

# Function to generate the feature list
def generate_features(message):
    prediction_dict = get_classification(message)
    print(prediction_dict)
    # Extract features from prediction_dict
    features = []
    for key in prediction_dict:
        # Append Predicted label and Confidence score
        features.append(float(prediction_dict[key]['Predicted label']))
        features.append(float(prediction_dict[key]['Confidence score']))

    return np.array(features).reshape(1, -1)


# Main prediction function
def predict_message(message):
    features = generate_features(message)
    print(features)
    prediction = loaded_model.predict(features)
    return 'spam' if prediction[0] == 1 else 'ham'


# Test the prediction
test_message = "07732584351 - Rodger Burns - MSG = We tried to call you re your reply to our sms for a free nokia mobile + free camcorder. Please call now 08000930705 for delivery tomorrow"
predicted_label = predict_message(test_message)
print(f"The message is predicted to be: {predicted_label}")
