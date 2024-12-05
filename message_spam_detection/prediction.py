import pickle
from spellchecker import SpellChecker
import language_tool_python
import pandas as pd

# Load the trained model
with open('spam_classifier_model_newtraining.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the TF-IDF vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Initialize tools
spell = SpellChecker()
tool = language_tool_python.LanguageTool('en-US')

# Feature extraction function
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
    number_count = sum(c.isdigit() for c in text)  # Add this back
    
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

# Predict function
def predict_spam(message):
    # Extract features
    extracted_features = extract_features(message)
    features_df = pd.DataFrame([extracted_features])

    # Transform message using the saved TF-IDF vectorizer
    tfidf_features = vectorizer.transform([message]).toarray()

    # Combine extracted features and TF-IDF features
    combined_features = pd.concat(
        [features_df, pd.DataFrame(tfidf_features)], axis=1
    )

    # Ensure all column names are strings
    combined_features.columns = combined_features.columns.astype(str)

    # Make prediction
    prediction = model.predict(combined_features)
    return "Spam" if prediction[0] == 1 else "Not Spam"


# Test Message
test_message = "Congratulations!!! You have won $1,000,000!!!"
print("Prediction:", predict_spam(test_message))