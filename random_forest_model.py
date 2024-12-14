import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

# Load the dataset
data_file = 'updated_messages.csv'
df = pd.read_csv(data_file)

# Preprocess the data
df['Label'] = df['Label'].map({'spam': 1, 'ham': 0})  # Convert labels to binary
features = df.drop(columns=['Label', 'Message'])  # Drop non-feature columns
target = df['Label']

# Ensure all features are numeric
features = features.apply(pd.to_numeric, errors='coerce')

# Handle any missing values
features.fillna(0, inplace=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Evaluate the model
y_pred = rf_model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model to a pickle file
model_file = 'random_forest_model.pkl'
with open(model_file, 'wb') as file:
    pickle.dump(rf_model, file)

print(f"Model saved to {model_file}")
