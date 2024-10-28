import pandas as pd
import random

# Base phrases for urgent messages
urgent_phrases = [
    "Your account will be suspended immediately if you do not respond.",
    "Urgent: Action required immediately to avoid penalty.",
    "Final notice: Complete the survey within 24 hours.",
    "Please submit the payment as soon as possible to avoid late fees.",
    "Immediate action needed: Update your information.",
    "Act now to secure your spot; only limited spaces available.",
    "Critical alert: Unauthorized login attempt detected.",
    "Immediate action required to verify your account details.",
    "Final reminder: This is your last chance to respond.",
    "Respond within 24 hours to prevent account deactivation.",
]

# Base phrases for non-urgent messages
non_urgent_phrases = [
    "Hello, just checking in to see how you're doing.",
    "Please find attached the report you requested.",
    "Let me know if you have any questions.",
    "Thank you for your purchase. We hope to serve you again.",
    "Here is the information you requested. Take your time to review.",
    "Thank you for your interest; feel free to reach out anytime.",
    "Hope you had a great weekend! Let us know if you need help.",
    "Looking forward to your feedback whenever convenient.",
    "We’re here to help. No rush to get back to us!",
    "Your order has been shipped and will arrive shortly.",
]


# Function to create variations for diversity
def generate_variations(base_phrases, count):
    data = []
    for _ in range(count):
        phrase = random.choice(base_phrases)

        # Add simple variations
        if "within" in phrase:
            phrase = phrase.replace("within", f"within {random.randint(12, 48)} hours")
        if "immediate" in phrase:
            phrase = phrase.replace(
                "immediate", random.choice(["immediate", "urgent", "critical"])
            )
        if "respond" in phrase:
            phrase = phrase.replace(
                "respond", random.choice(["reply", "get back", "respond"])
            )

        data.append(phrase)
    return data


# Generate 500 urgent and 500 non-urgent samples
urgent_messages = generate_variations(urgent_phrases, 500)
non_urgent_messages = generate_variations(non_urgent_phrases, 500)

# Create DataFrame
data = pd.DataFrame(
    {
        "text": urgent_messages + non_urgent_messages,
        "label": [1] * 500 + [0] * 500,  # 1 = Urgent, 0 = Non-Urgent
    }
)

# Save to CSV
data.to_csv("urgency_dataset.csv", index=False)
print("Urgency dataset created with 500 urgent and 500 non-urgent messages.")
