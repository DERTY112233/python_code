import requests

# Replace with your actual API key
api_key = 'YOUR_API_KEY'

# Replace with the customer's ID you want to retrieve
customer_id = 'CUSTOMER_ID'

# Define the API endpoint for customer details
api_endpoint = f'https://api.teamupbusiness.com/customers/{customer_id}'

# Set up headers with the API key for authentication
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

try:
    # Send a GET request to the API endpoint
    response = requests.get(api_endpoint, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        customer_data = response.json()
        print("Customer Details:")
        print(customer_data)
    else:
        print(f"Failed to retrieve customer details. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
