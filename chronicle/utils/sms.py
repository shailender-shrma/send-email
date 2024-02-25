import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
from dotenv import load_dotenv
import os

load_dotenv()


def send_sms(email):
    mailchimp = MailchimpTransactional.Client(os.environ.get("API_KEY"))
    message = {
        "from_email": "sshailender@mailchimp.com",
        "subject": "Hello world",
        "text": "Welcome to quest!",
        "to": [{"email": email, "Stype": "to"}],
    }

    try:
        response = mailchimp.messages.send({"message": message})
        return "API called successfully: {}".format(response)
    except ApiClientError as error:
        return "An exception occurred: {}".format(error.text)
