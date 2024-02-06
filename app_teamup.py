from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Your Teamup API key
API_KEY = 'YOUR_API_KEY'

# The Teamup API endpoint
TEAMUP_API_URL = 'https://api.teamup.com/'

@app.route('/')
def index():
    return 'Hello, Teamup API Integration with Flask!'

# Define a route to fetch events from Teamup
@app.route('/events', methods=['GET'])
def get_events():
    calendar_id = request.args.get('calendar_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not calendar_id or not start_date or not end_date:
        return jsonify({'error': 'Missing parameters'}), 400

    # Construct the URL to fetch events
    url = f'{TEAMUP_API_URL}{calendar_id}/events?startDate={start_date}&endDate={end_date}'
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
