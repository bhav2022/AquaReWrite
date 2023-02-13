import os

from flask import Blueprint, render_template, session, request, flash
from website import login_is_required, allowed_files
from werkzeug.utils import secure_filename
from datetime import datetime


posts = Blueprint('posts', __name__)


@posts.route('/UniqID_admin-23456789_PostDate-20230201_RandNum-9876543210_Substr-aquaAd', methods=['POST', 'GET'])
@login_is_required
def devices_story():
    return render_template('devices_story.html')

@posts.route('/user-submission/', methods=['GET', 'POST'])
def user_sub():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            new_filename = f'{session["name"]}_{filename.split(".")[0]}-{str(datetime.now())}-{filename.split(".")[1]}'
            new_filename = new_filename.replace('_', '-')
            flash("uploaded", category='success')
        else:
            flash("Wrong Extension", category="danger")
    return render_template('file_submission.html')