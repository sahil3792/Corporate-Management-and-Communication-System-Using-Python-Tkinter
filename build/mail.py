import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, to_email):
    # Email configuration
    sender_email = 'sahilshaikhykgn@gmail.com'  # Change to your email
    sender_password = 'your_password'  # Change to your email password
    smtp_server = 'smtp.example.com'  # Change to your SMTP server

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach message to email
    msg.attach(MIMEText(message, 'plain'))

    # Send email
    try:
        server = smtplib.SMTP(smtp_server, 587)  # Change port if required
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

# Example usage
def example_usage():
    subject = 'Test Email'
    message = 'This is a test email sent from Skive.'
    to_email = 'sahilharshalv@gmail.com'  # Change to recipient's email
    send_email(subject, message, to_email)

# Call the function to send the email
example_usage()