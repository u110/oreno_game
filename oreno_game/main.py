import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("rsc.pyxel")
        self.x = 0
        self.p = 0
        self.vp = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width
        self.p = max(0, min(self.p + self.vp, 120))
        if pyxel.btnp(pyxel.KEY_A):
            self.vp = min(self.vp - 1, 3)
        if pyxel.btnp(pyxel.KEY_S):
            self.vp = max(self.vp + 1, -3)
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, self.x + 7, 7, 9)
        pyxel.blt(self.p, 0, 0, 0, 0, 15, 15)


if __name__ == "__main__":
    App()
