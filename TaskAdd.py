import sys
import argparse
from src.TaskFlow import App
def main():
    # Crea un analizador de argumentos
    parser = argparse.ArgumentParser(description='Interfaz de línea de comandos para TaskFlow')
    parser.add_argument('add', help='El comando a ejecutar (add)')
    parser.add_argument('tarea', help='La tarea a añadir')

    # Analiza los argumentos de la línea de comandos
    args = parser.parse_args()

    # Ejecuta el comando correspondiente
    if args.comando == 'add':
        print(args.tarea)
        App.TaskAdd(args.tarea)
    else:
        print(f'Comando desconocido: {args.comando}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
