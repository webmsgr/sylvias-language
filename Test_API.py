#! python3

import lang
def hello_world():
    print("hello world!")

lang.addCommand("testapi",hello_world,0,False)
lang.parseSingle("testapi")
