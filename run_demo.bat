@echo off
REM Detect if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3 and try again.
    exit /b 1
)

REM Create a virtual environment
echo Creating a virtual environment...
python -m venv env
if %errorlevel% neq 0 (
    echo Failed to create the virtual environment. Exiting...
    exit /b 1
)

REM Activate the virtual environment
echo Activating the virtual environment...
call env\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate the virtual environment. Exiting...
    exit /b 1
)

REM Check for requirements.txt
if not exist requirements.txt (
    echo requirements.txt not found. Please provide a valid requirements file.
    deactivate
    exit /b 1
)

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install required packages. Exiting...
    deactivate
    exit /b 1
)

REM Check for app.py
if not exist app.py (
    echo app.py not found. Please ensure the Streamlit app file exists.
    deactivate
    exit /b 1
)

REM Run the Streamlit app
echo Starting the Streamlit app...
start cmd /k "streamlit run app.py"

REM Wait for a few seconds to ensure the app starts
timeout /t 3 >nul

REM Open the browser to the Streamlit app
start http://localhost:8501

REM Keep the command prompt open
echo The Streamlit app should now be running in your browser.
echo Press any key to close this window...
pause
