from flask import Blueprint, request, session, jsonify
import requests
from auth import get_access_token, get_user_profile  # Import necessary functions from auth.py

spotify_bp = Blueprint('spotify', __name__)

CLIENT_ID = '91ad79bc13fe4e21b070ff8c7a8271ca'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'  # This needs to be safe
REDIRECT_URI = 'http://127.0.0.1:5000/callback'

def create_playlist(user_id, access_token, playlist_name):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    playlist_data = {
        'name': playlist_name,
        'description': 'Generated playlist based on user input',
        'public': False  # Change to True if you want the playlist to be public
    }
    create_playlist_url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
    create_playlist_response = requests.post(create_playlist_url, headers=headers, json=playlist_data)
    return create_playlist_response

@spotify_bp.route('/callback')
def callback():
    code = request.args.get('code')
    access_token = get_access_token(code)
    session['access_token'] = access_token
    return 'Authentication successful. Access token obtained.'

@spotify_bp.route('/get_user_profile')
def get_user_profile_route():
    access_token = session.get('access_token')
    if access_token:
        profile_data = get_user_profile(access_token)
        return jsonify(profile_data)
    else:
        return 'Access token missing. Please authenticate.'

@spotify_bp.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    access_token = session.get('access_token')
    if access_token:
        playlist_name = request.form.get('playlist_name')
        profile_data = get_user_profile(access_token)
        if profile_data:
            user_id = profile_data.get('id')
            create_playlist_response = create_playlist(user_id, access_token, playlist_name)
            if create_playlist_response.status_code == 201:
                return 'Playlist created successfully!'
            else:
                return f'Failed to create playlist. Status code: {create_playlist_response.status_code}'
        else:
            return 'Failed to fetch user profile.'
    else:
        return 'Access token is missing. Please authenticate.'