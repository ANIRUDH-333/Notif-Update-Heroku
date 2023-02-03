import hashlib
import requests
import time
import smtplib

def get_website_content(url):
    response = requests.get(url)
    return response.content

def send_email(subject, message, recipient):
    # Replace sender_email and sender_password with your own email and password
    sender_email = "aniedpuganti@gmail.com"
    sender_password = "Ani@212003"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, sender_password)
        message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, recipient, message)
        print("Email sent!")
        server.quit()
    except Exception as e:
        print("Error: %s" % e)

# Define the URL of the website you want to monitor
url = "https://icai.nic.in/caresult/"

# Define the recipient email address to receive notifications
recipient = "venkatamohit2005@gmail.com"
content = get_website_content(url)
# Initialize a hash to compare with the new hash after each iteration
previous_hash = hashlib.sha256(content)
# print(previous_hash)
# Write a loop that periodically checks the website for changes
while True:
    # Get the website content
    content = get_website_content(url)

    # Calculate the hash of the content
    current_hash = hashlib.sha256(content)
    # print(current_hash)
    # print(previous_hash.hexdigest())
    # print(current_hash.hexdigest())
    # If the hash has changed, send a notification email
    if current_hash.hexdigest() != previous_hash.hexdigest():
        subject = "Website Update Notification"
        print(subject)
        message = "The website has been updated!"
        send_email(subject, message, recipient)
        break
        
    # Update the previous hash for the next iteration
    previous_hash = current_hash

    # Wait for some time before checking again
    time.sleep(60)  # Check every 60 seconds
