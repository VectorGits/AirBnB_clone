import cmd

class HBNBCommand(cmd.Cmd):
	"""Command line interpreter for AirBnB"""
	prompt = '(hbnb) '

	def do_quit(self, arg):
		"""Quit command to exit the program"""
		# self.exit(arg)
		return True
	
	def do_EOF(self, arg):
		"""EOF command to exit the program"""
		# self.exit(arg)
		return True
	
	def emptyline(self):
		"""Called when an empty line is entered in response to the prompt"""
		pass

if __name__ == '__main__':
	HBNBCommand().cmdloop()