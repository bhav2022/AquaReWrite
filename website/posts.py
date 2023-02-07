from flask import Blueprint, render_template

from website import login_is_required

posts = Blueprint('posts', __name__)


@posts.route('/UniqID_admin-23456789_PostDate-20230201_RandNum-9876543210_Substr-aquaAd', methods=['POST', 'GET'])
@login_is_required
def devices_story():
    return render_template('devices_story.html')
