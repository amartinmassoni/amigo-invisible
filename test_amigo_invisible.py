#!/usr/bin/python3

from amigo_invisible import *

FICHERO_PRUEBAS = 'lista_test.txt'

def test_tipo_lista():
    lista = leer_lista( FICHERO_PRUEBAS )
    assert type( lista ) == list

def test_longitud_lista():
    lista = leer_lista( FICHERO_PRUEBAS )
    assert len( lista ) == 3

def test_emparejar1():
    lista = leer_lista( FICHERO_PRUEBAS )
    pares = emparejar_lista( lista )
    assert len( pares ) == 3

