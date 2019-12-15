import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'andthentherewerenone'
    UPLOAD_FOLDER = '/home/bhushan/sanskrit-conversion/app/uploads/'
    ALLOWED_EXTENSIONS = {'docx'}
    DOWNLOAD_FOLDER = '/home/bhushan/sanskrit-conversion/app/downloads/'
