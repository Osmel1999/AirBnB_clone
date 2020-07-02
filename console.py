#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    'Command interpreter for HBnb Project'
    prompt = "(hbnb) "

    def do_quit(self, args):
        'Exit of the interpreter'
        return (True)

    def do_EOF(self, args):
        'End of File implementation. Exit interpreter'
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    command_prompt = HBNBCommand()
    command_prompt.cmdloop()
