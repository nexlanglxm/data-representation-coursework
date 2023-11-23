from flask import Blueprint, redirect

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


@auth_bp.route('/logout')
def logout():
    # Placeholder logic for logout
    return 'Logout Page'

# Other authentication-related routes