#!/usr/bin/python3
""" Command Line & Interactive shell for DogPlug """
import cmd
from models.base_model import BaseModel
from models.county import County
from models.dog import Dog
from models.groomer import Groomer
from models.location import Location
from models.owner import Owner
from models.review import Review
from models.service import Service
from models.town import Town
from models import storage
import shlex


classes = {
        "BaseModel": BaseModel,
        "County": County,
        "Dog": Dog,
        "Groomer": Groomer,
        "Location": Location,
        "Owner": Owner,
        "Review": Review,
        "Service": Service,
        "Town": Town
    }

class DogPlug(cmd.Cmd):
    """ Simple commands processor to test model objects """
    FRIENDS = ['Tony', 'Maiyo', 'Lupin']
    classes = ['BaseModel', 'County', 'Dog', 'Groomer', 'Location', 'Owner', 'Review', 'Service', 'Town']
    prompt = "(DogPlug)"
    intro = "Welcome to DogPlug"
    
    def do_greet(self, person):
        """ Greet the person """
        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' %person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = 'hello'
        print(greeting)
    
    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [
                f for f in self.FRIENDS if f.startswith(text)
            ]
        return completions
    
    def help_greet(self):
        print ('\n'.join([
            'greet [person]',
            'Greet the named person',
        ]))

    def emptyline(self):
        """ Execute nothing incase of an empty line"""
        return False
    
    def do_quit(self, line):
        """ Quit the CMD prompt"""
        return True
    
    def do_EOF(self, line):
        """ Safely exit the command processing """
        return True
    
    def help_create(self):
        print('\n'.join([
            'Create class instance',
            'Usage: create <class name>',
        ]))
    
    def complete_create(self, text, args, begidx, endidx):
        """ Give predictions when keying in class names to create instances"""
        if not text:
            completions = self.classes[:]
        else:
            completions = [
                f for f in self.classes if f.startswith(text)
            ]
        return completions
    
    def do_create(self, args):
        """ Create instances of classes"""
        args = args.split()
        if len(args) == 0:
            print("**class name missing**")
            return False
        if args[0] not in classes:
            print("**Invalid class name**")
            return False
        else:
            model_instance = classes[args[0]]()
            model_instance.save()
            print(model_instance.id)
    
    def help_show(self):
        print('\n'.join([
            'Show attributes of a specific class instance',
            'Usage: destroy <class name> <instance id>',
        ]))
    
    def complete_show(self, text, args, begidx, endidx):
        """ Give predictions when keying in class names to create instances"""
        if not text:
            completions = self.classes[:]
        else:
            completions = [
                f for f in self.classes if f.startswith(text)
            ]
        return completions
    
    def do_show(self, args):
        """ Display attributes of classes' instance"""
        args = args.split()
        if len(args) == 0:
            print("**class name missing")
        else:
            if args[0] not in classes:
                print("**Invalid class name**")
            else:
                if len(args) > 1:
                    key = "{}.{}".format(args[0], args[1])
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("**instance not found**")
                else:
                    print("**Instance id missing**")
    
    def help_destroy(self):
        print('\n'.join([
            'Delete a class instance from storage',
            'Usage: show <class name> <instance id>',
        ]))
    
    def complete_destroy(self, text, args, begidx, endidx):
        """ Give predictions when keying in class names to create instances"""
        if not text:
            completions = self.classes[:]
        else:
            completions = [
                f for f in self.classes if f.startswith(text)
            ]
        return completions
    
    def do_destroy(self, args):
        """ Display attributes of classes' instance"""
        args = args.split()
        if len(args) == 0:
            print("**class name missing")
        else:
            if args[0] not in classes:
                print("**Invalid class name**")
            else:
                if len(args) > 1:
                    key = "{}.{}".format(args[0], args[1])
                    if key in storage.all():
                        storage.all().pop(key)
                        storage.save()
                        print("{}.{} destroyed".format(args[0], args[1]))
                    else:
                        print("**instance not found**")
                else:
                    print("**Instance id missing**")
    
    def help_all(self):
        print('\n'.join([
            'Display all objects based on the class or not',
            'Usage: all <class name>',
            'or',
            'Usage: all',
        ]))
    
    def complete_all(self, text, args, begidx, endidx):
        """ Give predictions when keying in class names to create instances"""
        if not text:
            completions = self.classes[:]
        else:
            completions = [
                f for f in self.classes if f.startswith(text)
            ]
        return completions

    def do_all(self, args):
        """ Display all objects based on the class or not"""
        args = args.split()
        objs_dict = {}
        if len(args) == 0:
            objs = storage.all()
            for key,value in objs.items():
                objs_dict[key] = objs[key].to_dict()
            print(objs_dict)
        else:
            if args[0] in classes:
                objs = storage.all(args[0])
                for key,value in objs.items():
                    objs_dict[key] = objs[key].to_dict()
                print(objs_dict)
            else:
                print("**Invalid class name**")
    
    def help_update(self):
        print('\n'.join([
            'Update objects',
            'Usage: update <class name> <id> <attribute name> <attribute value>',
        ]))
    
    def complete_update(self, text, args, begidx, endidx):
        """ Give predictions when keying in class names to create instances"""
        if not text:
            completions = self.classes[:]
        else:
            completions = [
                f for f in self.classes if f.startswith(text)
            ]
        return completions
    
    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["weight, age, price"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                all_objs = storage.all()
                if k in storage.all():
                    instance = all_objs[k]
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Dog" or args[0] == "Service":
                                if args[2] == "weight" or args[2] == "age" or args[2] == "price":
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                            setattr(instance, args[2], args[3])
                            instance.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
        
    

if __name__ == '__main__':
    DogPlug().cmdloop()
