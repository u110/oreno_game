import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("rsc.pyxel")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, self.x + 7, 7, 9)
        pyxel.blt(0, 0, 0, 0, 0, 15, 15)


if __name__ == "__main__":
    App()
