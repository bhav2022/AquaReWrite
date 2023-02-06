from flask import Blueprint, render_template
from flask_login import login_required, current_user

posts = Blueprint('posts', __name__)

@posts.route('/UniqID_admin-23456789_PostDate-20230201_RandNum-9876543210_Substr-aquaAd', methods=['POST', 'GET'])
@login_required
def devices_story():
  return render_template('devices_story.html')
