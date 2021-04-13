from app import app, db
from data.todo_data import list_todo

with app.app_context():

    try:
        db.drop_all()
        db.create_all()

        db.session.add_all(list_todo)

        db.session.commit()    
        

        print('Everything committed 🐶')
    except Exception as e:
        print('There was an error.')
        print(e)