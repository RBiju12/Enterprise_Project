from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetchsoccer():
    url = "https://livescore6.p.rapidapi.com/teams/detail"

    querystring = {"ID":"3339"}

    headers = {
	"X-RapidAPI-Key": "c957e814a4mshe64ef3cce813326p1cde75jsnc3480bd5e8c5",
	"X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

#need to do parsing Soccerdata
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_team = request.form.get('team')
        return f"You selected {selected_team}."
    else:
        teams = fetchsoccer()
        return render_template('Soccer.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)
