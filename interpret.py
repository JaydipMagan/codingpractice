# Write a simple interpreter which understands "+", "-", and "*" operations.
# Apply the operations in order using command/arg pairs starting with the
# initial value of `value`. If you encounter an unknown command, return -1.
#
# interpret(1, ["+"], [1]) → 2
# interpret(4, ["-"], [2]) → 2
# interpret(1, ["+", "*"], [1, 3]) → 6

def interpret(value, commands, args):
    if len(commands) != len(args):
        return -1

    outCome = value
    i = 0
    for command in commands:
        if command == "+":
            outCome += args[i]
            i+=1
        elif command == "-":
            outCome -= args[i]
            i+=1
        elif command == "*":
            outCome = outCome * args[i]
            i+=1
        else:
            return -1
    return outCome

print(str(interpret(1,["+","*"],[1,3]))) #6
