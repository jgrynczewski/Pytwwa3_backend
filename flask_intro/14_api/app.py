# Web application
import requests #urllib

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/convert", methods=['POST'])
def convert():

    amount = request.form.get('amount')
    symbols = request.form.get('symbols').upper()

    response  = requests.get("http://data.fixer.io/api/latest",
                        params = {'access_key':'032053b70cf616de08638aeaeb1cfd1d',
                                'symbols': symbols}
                 )

    if response.status_code != 200:
        return f"Niepowowdznie. Kod HTTP {response.status_code}"

    res_dict = response.json()

    if not res_dict.get('success'):
        return f"Error: {res_dict.get('error').get('info')}"

    converter = res_dict.get('rates').get(symbols)

    result = float(amount) / converter

    return f"Wypłacono {round(result, 2)} euro."