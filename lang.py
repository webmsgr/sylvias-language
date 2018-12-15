#! python3

vars = {}

quellErrors = True
def listtostr(list):
    o = ""
    for item in list:
        o += item
    return o
import shlex,sys

def set(var,context):
    vars[var[0]] = context
    return context

def static(c):
    c = listtostr(c)
    return c
def cprint(data):
    print(listtostr(data))
    return ""


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

commands = {
    "print":{"func":cprint,"args":1,"passcontext":False},
    "invar":{"func":set,"args":1,"passcontext":True},
    "static":{"func":static,"args":1,"passcontext":False}
}
if __name__ == "__main__":
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
