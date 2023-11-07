# My Personal Website
This is my personal website to showcase my computer science portfolio.

## Technologies Used 
- Written in Python
- Built using Flask framework
- Uses Flask's jinja2 tags to dynamically load front-end
- Uses Flask routes to create an endpoint for sending me emails/contact messages

## How does it work?

### 1. The home page
The home page consists of the "/" route and the "/home" route. Below is the code for what this route returns and how it loads my skills as needed
```@app.route('/')
@app.route('/home')
def home():
    skills = ["Java", "Python", "Flask", "HTML", "CSS", "JavaScript", "Jinja2", "Git", "SQL"]
    return render_template('index.html', skills=skills)```
