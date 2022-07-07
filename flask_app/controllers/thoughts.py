from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.thought import Thouht
from flask_app.models.user import User

@app.route('/new/thought')
def new_thought():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('new_thought.html', user= User.get_by_id(data))

@app.route('/create/thought', methods=['POST'])
def create_thought():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Thought.validate_thought(request.form):
        return redirect('/new/thought')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "user_id": session["user_id"],
    }
    Thought.save(data)
    return redirect('/dashboard')


@app.route('/destroy/thought/<int:id>')
def destroy_thought(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    clickedThought = Thought.get_one(data)
    print(clickedThought)
    if clickedThought['user_id'] == session['user_id']:
        Thought.destroy(data)
        return redirect ('/dashboard')
    return redirect('/dashboard')


@app.route('/thought/<int:id>')
def show_thought(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    userData = {
        "id": session['user_id']
    }
    clickedThought = Thought.get_one(data)
    print(clickedThought)
    return render_template('show_thought.html', thought = thought.get_one(data), user=User.get_by_id(userData))

@app.route('/edit/thought/<int:id>')
def edit_thought(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    userData = {
        "id": session['user_id']
    }
    return render_template('edit_thought.html', edit = Thought.get_one(data), user=User.get_by_id(userData))

@app.route('/update/thought/', methods=['POST'])
def update_thought():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Thought.validate_thought(request.form):
        return redirect(request.referrer)
    
    data = {
         "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "id": request.form["id"],
    }
    Thought.update(data)
    return redirect('/dashboard')

