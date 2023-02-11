import os

from flask import Blueprint, render_template, session, send_file
from website import login_is_required

views = Blueprint('views', __name__)

os.environ["OAUTH_INSECURE_TRANSPORT"] = "1"


@views.route('/go-to-home/')
@login_is_required
def go_to_home():
    return render_template('home.html', session=session)


@views.route('/go-to-contact/')
def go_to_contact():
    return render_template('contact.html')


@views.route('/')
def intro():
    return render_template('intro.html')

@views.route('/privacy/')
def privacy():
    return send_file('static/Policies/AquaReWrite Privacy Policies.pdf')