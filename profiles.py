from flask import Flask, render_template, request, redirect, session, jsonify, Blueprint
from flask_session import Session
from datetime import datetime
import pytz
from sql import * #Used for database connection and management

profiles_blueprint = Blueprint('profiles', __name__)


@profiles_blueprint.route("/details", methods=["GET", "POST"])
def profiledetails():
    if not session.get("name"):
            return render_template("index.html", authentication=True)
    else:
            if request.method == "GET":
                return render_template("detailedForm.html")
            else:
                #Personal Information Field Collection
                dob = request.form.get("date_of_birth")
                gender = request.form.get("gender")
                phone = request.form.get("phone_number")
                address = request.form.get("address")

                #Health Profile Field Collection
                blood_type = request.form.get("blood_type")
                height= request.form.get("height")
                weight = request.form.get("weight")
                allergies = request.form.get("allergies")
                medical_conditions = request.form.get("medical_conditions")
                future_goals = request.form.get("future_goals")

                #Notification Preferences Field Collection
                notify_email = request.form.get("notify_email")
                notify_sms = request.form.get("notify_sms")
                notify_push = request.form.get("notify_push")

                notify_health_alerts = request.form.get("notify_health_alerts")
                notify_app_updates = request.form.get("notify_app_updates")
                notify_newsletter = request.form.get("notify_newsletter")

                #Privacy and Security Field Collection
                two_factor_auth = request.form.get("two_factor_auth")
                anonymous_data = request.form.get("share_anonymous_data")
                show_in_community = request.form.get("show_in_community")

                return "Work in Process"
