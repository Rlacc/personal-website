from flask import Flask, render_template, redirect, url_for, flash, request, send_file
from forms import ContactForm
import secrets
from flask_mail import Mail, Message
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'computersciencelac@gmail.com'
app.config['MAIL_PASSWORD'] = 'ritgqwlnvvlstelo'

mail = Mail(app)


@app.route('/')
@app.route('/home')
def home():
    skills = ["Java", "Python", "Flask", "HTML", "CSS", "JavaScript", "Jinja2", "Git", "SQL"]
    return render_template('index.html', skills=skills)


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/resume')
def resume():
    return send_file('./static/resume.pdf', as_attachment=False)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    success = 1
    if request.method == 'POST':
        try:
            if form.validate_on_submit():
                subject = "New Website Contact"
                sender = form.email.data
                recipients = ["rlacourciere1@gmail.com"]
                message_body = f"Name: {form.name.data}\nEmail: {form.email.data}\nMessage: {form.message.data}"
                message = Message(subject=subject, sender=sender, recipients=recipients, body=message_body)
                mail.send(message)
                success = 2

            else:
                success = 3
        except Exception as e:
            success = 4

    return render_template('contact.html', form=form, success=success)

if __name__ == "__main__":
    app.run(port=8080)