
# 🚀 Example Django Ninja OAuth project with Google login

This project demonstrates how to set up **OAuth authentication** using **Google** with **Django Ninja**, integrating **JWT tokens** for user authentication.

## 🌟 Overview
- **Google OAuth** for user authentication.
- **JWT tokens** to manage authenticated user sessions.
- **Django Ninja** for API routing and management.
- The project enables users to log in via Google, fetch their profile, and manage sessions using JWT.

## ⚙️ Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/ThisKarolGajda/ExampleDjangoNinjaOauth.git
```

### 2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. Migrate the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the development server:
```bash
python manage.py runserver
```

## 🔧 Configuration for Google OAuth

### Create a Project on Google Cloud Console
1. Go to **APIs & Services > Credentials**.
2. Create new **OAuth 2.0 credentials**.
3. Set the **Authorized Redirect URIs** to:
   ```bash
   http://127.0.0.1:8000/api/v1/auth/google-callback/
   ```

### Add your Google OAuth credentials to `settings.py`:
```python
OAUTH_GOOGLE_CLIENT_ID = 'your-client-id'
OAUTH_GOOGLE_CLIENT_SECRET = 'your-client-secret'
```

---

## 📡 API Endpoints

### **Google Login**
- **Endpoint**: `/api/v1/auth/google-login/`
- **Method**: `GET`
- **Description**: Redirects the user to Google’s OAuth authorization page.
- **Example URL**: 
  ```http
  GET http://127.0.0.1:8000/api/v1/auth/google-login/
  ```

---

### **Google Callback**
- **Endpoint**: `/api/v1/auth/google-callback/`
- **Method**: `GET`
- **Description**: Handles the redirect from Google after successful authentication, retrieves the user's Google profile, and generates a JWT token.
- **Example URL**: 
  ```http
  GET http://127.0.0.1:8000/api/v1/auth/google-callback/
  ```

---

### **Get User Info (Synchronous)**
- **Endpoint**: `/api/v1/users/get/`
- **Method**: `GET`
- **Description**: Requires a valid JWT token in the `Authorization` header. Returns user info synchronously.
- **Headers**:
  ```http
  Authorization: Bearer <your_jwt_token>
  ```
- **Example URL**: 
  ```http
  GET http://127.0.0.1:8000/api/v1/users/get/
  ```

---

### **Get User Info (Asynchronous)**
- **Endpoint**: `/api/v1/users/aget/`
- **Method**: `GET`
- **Description**: Requires a valid JWT token in the `Authorization` header. Returns user info asynchronously, ideal for handling long-running requests.
- **Headers**:
  ```http
  Authorization: Bearer <your_jwt_token>
  ```
- **Example URL**: 
  ```http
  GET http://127.0.0.1:8000/api/v1/users/aget/
  ```

---

## 🛠️ Technologies Used
- **Django**: Web framework for building APIs.
- **Django Ninja**: A fast and easy-to-use API framework for building APIs with Django and Python 3.6+.
- **JWT**: JSON Web Tokens for authentication.
- **Google OAuth**: User authentication using Google.

---
