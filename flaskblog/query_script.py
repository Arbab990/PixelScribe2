# query_script.py
from flaskblog import create_app, db
from flaskblog.models import User

app = create_app()

with app.app_context():
    # Query the database
    all_records = User.query.all()
    for record in all_records:
        print(record)
