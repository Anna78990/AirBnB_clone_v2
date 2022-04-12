#!/usr/bin/python3
"""Defines the command interpreter"""
import cmd
import shlex
import re
import sys
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
        args = arg.split(" ")
        if args[0] in self.__classes:
            a = self.__classes[args[0]]()
            storage.save()
            print(a.id)
            for i in args:
                defStr = re.match(r"(^{A-Z}*{a-z}*{=}{\"}{A-Z}*{a-z}*{\"}$)", i)
                if defStr:
                    key = i.split("=")
                    key[1].replace("_", " ")
                    num = re.search("{0-9}+", key[1])
                    if num:
                        num = int(num)
                    floatnum = re.search("{0-9}+{.}{0-9}+", key[1])
                    if floatnum:
                        floatnum = float(floatnum)
                    a.key[0] = key[1]
                else:
                    pass
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
            print("** instance id missing **")
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
            print("** instance id missing **")
        else:
            inst = "{}.{}".format(words[0], words[1])
            if inst not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[inst]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        words = arg.split()
        if len(arg) > 0 and words[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            list_obj = []
            for obj in storage.all().values():
                if len(arg) > 0 and words[0] == obj.__class__.__name__:
                    list_obj.append(obj.__str__())
                elif len(arg) == 0:
                    list_obj.append(obj.__str__())
            print(list_obj)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        words = shlex.split(arg)
        cls_name = words[0] if len(words) > 0 else None
        id = words[1] if len(words) > 1 else None
        attribute = words[2] if len(words) > 2 else None
        value = words[3] if len(words) > 3 else None
        obj = "{}.{}".format(cls_name, id)
        if cls_name is None:
            print("** class name missing **")
            return False
        if cls_name not in self.__classes:
            print("** class doesn't exist **")
            return False
        if id is None:
            print("** instance id missing **")
            return False
        if obj not in storage.all().keys():
            print("** no instance found **")
            return False
        if attribute is None:
            print("** attribute name missing **")
            return False
        if value is None:
            print("** value missing **")
            return False
        if len(words) == 4:
            setattr(storage.all()[obj], attribute, value)
            storage.save()

    def default(self, line):
        """Called when an unknown command is entered."""
        arg = line.split(".")
        if len(arg) > 0 and arg[0] in self.__classes:
            if (arg[1] == "all()"):
                self.do_all(arg[0])
            elif (arg[1] == "count()"):
                i = 0
                for obj in storage.all().values():
                    if arg[0] == obj.__class__.__name__:
                        i += 1
                print(i)
            elif (arg[1][0:4] == "show"):
                new_arg = arg[1][5:-1]
                self.do_show("{} {}".format(arg[0], new_arg))
            elif (arg[1][0:7] == "destroy"):
                new_arg = arg[1][8:-1]
                self.do_destroy("{} {}".format(arg[0], new_arg))
            elif (arg[1][0:6] == "update"):
                new_arg = arg[1][7:-1]
                li = new_arg.split("\"")
                li_ap = []
                for i in li:
                    if i != '' and i != ", ":
                        li_ap.append(i)
                args = ' '.join(li_ap)
                print(args)
                self.do_update("{} {}".format(arg[0], str(args)))

    def emptyline(self):
        """Do nothing when emptyline is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
