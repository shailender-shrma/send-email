# import mailchimp_marketing as MailchimpMarketing
# from mailchimp_marketing.api_client import ApiClientError

# try:
#   client = MailchimpMarketing.Client()
#   client.set_config({
#     "api_key": "9242be913605a8542b8261664db22a78-us18",

#   })

#   response = client.automations.list_all_workflow_emails("workflow_id")
#   print(response)
# except ApiClientError as error:
#   print("Error: {}".format(error.text))
# import mailchimp_marketing as MailchimpMarketing
# from mailchimp_marketing.api_client import ApiClientError

# try:
#     client = MailchimpMarketing.Client()
#     client.set_config(
#         {"api_key": "9242be913605a8542b8261664db22a78-us18", "server": "/"}
#     )

#     response = client.automations.get_workflow_email(
#         "sshailender26@gmail.com", "sshailender26@gmail.com"
#     )
#     print(response)
# except ApiClientError as error:
#     print("Error: {}".format(error.text))
import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError


def run():
    try:
        mailchimp = MailchimpTransactional.Client("md-BN2YiadoZCW4iB_pWIZWew")
        response = mailchimp.users.ping()
        print("API called successfully: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))


run()
