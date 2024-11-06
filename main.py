from prior_activy_promotion.prior_activy import classify_prior_activity
from req_to_update_info.update_info import classify_update_info
from urgency.urgency import get_urgency_classification
from threatening.threatening import get_threatening_classification
from requesting_personal_information.rpi import get_rpi_classification
from gift_card.gift_card import gf_classify
from requesting_money.rm_classifier import rm_classify

message = "Get a free gift card with your purchase."

get_urgency_classification(message)
get_threatening_classification(message)
get_rpi_classification(message)
gf_classify(message)
rm_classify(message)
classify_update_info(message)
classify_prior_activity(message)