import os

# Getting the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'kiosk.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False