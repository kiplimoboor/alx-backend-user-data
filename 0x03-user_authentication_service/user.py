#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""Module that contains class and details about user"""

Base = declarative_base()


class User(Base):
    """
    A user class that is also a users table
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)
