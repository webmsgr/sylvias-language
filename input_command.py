
def cinput(args):
    arg = args[0]
    return input(arg)
def makeCommands(func):
    func("input",cinput,1,False) # why do i have only this function in this file? i dont know!
