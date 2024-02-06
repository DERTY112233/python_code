from flask import Flask, request, redirect, jsonify
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
app.secret_key = '625810bcd1057b2299d32c656f47199d457b0f2f'  # Replace with your secret key
oauth = OAuth2Provider(app)

# Simulated database of users and clients (you should use a real database)
users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'},
}

clients = {
    'client1': {'secret': '625810bcd1057b2299d32c656f47199d457b0f2f', 'redirect_uris': ['https://localhost:5050/authorize?response_type=code&client_id=4ed23c352fcfd694de0e&redirect_uri=https%3A%2F%2Flocalhost%3A5050%2Fauthorized&state=CmBKAsYkd4KK1eK4r2tRqt6PkUffeK']},
}

@oauth.clientgetter
def load_client(client_id):
    return clients.get(client_id)

@oauth.usergetter
def get_user(username, password, *args, **kwargs):
    if users.get(username) and users[username]['password'] == password:
        return username
    return None

@app.route('/authorize', methods=['GET', 'POST'])
@oauth.authorize_handler
def authorize(*args, **kwargs):
    user = kwargs.get('user')
    if request.method == 'POST':
        confirm = request.form.get('confirm', 'no')
        return confirm == 'yes'
    return jsonify(client=kwargs['client_id'], user=user)

@app.route('/token', methods=['POST'])
@oauth.token_handler
def access_token():
    return None

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5050', debug=True)
