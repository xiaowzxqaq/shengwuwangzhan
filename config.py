#!/usr/bin/env python3

""" config for server """

import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'questions.db')

MULTIPLE_CHOICE_QUESTION_START_ID = 69

