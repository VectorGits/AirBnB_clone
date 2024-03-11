"""
This module contains the HBNBCommand class, which is a command line interpreter
for the AirBnB clone project. It uses the cmd module for the command line interface.
"""

import cmd

class HBNBCommand(cmd.Cmd):
	"""
	HBNBCommand class that contains the logic for the command line interpreter.
	
	Attributes:
		prompt (str): The command line prompt string.
	"""

	prompt = '(hbnb) '

	def do_quit(self, arg):
		"""
		Handles the 'quit' command, which exits the program.
		
		Args:
			arg: The arguments passed to the 'quit' command. Not used.
		
		Returns:
			True to signal the program to exit.
		"""
		return True

	def do_EOF(self, arg):
		"""
		Handles the 'EOF' command, which also exits the program.
		
		Args:
			arg: The arguments passed to the 'EOF' command. Not used.
		
		Returns:
			True to signal the program to exit.
		"""
		return True

	def emptyline(self):
		"""
		Handles the case where an empty line is entered in response to the prompt.
		Does nothing.
		"""
		pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()