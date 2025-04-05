import sqlite3
import os

database = open('users.db', 'w')
database.truncate(0)  
database.close()
connection = sqlite3.connect("users.db")
crsr = connection.cursor()

fields = [
    #Personal Information for Account Setup and Maintenance
          "username NOT NULL", 
          "password NOT NULL",
          "dateJoined",
          "accountStatus",
          "role", #Possible Doctor or Volunteer?
          "twoFactorAuth",
          "lastLogin",
          "emailAddress",
          "phoneNumber",
          "name", #Full Name
          "dateOfBirth",
          "gender", #Prefer Not to Say or Other
          "location",
    #Basic Health & Wellness Data
          "height",
          "weight",
          "BMI",
          "bloodType", 
    #Medical History & Health Conditions
          "existingConditions",
          "allergies",
          "familyMedicalHistory", #Possible paragraph to be examined by AI
          "medicationsTaken",
    #Lifestyle & Habits
          "dietaryRestrictions",
          "exerciseRoutine", #Possible paragraph for analysis again, or possible caloriesBurnt counter
          "sleepPatterns",
          "substanceConsumption",
    #Mental Health & Stress Levels
          "moodTracking",
          "stressLevels",
          "meditationHabits",
    #Wearable & App-Connected Data
          "stepsPerDay",
          "restingHeartRate",
          "bloodPressure", #Systolic and Diastolic separated by ","
          "oxygenSaturation",
          "caloriesBurned",
          "hydrationLevels",
    #Environmental & Location-Based Data, supplemental to Location
          "recentTravelHistory",
          "weatherUVexposure",
    #AI & Personalization Preferences
          "healthGoals",
          "preferredNotifications",
          "privacySettings"
        ]


#Easily convertible to MySQL or other databases due to iterative strategy as opposed to hardcoding the db create string, also improves readability and ease of maintenance and adding new fields

dbCreateString = "CREATE TABLE users (id INTEGER, "

for field in fields:
    dbCreateString += field+", "

dbCreateString+="PRIMARY KEY(id))"

print(dbCreateString)

crsr.execute(dbCreateString)
connection.commit()
crsr.close()
connection.close()

"""
🆔 User Profile Information
Full Name (or just a username for privacy)
Email Address (for account recovery & notifications)
Phone Number (optional, for alerts)
Date of Birth (for age-based recommendations)
Gender (optional, but useful for certain health insights)
Location (City & Country) (for local health trends, pollution levels, etc.)

⚕️ Health & Wellness Data
📏 Basic Health Metrics
Height (for BMI calculation)
Weight (for fitness tracking)
Body Mass Index (BMI) (calculated from height & weight)
Blood Type (useful for emergency data & diet suggestions)  find donors feature

🩺 Medical History & Health Conditions
Existing Conditions (diabetes, hypertension, asthma, etc.)
Allergies (food, medication, environmental)
Family Medical History (genetic risk factors)
Medications Taken (to avoid conflicts in AI suggestions)

💤 Lifestyle & Habits
Dietary Restrictions (vegetarian, vegan, keto, etc.)
Exercise Routine (sedentary, active, athlete level)
Sleep Patterns (tracked via wearables or manual input)
Smoking / Alcohol Consumption (for health risk predictions)

😃 Mental Health & Stress Levels
Mood Tracking (self-reported or AI-assisted analysis)
Stress Levels (integrated from wearables or surveys)
Meditation & Relaxation Habits

📊 Wearable & App-Connected Data
Steps Taken Per Day (Google Fit, Apple Health)
Heart Rate & Blood Pressure (if tracked)
Oxygen Saturation (SpO2) (from smart devices)
Calories Burned (from activity trackers)
Hydration Levels (manual input or smart bottles)

🌍 Environmental & Location-Based Data
Current Location (optional, city-based) (for air quality, pollution alerts)
Recent Travel History (for disease outbreak risk assessment)
Weather & UV Exposure (to provide sun safety tips)

🧠 AI & Personalization Preferences
Health Goals (weight loss, muscle gain, improved sleep, etc.)
Preferred Notifications (daily tips, weekly reports, emergency alerts)
Privacy Settings (what data can be shared or anonymized)

🔐 Privacy & Security Considerations
Store Sensitive Data Securely (hashed passwords, encrypted health data)
Allow Users to Control Data Sharing (opt-in for AI predictions)
Implement Data Anonymization (for crowdsourced reports)"

"""