from sqlalchemy import Boolean, Column, Integer, String, ForeignKey

from database import Base


class Case(Base):
    __tablename__ = 'cases'
    
    id = Column(Integer, primary_key=True)
    case_id = Column(Integer, unique=True)
    case_number = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    subject = Column(String)
    group_id = Column(Integer)
    status = Column(String)
    priority = Column(String)
    channel = Column(String)
    deleted = Column(Boolean)
    spam = Column(Boolean)
    created_at = Column(String)
    updated_at = Column(String)
    
    
class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, unique=True, primary_key=True)
    user_full_name = Column(String)
    user_screen_name = Column(String)
    type_connect = Column(String)
    user_phone = Column(String)
    active = Column(Boolean)
    deleted = Column(Boolean)
    created_at = Column(String)
    updated_at = Column(String)
    
    
class Macros(Base):
    __tablename__ = 'macros'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    

    
    