#!/usr/bin/python3
import json
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_quit(self, arg):
        'Quit command to exit the program'
        self.close()
        quit()
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        self.close()
        quit()
        return True

    def do_create(self, arg):
        'Create command to create a new instance'
        if str(*parse(arg)) == "":
            print("** class name missing **")
        elif str(*parse(arg)) == "BaseModel":
            bm = BaseModel()
            print(bm.id)
        else:
            print("** class doesn't exist **")

    def do_all
   
    def do_show(self, arg):
	a = (parse(arg)[1])
        b = (parse(arg)[2])
        with open("file.json", "r") as f:
             list_obj = json.load(f)
             for k in list_obj:
                 if k ==

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        pass

def parse(arg):
    'Convert argulents to an argument tuple'
    return tuple(map(str, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
