import pandas as pd

# Messages indicating promotional offers based on prior shopping or activity
promotional_messages = [
    "Get 20% off on your next purchase based on your recent order.",
    "We have special offers for items you previously viewed!",
    "Thanks for shopping with us! Here’s a discount code for your next purchase.",
    "Exclusive deal just for you! Buy 2, get 1 free on your favorite products.",
    "Your recent shopping activity qualifies you for a special discount.",
    "Flash sale on items similar to those you've bought before.",
    "Unlock 10% off your next purchase with this code.",
    "Don’t miss out on special deals on items related to your last purchase.",
    "We’ve noticed you liked these items. Here’s a limited-time offer!",
    "Exclusive offer on products you recently browsed.",
    # Add more messages similar to promotional messages...
] * 10  # Repeat to create 100 examples

# Messages not related to promotions
non_promotional_messages = [
    "Please find attached your recent invoice.",
    "Looking forward to our meeting tomorrow.",
    "Your package has been dispatched and is on the way.",
    "Reminder: Don’t forget to submit your timesheet.",
    "Thank you for reaching out to customer support.",
    "Your account has been updated as per your request.",
    "The event starts at 5 PM; let us know if you have questions.",
    "Hope you’re doing well. Please let us know if we can help.",
    "We have received your feedback. Thank you!",
    "Your subscription renewal is confirmed.",
    # Add more general messages...
] * 10  # Repeat to create 100 examples

# Combine and create a DataFrame
data = {
    "message": promotional_messages + non_promotional_messages,
    "label": [1] * len(promotional_messages) + [0] * len(non_promotional_messages)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("promotional_messages.csv", index=False)
print("Dataset saved as 'promotional_messages.csv'.")
