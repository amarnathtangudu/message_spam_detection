import pandas as pd

# Messages indicating a request for a money transfer
money_request_messages = [
    "Please transfer $500 to complete your purchase.",
    "Send the payment via bank transfer as soon as possible.",
    "Can you wire me the money today?",
    "I need $200 by the end of the day. Please transfer it to my account.",
    "Make sure to send the funds before the deadline.",
    "Transfer the money for the bill to my account.",
    "Please send the requested amount at your earliest convenience.",
    "You can transfer the amount using the provided bank details.",
    "Transfer the money by tomorrow.",
    "A wire transfer is required for processing your request.",
    # Add more messages requesting money...
] * 10  # Repeat to create 100 examples

# Messages not related to money requests
non_money_request_messages = [
    "Thank you for your response.",
    "Your package is on its way!",
    "Looking forward to our meeting tomorrow.",
    "Please complete the form at your convenience.",
    "Your account has been successfully updated.",
    "Happy birthday! Hope you have a wonderful day.",
    "Let’s discuss the project timeline in detail.",
    "Our team will contact you with more information.",
    "The event starts at 6 PM.",
    "Please call us if you have any questions.",
    # Add more general messages...
] * 10  # Repeat to create 100 examples

# Combine and create a DataFrame
data = {
    "message": money_request_messages + non_money_request_messages,
    "label": [1] * len(money_request_messages) + [0] * len(non_money_request_messages),
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("money_request_messages.csv", index=False)
print("Dataset saved as 'money_request_messages.csv'.")
