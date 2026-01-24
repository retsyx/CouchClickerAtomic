print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, ConsumerKey, KeyboardKey, make_key
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes
from kmk.modules.combos import Combos, Chord
from kmk.modules.power import Power
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()
combos = Combos()
keyboard.modules.append(combos)
power = Power()
keyboard.modules.append(power)

keyboard.extensions.append(MediaKeys())

codes = (
    (0x66, ('POWER',)),
    (0x4A, ('HOME',)),
)

for code, names in codes:
    make_key(names=names, constructor=KeyboardKey, code=code)

combos.combos = [
    Chord((KC.POWER, KC.MUTE, KC.VOLU), KC.BLE_DISCONNECT)
]

keyboard.col_pins = (board.D4, board.D1, board.D9, board.D3, board.D2)
keyboard.row_pins = (board.D5, board.D10, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.POWER, KC.F1, KC.F2, KC.F3, KC.F4,
     KC.ENTER, KC.LEFT, KC.UP, KC.RIGHT, KC.DOWN,
     KC.HOME, KC.ESC, KC.MUTE, KC.VOLD, KC.VOLU
    ]
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name='Couch Clicker Atomic')

