import pandas as pd

# Messages indicating an update request for bills
bill_update_requests = [
    "Please update your bank details for billing purposes.",
    "Kindly update your payment information for the electricity bill.",
    "Update required: Telephone bill needs new payment method.",
    "Please ensure your gas bill information is up to date.",
    "Your banking details for the monthly bill are outdated. Please update.",
    "Reminder: Update your payment info to avoid late fees.",
    "Please provide your latest bank details for billing.",
    "Your telephone bill account needs updated details.",
    "Urgent: Update your payment information for utility bills.",
    "Update your bank account details for direct billing.",
    # Add more messages requesting bill updates...
] * 10  # Repeat to create 100 examples

# Messages not related to bill updates
non_bill_update_requests = [
    "Meeting has been rescheduled to tomorrow.",
    "Your order has been shipped successfully.",
    "Reminder: Submit your timesheet by Friday.",
    "Your package is ready for pickup.",
    "No action is required on your part.",
    "Enjoy our latest offers on selected products.",
    "Looking forward to seeing you at the event.",
    "Let us know if you have any questions.",
    "Your account has been updated as requested.",
    "Thank you for being a valued customer.",
    # Add more general messages...
] * 10  # Repeat to create 100 examples

# Combine and create a DataFrame
data = {
    "message": bill_update_requests + non_bill_update_requests,
    "label": [1] * len(bill_update_requests) + [0] * len(non_bill_update_requests)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("bill_update_requests.csv", index=False)
print("Dataset saved as 'bill_update_requests.csv'.")
