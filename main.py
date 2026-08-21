import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
GENDER = os.environ.get("GENDER")
WEIGHT_KG = int(os.environ.get("WEIGHT_KG"))
HEIGHT_CM = int(os.environ.get("HEIGHT_CM"))
AGE = int(os.environ.get("AGE"))

nutrition_and_exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
workout_endpoint = "https://api.sheety.co/b31e3f1dcf8d6c6205b00bd0ba346c69/manoWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_question = input("Enter what activity you performed: ")

parameters = {
    "query": exercise_question,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(nutrition_and_exercise_endpoint, headers=headers, json=parameters)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_params = {
        "workout":{
        "exercise": exercise["name"].title(),
        "date": today_date,
        "time": now_time,
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
    }
    sheet_response = requests.post(workout_endpoint, json=sheet_params)