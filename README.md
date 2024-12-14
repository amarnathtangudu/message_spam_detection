Here's an updated version of the `README.md` for improved clarity and flow:

```markdown
# Project Name

This project contains scripts for retraining and testing a text classification model, specifically aimed at categorizing messages based on urgency.

## Project Files

- `requirements.txt`: Specifies the Python libraries needed to run the project.
- `training.py`: Script to retrain the model with new data.
- `main.py`: Runs test cases with the trained model to evaluate message classifications.

## Getting Started

### Prerequisites

Ensure you have Python installed (version 3.7 or newer is recommended).

### Installation

1. Clone this repository to your local machine or download the files directly.

2. Open a terminal in the project directory.

3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Code

1. Open `main.py` and locate the `message` variable:

   ```python
   message = "Final notice: Complete the survey within 24 hours."
   ```

   Modify the `message` value if you'd like to test a different message.

2. Save the changes to `main.py` if you modified the `message` variable.

3. Run the script in the terminal:

   ```bash
   python get_prediction.py
   ```

4. The script will output the predicted label and confidence score for each model, for example:

   ```plaintext
   Predicted label: Urgent
   Confidence score: 0.95
   --------------------------------------------------
   Predicted label: Threatening
   Confidence score: 0.64
   --------------------------------------------------
   ```

## Modifying the Test Message

To test different messages, change the `message` variable in `main.py`, save the file, and rerun the script.

## Model Details

- The model leverages `TfidfVectorizer` and `LogisticRegression` from `scikit-learn` for text vectorization and classification.
- This setup can be extended to handle various text classification tasks or tested with multiple message types for broader applications.

## License

This project is licensed under the MIT License.
```

This version consolidates information and streamlines the instructions for clarity. Let me know if there's anything specific you'd like to add!