from django.shortcuts import render
from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.http import urlencode
import smtplib
from email.mime.text import MIMEText
import dotenv
import os

dotenv.load_dotenv()

# Create your views here.
class IndexView(generic.TemplateView):
  template_name = 'contact/index.html'
  pass

def send(request):
  #Config
  port = 587
  #smtp_server = 'smtp-relay.brevo.com'
  smtp_server = 'smtp.gmail.com'
  #login = os.getenv('MAIL_USER')
  #password = os.getenv('MAIL_PASS')
  login = os.getenv('GOOG_USER')
  password = os.getenv('GOOG_APP_PASS')
  sender_email = 'no-reply@drrawley.com'
  receiver_email = os.getenv('GOOG_DESTINATION')

  #Get contact info from the form
  contact = {}
  contact['name'] = request.POST['contact[name]']
  contact['email'] = request.POST['contact[email]']
  contact['phone'] = request.POST['contact[phone]']
  contact['message'] = request.POST['contact[message]']
  #Build message text
  text = f"""Name: {contact['name']}
    E-mail: {contact['email']}
    Phone: {contact['phone']}
    Message: {contact['message']}
    """

  #Create MIME Text object
  message = MIMEText(text, 'plain')
  message['Subject'] = "Test Email"
  message['From'] = sender_email
  message['To'] = receiver_email

  with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

  return HttpResponseRedirect("https://drrawley.com")
  pass