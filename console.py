#!/usr/bin/python3
"""Defines a command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Represents the command interpreter"""
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
        """Close command"""
        if self.file:
            self.file.close()
            self.file = None

    def emptyline(self):
        """Empty line do nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
