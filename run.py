from app import app
from db import db

db.init_app(app)


with app.app_context():
        app.before_request_funcs = [(None, db.create_all())]
        
'''
@app.before_first_request
def create_tables():
    db.create_all()
'''