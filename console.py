#!/usr/bin/python3


import cmd

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

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
