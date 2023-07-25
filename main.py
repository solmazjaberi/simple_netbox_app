
from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

# loading the devices from data.json
def load_config():
    with open('data.json') as config_file:
        return json.load(config_file)

devices = load_config()

# interaction with netbox api

# NETBOX_URL = 'netbox-server-url/api/'
# NETBOX_TOKEN = 'netbox-api-token'

# def get_netbox_data(url, token):
#     headers = {
#         'Authorization': f'Token {NETBOX_TOKEN}',
#         'Accept': 'application/json',
#     }
    
#     try:
#         response = requests.get(f'{NETBOX_URL}dcim/devices/', headers=headers)
#         response.raise_for_status()  # Exception for unsuccessful requests
#         netbox_devices = response.json()
#     except requests.exceptions.RequestException as e:
#         return f"Error retrieving devices from NetBox: {e}"

#     return render_template('devices.html', devices=netbox_devices)


# @app.route('/')
# def index():
#     return redirect(url_for('netbox_devices'))




@app.route('/')
def network_status():
    return render_template('template.html', devices=devices)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)