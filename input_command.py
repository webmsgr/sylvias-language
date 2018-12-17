
def cinput(args):
    arg = args[0]
    return input(arg)
def makeCommands(func):
    func("input",cinput,1,False)
