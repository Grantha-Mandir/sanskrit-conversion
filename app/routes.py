from app import app
from flask import request, redirect, flash,url_for, render_template, send_from_directory
from  app.config import Config
from werkzeug.utils import secure_filename
from references.balaram_to_unicode import process_docx, clean_directory
import os
import shutil
#@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


def allowed_file(filename):
    conf = Config()
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in conf.ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # First clear Download folder
            clean_directory(app.config['DOWNLOAD_FOLDER'])
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded. Processing')
            new_file_name = process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            # Clean up Upload folder
            clean_directory(app.config['UPLOAD_FOLDER'])
            return redirect(url_for('uploaded_file', filename=new_file_name))

        else:
            flash('Allowed file types are .docx')
            return redirect(request.url)

    return render_template('index.html')



def process_file(path,filename):
    conf = Config()
    new_file_name = process_docx(path, filename, conf.DOWNLOAD_FOLDER)
    return new_file_name



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'],filename, as_attachment=True)

