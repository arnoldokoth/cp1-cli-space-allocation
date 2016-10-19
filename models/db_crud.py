from fellow import Fellow
from staff import Staff
from sqlalchemy.orm import sessionmaker
from database_structure import Person, Room, RoomAllocations, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_database()

Base = declarative_base()

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


def save_fellows(fellow_list=[]):
	if len(fellow_list) > 0:
		for fellow in fellow_list:
			add_fellow = Person(full_name=fellow, person_type="Fellow")
			session.add(add_fellow)
			# import pdb; pdb.set_trace()
		try:
			session.commit()
		except Exception:
			session.rollback()
			return "error occured or data already exists"
		
		return "fellows saved"
	else:
		return "no fellows in cache"


def save_staff(staff_list=[]):
	if len(staff_list) > 0:
		for staff in staff_list:
			add_staff = Person(full_name=staff, person_type="Staff")
			session.add(add_staff)
		try:
			session.commit()
		except Exception:
			session.rollback()
			return "error occured or data already exists"

		return "staff saved"
	else:
		return "no staff in cache"


def save_offices(office_list=[]):
	if len(office_list) > 0:
		for office in office_list:
			add_office = Room(room_name=office, room_type="Office")
			session.add(add_office)

		try:
			session.commit()
		except Exception as e:
			session.rollback()
			return "error occured or data already exists"

		return "offices saved"
	else:
		return "no offices in cache"


def save_livingspaces(livingspace_list=[]):
	if len(livingspace_list) > 0:
		for livingspace in livingspace_list:
			add_livingspace = Room(room_name=livingspace, room_type="Living Space")
			session.add(add_livingspace)
		try:
			session.commit()
		except Exception as e:
			session.rollback()
			return "error occured or data already exists"

		return "living spaces saved"
	else:
		return "no living spaces in cache"


def delete_allocations():
	session.query(RoomAllocations).delete()
	session.commit()


def save_allocations(room_allocations={}):
	delete_allocations()
	if len(room_allocations.keys()) > 0:
		for room_name in room_allocations.keys():
			for person in room_allocations[room_name]:
				add_allocation = RoomAllocations(full_name=person, room_name=room_name)
				session.add(add_allocation)
		try:
			session.commit()
		except Exception:
			session.rollback()
			return "error occured or data already exists"

		return "room allocations saved"
	else:
		return "there are no allocations available"


def get_all_fellows():
	fellows = []
	fellow_rows = session.query(Person).filter_by(person_type="Fellow").all()
	for fellow_row in fellow_rows:
		fellows.append(str(fellow_row.full_name))

	return fellows


def get_all_staff():
	staff = []
	staff_rows = session.query(Person).filter_by(person_type="Staff").all()
	for staff_row in staff_rows:
		staff.append(str(staff_row.full_name))

	return staff

def get_all_offices():
	offices = []
	office_rows = session.query(Room).filter_by(room_type="Office").all()
	for office_row in office_rows:
		offices.append(str(office_row.room_name)) 

	return offices

def get_all_livingspaces():
	livingspaces = []
	livingspace_rows = session.query(Room).filter_by(room_type="Living Space").all()
	for livingspace_row in livingspace_rows:
		livingspaces.append(str(livingspace_row.room_name))

	return livingspaces


def get_room_allocations():
	room_allocations = {}
	room_rows = session.query(RoomAllocations).all()
	for room in room_rows:
		rooms.append(str(room.room_name))

	for room in rooms:
		people_rows = session.query(RoomAllocations).filter_by(room_name=room).all()
		for person in people_rows:
			if str(person.room_name) in room_allocations.keys():
				room_allocations[str(person.room_name)].append(str(person.full_name))
			else:
				room_allocations[str(person.room_name)] = [str(person.full_name)]

	return room_allocations