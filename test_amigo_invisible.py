#!/usr/bin/python3

import amigo_invisible

FICHERO_PRUEBAS = 'lista_test.txt'
FICHERO_CONF_EMAIL = 'email_test.txt'


def test_tipo_lista():
    lista = amigo_invisible.leer_lista(FICHERO_PRUEBAS)
    assert type(lista) == list


def test_longitud_lista():
    lista = amigo_invisible.leer_lista(FICHERO_PRUEBAS)
    assert len(lista) == 5


def test_items_lista():
    lista = amigo_invisible.leer_lista(FICHERO_PRUEBAS)
    for item in lista:
        assert type(item) == list
        assert len(item) == 2


def test_emparejar1():
    lista = amigo_invisible.leer_lista(FICHERO_PRUEBAS)
    pares = amigo_invisible.emparejar_lista(lista)
    assert len(pares) == len(lista)


def test_emparejar2():
    lista = amigo_invisible.leer_lista(FICHERO_PRUEBAS)
    pares1 = amigo_invisible.emparejar_lista(lista)
    pares2 = amigo_invisible.emparejar_lista(lista)
    pares1.sort()
    pares2.sort()
    texto1 = "\n".join([str(p) for p in pares1])
    texto2 = "\n".join([str(p) for p in pares2])
    assert texto1 != texto2


def test_conf_email1():
    conf_email = amigo_invisible.leer_conf_email(FICHERO_CONF_EMAIL)
    assert type(conf_email) == dict
    assert "de" in conf_email
    assert "cc" in conf_email
    assert "cco" in conf_email
    assert "asunto" in conf_email
    assert "cuerpo" in conf_email
    assert "servidor" in conf_email
    assert "usuario" in conf_email
    assert "password" in conf_email
