import pandas as pd

# Messages indicating an offer for a gift card
gift_card_offers = [
    "Claim your $50 gift card now!",
    "Congratulations! You've won a $100 gift card.",
    "Get a free gift card with your next purchase.",
    "Earn a gift card by taking our survey.",
    "Use this code to redeem your $25 gift card.",
    "Receive a gift card as a thank-you for your feedback.",
    "Special offer: Free gift card for first-time users.",
    "Complete this task and earn a $10 gift card.",
    "Enjoy a $20 gift card on us!",
    "Limited time only: Gift card with every purchase.",
    # Add more messages offering gift cards...
] * 10  # Repeat to create 100 examples

# Messages not related to gift cards
non_gift_card_messages = [
    "Have a nice day!",
    "Your order has been shipped.",
    "Don't forget to submit your report by Monday.",
    "Thank you for your feedback!",
    "Reminder: Meeting is scheduled for tomorrow.",
    "Your account has been updated successfully.",
    "Enjoy our special discounts on selected items.",
    "Congratulations on completing the program!",
    "We hope you enjoy your purchase.",
    "Please contact customer support if you need assistance.",
    # Add more general messages...
] * 10  # Repeat to create 100 examples

# Combine and create a DataFrame
data = {
    "message": gift_card_offers + non_gift_card_messages,
    "label": [1] * len(gift_card_offers) + [0] * len(non_gift_card_messages),
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("gift_card_offers.csv", index=False)
print("Dataset saved as 'gift_card_offers.csv'.")
