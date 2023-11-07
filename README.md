# My Personal Website
This is my personal website to showcase my computer science portfolio.

## Technologies Used 
- Written in Python
- Built using Flask framework
- Utilizes boostrap library to style website
- Uses Flask's jinja2 tags to dynamically load front-end
- Uses Flask routes to create an endpoint for sending me emails/contact messages

## How does it work?

### 1. The home page
The home page consists of the "/" route and the "/home" route. Below is the code for what this route returns and how it loads my skills as needed
```
@app.route('/')
@app.route('/home')
def home():
    skills = ["Java", "Python", "Flask", "HTML", "CSS", "JavaScript", "Jinja2", "Git", "SQL"]
    return render_template('index.html', skills=skills)
```
### 2. The projects page
The projects page consists of the "/projects" route. Similar to the home page this is basically just a route that upon a get request, simply returns the html template of the projects page.
```
@app.route('/projects')
def projects():
    return render_template('projects.html')
```
### 3. The resume page
This page is handled by the "/resume" route. This page simply opens the pdf file of my resume on a new tab for the user to view. Below is the code.
```
@app.route('/resume')
def resume():
    return send_file('./static/resume.pdf', as_attachment=False)
```

### 4. The contact page
This page is a little bit different than the other pages as it contains a form that handles a post request. Below is the code that handles this "/contact" route. There is further explanation below this code as well as the repository that contains commenting for how each specific part of this code works.
```
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
```
