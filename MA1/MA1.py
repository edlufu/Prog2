"""
Solutions to module 1
Student: Edvin Lundberg
Mail: edvin.lundberg.se@gmail.com
Reviewed by: Joacim Stenlund
Reviewed date: 29/04 - 23
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib functionen.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""


import time
import math


def power(x, n: int):  # Optional
    """Computes x**n using multiplications and/or division"""

    def sqr(x):
        return x * x

    if n < 0:
        return (1 / x) * power(x, n + 1)
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return sqr(power(x, n / 2))
    else:
        return x * sqr(power(x, (n - 1) / 2))


def multiply(m: int, n: int) -> int:  # Compulsory
    """Computes m*n using additions"""

    def dubble(x):
        return x + x

    term = max(m, n)
    factor = min(m, n)

    if factor == 0:
        return 0
    elif factor % 2 == 0:
        return dubble(multiply(term, factor / 2))
    else:
        return term + dubble(multiply(term, (factor - 1) / 2))


def divide(t: int, n: int) -> int:  # Optional
    """Computes m//n using subtractions"""

    result = 0

    if t - n > 0:
        result += 1 + divide(t - n, n)

    return result


def harmonic(n: int) -> str:  # Compulsory
    """Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n == 1:
        return 1

    else:
        return (1 / n) + harmonic(n - 1)


def digit_sum_iter(x: int, base=10) -> int:  # Optional
    """Computes and returns the sum of the decimal (or other base) digits in x"""

    if base != 10:
        """Converts decimal integer x to base"""
        remainder = x % base
        quotient = x // base

        x_list = [str(remainder)]

        while quotient != 0:
            remainder = quotient % base
            quotient = quotient // base
            x_list = [str(remainder)] + x_list

    else:
        x_list = list(str(x))

    result = 0
    for e in x_list:
        result += int(e)

    return result


def get_binary(x: int) -> str:  # Compulsary
    """Returns the binary representation of x"""
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    elif x < 0:
        return "-" + get_binary(abs(x))
    else:
        return get_binary(x // 2) + f"{x % 2}"


def reverse_string(s: str) -> str:  # Optional
    """Returns the s reversed"""
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


def largest(a: iter):  # Compulsory
    """Returns the largest element in a"""

    def _max(a, b):
        if a > b:
            return a
        else:
            return b

    midpoint = len(a) // 2

    if len(a) == 1:
        return a[0]
    elif len(a) == 2:
        return _max(a[0], a[1])
    else:
        return _max(largest(a[:midpoint]), largest(a[midpoint:]))


def count(x, s: list) -> int:  # Compulsory
    """Counts the number of occurences of x on all levels in s"""
    tracker = 0

    if len(s) > 0:
        if s[0] == x:
            tracker += 1 + count(x, s[1:])
        elif type(s[0]) == list:
            tracker += count(x, s[0]) + count(x, s[1:])
        else:
            tracker += count(x, s[1:])

    return tracker


def zippa(l1: list, l2: list) -> list:  # Compulsory
    """Returns a new list from the elements in l1 and l2 like the zip function"""
    if len(l1) == 0 or len(l2) == 0:
        return l1 + l2
    else:
        return [l1[0]] + [l2[0]] + zippa(l1[1:], l2[1:])


def bricklek(f: str, t: str, h: str, n: int) -> str:  # Compulsory
    """Returns a string of instruction ow to move the tiles"""
    if n == 0:
        return []
    else:
        return bricklek(f, h, t, n - 1) + [f"{f}->{t}"] + bricklek(h, t, f, n - 1)


def fib(n: int) -> int:  # Compulsory
    """Returns the n:th Fibonacci number"""
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():

    print(count([1, 2], [[1, 2], [1, 2]]))

    print("\nCode that demonstates my implementations\n")
    "N/A"

    print("\n\nCode for analysing fib\n")

    def mean(x: list):
        return sum(x) / len(x)

    mtime = {}
    for x in [30, 31, 32, 33, 34, 35]:
        print(f"Tid för fib nr: {x}")
        tstart = time.perf_counter()
        fib(x)
        tstop = time.perf_counter()
        tmeasured = tstop - tstart
        print(f"{tmeasured:.4f} s")
        mtime[x] = tmeasured

    print("\nUträknat från testresultat så växer tiden (ungefär) med faktorn:")
    x = [
        mtime[31] / mtime[30],
        mtime[32] / mtime[31],
        mtime[33] / mtime[32],
        mtime[34] / mtime[33],
        mtime[35] / mtime[34],
    ]
    print(round(mean(x), 3))
    print("\n\nJämfört med det teoretiska värdet:\n1.618")

    print("\nBye!")


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:

  Antalet förflyttningar är Θ(2^n - 1).
  Vilket kan räknas från följande funktion:
  def moves(n):
    if n == 0:
        return 0
    else:
        return 1 + 2 * moves(n - 1)

    För 50 bricks behövs därmed 1125899906842623 förflyttnignar.
    I en takt på 1 sekund per förlyttng tar förflyttningarna 1125899906842623 s.
    Vilket motsvarar exakt 35 678 347.732779 år eller ca 36 miljoner år.

    

  Exercise 17: Time for Fibonacci:

  Tiden t(n) beräknas med
  t(n) = c * 1.618^n
  Där c är konstant och vars värde är tiden det tar för ett steg i uträkningen.
  Utifrån tidigare mätning av tiden för fib(35), t(35) = 3.189, kan c inexakt beräknas:
    c * 1.618^35 = 3.189
    c = 3.189 / 1.618^35
    c = 1.546701172*10^-7

  Nu kan vi då uppsakatta t(n) för fib(50) och fib(100)
    t(50)  ≈ 4348.427948 s          ≈ 1 timme och 12 minuter
    t(100) ≈ 1.222526107 * 10^14 s  ≈ 3 873 951 år

    
  
  Exercise 20: Comparison sorting methods:
  
  Instickssortering:
    t(n) = c * n^2
    
    uträkning av c:
    t(1000) = 1 sekund
    c * 1000^2 = 1
    c = 1000^(-2)

    Svar:
    t(10^6) = 1000^(-2) * 10^(6*2) 
            = 1 000 000 sekunder 
            ≈ 11 timmar 30 min

    t(10^9) = 1000^(-2) * 10^(9*2) 
            = 10^12 sekunder
            ≈ 31 688 år

  Mergesort:
    t(n) = c * nlog(n)
    
    uträkning av c:
    t(1000) = 1 sekund
    c * 1000log(1000) = 1               (bestämmer oss för log10)
    c = 3000^(-1)

    Svar:
    t(10^6) = 3000^(-1) * 10^6log(10^6)
            = 2 000 sekunder
            ≈ 30 min

    t(10^9) = 3000^(-1) * 10^9log(10^9)
            = 3 000 000 sekunder
            ≈ 35 dagar



  Exercise 21: Comparison Theta(n) and Theta(n log n)
    
    tA(n) = n                           (c = 1)
    tB(n) = c * nlog(n)

    utberäkning av cB:
        tB(10)      =  1 sekund      
    cB * 10log(10)  =  1 sekund         (bestämmer oss för log10)
                cB  =  1 / 10log(10)
                cB  =  0.1
  
    tB(n) = 0.1 * nlog(n)
  
    utberäkning av "vändpunkt":
    tA(n)   <   tB(n)
        n   <   0.1 * nlog(n)
        1   >   0.1 * log(n)
       10   >   log(n)
    10^10   >   10^log(n)
        n   <   100 000 000 000

    Svar:   n behöver vara större än 100 000 000 000 för att 
            algoritm A ska vara snabbare
"""
