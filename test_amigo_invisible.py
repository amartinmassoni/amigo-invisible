#!/usr/bin/python3

from amigo_invisible import *

FICHERO_PRUEBAS = 'lista_test.txt'

def test_tipo_lista():
    lista = leer_lista( FICHERO_PRUEBAS )
    assert type( lista ) == list

def test_longitud_lista():
    lista = leer_lista( FICHERO_PRUEBAS )
    assert len( lista ) == 5

def test_items_lista():
    lista = leer_lista( FICHERO_PRUEBAS )
    for item in lista:
        assert type( item ) == list
        assert len( item ) == 2

def test_emparejar1():
    lista = leer_lista( FICHERO_PRUEBAS )
    pares = emparejar_lista( lista )
    assert len( pares ) == len( lista )

def test_emparejar2():
    lista = leer_lista( FICHERO_PRUEBAS )
    pares1 = emparejar_lista( lista )
    pares2 = emparejar_lista( lista )
    pares1.sort()
    pares2.sort()
    texto1 = "\n".join( [ str( p ) for p in pares1 ] )
    texto2 = "\n".join( [ str( p ) for p in pares2 ] )
    assert texto1 != texto2

