from flask import Blueprint, request, session
import requests

spotify_bp = Blueprint('spotify', __name__)

CLIENT_ID = '91ad79bc13fe4e21b070ff8c7a8271ca'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET' #this needs to be safe
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

@spotify_bp.route('/get_user_profile')
def get_user_profile():
    access_token = session.get('access_token')
    if access_token:
        headers = {'Authorization': f'Bearer {access_token}'}
        profile_response = requests.get('https://api.spotify.com/v1/me', headers=headers)
        user_profile = profile_response.json()
        return f"User Profile: {user_profile}"
    else:
        return 'Access token missing. Please authenticate.'

# function for user input
@spotify_bp.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    access_token = session.get('access_token')
    if access_token:
        artists = request.form.get('artists')
        songs = request.form.get('songs')
        genres = request.form.get('genres')
    #will need to implement actual logic here
        return 'Generated Playlist Page' 
    else:
        return 'Access token is missing. Please be sure to authenticate.'

@spotify_bp.route('/callback')
def callback():
    code = request.args.get('code')
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

    # Store the access token securely (e.g., in session for demo purposes)
    session['access_token'] = access_token

    return 'Authentication successful. Access token obtained.'
