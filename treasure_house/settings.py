# -*- coding: utf-8 -*-
"""
    :author: Guowei
"""
import os
import sys

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('TREASURE_HOUSE Admin', MAIL_USERNAME)

    TREASURE_HOUSE_EMAIL = os.getenv('TREASURE_HOUSE_EMAIL')
    TREASURE_HOUSE_POST_PER_PAGE = 10
    TREASURE_HOUSE_MANAGE_POST_PER_PAGE = 15
    TREASURE_HOUSE_COMMENT_PER_PAGE = 15
    TREASURE_HOUSE_MOVIE_PER_PAGE = 18
    # ('theme name', 'display name')
    TREASURE_HOUSE_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    TREASURE_HOUSE_SLOW_QUERY_THRESHOLD = 1


class DevelopmentConfig(BaseConfig):
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'test'
    USERNAME = 'root'
    PASSWORD = '123456'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8". \
        format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'th'
    USERNAME = 'root'
    PASSWORD = '123456'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8". \
        format(username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
