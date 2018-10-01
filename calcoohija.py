#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora(object):
    def plus(self, op1, op2):
        """ Function to sum the operands. Ops have to be ints """
        return op1 + op2

    def minus(self, op1, op2):
        """ Function to substract the operands """
        return op1 - op2


class CalculadoraHija(Calculadora):
    def multi(self, op1, op2):
        """ Function to sum the operands. Ops have to be ints """
        return op1 * op2

    def dividir(self, op1, op2):
        """ Function to substract the operands """
        if op2 == 0:
            sys.exit("Error: Division by zero is not allowed")
        return op1 / op2


micalc = CalculadoraHija()

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = micalc.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = micalc.minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = micalc.mult(operando1, operando2)
    elif sys.argv[2] == "divide":
        result = micalc.dividir(operando1, operando2)
    else:
        cadena = 'Operación sólo puede ser sumar, restar, '
        cadena += 'multiplicar o dividir.'
        sys.exit(cadena)

    print(result)
