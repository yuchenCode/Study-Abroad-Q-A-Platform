from flask import render_template, redirect, request, url_for, flash, send_from_directory, make_response, current_app
from flask_login import login_user, logout_user, login_required, current_user
from .. import db
from . import recruitment
from ..models import Resume
import os


@recruitment.route('/mresumes', methods=['GET', 'POST'])
def my_resumes():
    resumes = current_user.resumes
    return render_template('recruitment/mresume.html', resumes=resumes, panel_id=1)


@recruitment.route('/mresumes_pass', methods=['GET', 'POST'])
def my_resumes_pass():
    resumes = current_user.resumes
    _resumes = [resume for resume in resumes if resume.status == 1]
    return render_template('recruitment/mresume.html', resumes=_resumes, panel_id=2)


@recruitment.route('/mresumes_inprogress', methods=['GET', 'POST'])
def my_resumes_inprogress():
    resumes = current_user.resumes
    _resumes = [resume for resume in resumes if resume.status == 0]
    return render_template('recruitment/mresume.html', resumes=_resumes, panel_id=3)


@recruitment.route('/mresumes_dismiss', methods=['GET', 'POST'])
def my_resumes_dismiss():
    resumes = current_user.resumes
    _resumes = [resume for resume in resumes if resume.status == 2]
    return render_template('recruitment/mresume.html', resumes=_resumes, panel_id=4)


@recruitment.route('/download/<filename>', methods=['GET', 'POST'])
def download_my_resume(filename):
    if request.method == 'GET':
        filepath = os.path.join(current_app.root_path, 'static/resumes')
        return send_from_directory(filepath, filename, as_attachment=True)




