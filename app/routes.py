from app import app
from flask import request, redirect, flash,url_for, render_template, send_from_directory
from  app.config import Config
from werkzeug.utils import secure_filename
import os
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
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded. Processing')
            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('uploaded_file', filename=filename))
        else:
            flash('Allowed file types are .doc, .docx')
            return redirect(request.url)

    return render_template('index.html')


def change_filename(filename):
    parts = filename.split('.')[:-1]
    parts.append('processed')
    f_name = '_'.join(parts) + '.docx'
    return f_name

def process_file(path,filename):
    conf = Config()
    with open(path,'rb') as f:
        doc = f.read()
    new_file = change_filename(filename)
    with open(os.path.join(conf.DOWNLOAD_FOLDER,new_file),'wb') as f:
        f.write(doc)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    new_file = change_filename(filename)
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], new_file, as_attachment=True)

