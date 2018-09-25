#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fichero = open(sys.argv[1],"r")
lineas = fichero.readlines()

for valor in lineas:

    operador = valor.rsplit(",")[0]
    operandos = valor.rsplit(",")[1:]

print("ok")

fichero.close()
