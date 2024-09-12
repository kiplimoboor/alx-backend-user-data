#!/usr/bin/env python3
"""DB module"""

from sqlalchemy import create_engine, select, update
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class that handles database activity
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a new user into the database
        Args
            (email): the new user's email
            (hashed_password): the new user's password
        Return:
            the newly created user, an instance of User
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Searches users table by row name and returns the matching user
        Args:
            (kwargs): keyword args with user properties
        Return:
            the first found user
        """

        if not kwargs:
            raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id, **kwargs) -> None:
        """
        Searches for a user and updates their data
        Args:
            (user_id): the id of the user to be updated
            (kwargs): values columns and values to be updated
        """
        if not kwargs:
            raise ValueError

        user = self.find_user_by(id=user_id)
        columns = User.__table__.columns.keys()

        for key, val in kwargs.items():
            if key not in columns:
                raise ValueError
            setattr(user, key, val)

        self._session.commit()
