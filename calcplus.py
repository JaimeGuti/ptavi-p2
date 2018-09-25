#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fichero = open(sys.argv[1],"r")
lineas = fichero.readlines()

micalc = calcoohija.CalculadoraHija()

if __name__ == "__main__":

    for valor in lineas:

        operador = valor.rsplit(",")[0]
        operandos = valor.rsplit(",")[1:]

        operaciones = operandos[1]
        result = int(operaciones)

        try:
            if operador == "suma":
                for suma in operandos:
                    result = micalc.plus((result), int(suma))
                print(result)
            if operador == "resta":
                for resta in operandos:
                    result = micalc.minus((result), int(resta))
                print(result)
            if operador == "multiplica":
                for multiplicacion in operandos:
                    result = micalc.multiplicar((result), int(multiplicacion))
                print(result)
            if operador == "divide":
                for division in operandos:
                    result = micalc.dividir((result), int(division))
                print(result)

        except KeyError:
            sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')

    #print(result)

fichero.close()
