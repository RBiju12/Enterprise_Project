from flask import Flask, render_template
import requests
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Crypto.html")

@app.route('/chart', methods=['GET'])
def chart1():
    url = "https://fcsapi.com/api-v3/crypto/supply?symbol=BTC,XRP&convert=USD&access_key=YJ0kxYoB0J79xzs4htS8K5BI8"

    data = requests.get(url)
    cryptodata = data.json()

    x_values = []
    y_values = []

    for item in cryptodata:
        x_values.append(item["percentage_change_24h"])
        y_values.append(item["price"])
    
    plt.plot(x_values, y_values)
    plt.xlabel('Daily Percent Change')
    plt.ylabel('Price')
    plt.title('API Data Plot')
    plt.show()


    plot_path = os.path.join(app.static_folder, 'plot.png')
    plt.savefig(plot_path)

    return f'<img src="{plot_path}">'

def chart2():
    url = "https://fcsapi.com/api-v3/crypto/supply?symbol=BTC,XRP&convert=USD&access_key=YJ0kxYoB0J79xzs4htS8K5BI8"
    data = requests.get(url)
    cryptodatav2 = data.json()

    x_axis = []
    y_axis = []

    for val in cryptodatav2:
        x_axis.append(val["percentage_change_7d"])
        y_axis.append(val["market_cap"])

    plt.plot(x_axis, y_axis)
    plt.xlabel("Weekly percent change")
    plt.ylabel("Market Cap")
    plt.title("Weekly Percentage change vs Market_Cap")
    plt.show()

    plot_path2 = os.path.join(app.static_folder, 'plot2.png')
    plt.savefig(plot_path2)


    return f'<img src="{plot_path2}">'


if __name__ == '__main__':
    app.run(debug=True)
