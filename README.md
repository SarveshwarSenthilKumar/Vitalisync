
# Vitalisync - Comprehensive Health Monitoring and Wellness Platform

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
   - [📍 Real-Time Health Tracking](#-real-time-health-tracking)
   - [🤖 AI-Powered Health Insights & Predictions](#-ai-powered-health-insights--predictions)
   - [🔔 Personalized Health Alerts & Wellness Tips](#-personalized-health-alerts--wellness-tips)
   - [🌍 Community & Crowdsourced Data](#-community--crowdsourced-data)
   - [📚 Holistic Health & Wellness Resources](#-holistic-health--wellness-resources)
   - [📊 Interactive Personal Health Dashboard](#-interactive-personal-health-dashboard)
   - [🍽️ AI-Powered Meal Recommendations](#-ai-powered-meal-recommendations)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Flask Development Template](#flask-development-template)
6. [Future Enhancements](#future-enhancements)
7. [Get Involved](#get-involved)
8. [Contact](#contact)
9. [Database Fields Breakdown](#database-fields-breakdown)

## Overview
**Vitalisync** is a comprehensive health monitoring and wellness platform designed to help users track their overall well-being, receive AI-powered health insights, and take proactive steps toward a healthier lifestyle. The app aggregates global health data, analyzes trends, and offers personalized recommendations for health improvement.

## Features

### 📍 Real-Time Health Tracking
- Aggregates global health data, including:
  - Disease outbreaks
  - Air quality
  - UV index
  - Pollution levels
- Displays real-time health alerts on an interactive map.

### 🤖 AI-Powered Health Insights & Predictions
- Uses AI to analyze trends in:
  - Disease outbreaks
  - Mental health patterns
  - Lifestyle habits
- Predicts potential health risks and provides early intervention tips.

### 🔔 Personalized Health Alerts & Wellness Tips
- Sends notifications about local health risks (e.g., air quality warnings, flu season alerts).
- Offers customized health advice based on user data (e.g., hydration reminders, exercise suggestions).

### 🌍 Community & Crowdsourced Data
- Allows users to anonymously report symptoms, wellness trends, or environmental health concerns.
- Health organizations can access anonymized data for better public health strategies.

### 📚 Holistic Health & Wellness Resources
- Provides educational content on:
  - Disease prevention
  - Mental health
  - Fitness
  - Nutrition
- Offers meditation and stress management guides.

### 📊 Interactive Personal Health Dashboard
- Users can track personal wellness metrics:
  - Steps
  - Sleep
  - Stress levels
  - Symptoms
- Integrates with wearables like Fitbit, Apple Health, and Google Fit for real-time tracking.

### 🍽️ AI-Powered Meal Recommendations
- Uses AI to generate personalized meal plans based on:
  - Dietary preferences
  - Nutritional needs
  - Health goals
  - Local food availability
- Suggests balanced meals to promote overall well-being.

## Tech Stack

- **Backend:** Flask (Python)
  - A lightweight Python web framework that makes it easy to develop APIs and web applications.
  
- **Database:** SQLite3
  - SQLite3 is used for local, lightweight database management. It will store user health data, preferences, and AI-generated recommendations.

- **Frontend:** HTML and CSS
  - Simple, clean HTML and CSS will be used to build the user interface. Future enhancements could include JavaScript and front-end frameworks like React or Vue.js.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SarveshwarSenthilKumar/Vitalisync.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Vitalisync
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```


5. Set up the databases by running each of the following scripts:
   ```bash
   python createDatabase.py
   ```

6. Run the Flask app:
   ```bash
   python app.py
   ```

7. Visit `http://127.0.0.1:5000/` in your browser to access the app.

## Flask Development Template
For this project, I used the **[Flask Development Template](https://github.com/SarveshwarSenthilKumar/Flask-Development-Template)** as the base template for building the backend. The template provides a solid foundation for developing Flask applications with best practices, including structure for routing, database handling, and integration with various extensions like Flask-Migrate for database migrations.

## Future Enhancements

- **Telehealth Integration:** Connect users with virtual health professionals.
- **Fitness Challenges:** Encourage healthy habits through social engagement.
- **Expanded Wearable Integration:** Support for more health tracking devices.
- **Mobile App Development:** Create mobile applications for better accessibility.

## Get Involved
Vitalisync is an open-source project aimed at improving global health awareness and personal well-being. Contributions are welcome! If you'd like to contribute, fork the repository and submit a pull request.

### Contact
For any questions, feedback, or contributions, feel free to reach out:

- **Email:** [sarveshwar313@gmail.com](mailto:sarveshwar313@gmail.com)
- **GitHub Repository:** [Vitalisync GitHub](https://github.com/SarveshwarSenthilKumar/Vitalisync)

## Database Fields Breakdown

The `users.db` database is structured to store various user profile details, health data, and preferences in order to provide a personalized health monitoring experience. Below is an explanation of each field:

### 🆔 User Profile Information

- **username**: A unique identifier for the user to log in and interact with the platform. It cannot be null.
- **password**: The user's password, stored securely (hashed). It cannot be null.
- **dateJoined**: The date when the user created their account.
- **accountStatus**: The current status of the user account (e.g., active, suspended).
- **role**: The role of the user, such as Doctor or Volunteer. This can help personalize the user experience.
- **twoFactorAuth**: A boolean field indicating whether two-factor authentication is enabled for extra account security.
- **lastLogin**: The timestamp of the user's last login.
- **emailAddress**: The user’s email address, used for account recovery and notifications.
- **phoneNumber**: The user's phone number (optional), used for alerts and reminders.
- **name**: Full name of the user (or just the username for privacy).
- **dateOfBirth**: The user's date of birth, which can be used to make age-based recommendations.
- **gender**: The user’s gender, which can help in generating gender-specific health insights (optional).
- **location**: The user’s geographical location (city and country), useful for contextualizing health data.

### ⚕️ Health & Wellness Data

- **height**: The user's height, which is used to calculate their Body Mass Index (BMI).
- **weight**: The user’s weight, also used in BMI calculation and fitness tracking.
- **BMI**: Body Mass Index, a calculated field derived from height and weight, used to assess the user’s fitness level.
- **bloodType**: The user’s blood type, useful for emergency data and potential health suggestions (e.g., blood donors).

### 🩺 Medical History & Health Conditions

- **existingConditions**: A list of the user's existing medical conditions (e.g., diabetes, hypertension, asthma), which helps personalize health recommendations.
- **allergies**: A list of known allergies (food, medication, environmental) to avoid triggers in health recommendations.
- **familyMedicalHistory**: Information about the user’s family medical history, which may indicate genetic predispositions to certain health conditions.
- **medicationsTaken**: A list of medications the user is currently taking, to avoid conflicts with AI-generated health suggestions.

### 💤 Lifestyle & Habits

- **dietaryRestrictions**: Information on dietary restrictions (e.g., vegetarian, vegan, keto) to ensure that meal suggestions meet the user’s preferences and health goals.
- **exerciseRoutine**: The user's exercise routine (e.g., sedentary, active, athlete) for personalized fitness suggestions and tracking.
- **sleepPatterns**: Information about the user's sleep patterns, either manually input or tracked via wearable devices, to help with health predictions.
- **substanceConsumption**: Information about the user's consumption of substances such as alcohol or smoking, used to assess health risks.

### 😃 Mental Health & Stress Levels

- **moodTracking**: Data on the user's mood, either self-reported or AI-assisted, for emotional health insights.
- **stressLevels**: A measure of the user's stress levels, tracked manually or from wearables, to identify stress-related health risks.
- **meditationHabits**: Information about the user's meditation or relaxation practices, useful for stress reduction recommendations.

### 📊 Wearable & App-Connected Data

- **stepsPerDay**: The number of steps the user takes per day, typically from a wearable device (e.g., Fitbit, Apple Watch), to track physical activity.
- **restingHeartRate**: The user's resting heart rate, which helps assess cardiovascular health.
- **bloodPressure**: Blood pressure data, separated into systolic and diastolic values (e.g., "120, 80").
- **oxygenSaturation**: The percentage of oxygen in the user’s blood, typically measured by wearables or health devices.
- **caloriesBurned**: The number of calories the user burns, tracked through activity monitoring.
- **hydrationLevels**: The user’s hydration levels, which
