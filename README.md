# sylvias-language

A minilanguige written in python3 for the develupment of sylvia's feather.

# Before you get started
After every command, a special variable called context is set. This can be auto passed into the next statement if requested. Variables are automagicly converted into text before parsing, like bash. Use `<varname` to insert variables. 

# Commands

```
static: Put some string on the context
invar: Take what is in context and put it into a variable
print: print stuff
```

# Example code

print string from var
```
static "yay github!"
invar string
print <string
```
put command into var and run it
```
static print
invar command
<command hi
```
Mixture of the two above
```
static print
invar command
static hi
invar arg
<command <arg
```
