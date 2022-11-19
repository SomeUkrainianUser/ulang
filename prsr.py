from lexer import *
from stack import *
import operator

def parse_code(u_code):
    lexems = lexem_analysis(u_code)
    vars = {}
    funcs = {}
    operators = ['+', '-', '*', '/', '**', '//', '%', '&', '|', '^', '~']
    s = Stack()
    i = 0
    def call(func, args):
        nonlocal s
        nonlocal i
        s.push(i)
        for j in args:
            s.push(j)
    def ret():
        nonlocal s
        nonlocal i
        i = s.pop().data
    while i < len(lexems):
        lexem = lexems[i][0]
        if lexem.startswith('//'): continue
        elif lexem == "print":
            if lexems[i][1].startswith('"'):
                print(lexems[i][1].replace("__", " ", -1).replace('"', '', 2))
            else:
                print(vars[lexems[i][1]])
        elif lexem == "var":
            vars[f'{lexems[i][1]}'] = lexems[i][2].replace('"', '', -1).replace("__", " ", -1)
        elif lexem == "delete":
            vars.pop(lexems[i][1], "")
            funcs.pop(lexems[i][1], "")
        elif lexem == "input":
            tmp = input(lexems[i][2].replace('"', '', 2).replace("__", " ", -1))
            vars[lexems[i][1]] = tmp
        elif lexem == "push":
            if lexems[i][1].startswith("&"):
                s.push(vars[lexems[i][1].replace("&")])
            else:
                s.push(lexems[i][1])
        elif lexem == "popto":
            vars[lexems[i][1]] = s.pop().data
        elif lexem == "pop":
            s.pop()
        elif lexems[i][1] in operators and lexems[i][3] == "is":
            op = lexems[i][1]
            op1 = lexems[i][0]
            op2 = lexems[i][2]
            res = lexems[i][4]
            try:
                if (op == '+'): vars[res] = int(vars[op1]) + int(vars[op2])
                if (op == '-'): vars[res] = int(vars[op1]) - int(vars[op2])
                if (op == '*'): vars[res] = int(vars[op1]) * int(vars[op2])
                if (op == '/'): vars[res] = int(vars[op1]) / int(vars[op2])
                if (op == '**'): vars[res] = int(vars[op1]) ** int(vars[op2])
                if (op == '//'): vars[res] = int(vars[op1]) // int(vars[op2])
                if (op == '%'): vars[res] = int(vars[op1]) % int(vars[op2])
                if (op == '&'): vars[res] = operator.and_(int(vars[op1]), int(vars[op2]))
                if (op == '|'): vars[res] = operator.or_(int(vars[op1]), int(vars[op2]))
                if (op == '^'): vars[res] = operator.xor(int(vars[op1]), int(vars[op2]))
                if (op == '~'): vars[res] = operator.inv(int(vars[op1]), int(vars[op2]))
            except:
                if (op == '+'): vars[res] = vars[op1] + vars[op2]
        elif lexem == "goto":
            i = int(lexems[i][1])-1
            continue
        elif lexem == "bgotoc":
            condition = lexems[i][1]
            op1 = int(vars[lexems[i][2]])
            op2 = int(vars[lexems[i][3]])
            destination = int(lexems[i][4])-1

            if condition == "eq" and op1 == op2:
                i = destination
                continue
            elif condition == "ne" and op1 != op2:
                i = destination
                continue
            elif condition == "gt" and op1 > op2:
                i = destination
                continue
            elif condition == "lt" and op1 < op2:
                i = destination
                continue
            elif condition == "ge" and op1 >= op2:
                i = destination
                continue
            elif condition == "e" and op1 <= op2:
                i = destination
                continue
        elif lexem == "ugotoc":
            condition = lexems[i][1]
            op = lexems[i][2]
            destination = int(lexems[i][3])-1
            if condition == 'z' and vars[op] == 0:
                i = destination
                continue
            elif condition == 'nz' and vars[op] != 0:
                i = destination
                continue
            elif condition == 'lt' and vars[op] < 0:
                i = destination
                continue
            elif condition == 'gt' and vars[op] > 0:
                i = destination
                continue
            elif condition == 'lz' and vars[op] <= 0:
                i = destination
                continue
            elif condition == 'gz' and vars[op] >= 0:
                i = destination
                continue
        elif lexem == "while":
            op1 = int(vars[lexems[i][1]])
            condition = lexems[i][2]
            op2 = int(vars[lexems[i][3]])
            wto = int(lexems[i][4])



        else:
            for j in range( len(vars) ):
                if lexems[i][0] not in vars:
                    print(f"Error: undefined reference to {lexems[i][0]}")
                    return
        i += 1
