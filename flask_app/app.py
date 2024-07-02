from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Cloudflare API bilgileri
CF_API_KEY = 'XXXXXXXXXXXXXXXXXXX'
CF_EMAIL = 'XXXXXXXXXXXXXXXXXXX'
ZONE_ID = 'XXXXXXXXXXXXXXXXXXX'
ACCOUNT_ID = 'XXXXXXXXXXXXXXXXXXX'
LIST_ID = 'XXXXXXXXXXXXXXXXXXX'

# API endpointleri
firewall_rules_url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/firewall/rules"
list_items_url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/rules/lists/{LIST_ID}/items"

# HTTP başlıkları
headers = {
    'X-Auth-Email': CF_EMAIL,
    'X-Auth-Key': CF_API_KEY,
    'Authorization': f'Bearer XXXXXXXXXXXXXXXXXXX',
    'Content-Type': 'application/json'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_rules')
def get_rules():
    response = requests.get(firewall_rules_url, headers=headers)
    if response.status_code == 200:
        rules = response.json()["result"]
        return jsonify(rules)
    else:
        return jsonify({'error': 'Failed to fetch rules'}), response.status_code

@app.route('/toggle_rule', methods=['POST'])
def toggle_rule():
    rule_id = request.json.get('rule_id')
    paused = request.json.get('paused')

    selected_rule = {"paused": not paused}

    update_url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/firewall/rules/{rule_id}"

    update_response = requests.put(update_url, headers=headers, json=selected_rule)

    if update_response.status_code == 200:
        return "Kural başarıyla güncellendi."
    else:
        return f"Hata oluştu: {update_response.status_code} - {update_response.text}"

@app.route('/add_ip', methods=['POST'])
def add_ip():
    data = request.json
    ipAddress = data.get('ipAddress')
    comment = data.get('comment')

    payload = [{"ip": ipAddress, "comment": comment}]
    
    response = requests.post(list_items_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return jsonify({'message': 'IP address successfully added.'})
    else:
        return jsonify({'message': 'An error occurred while adding the IP address.'}), 500

@app.route('/check_ip', methods=['POST'])
def check_ip():
    data = request.json
    ipAddress = data.get('ipAddress')

    response = requests.get(list_items_url, headers=headers)
    
    if response.status_code == 200:
        items = response.json().get('result', [])
        for item in items:
            if item.get('ip') == ipAddress:
                return jsonify({'message': 'IP address is in the list.'})
        return jsonify({'message': 'IP address is not in the list.'})
    else:
        return jsonify({'message': 'An error occurred while fetching the IP list.'}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
