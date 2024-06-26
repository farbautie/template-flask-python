# Flask Starter Template

This is a starter template for a Flask project. It provides a basic structure and initial configurations to quickly start developing web applications with Flask.

### Getting Started

Follow these steps to get started with your project

### Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/farbautie/template-flask-python.git
```

Set Up the Virtual Environment (Optional but Recommended)
It's recommended to use a virtual environment for this project. You can create and activate a virtual environment using env

```bash
python -m venv env
source env/bin/activate
```

### Install Dependencies

Install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a .env file in the root of the project and configure the necessary environment variables for your Flask application. These are the required environment variables for the project to function:

```bash
FLASK_APP='main.py'
FLASK_ENV='development' | 'production' | 'testing'
FLASK_DEBUG=True | False
```

### Run the Application

To run the application in development mode, you can use the boot.sh script:

```bash
./boot.sh
```

This will run your Flask application in development mode using Flask's built-in server.

### Access the Application

Once the application is up and running, you can access it from your web browser at the following address:

```bash
http://localhost:8000
```

### Project Structure

-   app/: Directory containing the Flask application files.
-   env/: Directory containing the virtual environment (ignored by Git).
-   boot.sh: Startup script to run the application.
-   requirements.txt: File containing Python dependencies for the project.
-   settings.py: Configuration file for the application.
-   main.py: Main file of the Flask application.

### Contribution

If you find any issues or have any suggestions for improvement, feel free to open an issue or submit a pull request.
