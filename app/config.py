import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'andthentherewerenone'
    UPLOAD_FOLDER = 'app/uploads/'
    ALLOWED_EXTENSIONS = {'docx'}
    DOWNLOAD_FOLDER = 'app/downloads/'
