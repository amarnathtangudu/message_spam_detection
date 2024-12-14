#!/bin/bash

# Function to detect operating system
detect_os() {
    case "$(uname -s)" in
        Linux*)     os="Linux";;
        Darwin*)    os="Mac";;
        CYGWIN*|MINGW*|MSYS*) os="Windows";;
        *)          os="Unknown";;
    esac
    echo $os
}

# Step 1: Detect the operating system
os=$(detect_os)
echo "Operating System detected: $os"

# Step 2: Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Step 3: Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv env

if [ $? -ne 0 ]; then
    echo "Failed to create a virtual environment. Exiting..."
    exit 1
fi

# Step 4: Activate the virtual environment
if [ "$os" == "Windows" ]; then
    source env/Scripts/activate
else
    source env/bin/activate
fi

if [ $? -ne 0 ]; then
    echo "Failed to activate the virtual environment. Exiting..."
    exit 1
fi

echo "Virtual environment activated."

# Step 5: Install required packages
if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt not found. Please provide a valid requirements file."
    deactivate
    exit 1
fi

echo "Installing required packages..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Failed to install required packages. Exiting..."
    deactivate
    exit 1
fi

echo "All packages installed successfully."

# Step 6: Run the Streamlit app
if [ ! -f "app.py" ]; then
    echo "'app.py' not found in the current directory."
    deactivate
    exit 1
fi

echo "Starting the Streamlit app..."
streamlit run app.py &

# Wait a few seconds for the app to start
sleep 3

# Step 7: Open the app in the browser
if [ "$os" == "Mac" ] || [ "$os" == "Linux" ]; then
    xdg-open "http://localhost:8501" 2>/dev/null || open "http://localhost:8501" 2>/dev/null
elif [ "$os" == "Windows" ]; then
    start "http://localhost:8501"
else
    echo "Please open your browser and navigate to http://localhost:8501"
fi

# Keep the script running until the user terminates the Streamlit process
wait
