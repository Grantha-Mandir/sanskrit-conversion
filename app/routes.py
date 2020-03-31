from app import app
from flask import request, redirect, flash,url_for, render_template, send_from_directory
from  app.config import Config
from werkzeug.utils import secure_filename
from references.balaram_to_unicode import process_docx, clean_directory
import os, flask

'''
def validate_upload(f):
  def wrapper():
    if 'completed' not in flask.session or not flask.session['completed']:
      return flask.redirect('/')
    return f()
  return wrapper
'''


@app.route('/index')
def index():
    return render_template('index.html')


def allowed_file(filename):
    conf = Config()
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in conf.ALLOWED_EXTENSIONS

#@validate_upload
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    session_name = flask.session['username']
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        source_font = request.form['Select'].lower()
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # First clear Upload folder

            upload_dir = os.path.join(full_path(app.config['UPLOAD_FOLDER']),session_name)
            download_dir = os.path.join(full_path(app.config['DOWNLOAD_FOLDER']),session_name)
            filename = secure_filename(file.filename)
            dirs = [upload_dir, download_dir]
            for dir in dirs:
                if os.path.exists(dir):
                    clean_directory(dir)
                else:
                    os.mkdir(dir)

            file.save(os.path.join(full_path(app.config['UPLOAD_FOLDER']),session_name, filename))
            flash('File successfully uploaded. Processing')
            new_file_name = process_file(os.path.join(upload_dir, filename),session_name, filename, source_font)
            # Clean up Upload folder
            clean_directory(upload_dir)
            #new_file_name = os.path.join(session_name,new_file_name)
            return redirect(url_for('uploaded_file', filename=new_file_name))

        else:
            flash('Allowed file types are .docx')
            return redirect(request.url)

    return render_template('index.html')



def process_file(path,user_name,filename, source_font):
    conf = Config()
    new_file_name = process_docx(path, user_name, filename, full_path(conf.DOWNLOAD_FOLDER), source_font)
    return new_file_name


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    session_name = flask.session['username']
    upload_folder = full_path(app.config['DOWNLOAD_FOLDER'])
    return send_from_directory(os.path.join(upload_folder,session_name),filename, as_attachment=True)



@app.route('/', methods = ['GET'])
def home():
  return render_template('login_form.html')

@app.route('/second', methods=['POST'])
def second():
  username = flask.request.form['username']
  flask.session['username'] = username
  flask.session['completed'] = True
  return flask.redirect(url_for('index'))

def full_path(path):
    full_path = os.path.abspath(path)
    while not os.path.exists(full_path):
        cwd = os.getcwd()
        base = os.path.split(cwd)[0]
        full_path = os.path.join(base,path)
    return full_path