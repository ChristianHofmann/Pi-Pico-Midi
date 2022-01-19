# Vorbereitung
#
# Benötigt werden:
# - Adafruit CircuitPython: https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython
#
# Zusätzlich die CircuitPython libs: adafruit_midi
# (in das Verzeichnis "lib" auf dem Pi Pico kopieren)
#
# Diese Datei als code.py auf dem Raspberry Pi Pico CIRCUITPY Laufwerk speichern!



# Importe
# =======
import time
import board
import busio
import usb_midi
import keypad

import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_bus_device.i2c_device import I2CDevice

from digitalio import DigitalInOut, Direction, Pull

# Variablen
#==========
midiChannelOut = 1
midiChannelIn = 1

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[midiChannelIn], out_channel=midiChannelOut)

# Pins für die Tastenmatrix
km = keypad.KeyMatrix(
    row_pins=(board.GP0, board.GP1),
    column_pins=(board.GP2, board.GP3, board.GP4),
)

# Midi Keycode für die dazugehörige Taste
KEYCODE = (51, 52, 53, 54, 55, 56)

# sendNoteOn sendet ein NoteON mit den übergebenen
# Parameter
def sendNoteOn(keycode, velocity=127):
    midi.send(NoteOn(keycode, velocity))

# sendNoteOn sendet ein NoteON mit den übergebenen
# Parameter
def sendNoteOff(keycode, velocity=0):
    midi.send(NoteOff(keycode, velocity))
    
# Hauptschleife
while True:
    event = km.events.get()
    if event:
        sendNoteOn(KEYCODE[event.key_number]) if event.pressed else sendNoteOff(KEYCODE[event.key_number])
