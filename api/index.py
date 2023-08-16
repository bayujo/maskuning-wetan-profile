import requests
from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data from {url}: {e}")
        return None

@app.route('/')
def home():
    population_response = fetch_data("https://sid.kemendesa.go.id/population-statistic/data?location_code=3511040003&province_id=&city_id=&district_id=&village_id=&on=population")
    sgds_response = fetch_data("https://sid.kemendesa.go.id/sdgs/searching/score-sdgs?location_code=3511040003&province_id=&city_id=&district_id=&village_id=")

    return render_template('index.html', population_response=population_response, sgds_response=sgds_response)
