class Room:

	room_cache = {}

	def __init__(self, **kwargs):
		self.name = kwargs.get("name", "no name")
		self.type = kwargs.get("type", "OF")

		if self.type == "OF":
			if "Living Space" in Room.room_cache.keys():
				Room.room_cache["Offices"].append(self.name)
			else:
				Room.room_cache["Offices"] = [self.name]
		elif self.type == "LS":
			if "Living Space" in Room.room_cache.keys():
				Room.room_cache["Living Spaces"].append(self.name)	
			else:
				Room.room_cache["Living Spaces"] = [self.name]