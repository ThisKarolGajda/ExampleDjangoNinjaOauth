# Example Django Ninja OAuth project with Google login
This project demonstrates how to set up OAuth authentication using Google with Django Ninja, along with the integration of JWT tokens for user authentication.

## Overview
- Google OAuth is used to authenticate users.
- JWT tokens are used to manage sessions for the authenticated users.
- Django Ninja handles the API routing.
- The project allows users to log in via Google, retrieve their profile, and manage sessions using JWT.

## Setup Instructions
### Clone the repository:
git clone https://github.com/ThisKarolGajda/ExampleDjangoNinjaOauth.git

### Install python requirements
pip install -r requirements.txt

### Migrate the database:
python manage.py makemigrations
python manage.py migrate

### Run the development server:
python manage.py runserver

## Configuration for Google OAuth
### Create a project on Google Cloud Console.
Go to APIs & Services > Credentials and create new OAuth 2.0 credentials.
Set the Authorized Redirect URIs to: http://127.0.0.1:8000/api/v1/auth/google-callback/.

### Add your Google OAuth credentials to settings.py:
OAUTH_GOOGLE_CLIENT_ID = 'your-client-id'
OAUTH_GOOGLE_CLIENT_SECRET = 'your-client-secret'

## API Endpoints
### **Google Login**
- **Endpoint**: `/api/v1/auth/google-login/`
- **Method**: `GET`
- **Description**: Redirects the user to Google’s OAuth authorization page for authentication.
- **Example URL**: 
  ```
  GET http://127.0.0.1:8000/api/v1/auth/google-login/
  ```

---

### **Google Callback**
- **Endpoint**: `/api/v1/auth/google-callback/`
- **Method**: `GET`
- **Description**: Handles the redirect from Google after successful authentication. Retrieves the user's Google profile and generates a JWT token for the authenticated user.
- **Example URL**: 
  ```
  GET http://127.0.0.1:8000/api/v1/auth/google-callback/
  ```

---

### **Get User Info (Synchronous)**
- **Endpoint**: `/api/v1/users/get/`
- **Method**: `GET`
- **Description**: Requires a valid JWT token in the `Authorization` header. This endpoint returns user information synchronously.
- **Headers**:
  ```
  Authorization: Bearer <your_jwt_token>
  ```
- **Example URL**: 
  ```
  GET http://127.0.0.1:8000/api/v1/users/get/
  ```

---

### **Get User Info (Asynchronous)**
- **Endpoint**: `/api/v1/users/aget/`
- **Method**: `GET`
- **Description**: Requires a valid JWT token in the `Authorization` header. This endpoint returns user information asynchronously, which is ideal for handling long-running requests or external API calls.
- **Headers**:
  ```
  Authorization: Bearer <your_jwt_token>
  ```
- **Example URL**: 
  ```
  GET http://127.0.0.1:8000/api/v1/users/aget/
  ```

---
