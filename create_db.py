from flaskblog import create_app, db
from flaskblog.models import Post

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created.")
    
        
