# IITHackthon First Responder Project - ScarletHack

This project was developed for a hackathon, likely ScarletHack, focusing on a "First Responder" or emergency alert system using a Flask web application.

## Overview

The IITHackthon First Responder project is a Flask-based web application designed to facilitate emergency alerts and communication. It allows users to report incidents with location and description, stores these alerts in a database, and can send emergency SMS messages to predefined contacts. The application also integrates with Vidyo.io for potential video conferencing capabilities.

## Features

- **User Authentication**: Secure login system for users.
- **Emergency Alert System**: Users can submit alerts with a rating, location, and description.
- **Location Services**: Uses Google Maps Geocoding API to get latitude and longitude for reported locations.
- **Telnyx SMS Integration**: Sends emergency "Help Me !!!!!!!" SMS messages to pre-configured phone numbers (likely emergency contacts).
- **Vidyo.io Integration**: Generates Vidyo.io tokens for video conferencing, potentially for first responders or emergency coordination.
- **Database**: Uses MongoDB to store user data and alert information.
- **Map Visualization**: Displays alerts on a map (inferred from `map_data` in `index.html` and `profile.html` rendering).

## Project Structure

- `app/`: Contains the core Flask application.
    - `__init__.py`: Initializes the Flask app and extensions.
    - `forms.py`: Defines web forms.
    - `user.py`: User model and login validation.
    - `views.py`: Defines application routes and logic, including alert submission, SMS sending, and API integrations.
    - `static/`: Static files (CSS, JavaScript, images).
    - `templates/`: HTML templates for rendering pages (e.g., `index.html`, `profile.html`, `login.html`).
- `config.py`: Configuration settings for the application.
- `requirements.txt`: Lists all Python dependencies.
- `run-dev.py`: Script to run the development server (on port 1010).
- `generateToken.py`: Script for generating tokens (e.g., Vidyo.io).
- `populateDB.py`: Script to populate the database with initial data.
- `userdata.csv`: CSV file for user data, possibly used by `populateDB.py`.
- `row0.json`, `row1.json`, `row2.json`: Example JSON data files, possibly for initial data or testing.
- `cert.pem`, `key.pem`: SSL certificates.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone [repository_url]
   cd ScarletHack/IITHackthon_FirstResponder
   ```

2. **Install dependencies**:
   It is highly recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the application**:
   Update `config.py` with your MongoDB connection details and API keys for Telnyx and Google Maps Geocoding.

4. **Start MongoDB**:
   Ensure your MongoDB instance is running, as the application connects to `127.0.0.1:27017`.

5. **Populate the database (optional)**:
   If you have `populateDB.py` and `userdata.csv`, you can run:
   ```bash
   python populateDB.py
   ```

6. **Run the development server**:
   ```bash
   python run-dev.py
   ```
   The application will typically run on `http://127.0.0.1:1010`.

## Technologies Used

- **Flask**: Web framework
- **MongoDB**: NoSQL Database
- **Vidyo.io**: Video conferencing API
- **Telnyx**: SMS API
- **Google Maps Geocoding API**: For location services.
- **Flask-Login**: User session management
- **Flask-WTF**: Web forms
- **Requests**: HTTP library
- **Pandas/Numpy/Scipy**: Data analysis libraries (if used for backend processing)
