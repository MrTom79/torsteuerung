# RPi.GPIO Layout verwenden (Pin-Nummern)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
LOGDIR              = '/var/log/Torsteuerung/'
# Pin-Nummern festlegen und Ein-/Ausgang definieren
# Eingaenge:
Tor_PIN           = 11
Decken_PIN        = 13
# Ausgaenge
Warnlampe_PIN         = 31
Torauf_PIN            = 33
Torzu_PIN             = 35
Strom_PIN             = 36
# Pin's setzen
GPIO.setup(Tor_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Decken_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Warnlampe_PIN, GPIO.OUT)
GPIO.setup(Torauf_PIN, GPIO.OUT)
GPIO.setup(Torzu_PIN, GPIO.OUT)
GPIO.setup(Strom_PIN, GPIO.OUT)
# Ausgaenge immer ausmachen
channel_list = [Warnlampe_PIN,Torauf_PIN,Torzu_PIN,Strom_PIN]
GPIO.output(channel_list, GPIO.LOW)  
###########################################################################################################