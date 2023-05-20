import smtplib, ssl
import os

port = 465
smtp_server = "smtp.gmail.com"
EMAIL = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
TARGET_EMAIL = os.environ.get('TARGET_EMAIL')

message = """\
Subject: GitHub Email Report

This is a test!
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, TARGET_EMAIL, message)