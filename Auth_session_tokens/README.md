# 🔐 Django Session Authentication System

A simple beginner-friendly Django project demonstrating **Session-based Authentication**, including:

- User Signup
- User Login
- User Logout
- Protected Dashboard (login required)
- Session Management
- Basic Form Handling

This project uses Django's **built-in User model** and Django’s default **session framework** for user authentication.

---

## 🚀 Features

### ✔ User Signup  
Users can create an account using a username and password.

### ✔ User Login  
Users can authenticate using Django’s built-in `authenticate()` + `login()` functions.

### ✔ User Logout  
Destroys the session using Django’s `logout()` function.

### ✔ Protected Dashboard  
Only logged-in users can access the dashboard using `@login_required`.

### ✔ Error Handling  
Displays errors such as:
- Invalid credentials  
- Username already exists  

---

## 🏗 Project Structure

