import pandas as pd
from spellchecker import SpellChecker
import language_tool_python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
from sklearn.feature_extraction.text import TfidfVectorizer

import pickle

# Load Dataset
path = r"C:\Users\Sumit\Downloads\archive (3)\spam.csv"
df = pd.read_csv(path, encoding="latin-1")
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Convert labels to binary
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Initialize Tools
spell = SpellChecker()
tool = language_tool_python.LanguageTool('en-US')

# Feature Extraction Function
def extract_features(text):
    grammar_errors = len(tool.check(text))
    misspelled_words = sum(1 for word in text.split() if word.lower() not in spell)
    exclamation_count = text.count("!")
    capitalized_count = sum(1 for word in text.split() if word.isupper())
    spammy_keywords = sum(1 for word in ["free", "click", "win", "offer", "money", "act now"] if word in text.lower())
    unusual_phrasing = sum(1 for phrase in ["call us now", "hurry up", "exclusive deal"] if phrase in text.lower())
    repetitive_words = len(set(text.split())) / len(text.split()) if len(text.split()) > 0 else 1
    vague_language = 1 if len(text.split()) <= 3 else 0
    jargon_count = sum(1 for word in text.split() if len(word) > 12)
    inconsistent_tense = sum(1 for word in ["is", "was", "are", "were", "has", "had", "will", "would"] if word in text.lower())
    url_count = text.count("http") + text.count("www")
    number_count = sum(c.isdigit() for c in text)
    
    return {
        "grammar_errors": grammar_errors,
        "misspelled_words": misspelled_words,
        "exclamation_count": exclamation_count,
        "capitalized_count": capitalized_count,
        "spammy_keywords": spammy_keywords,
        "unusual_phrasing": unusual_phrasing,
        "repetitive_words_ratio": repetitive_words,
        "vague_language": vague_language,
        "jargon_count": jargon_count,
        "inconsistent_tense": inconsistent_tense,
        "url_count": url_count,
        "number_count": number_count
    }

# Apply feature extraction to all messages
features = df['message'].apply(extract_features)
features_df = pd.DataFrame(features.tolist())

# Combine features with the original data
data = pd.concat([df, features_df], axis=1)

# Text Preprocessing and TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_tfidf = vectorizer.fit_transform(df['message'])

# Combine TF-IDF features with other extracted features
X = pd.concat([features_df, pd.DataFrame(X_tfidf.toarray())], axis=1)
y = data['label']

# Ensure all column names in X are strings
X.columns = X.columns.astype(str)

# Step 1: Handle class imbalance using SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Step 2: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

# Step 3: Hyperparameter Tuning with GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
}
grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42), param_grid=param_grid, cv=3, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Get best model
best_model = grid_search.best_estimator_

# Step 4: Evaluate Model
y_pred = best_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the best model to a file using pickle
with open('spam_classifier_model_newtraining.pkl', 'wb') as model_file:
    pickle.dump(best_model, model_file)

print("Model saved successfully.")