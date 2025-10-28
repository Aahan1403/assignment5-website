from flask import Flask, render_template, request, redirect, url_for, flash
import os
from DAL import init_db, get_projects, add_project

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'dev-secret')

# Ensure database exists and table is created
init_db()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    projects_list = get_projects()
    return render_template('projects.html', projects=projects_list)


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return redirect(url_for('thankyou'))
    return render_template('contact.html')


@app.route('/add_project', methods=['GET', 'POST'])
def add_project_view():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        imagefilename = request.form.get('imagefilename')
        if not title or not description:
            flash('Title and description are required.', 'error')
            return redirect(url_for('add_project_view'))
        add_project(title, description, imagefilename)
        flash('Project added successfully.', 'success')
        return redirect(url_for('projects'))
    return render_template('add_project.html')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
