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

midiChannelOut = 1
midiChannelIn = 1

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[midiChannelIn], out_channel=midiChannelOut)

km = keypad.KeyMatrix(
    row_pins=(board.GP0, board.GP1),
    column_pins=(board.GP2, board.GP3, board.GP4),
)

KEYCODE = (1, 2, 3, 4, 5, 6)


def sendNoteOn(keycode, velocity=127, channel=1):
    midi.send(NoteOn(keycode, velocity),channel)
    midi.send(NoteOn(keycode, velocity),2)
    midi.send(NoteOn(keycode, velocity),3)
    midi.send(NoteOn(keycode, velocity),4)


def sendNoteOff(keycode, velocity=0, channel=1):
    midi.send(NoteOff(keycode, velocity),channel)
    midi.send(NoteOff(keycode, velocity),2)
    midi.send(NoteOff(keycode, velocity),3)
    midi.send(NoteOff(keycode, velocity),4)
    
while True:
    event = km.events.get()
    if event:
        sendNoteOn(KEYCODE[event.key_number]) if event.pressed else sendNoteOff(KEYCODE[event.key_number])
