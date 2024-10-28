from urgency.urgency import get_urgency_classification
from threatening.threatening import get_threatening_classification

message = "Final notice: Complete the survey within 24 hours."

get_urgency_classification(message)
get_threatening_classification(message)