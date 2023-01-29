from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/go-to-home')
@login_required
def go_to_home():
  return render_template('home.html', user=current_user)


@views.route('/go-to-contact')
def go_to_contact():
  return render_template('contact.html', user=current_user)

@views.route('/devices-story')
def devices_story():
  return render_template('devices_story.html', user=current_user)