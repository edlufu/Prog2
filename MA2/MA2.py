"""
Solutions to module 2 - A calculator
Student: Edvin Lundberg
Mail: edvin.lundberg.se@gmail.com
Reviewed by: 13/04
Reviewed date: Ema Duljković
"""


from MA2tokenizer import TokenizeWrapper
import math
from tokenize import TokenError


# ---------------------------------- ERROR CLASSESS
class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


# ---------------------------------- CALCULATION
def statement(wtok, variables):
    """Handles EOL"""
    result = assignment(wtok, variables)
    if wtok.is_at_end() == False:
        raise SyntaxError("Expected end of line")
    return result


def assignment(wtok, variables):
    """
    Handles:
        expressions and variable definition
    """
    result = expression(wtok, variables)
    #   while next is assignment operator handle assignment
    while wtok.get_current() == "=":
        wtok.next()
        if wtok.is_name():
            #   if current is name, define with result and memorize
            variables[wtok.get_current()] = result
        else:
            raise SyntaxError("Excpected varaible name")
        wtok.next()

    return result


def expression(wtok, variables):
    """
    Handles:
        addition and subtraction of terms
    """
    result = term(wtok, variables)
    #   while there are more terms, add / subract
    while wtok.get_current() == "+" or wtok.get_current() == "-":
        if wtok.get_current() == "+":
            wtok.next()
            result = result + term(wtok, variables)
        else:
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """
    Handles:
        Division and multiplications of factors
    """

    result = factor(wtok, variables)
    #   while there are more factors, multiply / divide
    while wtok.get_current() == "*" or wtok.get_current() == "/":
        wtok.next()
        if wtok.get_previous() == "*":
            result = result * factor(wtok, variables)
        #   If division by zero, Evaluation Error message
        else:
            try:
                result = result / factor(wtok, variables)

            except ZeroDivisionError:
                raise EvaluationError("Division by zero")
    return result


def factor(wtok, variables):
    """
    Handles:
        Calculations att lowest level.
        Such as: functions, variable value retreving, numebers, etc.
    """

    # ----------------- CALCULATOR FUNCTIONS
    def fib(n):
        memory = {0: 0, 1: 1}
        # if n is not positive integer, raise EvalErr.
        if n < 0 or n % 1 != 0:
            raise EvaluationError(f"Argument to fib is {n}, must be positive integer")
        else:

            def _fib(n):
                if n not in memory:
                    memory[n] = _fib(n - 1) + _fib(n - 2)
                return memory[n]

            return _fib(n)

    def fac(n):
        result = 1
        # if n is not positive integer, raise EvalErr.
        if n < 0 or n % 1 != 0:
            raise EvaluationError(f"Argument to fac is {n}, must be positive integer")
        elif n > 0:
            # makes shure function return int
            x = int(n)
            result = x * fac(x - 1)
        return result

    def log(n):
        # if n is not larger than 0, raise EvalErr.
        if n <= 0:
            raise EvaluationError(f"Argument to log is {n}, must be larger than 0")
        else:
            return math.log(n)

    def mean(arglist):
        return sum(arglist) / len(arglist)

    # ----------------- LEXICONS WTIH FUNCTION NAME:OBJECT
    function_1 = {
        "sin": math.sin,
        "cos": math.cos,
        "exp": math.exp,
        "log": log,
        "fib": fib,
        "fac": fac,
    }

    function_n = {"min": min, "max": max, "sum": sum, "mean": mean}

    # ----------------- HANDLES RECOGNIZED FACTOR TYPES
    if wtok.get_current() == "(":
        # handles expresion in parenthasies before others
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ")":
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.get_current() in function_1:
        # handles functions with one argument
        function = function_1[wtok.get_current()]
        wtok.next()
        if wtok.get_current() == "(":
            argument = factor(wtok, variables)
            result = function(argument)

        else:
            raise SyntaxError('Expected "(" after function name')

    elif wtok.get_current() in function_n:
        # handles functions with multible arguments
        function = function_n[wtok.get_current()]
        wtok.next()
        result = function(arglist(wtok, variables))

    elif wtok.is_name():
        # fetches variable values
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError(f"Undefined variable: {wtok.get_current()}")

    elif wtok.is_number():
        # handles numbers
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == "-":
        # handles unary minus
        wtok.next()
        result = -factor(wtok, variables)

    else:
        raise SyntaxError("Expected number, variable, '(' or '-")
    return result


def arglist(wtok, variables) -> list:
    """Converts argument sequence into usable list"""
    # arglist starts with "("
    if wtok.get_current() == "(":
        wtok.next()
        arguments = [assignment(wtok, variables)]

        # while more arguments, add to list
        while wtok.get_current() == ",":
            wtok.next()
            arguments.append(assignment(wtok, variables))

        # arglist ends with ")""
        if wtok.get_current() != ")":
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
    else:
        raise SyntaxError("Expected '(' after function name")
    return arguments


# ---------------------------------- MAIN
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file.
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi, "F1": 2}
    init_file = "MA2init.txt"
    lines_from_file = ""
    try:
        with open(init_file, "r") as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print("init  :", line)
        else:
            line = input("\nInput : ")
        if line == "" or line[0] == "#":
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == "quit" or wtok.get_current() == "q":
            print("Bye")
            exit()

        elif wtok.get_current() == "vars":
            for var in variables.keys():
                print(f"  {var}\t: {variables[var]}")

        else:
            try:
                result = statement(wtok, variables)
                variables["ans"] = result
                print("Result:", result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'"
                )

            except EvaluationError as ee:
                print("*** Evaluation error: ", ee)

            except TokenError as te:
                print("*** Syntax error: Unbalanced parentheses")


if __name__ == "__main__":
    main()
