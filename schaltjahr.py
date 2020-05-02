# Programm zur Berechnung, 
# ob ein bestimmtes Jahr ein Schaltjahr ist

def ist_schaltjahr( jahr ):
    """Gibt True zurück falls jahr ein Schaltjahr ist."""
    if( jahr % 4 == 0 ):
        return True
    return False

jahr = eval( input("Bitte gib eine Jahreszahl ein: ") )
print( "Schaltjahr" if ist_schaltjahr(jahr) else "Kein Schaltjahr" )
