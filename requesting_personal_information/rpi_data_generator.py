import pandas as pd

# Messages requesting personal information
personal_info_requests = [
    "Please provide your social security number.",
    "We need your credit card details to process the payment.",
    "Kindly send your bank account information for verification.",
    "Enter your password to continue.",
    "Please verify your identity by providing your ID number.",
    "We need your mother's maiden name for security reasons.",
    "Provide your account PIN for validation.",
    "Confirm your personal details including date of birth and address.",
    "Send your driver's license number to complete registration.",
    "Update your billing address for account security.",
    # Add more personal information request messages...
] * 10  # Repeat to create 100 examples

# Messages not requesting personal information
non_personal_info_requests = [
    "Have a nice day!",
    "Can we reschedule the meeting to next week?",
    "The weather is great today.",
    "Your package is on the way.",
    "Don't forget to submit your project by Friday.",
    "Thank you for your purchase!",
    "Our customer support is available 24/7.",
    "This is a reminder for your upcoming appointment.",
    "Your feedback is valuable to us.",
    "Congratulations on completing the course!",
    # Add more general messages...
] * 10  # Repeat to create 100 examples

# Combine and create a DataFrame
data = {
    "message": personal_info_requests + non_personal_info_requests,
    "label": [1] * len(personal_info_requests) + [0] * len(non_personal_info_requests),
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("personal_info_requests.csv", index=False)
print("Dataset saved as 'personal_info_requests.csv'.")
