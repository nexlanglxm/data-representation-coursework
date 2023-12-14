from flask import Blueprint, redirect, request, session, jsonify, url_for
import requests
from routes.auth import get_access_token, get_user_profile  # Import necessary functions from auth.py
from dotenv import load_dotenv
import os

spotify_bp = Blueprint('spotify', __name__) # Create a Blueprint object

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')


def create_playlist(user_id, access_token, playlist_name):
    '''
    Handles the API call to create a playlist on Spotify
    
    Args:
        user_id: Spotify user ID
        access_token: Access token to authenticate API calls
        playlist_name: Name of the playlist to be created
    Returns:
        requests.Response: Contains the result of the playlist creation request
    '''
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

@spotify_bp.route('/get_user_profile')
def get_user_profile_route():
    '''
    Route to get user profile data
    
    Returns:
        JSON: User profile data or error message
    '''
    access_token = session.get('access_token')
    if access_token: # Check if access token is present
        profile_data = get_user_profile(access_token)
        return jsonify(profile_data)
    else:
        return 'Access token missing. Please authenticate.'

@spotify_bp.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    '''
    Route to generate a playlist based on user input when the form is submitted
    
    Returns:
        str: Success or error message or redirects to login
    '''
    access_token = session.get('access_token')
    if access_token:
        playlist_name = request.form.get('playlist_name') # Get the playlist name from the form
        profile_data = get_user_profile(access_token)
        if profile_data: # Check if profile data is present
            user_id = profile_data.get('id')
            create_playlist_response = create_playlist(user_id, access_token, playlist_name)
            if create_playlist_response.status_code == 201:
                return 'Playlist created successfully!'
            else:
                return f'Failed to create playlist. Status code: {create_playlist_response.status_code}'
        else:
            return 'Failed to fetch user profile.'
    else:
        return redirect(url_for('auth.login')) # Redirect to login if access token is missing