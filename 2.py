import sys

argument = sys.argv[1:]
a = str(argument[0])

arithmetic = {"add": "+",
              "sub": "-",
              "mul": "*",
              "div": "/"}

print(eval(arithmetic[a].join(sys.argv[2:])))
