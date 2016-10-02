# Office Space Allocation

## Usage Commands
1. `create_room <room_name>...` - Creates a room in Amity. This command can create as many rooms as possible by specifying multiple room names
2. `add_person <person_name> <FELLOW|STAFF>` - Add a person to the system and allocates the person to a random room
3. `reallocate_person <person_identifier> <new_room_name>` - Reallocate the person with person with `person_identifier` to `new_room_name`
4. `load_people` - Adds people to rooms from a text file
5. `print_allocations [-o=filename]` - Prints a list of allocations  onto the screen. Specifying the optional -o option here outputs the information to the text file provided
6. `print_unallocated [-o=filename]` - Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the text file provided
7. `print_room <room_name>` - Prints the names of the people in `room_name` on the screen
8. `save_state [--db=sqlite_database]` - Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified.
9. `load_state <sqlite_database>` - Loads data from a database into the application.