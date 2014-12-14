#!/usr/bin/python3
import sys
import argparse
import os

__author__ = "Axel Díaz"
__credits__ = ["Axel Díaz"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Axel Díaz"
__email__ = "diaz.axelio@gmail.com"
__status__ = "Development"


AUDIO = ('clementine',)

MULTIMEDIA = ('vlc',
    'audacity')

DESARROLLO = ('geany',
              'git',
              'python3',
              'vim',
              'build-essential',
              'python-dev',
              'python-pip'
              )

OFICINA = ('libreoffice',
    'dia'
    )

SERVIDOR = ('postgresql',
    'postgresql-server-dev-all',
    'ssh',
    'openssh-client'
    )

GNOME = ('gnome',)

WEB = ('iceweasel',
    'icedove',)

JUEGOS = ('0ad',
    'armagetronad',
)

def add_apps(apps):
    list_app = ''
    for app in apps:
        list_app = list_app + '%s ' % (app)

    return list_app


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--desarrollo', dest='desarrollo',
        action='store_true',
        help='Activa la instalación de: %s' % ([x for x in DESARROLLO]))
    parser.add_argument('-m', '--multimedia', dest='multimedia',
        action='store_true',
        help='Activa la instalación de: %s' % ([x for x in MULTIMEDIA]))
    parser.add_argument('-a', '--audio', dest='audio', action='store_true',
        help='Activa la instalación de: %s' % ([x for x in AUDIO]))
    parser.add_argument('-s', '--servidor', dest='servidor',
        action='store_true',
        help='Activa la instalación de: %s' % ([x for x in SERVIDOR]))
    parser.add_argument('-g', '--gnome', dest='gnome', action='store_true',
        help='Activa la instalación de: %s' % ([x for x in GNOME]))
    parser.add_argument('-w', '--web', dest='web', action='store_true',
        help='activa la instalación de: %s' % ([x for x in WEB]))
    parser.add_argument('-j', '--juegos', dest='juegos', action='store_true',
        help='activa la instalación de: %s' % ([x for x in JUEGOS]))
    parser.add_argument('-o', '--oficina', dest='oficina', action='store_true',
        help='activa la instalación de: %s' % ([x for x in OFICINA]))
    parser.add_argument('-t', '--todas', dest='todas', action='store_true',
        help='activa la instalación de todas las aplicaciones listadas')

    args = parser.parse_args()
    
    apps = ''
    if args.desarrollo or args.todas:
        apps = apps + add_apps(DESARROLLO)

    if args.multimedia or args.todas:
        apps = apps + add_apps(MULTIMEDIA)

    if args.audio or args.todas:
        apps = apps + add_apps(AUDIO)

    if args.servidor or args.todas:
        apps = apps + add_apps(SERVIDOR)

    if args.gnome or args.todas:
        apps = apps + add_apps(GNOME)

    if args.web or args.todas:
        apps = apps + add_apps(WEB)

    if args.juegos or args.todas:
        apps = apps + add_apps(JUEGOS)

    if args.oficina or args.todas:
        apps = apps + add_apps(OFICINA)

    if apps is '':
        print("No se introdujo ninguna opción.")

    else:
        respuesta = False
        while respuesta == False:
            print("Se instalarán: %s" % (apps))
            respuesta = input("¿Ud confirma esto? (S/n): ")

            if respuesta.upper() == 'S':
                respuesta = True
                os.system("su -c 'aptitude install %s'" % (apps))
                pass
            elif respuesta.upper() == 'N':
                print("Instalación cancelada.")
                pass
            else:
                respuesta = False
                print("Respuesta inválida.")


__main__()
