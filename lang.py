#! python3

vars = {}

line = 0

quellErrors = True
def listtostr(list):
    o = ""
    for item in list:
        o += item
    return o

import shlex,sys,os

def set(var,context):
    vars[var[0]] = context
    return context

def static(c):
    c = listtostr(c)
    return c
def cprint(data):
    print(listtostr(data))
    return ""

def importFunc(name):
    try:
        imported = __import__(name)
    except ImportError:
        error("Import Failed")
    imported.makeCommands(addCommand)



def error(message):
    print(" ERROR ".center(11,"="))
    print(message)
    print("".center(11,"="))
    if not quellErrors:
        sys.exit(1)

def parseSingle(d,context):
    tokens = shlex.split(d)
    # Varables first
    c = 0
    tktmp = tokens
    for token in tokens:
        if token[0] == "<":
            var = token[1:]
            if var in vars:
                #print(c)
                tktmp[c] = vars[var]
                #print(tktmp)
            else:
                error("Varable not found ({})".format(var))
                return
        if token == "$const":
            tokens[c] = context
        c += 1
    tokens = tktmp
    if not tokens[0] in commands:
        error("Command not found ({})".format(tokens[0]))
        return

    command = commands[tokens[0]]
    if command["args"] > 0:
        if len(tokens) >= command["args"] + 1:
            args = tokens[1:command["args"]+1]
            if command["passcontext"]:
                c = command["func"](args,context)
            else:
                c = command["func"](args)
        else:
            error("statement {} expected {} arguments. Got {}".format(tokens[0],command["args"],len(tokens)-1))
            return
    else:
        if command["passcontext"]:
            c = command["func"](context)
        else:
            c = command["func"]()
    return c
def parsemultiple(toparse):
    global line
    line = 0
    c = ""
    while True:
        try:
            #print("toparse[{}] = {}".format(line,toparse[line]))
            c = parseSingle(toparse[line],c)
        except IndexError:
            #error(line)
            break
        line = line + 1
        if line <= -1:
            break

def concat(args):
    return listtostr(args)
def jump(args):
    global line
    #print("setting line to {}".format(int(args[0]) - 2))
    line = int(args[0]) - 2
commands = {}
def addCommand(name,func,args,passcontext):
    commands[name] = {"func":func,"args":args,"passcontext":passcontext}
def exit():
    global line
    line = -2
def parsefile(name):
    with open(name) as f:
        data = f.read()
        #print(data)
        f.close()
    data = data.split("\n")
    parsemultiple(data)
def imprt(args):
    arg = args[0]
    importfunc(arg)
# Commands
addCommand("print",cprint,1,False)
addCommand("jump",jump,1,False)
addCommand("invar",set,1,True)
addCommand("static",static,1,False)
addCommand("concat",concat,2,False)
addCommand("exit",exit,0,False)
importFunc("input_command")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            parsefile(sys.argv[1])
        else:
            print("file does not exist")
            sys.exit(1)
        sys.exit(0)

    q = True
    c = ""
    print("Sylvia's Programming Languge Shell")
    print("V1.0")
    print("Type 'quit' to quit")
    while q:
        cmd = input(">>> ")
        cmd = cmd.strip()
        if cmd == "quit":
            q = False
        else:
            c = parseSingle(cmd,c)
