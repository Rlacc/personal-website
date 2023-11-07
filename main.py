from flask import Flask, render_template, redirect, url_for, flash, request, send_file
from forms import ContactForm
import secrets
from flask_mail import Mail, Message
import os

# initiates our flask app and with its respective templates and static folders
app = Flask(__name__, template_folder='templates', static_folder='static')


app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
# for security purposes the app username and password to the email account used to send me messages is hidden in the
# .env file of my project
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)


# Flask route that handles the home/default page. Here we load the index.html template and pass along the array of my
# skills to be rendered with jinja2 on the front end/ in the template
@app.route('/')
@app.route('/home')
def home():
    skills = ["Java", "Python", "Flask", "HTML", "CSS", "JavaScript", "Jinja2", "Git", "SQL"]
    return render_template('index.html', skills=skills)

# route responsible for displaying the projects page of the website
@app.route('/projects')
def projects():
    return render_template('projects.html')

# route responsible for opening my resume when a user clicks on it
@app.route('/resume')
def resume():
    return send_file('./static/resume.pdf', as_attachment=False)


# This is a flask route that handles the post requests from the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # instantiate a new instance of the contact form class and store it in the form variable
    form = ContactForm()
    # this success variable keeps track of the status of the form. By default, it's initiated at 1.
    success = 1
    # when a post request is sent to this endpoint, we process the associative form submission
    if request.method == 'POST':
        # we nest the processing in this form just in case an error occurs, and we are thrown an exception
        try:
            # using the WTForms library we check to see if the form submitted is valid
            if form.validate_on_submit():
                # The following code outlines the email that will be sent to me. Things like the subject of the email,
                # who sent the email and their message to me.
                subject = "New Website Contact"
                sender = form.email.data
                recipients = ["rlacourciere1@gmail.com"]
                message_body = f"Name: {form.name.data}\nEmail: {form.email.data}\nMessage: {form.message.data}"
                message = Message(subject=subject, sender=sender, recipients=recipients, body=message_body)
                mail.send(message)
                # if the message is successfully sent then we update the success variable as it will be used to
                # determine what is displayed on the front end.
                success = 2

            else:
                # if the form fails because of formatting or user error, the success variable is updated and the front
                # end handles that accordingly.
                success = 3
        # if an exception is thrown we update the success variable. Typically, an exception will be thrown if something
        # out of the user's control causes the submission to fail. In this case we front-end will tell the user to just
        # resubmit the form.
        except Exception as e:
            success = 4
    # if the request was a get request we just render the contact.html template. We also pass along the
    return render_template('contact.html', form=form, success=success)


if __name__ == "__main__":
    app.run(port=8080)
