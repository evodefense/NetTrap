import requests
import time

# Set up your canary token URL and notification email address
CANARY_TOKEN_URL = "https://canarytokens.org/generate/[YOUR_TOKEN_ID]"
NOTIFICATION_EMAIL = "[YOUR_EMAIL_ADDRESS]"

# Set up a function to send an email notification
def send_notification(subject, body):
    # Replace [YOUR_EMAIL_ADDRESS] and [YOUR_EMAIL_PASSWORD] with your email address and password
    email_auth = ("[YOUR_EMAIL_ADDRESS]", "[YOUR_EMAIL_PASSWORD]")
    email_to = NOTIFICATION_EMAIL
    email_subject = subject
    email_body = body

    # Use the requests library to send an email via the Mailgun API
    response = requests.post(
        "https://api.mailgun.net/v3/[YOUR_MAILGUN_DOMAIN]/messages",
        auth=email_auth,
        data={"from": "[YOUR_EMAIL_ADDRESS]",
              "to": [email_to],
              "subject": email_subject,
              "text": email_body})
    return response

# Set up a loop to check the canary token URL every 5 minutes
while True:
    # Make a request to the canary token URL
    response = requests.get(CANARY_TOKEN_URL)

    # If the URL has been accessed, send a notification email
    if response.status_code == 200:
        send_notification("Intrusion detected!", "Your canary token has been accessed. This may indicate an unauthorized access to your system.")
    
    # Sleep for 5 minutes before checking the URL again
    time.sleep(300)
