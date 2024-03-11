import json
import os

class FileStorage:
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""Returns the dictionary __objects."""
		return FileStorage.__objects
	
	def new(self, obj):
		"""Sets in __objects the obj with key <obj class name>.id."""
		key = obj.__class__.__name__ + "." + obj.id
		FileStorage.__objects[key] = obj

	def save(self):
		"""Serializes __objects to the JSON file."""
		with open(FileStorage.__file_path, "w") as file:
			json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, file)

	def reload(self):
		"""Deserializes the JSON file to __objects."""
		if os.path.exists(FileStorage.__file_path):
			with open(FileStorage.__file_path, "r") as file:
				FileStorage.__objects = json.load(file)
				for k, v in FileStorage.__objects.items():
					cls_name = v.pop('__class__', None)
					if cls_name:
						FileStorage.__objects[k] = eval(cls_name)(**v)