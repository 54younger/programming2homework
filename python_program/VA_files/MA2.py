"""
Solutions to module 2 - A calculator
Student:
Mail:
Reviewed by:
Reviewed date:
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper

dict = {"function_1": ['sin', 'cos', 'exp', 'log', 'fac', 'fib'],"function_n": ['max', 'sum', 'std', 'min']}

class SyntaxError(Exception):
    def __init__(self, func_result):
        self.func_result = func_result
        super().__init__(self.func_result)

class EvaluationError(Exception):
    def __init__(self, func_result):
        self.func_result = func_result
        super().__init__(self.func_result)


def statement(wtok, variables):
    """ See syntax chart for statement"""

    result = assignment(wtok, variables)
    if wtok.is_comment():
        raise SyntaxError("Unexpected comment")
    if not wtok.is_at_end():
        raise SyntaxError("Expected end of statement")
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)

    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
            wtok.next()

        else:
            raise SyntaxError(" Expected variable after '='")


    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)

    while wtok.get_current() == '+' or wtok.get_current() == '-':
      while wtok.get_current() == '+':
          wtok.next()
          result = result + term(wtok, variables)

      while wtok.get_current() == '-':
          wtok.next()
          result = result - term(wtok, variables)

    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)

    while wtok.get_current() == '*' or wtok.get_current() == '/':
      while wtok.get_current() == '*':
          wtok.next()
          result = result * factor(wtok, variables)

      while wtok.get_current() == '/':
          wtok.next()
          divisor = factor(wtok, variables)
          if divisor == 0:
              raise EvaluationError("Division by zero")
          result = result / divisor

    return result

def math_function(wtok, variables):
    func = wtok.get_current()
    wtok.next()

    if wtok.get_current() != '(':
        raise SyntaxError("Expected '('")

    wtok.next()
    func_result = assignment(wtok, variables)

    if wtok.get_current() != ')':
        raise SyntaxError("Expected ')'")

    wtok.next()
    if func == 'sin':
        result = math.sin(func_result)
    elif func == 'cos':
        result = math.cos(func_result)
    elif func == 'exp':
        result = math.exp(func_result)
    elif func == 'log':
        if func_result <= 0:
            raise EvaluationError("there can not equal or less than 0 in log")
        result = math.log(func_result)
    elif func == 'fac':
        if not func_result.is_integer() or func_result < 0:
            raise EvaluationError("Expected nonnegative integer")
        result = math.factorial(int(func_result))
    elif func == 'fib':
        if not func_result.is_integer() or func_result < 0:
            raise EvaluationError("Expected nonnegative integer")
        fib_mem = [0, 1]
        def fib(n):
            if n < len(fib_mem):
                return fib_mem[n]
            else:
                fib_mem.append(fib(n-1) + fib(n-2))
                return fib_mem[n]
        result = fib(int(func_result))
    else:
        raise SyntaxError("Unknown function")
    return result



def arglist(wtok, variables):

    arg = []
    if wtok.get_current() != '(':
        #print(wtok.get_current())
        raise SyntaxError("arglist Expected '('")
    wtok.next()
    while 1:
        arg.append(assignment(wtok, variables))

        if wtok.get_current() == ',':
            wtok.next()
            continue
        elif wtok.get_current() == ')':
            wtok.next()
            return arg
        elif wtok.is_at_end:
            raise SyntaxError("Expected ')'")

def factor(wtok, variables):
    """ See syntax chart for factor"""

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() in dict["function_1"]:
        result = math_function(wtok, variables)

    elif wtok.get_current() in dict["function_n"]:

        function_n_name = wtok.get_current()
        wtok.next()
        arg = arglist(wtok, variables)
        if function_n_name == 'max':
            result = max(arg)
        elif function_n_name == 'sum':
            result = sum(arg)
        elif function_n_name == 'std':
            result = sum(arg) / len(arg)
        elif function_n_name == 'min':
            result = min(arg)

    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError(f" Undefined variable: '{wtok.get_current()}'")

    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)
    else:
        raise SyntaxError(
            "Expected number, name or '(' or function")

    return result



def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation
    # requires another initiation you have to update the test file accordingly.
    init_file = './python_program/MA2Files/MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        print("file not find")

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('\ninit  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'vars':
            for key, value in variables.items():
                print(f'  {key} = {value}')
            continue

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')



if __name__ == "__main__":
    main()
