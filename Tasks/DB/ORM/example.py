from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# Configuration
Base.metadata.bind = engine
session = sessionmaker(bind=engine)
my_session = session()

# Create a new user
"""
new_user = user(username="bob", email="bob@bob", password="bob")
my_session.add(new_user)
my_session.commit()
"""

result = my_session.query(user).all()
for r in result:
    print(r.username, r.email, r.password)

