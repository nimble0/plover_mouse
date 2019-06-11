from collections.abc import Iterable
from plover.engine import StenoEngine
from pynput.mouse import Button, Controller
from typing import List

mouse = Controller()

def parse_int_args(args: str, alt: List[int]) -> List[int]:
    args2 = args.split(",")
    return [
        alt[i] if(x.strip() == "" and i < len(alt)) else int(x)
        for i, x in enumerate(args2)
    ] + list(alt[len(args2):])

def mouse_position(engine: StenoEngine, args: str):
    global mouse
    (x, y) = parse_int_args(args, mouse.position)
    mouse.position = (x, y)
def mouse_move(engine: StenoEngine, args: str):
    global mouse
    (x, y) = parse_int_args(args, (0, 0))
    mouse.move(x, y)
def mouse_scroll(engine: StenoEngine, args: str):
    global mouse
    (x, y) = parse_int_args(args, (0, 0))
    mouse.scroll(x, y)

def mouse_press(engine: StenoEngine, args: str):
    global mouse
    mouse.press(Button.left if(args == "") else Button[args.strip()])
def mouse_release(engine: StenoEngine, args: str):
    global mouse
    mouse.release(Button.left if(args == "") else Button[args.strip()])
def mouse_click(engine: StenoEngine, args: str):
    global mouse
    args2 = args.split(",")
    args2 = [x.strip() for x in args2] + [""] * (2 - len(args2))
    button = Button.left if(args2[0] == "") else Button[args2[0].strip()]
    clicks = 1 if(args2[1] == "") else int(args2[1])
    mouse.click(button, clicks)

