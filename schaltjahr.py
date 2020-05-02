# Programm zur Berechnung, 
# ob ein bestimmtes Jahr ein Schaltjahr ist

import tkinter

def ist_schaltjahr( jahr ):
    """Gibt True zurück falls jahr ein Schaltjahr ist."""
    if( jahr % 4 == 0 ):
        return True
    return False

def button_pruefe_click():
    jahr = eval( eingabe_feld.get() )
    text1 = str(jahr)+" ist "+("ein" if ist_schaltjahr(jahr) else "kein")+" Schaltjahr"
    label_ausgabe.config( text = text1 )
    
    
# Erzeuge Fenster
tkFenster = tkinter.Tk()
tkFenster.title('Schaltjahr')
tkFenster.geometry('250x180')

# Label mit der Aufschrift "Jahreszahl hier eingeben:"
label_funktion = tkinter.Label( tkFenster )
label_funktion.place(x=50, y=20, width=150, height=27)
label_funktion.config( text = "Jahreszahl hier eingeben:" )

# Eingabefeld für Jahreszahl
eingabe_feld = tkinter.Entry(tkFenster)
eingabe_feld.place(x=50, y=40, width=150, height=27)

# Button zum Prüfen auf Schaltjahr
button_pruefe = tkinter.Button( tkFenster, 
                                text = " Prüfe auf Schaltjahr ", 
                                command = button_pruefe_click )
button_pruefe.place(x=50, y=80, width=150, height=27)

# Ausgabe, ob Schaltjahr
label_ausgabe = tkinter.Label( tkFenster )
label_ausgabe.place(x=50, y=120, width=150, height=27)


# Aktivierung des Fensters
tkFenster.mainloop()
