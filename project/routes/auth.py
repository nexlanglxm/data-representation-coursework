from flask import Blueprint, redirect, session, request, jsonify, url_for
import requests
import hashlib
import base64
import secrets
from dotenv import load_dotenv
import os

auth_bp = Blueprint('auth', __name__)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

def generate_code_verifier():
    return base64.urlsafe_b64encode(secrets.token_bytes(32)).decode('utf-8').rstrip('=')

def generate_code_challenge(code_verifier):
    code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    return base64.urlsafe_b64encode(code_challenge).decode('utf-8').rstrip('=')

@auth_bp.route('/login')
def login():
    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)
    
    session['code_verifier'] = code_verifier

    auth_url = 'https://accounts.spotify.com/authorize'
    scopes = 'user-read-private user-read-email'  # Define required scopes
    auth_params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': scopes,
        'code_challenge': code_challenge,
        'code_challenge_method': 'S256'
    }
    
    return redirect(f"{auth_url}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={scopes}&code_challenge={code_challenge}&code_challenge_method=S256")

@auth_bp.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    code_verifier = session.get('code_verifier')
    access_token = get_access_token(code, code_verifier)
    session['access_token'] = access_token
    
    return redirect(url_for('spotify.generate_playlist'))

@auth_bp.route('/logout')
def logout():
    if 'access_token' in session:
        access_token = session['access_token']
        session.pop('access_token') #clears the access token from the session 
        
    return 'Logged out successfully!'

def get_access_token(code, code_verifier):
    token_url = 'https://accounts.spotify.com/api/token' # URL to get token from Spotify accounts
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'code_verifier': code_verifier,
        'client_secret': CLIENT_SECRET,
    }
    token_response = requests.post(token_url, data=token_data)
    access_token = token_response.json().get('access_token')
    return access_token

def get_user_profile(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    profile_response = requests.get('https://api.spotify.com/v1/me', headers=headers)
    return profile_response.json()