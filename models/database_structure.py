import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
	pass

class Room(Base):
	pass

class RoomAllocations(Base):
	pass