from flask import Blueprint, redirect, session, request, jsonify
import requests

auth_bp = Blueprint('auth', __name__)

CLIENT_ID = '91ad79bc13fe4e21b070ff8c7a8271ca'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

@auth_bp.route('/login')
def login():
    # Redirect users to Spotify's authorization URL
    auth_url = 'https://accounts.spotify.com/authorize'
    scopes = 'user-read-private user-read-email'  # Define required scopes
    auth_params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': scopes
    }
    return redirect(f"{auth_url}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={scopes}")

@auth_bp.route('/callback')
def callback():
    code = request.args.get('code')
    access_token = get_access_token(code)  # Utilize the defined function from spotify.py
    session['access_token'] = access_token
    return 'Authentication successful. Access token obtained.'

@auth_bp.route('/logout')
def logout():
    # Placeholder logic for logout
    return 'Logout Page'

# Define the get_access_token function here
def get_access_token(code):
    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    token_response = requests.post(token_url, data=token_data)
    access_token = token_response.json().get('access_token')
    return access_token

# Define the get_user_profile function here
def get_user_profile(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    profile_response = requests.get('https://api.spotify.com/v1/me', headers=headers)
    return profile_response.json()