#!/usr/bin/python

#
# simple mailer for artillery
#
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
from src.core import *

# username for smtp server
user = check_config("SMTP_USERNAME=")
# pw for smtp server
pwd = check_config("SMTP_PASSWORD=")
# smtp address for smtp
smtp_address = check_config("SMTP_ADDRESS=")
# port we use, default is 25
smtp_port = check_config("SMTP_PORT=")
# convert to integer
smtp_port = int(smtp_port)
# who we are sending the email to
smtp_to = check_config("SMTP_TO")

def mail(to, subject, text):
        msg = MIMEMultipart()
        # message from
        msg['From'] = user
        # message to
        msg['To'] = to
        # subject line
        msg['Subject'] = subject
        msg.attach(MIMEText(text))
        # prep the smtp server
        mailServer = smtplib.SMTP("%s" % (smtp_address), smtp_port)
        # send ehlo
        mailServer.ehlo()
        # tls support?
        mailServer.starttls()
        # some servers require ehlo again
        mailServer.ehlo()
        # login to server
        mailServer.login(user, pwd)
        # send email
        mailServer.sendmail(smtp_to, to, msg.as_string())
        # close connection
        mailServer.close()
