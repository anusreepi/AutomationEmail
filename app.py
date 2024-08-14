import csv
import os
import uuid
from flask import Flask, redirect, render_template_string, url_for, request
from flask_mail import Mail, Message
import schedule
import time
import pandas as pd
import threading
from datetime import datetime, timedelta
from urllib.parse import quote

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='arkaconsultancy.xyz',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='anushree@arkaconsultancy.xyz',
    MAIL_PASSWORD='&hZRM;$i]ha#',
    SERVER_NAME='ec2-13-233-17-191.ap-south-1.compute.amazonaws.com',
    APPLICATION_ROOT='/',
    PREFERRED_URL_SCHEME='http'
)

mail = Mail(app)

follow_up_data = {}
new_data = pd.DataFrame()
subject_not=""
body_not=""
no_datetime=""
tracking_url_yes=""

sender_email=""
initial_subject=""
subject_no=""
body_no=""
no_datetime4=""
subject_no4=""
body_no4=""
no_datetime6=""
subject_no6=""
body_no6=""
no_datetime10=""
subject_no10=""
body_no10=""
no_datetime14=""
subject_no14=""
body_no14=""
subject_subscribe=""
body_subscribe=""
datetime_subscribe=""
tracking_url_no="https://arkaconsultancy.xyz/"
global filename
filename=''
@app.route('/track_click')
def track_click():
    email = request.args.get('email')
    response = request.args.get('response')
    if email in follow_up_data:
        name = follow_up_data[email]['name']
        subject_yes = follow_up_data[email]['subject_yes']
        body_yes = follow_up_data[email]['body_yes']
        yes_datetime = follow_up_data[email]['yes_datetime']

        subject_unsubscribe = follow_up_data[email]['subject_unsubscribe']
        body_unsubscribe = follow_up_data[email]['body_unsubscribe']
        datetime_unsubscribe = follow_up_data[email]['datetime_unsubscribe']

        # tracking_url_yes = follow_up_data[email]['tracking_url_yes']
        # tracking_url_no = follow_up_data[email]['tracking_url_no']
        tracking_url_subscribe = follow_up_data[email]['tracking_url_subscribe']
        tracking_url_unsubscribe = follow_up_data[email]['tracking_url_unsubscribe']

        tracking_url_not4 = follow_up_data[email]['tracking_url_not4']
        subject_no4 = follow_up_data[email]['subject_no4']
        body_no4 = follow_up_data[email]['body_no4']
        no_datetime4 = follow_up_data[email]['no_datetime4']

        tracking_url_not6 = follow_up_data[email]['tracking_url_not6']
        subject_no6 = follow_up_data[email]['subject_no6']
        body_no6 = follow_up_data[email]['body_no6']
        no_datetime6 = follow_up_data[email]['no_datetime6']

        tracking_url_not10 = follow_up_data[email]['tracking_url_not10']
        subject_no10 = follow_up_data[email]['subject_no10']
        body_no10 = follow_up_data[email]['body_no10']
        no_datetime10 = follow_up_data[email]['no_datetime10']

        tracking_url_not14 = follow_up_data[email]['tracking_url_not14']
        subject_no14 = follow_up_data[email]['subject_no14']
        body_no14 = follow_up_data[email]['body_no14']
        no_datetime14 = follow_up_data[email]['no_datetime14']
        initial_subject = follow_up_data[email]['initial_subject']
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  

        with open(filename, 'a') as log_file:
                   log_file.write(f"{email},{response},{datetime.now()}\n")
        if response:
            if response == 'yes':
                # Schedule follow-up email for Yes response
                schedule_one_time_task(sender_email,yes_datetime, email, name, subject_yes, body_yes, tracking_url_subscribe, tracking_url_unsubscribe)
                return redirect(tracking_url_yes)
            elif response == 'subscribe':
                # Schedule follow-up email for Subscribe response
                schedule_one_time_task_without_url(sender_email,datetime_subscribe, email, name, subject_subscribe, body_subscribe)
                return redirect("https://arkaconsultancy.xyz/")
                # Schedule follow-up email for Yes response    
                schedule_one_time_task(sender_email,yes_datetime, email, name, subject_yes, body_yes)   
                return redirect(tracking_url_yes)           

            elif response == 'unsubscribe':
                # Schedule follow-up email for Unsubscribe response
                schedule_one_time_task_without_url(sender_email,datetime_unsubscribe, email, name, subject_unsubscribe, body_unsubscribe)
                return redirect("https://arkaconsultancy.xyz/")
            elif response=="Yes":
                click_time = datetime.now()    
                schedule_follow_up_email(sender_email,click_time,email,name, subject_yes, body_yes)
                return redirect(tracking_url_yes)
            elif response == 'Unsubscribe':
                # Schedule follow-up email for Unsubscribe response
                schedule_one_time_task_without_url(sender_email,email, name, subject_unsubscribe, body_unsubscribe)
                return redirect("https://arkaconsultancy.xyz/")
    else:
        return "No follow-up data found for the provided email."

def check_for_non_opens():
    print("Scheduling email for non openers")
    responses = extract_responses_from_log(filename)

                schedule_follow_up_email_without_url(sender_email,email, name, subject_unsubscribe, body_unsubscribe)
                return redirect("https://arkaconsultancy.xyz/")   
            elif response=='no':
                return redirect("https://arkaconsultancy.xyz/")             
    else:
        return "No follow-up data found for the provided email."          
def check_for_yes_response(datetime1,subject1,body1):
    df = extract_responses_from_log(filename)
    df_yes=df[df['Response'] == 'yes']
    df3 = pd.merge(new_data, df_yes[['Email']], on='Email')
    print(df3)
    for _, row in  df3.iterrows():
            recipient = row['Email']
            name = row['Name']    
            schedule_one_time_task_without_url(sender_email,datetime1,recipient,name,subject1,body1)
def schedule_task_at_yes(datetime1,subject1,body1):
    # Parse the provided time string
    target_datetime = datetime.strptime(datetime1, "%Y-%m-%dT%H:%M")
    time_before = target_datetime - timedelta(minutes=2)
    
    # Get the current time
    now = datetime.now()
    
    # Calculate the delay in seconds
    delay = (time_before - now).total_seconds()
    # Schedule the check_for_non_opens function
    print(delay)
    if delay > 0:
        threading.Timer(delay, check_for_yes_response,args=[datetime1,subject1,body1]).start()
def check_for_non_opens(datetime1,subject1,body1):  
    responses = extract_responses_from_log(filename)    
>>>>>>> origin/master
    merged_df = pd.merge(new_data, responses[['Email']], on='Email', how='left', indicator=True)
    non_responders_df = merged_df[merged_df['_merge'] == 'left_only'][['Email', 'Name']]
    print(non_responders_df) 
    for _, row in  non_responders_df.iterrows():
            recipient = row['Email']
<<<<<<< HEAD
            name = row['Name']
            schedule_daily_task(sender_email,not_datetime,recipient, name, subject_not,body_not,tracking_url_yes, tracking_url_no)
def schedule_task_at(not_datetime_str):
    # Parse the provided time string
    print("Checking non openers")
    target_datetime = datetime.strptime(not_datetime_str, "%Y-%m-%dT%H:%M")
    time_before = target_datetime - timedelta(minutes=2)

    # Get the current time
    now = datetime.now()
=======
            name = row['Name']    
            schedule_daily_task6(sender_email,datetime1,recipient, name, subject1,body1,tracking_url_yes)
def schedule_task_at(datetime1,subject1,body1):
    # Parse the provided time string
    target_datetime = datetime.strptime(datetime1, "%Y-%m-%dT%H:%M")
    time_before = target_datetime - timedelta(minutes=2)   
    # Get the current time
    now = datetime.now()  
>>>>>>> origin/master
    # Calculate the delay in seconds
    delay = (time_before - now).total_seconds()
    # Schedule the check_for_non_opens function
    print(delay)
    if delay > 0:
<<<<<<< HEAD
        threading.Timer(delay, check_for_non_opens).start()

def load_email_list_from_excel(excel_path):
    """
    Loads a list of email addresses from an Excel file.

    Args:
        excel_path (str): Path to the Excel file containing the email list.

    Returns:
        list: A list of email addresses.
    """
    # Read the Excel file using pandas
    df = pd.read_excel(excel_path)

    # Assuming the email addresses are in a column named 'Email'
    email_list = df['Email'].tolist()

    return email_list

def convert_log_to_csv(log_file, csv_file):
        with open(log_file, 'r') as infile, open(csv_file, 'w', newline='') as outfile:
            reader = infile.readlines()
            writer = csv.writer(outfile)
            writer.writerow(["email", "response"])  # Writing the header row
            for line in reader:
                email, response = line.strip().split(',')
                writer.writerow([email, response])
=======
        threading.Timer(delay, check_for_non_opens,args=[datetime1,subject1,body1]).start() 
>>>>>>> origin/master
def extract_responses_from_log(log_csv_path):
    # column_names = ['Email', 'Response', 'Timestamp']
    df_response= pd.read_csv(log_csv_path)

    return df_response
def parse_datetime(datetime_str):
    return datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M")

def schedule_daily_task(sender_email,initial_time_str, recipient, name, subject, body, tracking_url_yes):
    """ Schedule a daily task """
    target_datetime = datetime.strptime(initial_time_str, "%Y-%m-%dT%H:%M")
    now = datetime.now()
    time_diff = (target_datetime - now).total_seconds()

    if time_diff > 0:
        threading.Timer(time_diff, send_mail, args=[sender_email,recipient, subject, prepare_email_content(subject, name, body, recipient, tracking_url_yes)]).start()
    else:
        print("Scheduled time is in the past.")
def schedule_daily_task6(sender_email,initial_time_str, recipient, name, subject, body, tracking_url_yes):
    """ Schedule a daily task """
    target_datetime = datetime.strptime(initial_time_str, "%Y-%m-%dT%H:%M")
    now = datetime.now()
    time_diff = (target_datetime - now).total_seconds()
    if time_diff > 0:
        threading.Timer(time_diff, send_mail1, args=[sender_email,recipient, subject, prepare_email_content4(subject, name, body, recipient, tracking_url_yes)]).start()
        
    else:
        print("Scheduled time is in the past.")
def schedule_follow_up_email(sender_email,click_time,recipient, name, subject, body):
    # Calculate the time 2 days from now
    initial_time = datetime.now()

# Add 2 days to the initial time
    target_datetime_plus_2_days = initial_time + timedelta(days=2)

    # Get the current time again (this step is redundant here since initial_time is already the current time)
    now = datetime.now()


    # Calculate the difference in seconds between now and the target time 2 days later
    time_diff = (target_datetime_plus_2_days - now).total_seconds()
    if time_diff > 0:
        threading.Timer(time_diff, send_mail,args=[sender_email,recipient, subject,prepare_email_content_3(subject, name, body, recipient)]).start()
    else:
        print("Scheduled time is in the past.")
def schedule_follow_up_email_without_url(sender_email,recipient, name, subject, body):
    initial_time = datetime.now()

# Add 2 days to the initial time
    target_datetime_plus_2_days = initial_time + timedelta(days=2)

    # Get the current time again (this step is redundant here since initial_time is already the current time)
    now = datetime.now()

    # Calculate the difference in seconds between now and the target time 2 days later
    time_diff = (target_datetime_plus_2_days - now).total_seconds()
    if time_diff > 0: 
    # Schedule the follow-up email
        threading.Timer((time_diff - datetime.now()).total_seconds(),send_mail,args=[sender_email,recipient, subject,prepare_email_content_2(subject, name, body, recipient)]).start()
    else:
        print("Scheduled time is in the past.")
def schedule_one_time_task(sender_email,target_datetime_str, recipient, name, subject, body):
    """ Schedule a one-time task to send follow-up email """
    target_datetime = datetime.strptime(target_datetime_str, "%Y-%m-%dT%H:%M")
    now = datetime.now()
    time_diff = (target_datetime - now).total_seconds()

    if time_diff > 0:
        threading.Timer(time_diff, send_mail, args=[sender_email,recipient, subject, prepare_email_content_1(subject, name, body, recipient)]).start()
    else:
        print("Scheduled time is in the past.")

def schedule_one_time_task_without_url(sender_email,target_datetime_str, recipient, name, subject, body):
    target_datetime = parse_datetime(target_datetime_str)
    now = datetime.now()
    time_diff = (target_datetime - now).total_seconds()

    if time_diff > 0:
        threading.Timer(time_diff, send_mail, args=[sender_email,recipient, subject, prepare_email_content_2(subject, name, body, recipient)]).start()
    else:
        print("Scheduled time is in the past.")
# def schedule_one_time_task1(sender_email,target_datetime_str, recipient, name, subject, body, tracking_url1, tracking_url2, r1, r2):
#     target_datetime = parse_datetime(target_datetime_str)
#     now = datetime.now()
#     time_diff = (target_datetime - now).total_seconds()

#     if time_diff > 0:
#         threading.Timer(time_diff, send_mail, args=[sender_email,recipient, subject, prepare_email_content_3(subject, name, body, recipient, tracking_url1, tracking_url2, r1, r2)]).start()
#     else:
#         print("Scheduled time is in the past.")
def send_mail(sender_email,recipient, subject, html_body):
    with app.app_context():   
        emailFrom = sender_email
        msg = Message(subject, sender=emailFrom, recipients=[recipient])
        msg.html = html_body
        mail.send(msg)
        print(f"Email sent to {recipient} with subject: {subject}")
        
def send_mail1(sender_email,recipient, subject, html_body):
    with app.app_context():   
        emailFrom = sender_email
        msg = Message(subject, sender=emailFrom, recipients=[recipient])
        msg.html = html_body
        mail.send(msg)
        print(f"Email sent to {recipient} with subject: {subject}")
        return redirect(tracking_url_yes)

def prepare_email_content(subject, name, body, recipient, tracking_url_yes):
    tracking_url_yes_redirect = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response=yes&tracking_url={quote(tracking_url_yes)}"
    # tracking_url_no_redirect = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response=no&tracking_url={quote(tracking_url_no)}"
    html_body = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email</title>
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
    <div style="width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <div style="text-align: left; padding-bottom: 20px;">
            <h1 style="margin: 0; font-size: 24px; color: #333333;">Hello, {name}!</h1>
        </div>
        <div style="font-size: 16px; color: #555555; line-height: 1.4;">
            <p>{body}</p>
            <a href="{tracking_url_yes_redirect }" style="display: inline-block; padding: 10px 20px; font-size: 14px; color: #ffffff; background-color: #007bff; text-decoration: none; border-radius: 3px;">Book A Call</a>
        </div>
        <div style="text-align: left; padding-top: 20px; border-top: 1px solid #dddddd; font-size: 14px; color: #888888;">
            <p>Best regards,<br>Your Company</p>
        </div>
    </div>
</body>
</html>

    
    """
    return html_body
def prepare_email_content4(subject, name, body, recipient, tracking_url_yes):
    tracking_url_no="https://arkaconsultancy.xyz/"
    tracking_url_yes_redirect = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response=Yes&tracking_url={quote(tracking_url_yes)}"
    tracking_url_no_redirect = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response=no&tracking_url={quote(tracking_url_no)}"
    html_body = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email</title>
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
    <div style="width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <div style="text-align: left; padding-bottom: 20px;">
            <h1 style="margin: 0; font-size: 24px; color: #333333;">Hello, {name}!</h1>
        </div>
        <div style="font-size: 16px; color: #555555; line-height: 1.4;">
            <p>{body}</p>
            <a href="{tracking_url_yes_redirect }" style="display: inline-block; padding: 10px 20px; font-size: 14px; color: #ffffff; background-color: #007bff; text-decoration: none; border-radius: 3px;">Book A Call</a>
            <a href="{tracking_url_no_redirect }" style="display: inline-block; padding: 10px 20px; font-size: 14px; color: #ffffff; background-color: #007bff; text-decoration: none; border-radius: 3px;">Unsubscribe</a>
        </div>
        <div style="text-align: left; padding-top: 20px; border-top: 1px solid #dddddd; font-size: 14px; color: #888888;">
            <p>Best regards,<br>Your Company</p>
        </div>
    </div>
</body>
</html>


    """
    return html_body

def prepare_email_content_1(subject, name, body, recipient):
    tracking_url_unsubscribe="https://arkaconsultancy.xyz/"
    # tracking_url_subscribe_redirect = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response=subscribe&tracking_url={quote(tracking_url_subscribe)}"
    tracking_url_unsubscribe_redirect = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response=unsubscribe&tracking_url={quote(tracking_url_unsubscribe)}"
    html_body = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email</title>
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
    <div style="width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <div style="text-align: left; padding-bottom: 20px;">
            <h1 style="margin: 0; font-size: 24px; color: #333333;">Hello, {name}!</h1>
        </div>
        <div style="font-size: 16px; color: #555555; line-height: 1.6;">
            <p>{body}</p>
<<<<<<< HEAD
            <a href="{tracking_url_subscribe_redirect}" style="display: inline-block; padding: 10px 10px; font-size: 16px; color: #ffffff; background-color: #007bff; text-decoration: none; border-radius: 3px;">Subscribe</a>
           <a href="{tracking_url_unsubscribe_redirect}" style="display: inline-block; padding: 10px 10px; font-size: 16px; color: #ffffff; background-color: #007bff; text-decoration: none; border-radius: 3px;">Unsubscribe</a>
=======
           <a href="{tracking_url_unsubscribe_redirect}" style="display: inline-block; padding: 10px 20px; font-size: 16px; color: #ffffff; background-color: #007bff; text-decoration: none; border-radius: 5px;">Unsubscribe</a>
>>>>>>> origin/master
        </div>
        <div style="text-align: ;eft; padding-top: 20px; border-top: 1px solid #dddddd; font-size: 14px; color: #888888;">
            <p>Best regards,<br>Your Company</p>
        </div>
    </div>
</body>
</html>

    """
    return html_body
def prepare_email_content_2(subject, name, body, recipient):
    # tracking_url_subscribe_redirect = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response=subscribe&tracking_url={quote(tracking_url_subscribe)}"
    # tracking_url_unsubscribe_redirect = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response=unsubscribe&tracking_url={quote(tracking_url_unsubscribe)}"
    html_body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email</title>
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
    <div style="width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <div style="text-align:left; padding-bottom: 20px;">
            <h1 style="margin: 0; font-size: 24px; color: #333333;">Hello, {name}!</h1>
        </div>
        <div style="font-size: 16px; color: #555555; line-height: 1.6;">
            <p>{body}</p>
        </div>
        <div style="text-align:left; padding-top: 20px; border-top: 1px solid #dddddd; font-size: 14px; color: #888888;">
            <p>Best regards,<br>Your Company</p>
        </div>
    </div>
</body>
</html>
    """
    return html_body
def prepare_email_content_3(subject, name, body, recipient):
    r2 = "Unsubscribe"
    tracking_url2="https://arkaconsultancy.xyz/"
    # url1 = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response={quote(r1)}&tracking_url={quote(tracking_url1)}"
    # url2 = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response={quote(r2)}&tracking_url={quote(tracking_url2)}"
    url2 = f"https://{app.config['SERVER_NAME']}/track_click?email={quote(recipient)}&response={quote(r2)}&tracking_url={quote(tracking_url2)}"
    html_body = f"""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email</title>
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4;">
    <div style="width: 100%; max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <div style="text-align:left; padding-bottom: 20px;">
            <h1 style="margin: 0; font-size: 24px; color: #333333;">Hello, {name}!</h1>
        </div>
        <div style="font-size: 16px; color: #555555; line-height: 1.6;">
            <p>{body}</p>
           <a href="{url2}" style="display: inline-block; padding: 10px 20px; font-size: 16px; color: #ffffff; background-color: #007bff; text-decoration: none; border-radius: 5px;">{r2}</a>
        </div>
        <div style="text-align:left; padding-top: 20px; border-top: 1px solid #dddddd; font-size: 14px; color: #888888;">
            <p>Best regards,<br>Your Company</p>
        </div>
    </div>
</body>
</html>
    """
    return html_body
@app.route('/', methods=['GET', 'POST'])
def index():
    global follow_up_data
    global new_data
    global no_datetime,subject_no,body_no,no_datetime4,subject_no4,body_no4,no_datetime6,subject_no6,body_no6,no_datetime10,subject_no10,body_no10,no_datetime14,subject_no14,body_no14
    global tracking_url_yes, tracking_url_no,sender_email,initial_subject,filename,subject_subscribe,body_subscribe,datetime_subscribe
    if request.method == 'POST':
        data = pd.read_excel(request.files['emails'])
        email_list=request.files['emails']
        sender_email= request.form['sender_email']
        initial_body = request.form['initial_body']
        initial_datetime_str = request.form['initial_datetime']
        initial_subject = request.form['initial_subject']
        subject_yes = request.form['yes_1_subject']
        body_yes = request.form['yes_1_body']
        yes_datetime = request.form['initial_datetime_yes']
        subject_no = request.form['no_subject']
        body_no = request.form['no_body']
        no_datetime = request.form['no_datetime']
        subject_subscribe = request.form['Subscribe_subject']
        body_subscribe = request.form['Subscribe_body']
        datetime_subscribe = request.form['Subscribe_datetime']

        subject_unsubscribe = request.form['Unsubscribe_subject']
        body_unsubscribe = request.form['Unsubscribe_body']
        datetime_unsubscribe = request.form['Unsubscribe_datetime']

        tracking_url_yes = request.form['tracking_url_yes']
        subject_no4 = request.form['no_subject4']
        body_no4= request.form['no_body4']
        no_datetime4 = request.form['no_datetime4']


        subject_no6 = request.form['no_subject6']
        body_no6= request.form['no_body6']
        no_datetime6 = request.form['no_datetime6']
       

        subject_no10 = request.form['no_subject10']
        body_no10= request.form['no_body10']
        no_datetime10 = request.form['no_datetime10']


        subject_no14 = request.form['no_subject14']
        body_no14= request.form['no_body14']
        no_datetime14 = request.form['no_datetime14']
        
        new_data = pd.concat([new_data,data],ignore_index=True)
        directory = 'log'

      # Check if the directory exists, and create it if it doesn't
        if not os.path.exists(directory):
           os.makedirs(directory)
           print(f"The directory '{directory}' was not found, so it has been created.")
        filename = 'log/'+initial_subject+'.csv'
        headers = ['Email', 'Response', 'Timestamp']
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        print(f"CSV file '{filename}' created with headers.")
        # schedule_task_at(not_datetime)
        schedule_task_at_yes(datetime_subscribe,subject_subscribe,body_subscribe)
        schedule_task_at(no_datetime,subject_no,body_no)
        schedule_task_at(no_datetime4,subject_no4,body_no4)
        schedule_task_at(no_datetime6,subject_no6,body_no6)
        schedule_task_at(no_datetime10,subject_no10,body_no10)
        schedule_task_at(no_datetime14,subject_no14,body_no14)
        for _, row in data.iterrows():
            recipient = row['Email']
            name = row['Name']
            # html_body = prepare_email_content(initial_subject, name, initial_body, recipient, tracking_url_yes, tracking_url_no)
<<<<<<< HEAD
            schedule_daily_task(sender_email,initial_datetime_str, recipient, name, initial_subject, initial_body, tracking_url_yes, tracking_url_no)

=======
            schedule_daily_task(sender_email,initial_datetime_str, recipient, name, initial_subject, initial_body, tracking_url_yes)
            
>>>>>>> origin/master
            follow_up_data[recipient] = {
                'email_list':email_list,
                'sender_email':sender_email,
                'name': name,
                'initial_subject':initial_subject,
                'initial_datetime_str':initial_datetime_str,
                'subject_yes': subject_yes,
                'body_yes': body_yes,
                'yes_datetime': yes_datetime,
                'subject_subscribe': subject_subscribe,
                'subject_unsubscribe': subject_unsubscribe,
                'body_unsubscribe': body_unsubscribe,
                'datetime_unsubscribe': datetime_unsubscribe,
                'tracking_url_yes': tracking_url_yes,
              
                
                'subject_no4': subject_no4,
                'body_no4': body_no4,
                'no_datetime4':no_datetime4,
                'subject_no6': subject_no6,
                'body_no6': body_no6,
                'no_datetime6':no_datetime6,
               
                'subject_no10': subject_no10,
                'body_no10': body_no10,
                'no_datetime10':no_datetime10,
               
                'subject_no14': subject_no14,
                'body_no14': body_no14,
                'no_datetime14':no_datetime14,
                
            }

    return render_template_string('''
    <!doctype html>
    <title>Email Campaign</title>
    <h1>Schedule Your Email Campaign</h1>
    <form method=post enctype=multipart/form-data>
        <label for="sender_email">Sender Email:</label>
        <input type="text" id="sender_email" name="sender_email" required><br><br>
        <label for="initial_subject">Initial Email Subject:</label>
        <input type="text" id="initial_subject" name="initial_subject" required><br><br>
        <label for="initial_body">Initial Email Body:</label>
        <textarea id="initial_body" name="initial_body" rows="10" cols="30" required></textarea><br><br>
        <label for="initial_datetime">Initial Email Date and Time:</label>
        <input type="datetime-local" id="initial_datetime" name="initial_datetime" required><br><br>
        <label for="emails">Upload Email List (Excel):</label>
        <input type="file" id="emails" name="emails" accept=".xlsx" required><br><br>
        <label for="tracking_url_yes">Tracking URL for Booking a Call:</label>
        <input type="text" id="tracking_url_yes" name="tracking_url_yes" required><br><br>
<<<<<<< HEAD
        <label for="tracking_url_no">Tracking URL for No Response:</label>
        <input type="text" id="tracking_url_no" name="tracking_url_no" required><br><br>

        <h2>Follow-Up Emails for "Yes" Responses</h2>
        <label for="yes_1_subject">Follow-Up 1 Subject:</label>
=======
                                                          
        <h2>Follow-Up Emails After Booking the call- Newsletter1</h2>
        <label for="yes_1_subject">Follow-Up Subject for Newsletter:</label>
>>>>>>> origin/master
        <input type="text" id="yes_1_subject" name="yes_1_subject" required><br><br>
        <label for="yes_1_body">Follow-Up 1 Body:</label>
        <textarea id="yes_1_body" name="yes_1_body" rows="10" cols="30" required></textarea><br><br>
        <label for="initial_datetime_yes">Follow-Up Email Date and Time:</label>
        <input type="datetime-local" id="initial_datetime_yes" name="initial_datetime_yes" required><br><br> 
       
         <h2>Follow-Up Emails for Newsletter2</h2>
        <label for="Subscribe_subject">Subscribe Subject:</label>
        <input type="text" id="Subscribe_subject" name="Subscribe_subject" required><br><br>
        <label for="Subscribe_body">Subscribe Body:</label>
        <textarea id="Subscribe_body" name="Subscribe_body" rows="10" cols="30" required></textarea><br><br>
        <label for="Subscribe_datetime">Subscribe Date and Time:</label>
        <input type="datetime-local" id="Subscribe_datetime" name="Subscribe_datetime" required><br><br>
        
        <h2>Follow-Up Emails for "Unsubscribe"</h2>
        <label for="Unsubscribe_subject">Unsubscribe Subject:</label>
        <input type="text" id="Unsubscribe_subject" name="Unsubscribe_subject" required><br><br>
        <label for="Unsubscribe_body">Unsubscribe Body:</label>
        <textarea id="Unsubscribe_body" name="Unsubscribe_body" rows="10" cols="30" required></textarea><br><br>
        <label for="Unsubscribe_datetime">Unsubscribe Date and Time:</label>
        <input type="datetime-local" id="Unsubscribe_datetime" name="Unsubscribe_datetime" required><br><br>
                                 
                                  
        <h2>Follow-Up Emails for "No" Responses</h2>
        <label for="no_subject">Follow-Up No Subject:</label>
        <input type="text" id="no_subject" name="no_subject" required><br><br>
        <label for="no_body">Follow-Up No Body:</label>
        <textarea id="no_body" name="no_body" rows="10" cols="30" required></textarea><br><br>
        <label for="no_datetime">Follow-Up Email Date and Time:</label>
        <input type="datetime-local" id="no_datetime" name="no_datetime" required><br><br>
        
        
        <h2>Follow-Up Emails for "No" Responses Day 4</h2>
        <label for="no_subject4">Follow-Up No Subject:</label>
        <input type="text" id="no_subject4" name="no_subject4" required><br><br>
        <label for="no_body4">Follow-Up No Body:</label>
        <textarea id="no_body4" name="no_body4" rows="10" cols="30" required></textarea><br><br>
        <label for="no_datetime4">Follow-Up Email Date and Time:</label>
        <input type="datetime-local" id="no_datetime4" name="no_datetime4" required><br><br>
        
        
        <h2>Follow-Up Emails for "No" Responses Day 6</h2>
        <label for="no_subject6">Follow-Up No Subject:</label>
        <input type="text" id="no_subject6" name="no_subject6" required><br><br>
        <label for="no_body6">Follow-Up No Body:</label>
        <textarea id="no_body6" name="no_body6" rows="10" cols="30" required></textarea><br><br>
        <label for="no_datetime6">Follow-Up Email Date and Time:</label>
        <input type="datetime-local" id="no_datetime6" name="no_datetime6" required><br><br>
                                  
        <h2>Follow-Up Emails for "No" Responses Day 10</h2>
        <label for="no_subject10">Follow-Up No Subject:</label>
        <input type="text" id="no_subject10" name="no_subject10" required><br><br>
        <label for="no_body10">Follow-Up No Body:</label>
        <textarea id="no_body10" name="no_body10" rows="10" cols="30" required></textarea><br><br>
        <label for="no_datetime10">Follow-Up Email Date and Time:</label>
        <input type="datetime-local" id="no_datetime10" name="no_datetime10" required><br><br>
        
                                  
        <h2>Follow-Up Emails for "No" Responses Day 14</h2>
        <label for="no_subject14">Follow-Up No Subject:</label>
        <input type="text" id="no_subject14" name="no_subject14" required><br><br>
        <label for="no_body14">Follow-Up No Body:</label>
        <textarea id="no_body14" name="no_body14" rows="10" cols="30" required></textarea><br><br>
        <label for="no_datetime14">Follow-Up Email Date and Time:</label>
        <input type="datetime-local" id="no_datetime14" name="no_datetime14" required><br><br>
        <input type="submit" value="Schedule Emails">
    </form>
    ''')

def run_scheduler():
    with app.app_context():
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
<<<<<<< HEAD
=======
    
    app.run(host='127.0.0.1', port=5000, debug=True)
>>>>>>> origin/master
