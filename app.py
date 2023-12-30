from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    description = request.form['description']
    
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = Task.query.get(task_id)
    task.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_task', methods=['POST'])
def update_task():
    task_id = int(request.form['taskId'])
    edited_title = request.form['editedTitle']
    edited_description = request.form['editedDescription']

    task = Task.query.get(task_id)
    task.title = edited_title
    task.description = edited_description
    db.session.commit()

    return {'message': 'Task updated successfully'}

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)
