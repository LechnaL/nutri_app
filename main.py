import requests
import datetime

#insert your nutritionix api keys here
NUTRITIONIX_API ={
    "x-app-id":"",
    "x-app-key":"",
}
#insert your sheety api url for your spreadsheet
SHEETY_URL="https://api.sheety.co/"



EXCERCIZE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

#here you can configure parameters so they match yours
e_query = str(input("What excercizes did you do?:"))
gender = "male"
weight_kg = 73
height_cm = 181
age = 23

excercize_params = {
    "query": e_query,
}

response = requests.post(url=EXCERCIZE_URL, json=excercize_params, headers=NUTRITIONIX_API)
result = response.json()
print(result)

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "arkusz1": {
            "date": today_date,
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_URL, json=sheet_inputs)
    print(sheet_response.text)
print("Powered by Nutritionix: https://www.nutritionix.com")



