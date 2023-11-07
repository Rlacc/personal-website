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
The code above uses WTForms a python library for handling forms to validate the form submitted. Inside the forms.py file I created a ContactForm() class that outlines the requirements for this form. Following form validation, I outline how the emails/messages to me should be formatted (things like their subject and message). Finally, I pass the success variable to Flask's jinja2 library to process the result of the form submission and present it on the front-end accordingly (a more detailed outline of the specific success cases are in the code comments).

### 5. The navigation bar
I thought to finish this off I would talk a bit about the navigation bar and how that works. Essentially, the navigation bar is turned into a compoenent using jinja 2 tags. With this im able to extend the nav bar onto each template of my choosing easily with jinja2 tags. Below is the code for the nav bar it's self. It was mainly built using bootstrap. 
```
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
        <a class="navbar-brand" href="/">Home</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/projects">Projects</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/resume" target="_blank">Resume</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/contact">Contact Me</a>
                </li>
            </ul>
        </div>
    </div>

    <a href="https://www.linkedin.com/in/ryan-lacourciere/" target="_blank">
        <i class="fab fa-linkedin fa-lg" style="color: #6c757d; margin-right: 10px;"></i>
    </a>
    <a href="https://github.com/Rlacc" target="_blank">
        <i class="fab fa-github fa-lg" style="color: #6c757d; margin-right: 10px;"></i>
    </a>
</nav>
```
