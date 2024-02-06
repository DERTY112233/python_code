from requests_oauthlib import OAuth2Session

client_id = '4ed23c352fcfd694de0e'  # Your client ID
client_secret = '625810bcd1057b2299d32c656f47199d457b0f2f'  # Your client secret
authorization_base_url = 'https://localhost:5050/authorize'
token_url = 'https://localhost:5050/token'
redirect_uri = 'https://localhost:5050/authorized'

# Create an OAuth2Session with client ID and secret
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

# Generate authorization URL
authorization_url, state = oauth.authorization_url(authorization_base_url)

print('Authorization URL:', authorization_url)

# Open the URL in a web browser, and the user will authorize the client
# After authorization, the user will be redirected to the 'redirect_uri' specified above

# Parse the callback URL after authorization
authorization_response = input('Enter the callback URL after authorization: ')
token = oauth.fetch_token(token_url, authorization_response=authorization_response, client_secret=client_secret)

# You can now use 'token' to make authenticated API requests
print('Access token:', token)
