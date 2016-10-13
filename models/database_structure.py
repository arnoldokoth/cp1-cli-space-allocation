import os
import sys
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

class Person(Base):
	__tablename__ = 'people'
	person_id = Column(Integer, primary_key=True, autoincrement=True)
	full_name = Column(String(50), nullable=False, unique=True)
	person_type = Column(String(50), nullable=False)


class Room(Base):
	__tablename__ = 'rooms'
	room_name = Column(String(50), nullable=False, unique=True, primary_key=True)
	room_type = Column(String(50), nullable=False)


class RoomAllocations(Base):
	__tablename__ = 'room_allocations'
	allocation_id = Column(Integer, primary_key=True)
	full_name = Column(String(50), nullable=False)
	room_name = Column(String(50), nullable=False)


def create_database(database_name=""):
	if database_name:
		engine = create_engine("sqlite:///{}".format(database_name))
	else:
		engine = create_engine("sqlite:///default.db")

	return engine

engine = create_database()

Base.metadata.create_all(engine)