from flask import Flask, render_template, request
import json

app = Flask(__name__, template_folder='Templates')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/marchmadness")
def fetchmbasketball():
    with open("2018.json") as file:
        data = json.load(file)

    game = []
    top_10 = sorted(data["team"][:10])
    for teams in top_10:
        for place in data["seed"]:
            if place > 10:
                return teams
    game.append(teams)

    if request.method == 'POST':
        selected_team = request.form.get('team')
        return f"You selected {selected_team}."
    else:
        return render_template('marchmadness.html', teams=top_10)

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)

