import pandas as pd

from prior_activy_promotion.prior_activy import classify_prior_activity
from req_to_update_info.update_info import classify_update_info
from urgency.urgency import get_urgency_classification
from threatening.threatening import get_threatening_classification
from requesting_personal_information.rpi import get_rpi_classification
from gift_card.gift_card import gf_classify
from requesting_money.rm_classifier import rm_classify

# message = "Get a free gift card with your purchase."

def get_classification(message):
    urgency_result = get_urgency_classification(message)
    threatening_result = get_threatening_classification(message)
    requesting_personal_information_result = get_rpi_classification(message)
    gift_card_offer_result = gf_classify(message)
    requesting_money_result = rm_classify(message)
    update_bill_result = classify_update_info(message)
    prior_activity_result = classify_prior_activity(message)
    result = {
        "urgency_result": urgency_result,
        "threatening_result": threatening_result,
        "requesting_personal_information_result": requesting_personal_information_result,
        "gift_card_offer_result": gift_card_offer_result,
        "requesting_money_result": requesting_money_result,
        "update_bill_result": update_bill_result,
        "prior_activity_result": prior_activity_result
    }
    return result


# Read the CSV file
# input_file = 'spam.csv'  # Replace with your actual file path
# output_file = 'updated_messages.csv'
#
# df = pd.read_csv(input_file)
#
# # Process each message to add prediction results
# for index, row in df.iterrows():
#     message = row['Message']  # Adjust column name if different
#     predictions = get_classification(message)
#     for key, value in predictions.items():
#         label_column = f"{key}_label"
#         score_column = f"{key}_score"
#         df.at[index, label_column] = value['Predicted label']
#         df.at[index, score_column] = value['Confidence score']
#
# # Save the updated data to a new CSV file
# df.to_csv(output_file, index=False)

