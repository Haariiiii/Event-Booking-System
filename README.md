# Event-Booking-System
An online event booking system with Email Confirmation using SMTP
vent Management System

A full-stack web application developed using Django and MySQL for managing and booking events online. The system allows users to register, browse events, and book tickets with secure email confirmation functionality.

Features
User Registration and Login
Event Creation and Management
Event Booking System
Email Confirmation using SMTP
Responsive User Interface
Admin Panel for Managing Events and Users
Secure Authentication System
Technologies Used
Backend
Python
Django
Frontend
HTML5
CSS3
JavaScript
Database
MySQL
Other Tools
SMTP Email Service
Git & GitHub
Project Structure
Event-Management-System/
│
├── event/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md
Installation
1. Clone the Repository
git clone https://github.com/yourusername/event-management-system.git
2. Navigate to Project Directory
cd event-management-system
3. Create Virtual Environment
python -m venv env
4. Activate Virtual Environment
Windows
env\Scripts\activate
Linux/Mac
source env/bin/activate
Install Dependencies
pip install -r requirements.txt
Configure Database

Update your MySQL database settings in:

settings.py

Example:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eventdb',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Apply Migrations
python manage.py makemigrations
python manage.py migrate
Run the Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
Email Configuration

SMTP is used for email confirmation and notifications.

Example configuration in settings.py:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
EMAIL_USE_TLS = True
Future Improvements
Online Payment Integration
QR Code Ticket Verification
Event Recommendations
User Dashboard Analytics
Author

HARIGOVIND P

LinkedIn: LinkedIn Profile
Email: harigovindp004@gmail.com
