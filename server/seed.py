from server.config import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

def seed():
    db.drop_all()
    db.create_all()
    
    user = User(username='admin')
    user.set_password('password')
    db.session.add(user)
    
    guest1 = Guest(name='John Doe', occupation='Actor')
    guest2 = Guest(name='Jane Smith', occupation='Comedian')
    db.session.add_all([guest1, guest2])
    
    episode1 = Episode(date=date(2025, 6, 1), number=101)
    episode2 = Episode(date=date(2025, 6, 2), number=102)
    db.session.add_all([episode1, episode2])
    
    appearance1 = Appearance(rating=4, guest_id=1, episode_id=1)
    appearance2 = Appearance(rating=5, guest_id=2, episode_id=2)
    db.session.add_all([appearance1, appearance2])
    
    db.session.commit()
    print('Database seeded!')

if __name__ == '__main__':
    with app.app_context():
        seed()