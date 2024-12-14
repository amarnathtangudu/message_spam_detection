from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle

# Load the CSV file
data = pd.read_csv('updated_messages.csv')

# Select features and target
feature_columns = [
    "urgency_result_label", "urgency_result_score",
    "threatening_result_label", "threatening_result_score",
    "requesting_personal_information_result_label", "requesting_personal_information_result_score",
    "gift_card_offer_result_label", "gift_card_offer_result_score",
    "requesting_money_result_label", "requesting_money_result_score",
    "update_bill_result_label", "update_bill_result_score",
    "prior_activity_result_label", "prior_activity_result_score",
]
X = data[feature_columns]
y = data["Label"].map({"ham": 0, "spam": 1})  # Encode labels as 0/1

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the trained model to a file
with open('random_forest_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as random_forest_model.pkl")
