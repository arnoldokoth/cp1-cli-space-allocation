from sqlalchemy.orm import sessionmaker
from database_structure import Person, Room, RoomAllocations
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Database:
    def __init__(self, engine):
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def save_fellows(self, fellow_list):
        if len(fellow_list) > 0:
            for fellow in fellow_list:
                add_fellow = Person(full_name=fellow, person_type="Fellow")
                self.session.add(add_fellow)
            try:
                self.session.commit()
            except Exception:
                self.session.rollback()
                return "error occured or data already exists"

            return "fellows saved"
        else:
            return "no fellows in cache"

    def save_staff(self, staff_list):
        if len(staff_list) > 0:
            for staff in staff_list:
                add_staff = Person(full_name=staff, person_type="Staff")
                self.session.add(add_staff)
            try:
                self.session.commit()
            except Exception:
                self.session.rollback()
                return "error occured or data already exists"

            return "staff saved"
        else:
            return "no staff in cache"

    def save_offices(self, office_list):
        if len(office_list) > 0:
            for office in office_list:
                add_office = Room(room_name=office, room_type="Office")
                self.session.add(add_office)

            try:
                self.session.commit()
            except Exception as e:
                self.session.rollback()
                return "error occured or data already exists"

            return "offices saved"
        else:
            return "no offices in cache"

    def save_livingspaces(self, livingspace_list):
        if len(livingspace_list) > 0:
            for livingspace in livingspace_list:
                add_livingspace = Room(room_name=livingspace, room_type="Living Space")
                self.session.add(add_livingspace)
            try:
                self.session.commit()
            except Exception as e:
                self.session.rollback()
                return "error occured or data already exists"

            return "living spaces saved"
        else:
            return "no living spaces in cache"

    def delete_allocations(self):
        self.session.query(RoomAllocations).delete()
        self.session.commit()

    def save_allocations(self, room_allocations):
        self.delete_allocations()
        if len(room_allocations.keys()) > 0:
            for room_name in room_allocations.keys():
                for person in room_allocations[room_name]:
                    add_allocation = RoomAllocations(full_name=person, room_name=room_name)
                    self.session.add(add_allocation)
            try:
                self.session.commit()
            except Exception:
                self.session.rollback()
                return "error occured or data already exists"

            return "room allocations saved"
        else:
            return "there are no allocations available"

    def get_all_fellows(self):
        fellows = []
        fellow_rows = self.session.query(Person).filter_by(person_type="Fellow").all()
        for fellow_row in fellow_rows:
            fellows.append(str(fellow_row.full_name))

        return fellows

    def get_all_staff(self):
        staff = []
        staff_rows = self.session.query(Person).filter_by(person_type="Staff").all()
        for staff_row in staff_rows:
            staff.append(str(staff_row.full_name))

        return staff

    def get_all_offices(self):
        offices = []
        office_rows = self.session.query(Room).filter_by(room_type="Office").all()
        for office_row in office_rows:
            offices.append(str(office_row.room_name))

        return offices

    def get_all_livingspaces(self):
        livingspaces = []
        livingspace_rows = self.session.query(Room).filter_by(room_type="Living Space").all()
        for livingspace_row in livingspace_rows:
            livingspaces.append(str(livingspace_row.room_name))

        return livingspaces

    def get_room_allocations(self):
        room_allocations = {}
        rooms = []
        room_rows = self.session.query(RoomAllocations).all()
        for room in room_rows:
            rooms.append(str(room.room_name))

        people_rows = None
        for room in rooms:
            people_rows = self.session.query(RoomAllocations).filter_by(room_name=room).all()

        for person in people_rows:
            if str(person.room_name) in room_allocations.keys():
                room_allocations[str(person.room_name)].append(str(person.full_name))
            else:
                room_allocations[str(person.room_name)] = [str(person.full_name)]

        return room_allocations
