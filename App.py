from flask import Flask, render_template
import requests
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Crypto.html")

@app.route('/chart', methods=['GET'])
def charts():
    url = "https://fcsapi.com/api-v3/crypto/supply?symbol=BTC,XRP&convert=USD&access_key=YJ0kxYoB0J79xzs4htS8K5BI8"

    data = requests.get(url)
    cryptodata = data.json()

    x_values = []
    y_values = []

    for item in cryptodata:
        x_values.append(item["percentage_change_24h"])
        y_values.append(item["price"])
    
    plt.plot(x_values, y_values)
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('API Data Plot')
    plt.show()


    plot_path = os.path.join(app.static_folder, 'plot.png')
    plt.savefig(plot_path)

    return f'<img src="{plot_path}">'

if __name__ == '__main__':
    app.run(debug=True)
