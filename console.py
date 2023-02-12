#!/usr/bin/python3
""" The console is the entry point of the AirBnB-clone command interpreter."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ The command-line interpreter that defines commands."""
    prompt = "(hbnb) "

    __cls = {
            'BaseModel',
            'User',
            'State',
            'City',
            'Place',
            'Amenity',
            'Review'
            }

    def do_create(self, args):
        """ Creates a new instance of a model,
        saves it (to the JSON file) and prints the id.
        """
        slist = args.split()
        if len(slist) == 0:
            print("** class name missing **")
        elif len(slist) > 1:
            pass
        else:
            if slist[0] in HBNBCommand.__cls:
                print(eval(slist[0])().id)
                storage.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints string representation of instance
        based on the class name and id.
        """
        slist = args.split()
        objdict = storage.all()
        if len(slist) == 0:
            print("** class name missing **")
        elif (len(slist) == 1 and slist[0] not in HBNBCommand.__cls):
            print("** class doesn't exist **")
        elif len(slist) == 1 and slist[0] in HBNBCommand.__cls:
            print("** instance id missing **")
        elif len(slist) == 2 and slist[0] in HBNBCommand.__cls:
            try:
                obj = objdict["{}.{}".format(slist[0], slist[1])]
                print(obj.__str__())
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id. """
        slist = args.split()
        objdict = storage.all()
        if len(slist) == 0:
            print("** class name missing **")
        elif (len(slist) == 1 and slist[0] not in HBNBCommand.__cls):
            print("** class doesn't exist **")
        elif len(slist) == 1 and slist[0] in HBNBCommand.__cls:
            print("** instance id missing **")
        elif len(slist) == 2 and slist[0] in HBNBCommand.__cls:
            try:
                del objdict["{}.{}".format(slist[0], slist[1])]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, args):
        """ Prints string representation of all instances
        based or not on the class name.
        """
        slist = args.split()
        objdict = storage.all()
        if len(slist) == 0:
            for k in objdict.keys():
                print(objdict[k].__str__())
        elif len(slist) == 1:
            retlist = []
            if slist[0] in HBNBCommand.__cls:
                for obj in objdict.values():
                    if slist[0] == obj.__class__.__name__:
                        retlist.append(obj.__str__())
                    else:
                        continue
                print(retlist)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """  Updates an instance based on the class name
        and id by adding or updating attribute.
        """
        slist = args.split()
        objdict = storage.all()
        if len(slist) == 0:
            print("** class name missing **")
        elif len(slist) == 1 and slist[0] not in HBNBCommand.__cls:
            print("** class doesn't exist **")
        elif len(slist) == 1 and slist[0] in HBNBCommand.__cls:
            print("** instance id missing **")
        elif len(slist) == 2 and slist[0] in HBNBCommand.__cls:
            try:
                obj = objdict["{}.{}".format(slist[0], slist[1])]
                print("** attribute name missing **")
            except KeyError:
                print("** instance id missing **")
        elif len(slist) == 3:
            print("** value missing **")
        elif len(slist) == 4:
            obj = objdict["{}.{}".format(slist[0], slist[1])]
            obj[slist[2]] = slist[3]
            storage.save()

    def do_quit(self, args):
        """ Quits console when the command 'quit' is executed."""
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
