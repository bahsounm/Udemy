import requests
import datetime as dt
import sys, os

API_KEY = os.environ.get("API_KEY")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
WEIGHT = 230
DATE_TODAY = dt.datetime.now().strftime("%Y/%m/%d")

NATURAL_EXERCISE_ENDPOINT = "https://api.api-ninjas.com/v1/caloriesburned"
ACTIVITIES_ENDPOINT = "https://api.api-ninjas.com/v1/caloriesburnedactivities"
SHEETY_ENPOINT = "https://api.sheety.co/247e75aa2439b0d8bf6b9e44d3031a5f/myWorkouts/workouts"



# Getting the workout from the user
exercise_text = input("Tell me which exercise you did: ")
time_of_exercise = input("Tell me how long you did this for (minutes): ")
time_logged = str(dt.datetime.now().time())[:8]
headers = {
    "X-Api-Key": API_KEY
}
exercise_param = {
    "activity": exercise_text,
    "weight":WEIGHT,
    "duration": int(time_of_exercise)

}
response = requests.get(NATURAL_EXERCISE_ENDPOINT, headers=headers, params=exercise_param)
response.raise_for_status()
data = response.json()
if not data:
    print("Please Make sure your workout is part of our available options")
    sys.exit()

for i in range(len(data)):
    print("{}. {}".format(i, data[i]["name"]))

user_selection = input("Which Workout best describes what you did (will default to 0 upon no selection): ")
user_selection = int(user_selection) if user_selection else 0

workout_data = {"Exercise": data[user_selection]["name"], "Time":time_logged, "Duration": data[user_selection]["duration_minutes"], "Calories": data[user_selection]["total_calories"], "Date": DATE_TODAY}

# Placing the Workout into the sheet
our_workout = {"workout":{
    "date":workout_data["Date"],
    "time":workout_data["Time"],
    "exercise":workout_data["Exercise"],
    "duration":workout_data["Duration"],
    "calories":workout_data["Calories"]
}}

headers = {
    "Authorization": SHEETY_AUTH
}
response = requests.post(url=SHEETY_ENPOINT, json=our_workout, headers=headers)
response.raise_for_status()

