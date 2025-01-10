import json
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Function to load JSON data from a file
def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to display the hero statistics in a table
def display_hero_statistics(json_data):
    # Convert JSON data to a pandas DataFrame
    df = pd.DataFrame(json_data)
    
    # Display the DataFrame
    print(df)

# Function to send email with JSON file attachment
def send_email(subject, body, to_email, attachment_path):
    from_email = os.getenv('EMAIL_USER')
    from_password = os.getenv('EMAIL_PASS')

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file
    attachment = MIMEBase('application', 'octet-stream')
    with open(attachment_path, 'rb') as file:
        attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
    msg.attach(attachment)

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.send_message(msg)
    server.quit()

# Main function to load data, display it, and send email
def main():
    # Load hero data from JSON file
    hero_statistics = load_json_data('hero_statistics.json')
    
    # Display the hero statistics
    display_hero_statistics(hero_statistics)
    
    # Email details
    subject = "Hero Statistics JSON File"
    body = "Please find attached the hero_statistics.json file."
    to_email = "tretre33333333@gmail.com"
    attachment_path = 'hero_statistics.json'

    # Send the email with attachment
    send_email(subject, body, to_email, attachment_path)

if __name__ == "__main__":
    main()