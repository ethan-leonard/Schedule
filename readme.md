# Django Schedule App

This project is a scheduling application built with Django.

## Project Setup

### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of [Python](https://www.python.org/downloads/).

### Backend

The backend of the project is located in the `schedule` directory.

1. Navigate to the `schedule` directory.

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv .env
    ```

    ### For Windows
    ```bash
    .env/Scripts/activate
    ```

    *If you get an error saying you can't run the script, run this command:*
    ```bash
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    ```

    ### For Linux
    ```bash
    source .env/bin/activate  
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the Django server:

    ```bash
    python manage.py runserver
    ```

Now, you should be able to access the application at http://localhost:8080.
