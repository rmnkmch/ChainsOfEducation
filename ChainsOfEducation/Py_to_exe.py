import manim as M


class Py_to_exe(M.Scene):
    def construct(self):
        tts = 36.0
        txs = 30.0
        tx9 = r"P_r = + 40 - 6 - "
        tex9 = M.MathTex(tx9, font_size = txs)
        txt9 = M.Text("дБВт", font_size = tts)
        gr9 = M.VGroup(tex9, txt9).arrange()
        self.add(gr9)
