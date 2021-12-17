#!/usr/bin/python3

import random
import argparse


def emparejar_lista(lista):
    compran = lista[:]
    reciben = lista[:]
    random.shuffle(compran)
    for i in range(10):
        random.shuffle(reciben)
        resultado = list(zip(compran, reciben))
        if not [(r1, r2) for (r1, r2) in resultado if r1 == r2]:
            resultado.sort()
            return resultado
    raise ValueError


def leer_lista(nombrefichero):
    return [[item for item in linea.strip().split('\t') if item]
            for linea in open(nombrefichero, 'r')]


def leer_conf_email(nombrefichero):
    return dict([[item.strip() for item in linea.split('=', 1)]
                for linea in open(nombrefichero, 'r')])


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('lista',
                        help='Lista de participantes (lista_test.txt)')
    parser.add_argument('--envio',
                        help='Configuracion de email (email_test.txt)')
    args = parser.parse_args()

    if args.envio:
        conf_email = leer_conf_email(args.envio)
    personas = leer_lista(args.lista)
    resultado = emparejar_lista(personas)
    for (regalan, reciben) in resultado:
        print(regalan[0], "regalan a", reciben[0])
        if conf_email:
            print("======= email para", regalan[1], "=========")
            print("From", conf_email['de'])
            print("To", regalan[1])
            print("Subject", conf_email['asunto'])
            print(eval(conf_email['cuerpo']))
            print("=============================================")
