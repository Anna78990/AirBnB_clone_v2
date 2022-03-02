#!/usr/bin/python3
"""Defines the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define the command interpreter"""

    prompt = '(hbnb) '
    file = None
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        return True

    def do_create(self, arg):
        'Create command to create a new instance'
        if arg == "":
            print("** class name missing **")
        elif arg in self.__classes:
            a = self.__classes[arg]()
            storage.save()
            print(a.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show an instance with class name and the id"""
        words = arg.split()
        if arg == "":
            print("** class name missing **")
        elif words[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance is missing **")
        else:
            inst = "{}.{}".format(words[0], words[1])
            if inst not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[inst])

    def do_destroy(self, arg):
        """Destroy a instance with class name and id"""
        words = arg.split()
        if arg == "":
            print("** class name missing **")
        elif words[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance is missing **")
        else:
            inst = "{}.{}".format(words[0], words[1])
            if inst not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[inst]
                storage.save()

    def emptyline(self):
        """Do nothing when emptyline is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
