from badge import BaseApp, display
from badge.input import get_button, Buttons
from framebuf import FrameBuffer, MONO_HLSB

def relpath(path):
    return "/".join(__file__.split("/")[:-1] + [path])

def draw_text(string, x, y, color=0, show=True):
    mask = (0xFF, 0x00)[color]
    with open(relpath("zh.bin"), "rb") as f:
        if all(ord(i) >= 0x3200 and ord(i) < 0xa000 for i in string):
            for j, i in enumerate(string):
                arr_index = (ord(i) - 0x3200) * 32
                f.seek(arr_index)
                display.blit(FrameBuffer(bytearray(k ^ mask for k in f.read(32)), 16, 16, MONO_HLSB), x + j * 16, y)
        elif all(ord(i) < 0x80 for i in string):
            for j, i in enumerate(string):
                display.text(i, x + 4 + j * 16, y + 4, color)
        else:
            raise ValueError("Only Chinese characters are supported")
    if show:
        display.show()

search, typed = "", ""
def display_typed():
    global search, typed
    display.fill_rect(77, 0, 200 - 77, 200, 1)
    draw_text(search, 77, 12, show=False)
    for j, i in enumerate(typed [-60:]):
        draw_text(i, 77 + (j % 6) * 16, 28 + (j // 6) * 16, show=False)

def select_24(items):
    page = 0
    def draw_page():
        display.fill_rect(0, 0, 55 + 16, 200, 1)
        count = page * 24
        for y in (15, 37, 59, 81, 103, 125, 147, 169):
            for x in (11, 33, 55):
                if count < len(items):
                    draw_text(items[count], x, y, show=False)
                count += 1
        display_typed()
        display.show()
    draw_page()
    while True:
        if get_button(Buttons.SW5):
            page = (page + 1) % -(len(items) // -24)
            draw_page()
            while get_button(Buttons.SW5):
                pass
            continue
        elif get_button(Buttons.SW4):
            while get_button(Buttons.SW4):
                pass
            return None
        for j, i in enumerate((Buttons.SW15, Buttons.SW8, Buttons.SW16)):
            if get_button(i):
                for l, k in enumerate((Buttons.SW9, Buttons.SW18, Buttons.SW10, Buttons.SW17, Buttons.SW7, Buttons.SW13, Buttons.SW6, Buttons.SW14)):
                    if get_button(k):
                        while get_button(i) or get_button(k):
                            pass
                        if page * 24 + l * 3 + j < len(items):
                            return items[page * 24 + l * 3 + j]

class App (BaseApp):
    def on_open(self):
        global typed
        typed = ""
        display.fill(1)

    def loop(self):
        global search, typed
        letter, search = "", ""
        while letter is not None and len(search) < 6:
            search += letter
            letter = select_24(list("ABCDEFGHIJKLMNOPQRST_XYZ".replace("_", "W" if search == "" else "U")))
        if search == "":
            return
        search += select_24(list("111222333444111222333444")) or ""
        search = search.lower()
        with open(relpath("pinyin.txt")) as f:
            line = None
            while line != "":
                line = f.readline().strip()
                if line.startswith(search + " "):
                    break
            else:
                return
        typed += select_24(line.split(" ")[1]) or ""