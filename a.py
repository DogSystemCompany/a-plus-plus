from sys import argv

file = open(argv[1], "r").read()

###
### --------------------
###
### The Programming Language Brain
###
### --------------------
###

def if_integer(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False

variables = {}
tok = ""
lineNumber = 1
thingInError = ""
printNumberStarted = 0
printNumber = ""
printStarted = 0
printText = ""
printStrType = 0
printIntType = 0
commentStarted = 0
varStarted = 0
varName = ""
varTextIntStr = ""
varEquals = 0

for char in file:
    tok += char
    if tok == "\n":
        lineNumber += 1
        tok = ""
    elif tok == "$":
        varStarted = 1
    elif tok == "print " or tok == "PRINT ":
        printStarted = 1
        tok = ""
    elif tok == "//":
        commentStarted = 1
        tok = ""
    elif varStarted == 1:
        if tok == "=":
            varEquals = 1
            varStarted = 0
            tok = ""
        elif tok == " ":
            tok = ""
        else:
            varName += tok
            tok = ""
    elif varEquals == 1:
        if tok == ";":
            if if_integer(varTextIntStr):
                variables[varName] = int(varTextIntStr)
                varEquals = 0
                varStarted = 0
                varTextIntStr = ""
                varName = ""
                tok = ""
            else:
                variables[varName[1:]] = varTextIntStr
                varEquals = 0
                varStarted = 0
                varTextIntStr = ""
                varName = ""
                tok = ""
        else:
            varTextIntStr = varTextIntStr + tok
            tok = ""
    elif commentStarted == 1:
        if tok == "*":
            commentStarted = 0
            tok = ""
        else:
            tok = ""
    elif printStarted == 1:
        if tok == ";" and printIntType == 0:
            print(printText)
            printText = ""
            printStrType = 0
            printStarted = 0
            tok = ""
        elif tok == "\"" or tok == "'" and printStrType == 0:
            if printIntType == 1:
                print("Error, Cannot Put Double Quote Before A Int OR Character... At Line " + str(lineNumber))
                quit()
            else:
                printStrType = 1
                tok = ""
        elif printStrType == 1 and tok == "\"" or tok == "'":
            printStrType = 0
            tok = ""
        elif printIntType == 1 and tok == ";":
            if if_integer(printText):
                print(printText)
                printStarted = 0
                printIntType = 0
                printText = ""
                tok = ""
            else:
                print("Not A Integer... A String... At Line " + str(lineNumber))
                quit()
        elif printStrType == 1:
            printText += tok
            tok = ""
        else:
            printIntType = 1
            printText += tok
            tok = ""
    elif tok == " ":
        tok = ""
