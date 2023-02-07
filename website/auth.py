import os
import pathlib

import google.auth.transport.requests
from google.oauth2 import id_token
from pip._vendor import cachecontrol
import google.auth.transport.requests
import requests
from flask import Blueprint, render_template, request, flash, redirect, session, abort
from . import login_is_required, flow, GOOGLE_CLIENT_ID

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

auth = Blueprint('auth', __name__)


@auth.route('/login-page', methods=['POST', 'GET'])
def login():
    autherization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(autherization_url)


@login_is_required
@auth.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@auth.route('/callback')
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500)  # State not matched

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    user_name = id_info["name"]
    return redirect("/go-to-home", session["name"])
