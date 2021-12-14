#!/usr/bin/python3

import random
import argparse

def emparejar_lista( lista ):
    compran = lista[:]
    reciben = lista[:]
    random.shuffle( compran )
    for i in range( 10 ):
        random.shuffle( reciben )
        resultado = list( zip( compran, reciben ) )
        if not [ ( r1, r2 ) for ( r1, r2 ) in resultado if r1 == r2 ]:
            resultado.sort()
            return resultado
    raise ValueError

def leer_lista( nombrefichero ):
    return [ [ item for item in linea.strip().split( '\t' ) if item ]
             for linea in open( nombrefichero, 'r' ) ]

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument( 'lista' )
    args = parser.parse_args()

    personas = leer_lista( args.lista )
    resultado = emparejar_lista( personas )
    for ( regalan, reciben ) in resultado:
        print( regalan[ 0 ], "regalan a", reciben[ 0 ] )

