# Python-Modul: mymodul.py - ein erstes Python-Modul mit ein wenig Inhalt

if __name__ == '__main__':
    # Ein Modul sollte NICHT als Haupt-Programm gestartet werden können
    # => hier wird der Aufruf DIREKT beendet
    print('module bitte nicht direkt aufrufen, sondern importieren')
    exit()

#
# wenn im Modul etwas importiert werden muss, dann HIER !!!
#

# das ist debug-output - muss im fertigen Projekt entfernt werden
print(f'Das Modul mymodul.py wird importiert und __name__ im Modul ist {__name__}')


#
# Der eigentliche Inhalt des Moduls: 
#

def myFunction():
    print('myFunction() in mymodul')


class MyClass:

    def show(self):
        print('Methode show() in MyClass from mymodul')

