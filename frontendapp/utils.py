import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings
from datetime import datetime
from django.core.mail import EmailMultiAlternatives


def initialize_client():
    # Initialize the API client configuration
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY

    # Create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    return api_instance



# Send email function
def send_email(subject, message_content, from_name, from_email, to_email):
    # Ensure the email address is in a valid format
    if not isinstance(to_email, str) or not to_email.strip():
        raise ValueError("Invalid recipient email address.")
    
    # Create email
    email = EmailMultiAlternatives(
        subject,
        message_content,
        f"{from_name} <{from_email}>",
        [to_email],  # Make sure this is a list of valid email addresses
    )
    email.attach_alternative(message_content, "text/html")
    email.send()

def send_quote_notification(name, email, company, team_email, quote_details):
    current_year = datetime.now().year
    
    # Email content for user
    user_subject = 'Quote Request Confirmation - The Netforge Technologies'
    user_message_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <table align="center" width="100%" cellspacing="0" cellpadding="20" style="max-width: 600px; border: 1px solid #ddd; border-radius: 8px; background-color: #f9f9f9;">
            <tr>
                <td style="text-align: center;">
                    <img src="" alt="The Netforge Technologies" style="width: 150px;"/>
                </td>
            </tr>
            <tr>
                <td>
                    <h2 style="color: #0056b3;">Dear {name},</h2>
                    <p>Thank you for requesting a quote from <strong>The Netforge Technologies</strong>. We have received your request for your company <strong>{company}</strong>.</p>
                    <p><strong>Message details:</strong></p>
                    <pre style="background-color: #eee; padding: 10px; border-radius: 4px;">{quote_details}</pre>
                    <p>If you have any further questions, feel free to contact us at <a href="mailto:support@Netforgetours.com">support@Netforgetours.com</a> or call us at +91 7006998653, +91 9682123179.</p>
                    <p>We will be in touch with a quote soon. Thank you for choosing The Netforge Technologies!</p>
                    <p style="font-size: 0.9em; color: #777;">Note: This is an automatic confirmation. Our agent will reach out to you shortly.</p>
                </td>
            </tr>
            <tr>
                <td style="text-align: center; padding-top: 10px;">
                    <p style="font-size: 0.8em; color: #aaa;">&copy; {current_year} The Netforge Technologies. All rights reserved.</p>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    send_email(user_subject, user_message_content, "The Netforge Technologies", settings.DEFAULT_FROM_EMAIL, email)

    # Email content for team
    team_subject = 'New Quote Request Alert - System Notification | The Netforge Technologies'
    team_message_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <table align="center" width="100%" cellspacing="0" cellpadding="20" style="max-width: 600px; border: 1px solid #ddd; border-radius: 8px; background-color: #f9f9f9;">
            <tr>
                <td style="text-align: center;">
                    <img src="https://Netforgekashmir.com/images/Netforge_tour _and_tavels_loo.png" alt="The Netforge Technologies" style="width: 150px;"/>
                </td>
            </tr>
            <tr>
                <td>
                    <h2 style="color: #0056b3;">Dear Netforge Team,</h2>
                    <p>A new quote request from <strong>{name}</strong> for the company <strong>{company}</strong> has been received.</p>
                    <p><strong>Message details:</strong></p>
                    <pre style="background-color: #eee; padding: 10px; border-radius: 4px;">{quote_details}</pre>
                    <p>Please ensure a timely response.</p>
                    <p>Best Regards,<br>Your Netforge Tour and Travel Notification System</p>
                </td>
            </tr>
            <tr>
                <td style="text-align: center; padding-top: 10px;">
                    <p style="font-size: 0.8em; color: #aaa;">&copy; {current_year} The Netforge Technologies. All rights reserved.</p>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    send_email(team_subject, team_message_content, "The Netforge Technologies", settings.DEFAULT_FROM_EMAIL, team_email)

def send_comment_notification(name, email, website, comment_details, team_email):
    current_year = datetime.now().year

    def prepare_email_content(recipient_type):
        if recipient_type == 'user':
            subject = 'Comment Confirmation - The Netforge Technologies'
            message_content = f"""
            <html>
            <body style="font-family: Arial, sans-serif; color: #333;">
                <table align="center" width="100%" cellspacing="0" cellpadding="20" style="max-width: 600px; border: 1px solid #ddd; border-radius: 8px; background-color: #f9f9f9;">
                    <tr>
                        <td style="text-align: center;">
                            <img src="https://Netforgekashmir.com/images/Netforge_tour_and_tavels_loo.png" alt="The Netforge Technologies" style="width: 150px;"/>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <h2 style="color: #0056b3;">Dear {name},</h2>
                            <p>Thank you for your review! We have received your Comment and our team will get in touch with you shortly.</p>
                            <p><strong>Comment details:</strong></p>
                            <pre style="background-color: #eee; padding: 10px; border-radius: 4px;">{comment_details}</pre>
                            <p>We appreciate your interest in our services. If you have any further questions, feel free to reach out to us at <a href="mailto:support@Netforgetours.com">support@Netforgetours.com</a> | +91 7006998653, +91 9682123179.</p>
                            <p>Best regards,<br>The Netforge Technologies Team</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: center; padding-top: 10px;">
                            <p style="font-size: 0.8em; color: #aaa;">&copy; {current_year} The Netforge Technologies. All rights reserved.</p>
                        </td>
                    </tr>
                </table>
            </body>
            </html>
            """
            return subject, message_content

        elif recipient_type == 'team':
            subject = 'New Comment Alert - System Notification | The Netforge Technologies'
            message_content = f"""
            <html>
            <body style="font-family: Arial, sans-serif; color: #333;">
                <table align="center" width="100%" cellspacing="0" cellpadding="20" style="max-width: 600px; border: 1px solid #ddd; border-radius: 8px; background-color: #f9f9f9;">
                    <tr>
                        <td style="text-align: center;">
                            <img src="https:/.png" alt="The Netforge Technologies" style="width: 150px;"/>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <h2 style="color: #0056b3;">Hello Netforge Admin,</h2>
                            <p>A new comment has been received from <strong>{name}</strong> ({email}).</p>
                            <p><strong>Comment details:</strong></p>
                            <pre style="background-color: #eee; padding: 10px; border-radius: 4px;">{comment_details}</pre>
                            <p>Thank you for providing excellent service!</p>
                            <p>Best Regards,<br>Your Netforge Technologies Comment Notification System</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="text-align: center; padding-top: 10px;">
                            <p style="font-size: 0.8em; color: #aaa;">&copy; {current_year} The Netforge Technologies. All rights reserved.</p>
                        </td>
                    </tr>
                </table>
            </body>
            </html>
            """
            return subject, message_content

    # Prepare and send email to user
    user_subject, user_message_content = prepare_email_content('user')
    send_email(user_subject, user_message_content, "The Netforge Technologies", settings.DEFAULT_FROM_EMAIL, email)

    # Prepare and send email to team
    team_subject, team_message_content = prepare_email_content('team')
    send_email(team_subject, team_message_content, "The Netforge Technologies", settings.DEFAULT_FROM_EMAIL, team_email)
