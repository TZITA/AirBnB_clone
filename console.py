#!/usr/bin/python3
""" The console is the entry point of the AirBnB-clone command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """ The command-line interpreter that defines commands."""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Quits the console when the command 'quit' is executed."""
        return True

    def do_EOF(self, args):
        """Quits the console when Ctrl+D is pressed."""
        return True

    def emptyline(self):
        """By default, this method of cmd.Cmd module remembers and
           executes the last command when 'Enter' is pressed on an
           empty line.

           To prevent this, this module is modified to do nothing.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
