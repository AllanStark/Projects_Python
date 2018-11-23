#!usr/bin/env Python
# -*- coding: utf-8 -*-

import os, sys
import subprocess

# Ejecutar un comando con "os.system(comando)" y mostrar en
# pantalla la salida del comando y el resultado de la 
# ejecución.
# Si su valor es 0 la ejecución finalizó con éxito.

valor1 = os.system("./mov_Brgs")
print("Resultado:", valor1)
