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
#from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, HTMLBody
import re

#twilio set up as backup
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("privatekeys.env")
twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_phone_number= os.environ.get("TWILIO_PHONE_NUMBER")



#TODO:
#Loop only checks newest email every 30 seconds. If 2 are sent within that window, one is ignored. Fix this.
#Parse text to connect to pump script
#Send texts with drink list to users, or to confirm that orders are received


# account credentials
username = os.environ.get("guser")
password = os.environ.get("gpass")


def save_attachment(part):
    filename = part.get_filename()
    if filename:
        with open(filename, 'wb') as f:
            f.write(part.get_payload(decode=True))

#Extracts the text from the .txt file sent to the email
def get_contents(pmsg):
    if not pmsg.is_multipart():
        pass
    for part in pmsg.walk():
        # extract content type of email
        content_type = part.get_content_type()
        content_disposition = str(part.get("Content-Disposition"))
        try:
            # get the email body
            body = part.get_payload(decode=True).decode()
        except:
            pass
        if content_type == "text/plain" and "attachment" not in content_disposition:
            # print text/plain emails and skip attachments, will print here for T-Mobile, but not for AT&T
            return body
        elif "attachment" in content_disposition:
            # print attachment contents, will print here for AT&T. Assumes that file is a .txt, because we should only be receiving texts
            filename = part.get_filename()
            if filename:
                save_attachment(part)
                f = open(filename, 'r')
                file_contents = f.read()
                
                return file_contents
    return "No text contents found"

def send_sms_twilio(to, body):
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body=body + '\nPlease do not reply to this number',
        from_=twilio_phone_number,
        to=to
    )
    print("Message sent to", to)

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

#Google Voice emails include the sender's phone number, so you can reply to them ??
def get_phone_from_gvoice(msg_from):
    # From field format: "(908) 361-2517" <15402517822.19083612517...@txt.voice.google.com>
    # Extract the 10-digit number from the display name
    match = re.search(r'\((\d{3})\)\s*(\d{3})-(\d{4})', msg_from)
    if match:
        return "+1" + match.group(1) + match.group(2) + match.group(3)
    return None


def process_order(content, phone):
    reply_to = f"{phone}@txt.voice.google.com"
    
#Main loop
def checkMail():
    imap_server = "imap.gmail.com"
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, password)
    status, messages = imap.select("INBOX")
    rem = int(messages[0])
 
    try:
        while True:
            status, messages = imap.select("INBOX")
            total = int(messages[0])
 
            if total != rem:
                # Fetch ALL new messages since last check
                for i in range(rem + 1, total + 1):
                    res, msg = imap.fetch(str(i), "(RFC822)")
                    for response in msg:
                        if isinstance(response, tuple):
                            parsed = email.message_from_bytes(response[1])
                            sender = parsed['From']
                            subject = parsed.get('Subject', '')
                            print(f"Email from: {sender}")
                            print(f"Subject: {subject}")
 
                            if "txt.voice.google.com" in sender:
                                phone = get_phone_from_gvoice(sender)
                                content = get_contents(parsed)
                                print(f"Text received from: {phone}")
                                print(f"Content: {content}")
                                process_order(content, phone)
                            else:
                                print("Ignored non-Google Voice email")
                rem = total
 
            print("Looped")
            time.sleep(5)
 
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        imap.close()
        imap.logout()
 

if __name__ == "__main__":
    print("Waiting for texts...")
    content, phone = checkMail()
    print(f"Order received: {content}")
    print(f"From: {phone}")