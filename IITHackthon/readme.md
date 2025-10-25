# IITHackthon Project - ScarletHack

This project was developed for a hackathon, likely ScarletHack, and is a Flask-based web application integrating various communication APIs.

## Overview

The IITHackthon project is a web application built with Flask, designed to demonstrate integrations with real-time communication and messaging services. It features user authentication and leverages APIs for video conferencing, faxing, and SMS capabilities.

## Features

- **User Authentication**: Secure login system for users.
- **Vidyo.io Integration**: Generates Vidyo.io tokens for video conferencing.
- **Phaxio Integration**: Sends faxes using the Phaxio API.
- **Telnyx SMS Integration**: Sends SMS messages via the Telnyx API.
- **Database**: Uses MongoDB for user management.

## Project Structure

- `app/`: Contains the core Flask application.
    - `__init__.py`: Initializes the Flask app and extensions.
    - `forms.py`: Defines web forms.
    - `user.py`: User model and login validation.
    - `views.py`: Defines application routes and logic, including API integrations.
    - `static/`: Static files (CSS, JavaScript, images).
    - `templates/`: HTML templates for rendering pages.
- `config.py`: Configuration settings for the application.
- `requirements.txt`: Lists all Python dependencies.
- `run-dev.py`: Script to run the development server.
- `generateToken.py`: Script for generating tokens (e.g., Vidyo.io).
- `populateDB.py`: Script to populate the database with initial data.
- `userdata.csv`: CSV file for user data, possibly used by `populateDB.py`.
- `cert.pem`, `key.pem`: SSL certificates.
- `.Presentation.pptx.icloud`: Presentation file.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone [repository_url]
   cd ScarletHack/IITHackthon
   ```

2. **Install dependencies**:
   It is highly recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the application**:
   Update `config.py` with your MongoDB connection details and API keys for Phaxio and Telnyx.

4. **Populate the database (optional)**:
   If you have `populateDB.py` and `userdata.csv`, you can run:
   ```bash
   python populateDB.py
   ```

5. **Run the development server**:
   ```bash
   python run-dev.py
   ```
   The application will typically run on `http://127.0.0.1:9090`.

## Technologies Used

- **Flask**: Web framework
- **MongoDB**: NoSQL Database
- **Vidyo.io**: Video conferencing API
- **Phaxio**: Fax API
- **Telnyx**: SMS API
- **Flask-Login**: User session management
- **Flask-WTF**: Web forms
- **Requests**: HTTP library
- **Pandas/Numpy/Scipy**: Data analysis libraries (if used for backend processing)
