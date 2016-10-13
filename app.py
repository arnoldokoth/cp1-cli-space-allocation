"""
	Commands:
		add_person <first_name> <last_name> <FELLOW|STAFF> [wants_accomodation=N]
		create_room <room_type> <room_name>...
		reallocate_person <full_name> <new_room_name>
		load_people <filename>
		print_allocations [--o=filename]
		print_unallocated [--o=filename]
		print_room <room_name>
		save_state [--db=sqlite_database]
		load_state [--db=sqlite_database]
		quit
	Options:
		-h, --help  Show this screen and exit
		--version  Show version
"""


import cmd
import os
from docopt import docopt, DocoptExit
from models.amity import Amity

def docopt_cmd(func):
	"""
	This decorator is used to simplify the try/except block and pass the result
	of the docopt parsing to the called action
	"""
	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__, arg)

		except DocoptExit as e:
			# The DocoptExit is thrown when the args do not match
			# We print a message to the user and the usage block
			print('Invalid Command!')
			print(e)
			return 

		except SystemExit:
			# The SystemExit exception prints the usage for --help
			# We do not need to do the print here
			return


		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)
	return fn


def introduction():
	pass


def save_state_on_interrupt():
	print("saving state...")
	Amity.save_state()


class AmityCLI(cmd.Cmd):
	prompt = "$amity>>"

	@docopt_cmd
	def do_add_person(self, arg):
		"""Usage: add_person <first_name> <last_name> <designation> [--wants_accomodation=N]"""
		first_name = arg["<first_name>"]
		last_name = arg["<last_name>"]
		designation = arg["<designation>"]
		if arg["--wants_accomodation"] is None:
			wants_accomodation = "N"
		else:
			wants_accomodation = arg["--wants_accomodation"]

		# print(type(wants_accomodation))
		Amity.add_person(first_name=first_name.strip(), last_name=last_name.strip(), person_type=designation.strip(), wants_accomodation=wants_accomodation.strip())

	@docopt_cmd
	def do_create_room(self, arg):
		"""Usage: create_room <room_type> <room_name>..."""
		room_type = arg["<room_type>"]
		rooms = arg["<room_name>"]

		Amity.create_room(room_type.strip(), rooms)

	@docopt_cmd
	def do_reallocate_person(self, arg):
		"""Usage: reallocate_person <first_name> <last_name> <new_room_name>"""
		first_name = arg["<first_name>"]
		last_name = arg["<last_name>"]
		full_name = first_name.strip() + " " + last_name.strip()
		new_room_name = arg["<new_room_name>"]

		Amity.reallocate_person(full_name, new_room_name.strip())

	@docopt_cmd
	def do_load_people(self, arg):
		"""Usage: load_people <filename>"""
		filename = arg["<filename>"]

		Amity.load_people(filename)

	@docopt_cmd
	def do_print_allocations(self, arg):
		"""Usage: print_allocations [--o=filename]"""
		filename = arg["--o"]

		if filename:
			Amity.print_allocations(filename)
		else:
			Amity.print_allocations()

	@docopt_cmd
	def do_print_unallocated(self, arg):
		"""Usage: print_unallocated [--o=filename]"""
		filename = arg['--o']

		if filename:
			Amity.print_unallocated(filename)
		else:
			Amity.print_unallocated()

	@docopt_cmd
	def do_print_room(self, arg):
		"""Usage: print_room <room_name>"""
		room_name = arg["<room_name>"]

		Amity.print_room(room_name)

	@docopt_cmd
	def do_save_state(self, arg):
		"""Usage: save_state [--db=sqlite_database]"""
		database_name = arg["--db"]
		Amity.save_state(database_name)

	@docopt_cmd
	def do_load_state(self, arg):
		"""Usage: load_state [--db=sqlite_database]"""
		database_name = arg["--db"]
		if os.path.exists(database_name):
			Amity.load_state(database_name)
		else:
			print("database not found")

	@docopt_cmd
	def do_quit():
		print("goodbye!")
		exit()

if __name__ == "__main__":
	introduction()
	try:
		AmityCLI().cmdloop()
	except KeyboardInterrupt:
		save_state_on_interrupt()
