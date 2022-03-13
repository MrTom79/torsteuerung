# torsteuerung
Python Scrpit zum schließen eines Garagentores
Mit diesem Python Scrpit soll ein automatisches schließen eines Garagentores über einen Raspberry PI4 realisiert werden.
Dazu ist an der Decke ein Sensor angebracht der erfasst ob sich das Fahrzeug auf dem Stellplatz befindet.
Zusätzlich überwacht am Tor ein Sensor ob sich das Fahrzeug/Personen/Gegenstände im Schließbereich befinden.
Aufgerufen wird das Script von einem anderen externen Programm
Am Anfang sollte überprüft werden ob sich das Fahrzeug am Stellplatz befindet und der Torbereich frei ist (Plausiprüfung)
Die Ausfahrt des Fahrzeugs wird erfasst wenn beide Sensoren gleichzeitig mind. 0,5s ein Objekt erfasst und "High" sind
Das Tor sollte geschlossen werden wenn nach dem ausfahren des Fahrzeugs die beiden Sensoren für 2 min "Low" sind.
Vor dem Schließen wird eine Warnlampe angesteuert
Während des Schließvorgangs den Sensorbereich überwachen, sollten Hindernisse erfasst werden den Schließvorgang abbrechen und Torbewegung umsteuern.
