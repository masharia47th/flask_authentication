from app import db, create_app
from app.models import User
from flask_bcrypt import Bcrypt

app = create_app()
bcrypt = Bcrypt(app)

def seed_data():
    admin_password = bcrypt.generate_password_hash('adminpass').decode('utf-8')
    admin = User(username='admin', email='admin@example.com', password=admin_password, is_admin=True)
    db.session.add(admin)
    db.session.commit()
    print("Admin user created.")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
