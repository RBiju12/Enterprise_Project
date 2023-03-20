from flask import Flask, render_template
import requests
import matplotlib.pyplot as plt
import os

app = Flask(__name__, template_folder='Templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/chart1')
def chart1():
    url = "https://fcsapi.com/api-v3/crypto/supply?symbol=BTC,XRP&convert=USD&access_key=YJ0kxYoB0J79xzs4htS8K5BI8"

    data = requests.get(url)
    cryptodata = data.json()

    x_values = []
    y_values = []

    for item in cryptodata['response']:
        quote = item['quote']['USD']
        x_values.append(float(quote["percentage_change_24h"]))
        y_values.append(float(quote["price"]))
    
    plt.plot(x_values, y_values)
    plt.xlabel('Daily Percent Change')
    plt.ylabel('Price')
    plt.title('API Data Plot')
    plot_path = 'static/plot1.png'
    plt.savefig(plot_path)

    return render_template('chart1.html', chart1_url=plot_path)


@app.route('/chart2')
def chart2():
    url = "https://fcsapi.com/api-v3/crypto/supply?symbol=BTC,XRP&convert=USD&access_key=YJ0kxYoB0J79xzs4htS8K5BI8"
    data = requests.get(url)
    cryptodatav2 = data.json()

    x_axis = []
    y_axis = []

    for val in cryptodatav2['response']:
        quote = val['quote']['USD']
        x_axis.append(float(quote["percentage_change_7d"]))
        y_axis.append(float(quote["market_cap"]))

    plt.plot(x_axis, y_axis)
    plt.xlabel("Weekly percent change")
    plt.ylabel("Market Cap")
    plt.title("Weekly Percentage change vs Market_Cap")
    plot_path = 'static2/plot2.png'
    plt.savefig(plot_path)

    return render_template('chart2.html', chart2_url=plot_path)


if __name__ == '__main__':
    app.run(debug=True)
