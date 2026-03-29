#AIzaSyCrCyfLHsXhD_AgbDyE66re2LI9ylX3OKk

import imaplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import email
from email.header import decode_header
from itertools import chain
import webbrowser
import os
import time
import select
import sys
from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, HTMLBody
import re

def send_email_gmail(to, subject, body):
    # Create an SMTP connection to Gmail's server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Use TLS port
    smtp_username = username
    smtp_password = password

    try:
        smtp_server = smtplib.SMTP(smtp_server, smtp_port)
        smtp_server.starttls()
        smtp_server.login(smtp_username, smtp_password)



        # Attach the body
        message = ("From: %s\r\n" % smtp_username + "To: %s\r\n" % to + "Subject: %s\r\n" % '' + "\r\n" + body)


        # Send the email
        smtp_server.sendmail(smtp_username, to, message)

        # Close the SMTP connection
        smtp_server.quit()

        print(f"Email sent to {to}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


def checkForCMDInput():
    message = ""
    while True:
        time.sleep(15)
        ready, _, _ = select.select([sys.stdin], [], [], 0.1)  # Timeout is 0.1 seconds
        if ready:
            message = sys.stdin.readline().strip()
            if message: 
                print(f"Command Line Order: {message}")
                return message
        
        time.sleep(0.1)

# Modify the checkMail function as needed for Gmail, but keep the IMAP connection logic.

#Main loop
def checkMail():
    imap_server = "imap.gmail.com"

    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, password)
    status, messages = imap.select("INBOX")
    messages = int(messages[0])
    rem = messages

    while True:
        #imap = imaplib.IMAP4_SSL(imap_server)
        #imap.login(username, password)
        status, messages = imap.select("INBOX")
        messages = int(messages[0])

        if messages != rem:
            res, msg = imap.fetch(str(messages), "(RFC822)") 
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    print(msg['From'])
                    return get_contents(msg), msg['From']
            rem = messages

        print("Looped")
        time.sleep(5)

    # Close the connection and logout (you can move this to outside the loop)
    imap.close()
    imap.logout()
