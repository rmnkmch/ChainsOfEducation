import manim as M
import random


EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
en = "abcdefghijklmnopqrstuvwxyz"
RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
data_my = "A0.2 B0.05 C0.15 D0.1 E0.49 F0.01"
PRB_NUM: int = 4
UL_CORNER = M.LEFT * 5.5 + M.UP * 3.5

data_1 = "A0.2 B0.05 C0.15 D0.1 E0.4999 F0.0001"
data_2 = "A0.07 B0.1 C0.15 D0.1 E0.34 F0.015 G0.1 H0.11 I0.01 J0.005"


class SSCTV(object):
    """SSCTV pictures and animations"""

    @staticmethod
    def get_symbols_and_probabilities(text: str):
        ret = []
        global PRB_NUM
        for ch_p in text.split():
            symbol = ch_p[0]
            probability = ch_p[1:]
            PRB_NUM = max(PRB_NUM, len(probability) - 2)
            ret.append(ProbabilitySymbol(symbol, probability, False))
        return ret

    @staticmethod
    def check_probability(all_ps):
        p = 0.0
        for ps in all_ps:
            p += ps.probability
        print(p)
        return round(p, PRB_NUM) == 1.0

    @staticmethod
    def get_random_symbols(n, alphabet: str):
        ret = []
        abt = []
        for char in alphabet:
            abt.append(char)
        if n >= len(alphabet): return abt
        else:
            for _ in range(n):
                r = round(random.random() * (len(abt) - 1))
                ret.append(abt[r])
                abt.remove(abt[r])
        return ret

    @staticmethod
    def get_random_probabilities(n):
        ret = []
        sm = 0.0
        for _ in range(n):
            r = random.random()
            ret.append(r)
            sm += r
        for pb in range(len(ret)):
            ret[pb] = round(ret[pb] / sm, 2)
            if ret[pb] <= 0.0001: ret[pb] = 0.01
        return ret

    @staticmethod
    def get_random_ps(n):
        pb = [0.1]
        while abs(sum(pb) - 1.0) > 0.005:
            pb = SSCTV.get_random_probabilities(n)
        sm = SSCTV.get_random_symbols(n, RU)
        data = ""
        for i in range(len(pb)):
            data += sm[i] + str(round(pb[i], 2)) + " "
        print(data)
        return data

    @staticmethod
    def sym_size_by_n(n):
        if n <= 6: return 54.0
        elif n <= 8: return 50.0
        elif n <= 10: return 44.0
        elif n <= 12: return 40.0
        elif n <= 14: return 36.0
        elif n <= 16: return 32.0
        elif n <= 18: return 28.0
        elif n <= 23: return 24.0
        else: return 20.0

    @staticmethod
    def prb_size_by_n(n):
        if n <= 6: return 32.0
        elif n <= 8: return 25.0
        elif n <= 10: return 20.0
        elif n <= 12: return 18.0
        elif n <= 14: return 17.0
        elif n <= 16: return 16.0
        elif n <= 18: return 14.0
        elif n <= 22: return 12.0
        else: return 10.0

    @staticmethod
    def zline_size_by_n(n):
        if n <= 6: return 0.25
        elif n <= 8: return 0.19
        elif n <= 10: return 0.14
        elif n <= 12: return 0.12
        elif n <= 14: return 0.1
        elif n <= 16: return 0.07
        elif n <= 18: return 0.05
        else: return 0.03

    @staticmethod
    def zline_stroke_width_by_n(n):
        if n <= 9: return 4
        elif n <= 13: return 3
        elif n <= 17: return 2
        else: return 1

    @staticmethod
    def make_all(scene: M.Scene):
        for i in range(6, 26, 1):
            SSCTV.make_one(scene, i)
            scene.wait(2.0)
            scene.clear()

    @staticmethod
    def make_one(scene: M.Scene, nnn = 6):
        all_ps = SSCTV.get_symbols_and_probabilities(SSCTV.get_random_ps(nnn))
        all_len = len(all_ps)
        vert_offset = 8.0 / (all_len + 2)
        sym_size = SSCTV.sym_size_by_n(all_len)
        prb_size = SSCTV.prb_size_by_n(all_len)
        zline_size = SSCTV.zline_size_by_n(all_len)
        zline_stroke_width = SSCTV.zline_stroke_width_by_n(all_len)
        horz_offset = 12.0 / (all_len - 1)
        if not SSCTV.check_probability(all_ps): return
        all_ps.sort()
        all_ps.reverse()
        all_ps_old = all_ps.copy()
        for psi in range(all_len):
            scene.add(M.Text(
                all_ps[psi].symbol + ":",
                font_size = sym_size).move_to(
                    UL_CORNER + M.LEFT + M.UP * 0.07
                    + M.DOWN * vert_offset * (psi + 1)))
        for cycle in range(all_len):
            max_width = 0.0
            max_height = 0.0
            for psi in range(len(all_ps)):
                new_text = M.Text(
                    str(round(all_ps[psi].probability, PRB_NUM)),
                    font_size = prb_size).move_to(
                        UL_CORNER
                        + M.DOWN * vert_offset * (psi + 1)
                        + M.RIGHT * horz_offset * cycle)
                max_width = max(max_width, new_text.width)
                max_height = max(max_height, new_text.height)
                scene.add(new_text)
            if cycle != all_len - 1:
                line = M.Line(
                    UL_CORNER
                    + M.DOWN * vert_offset * (len(all_ps) - 1 - max_height * 0.6)
                    + M.RIGHT * (horz_offset * cycle + max_width * 0.7),
                    UL_CORNER
                    + M.DOWN * vert_offset * (len(all_ps) + max_height * 0.6)
                    + M.RIGHT * (horz_offset * cycle + max_width * 0.7),
                    stroke_width = zline_stroke_width)
                n0 = M.Text("0", font_size = prb_size).next_to(
                    line, M.UR, max_width * 0.1)
                n0.shift(M.DOWN * n0.height)
                n1 = M.Text("1", font_size = prb_size).next_to(
                    line, M.DR, max_width * 0.1)
                n1.shift(M.UP * n1.height)
                scene.add(line, n0, n1)
                p1 = all_ps.pop()
                p2 = all_ps.pop()
                all_ps.append(ProbabilitySymbol(
                    p1.symbol + p2.symbol, p1.probability + p2.probability, True))
                all_ps.sort()
                all_ps.reverse()
                used_index = []
                for index_from in range(len(all_ps_old) - 2):
                    index_to = -1
                    for psi_new in range(len(all_ps)):
                        if all_ps_old[index_from].symbol == all_ps[psi_new].symbol:
                            used_index.append(psi_new)
                            index_to = psi_new
                            break
                    ln = ZLine([
                        UL_CORNER + M.DOWN * vert_offset * (index_from + 1)
                        + M.RIGHT * (horz_offset * (cycle) + max_width * 0.7),
                        UL_CORNER + M.DOWN * vert_offset * (index_to + 1)
                        + M.RIGHT * (horz_offset * (cycle + 1) - max_width * 0.7)],
                               zline_size, zline_stroke_width)
                    scene.add(ln)
                for psi_new in range(len(all_ps)):
                    if psi_new not in used_index:
                        index_to = psi_new
                used_index = []
                ln = ZLine([
                    UL_CORNER + M.DOWN * vert_offset * (len(all_ps_old) - 0.5)
                    + M.RIGHT * (horz_offset * (cycle) + max_width * 0.7),
                    UL_CORNER + M.DOWN * vert_offset * (len(all_ps_old) - 0.5)
                    + M.RIGHT * (horz_offset * (cycle + 0.44)),
                    UL_CORNER + M.DOWN * vert_offset * (index_to + 1)
                    + M.RIGHT * (horz_offset * (cycle + 0.56)),
                    UL_CORNER + M.DOWN * vert_offset * (index_to + 1)
                    + M.RIGHT * (horz_offset * (cycle + 1) - max_width * 0.7)],
                           zline_size, zline_stroke_width)
                scene.add(ln)
                all_ps_old = all_ps.copy()


class ProbabilitySymbol(object):
    def __init__(self, symbol: str, probability: str, merged: bool, code: str = ""):
        self.symbol = symbol
        self.probability = float(probability)
        self.merged = merged
        self.code = code

    def __str__(self):
        return f"{self.symbol}: {self.probability} - {self.merged}"

    def __lt__(self, other):
        if self.probability == other.probability:
            if self.merged and not other.merged: return True
            else:
                return self.symbol < other.symbol
        return self.probability < other.probability

    def __eq__(self, other):
        return self.probability == other.probability


class ZLine(M.TipableVMobject):
    def __init__(self, points, size = 0.2, stroke_width = 4, **kwargs):
        super().__init__(
            stroke_color = "#FFFFFF",
            stroke_opacity = 1.0,
            stroke_width = stroke_width,
            background_stroke_color = "#000000",
            background_stroke_opacity = 1.0,
            background_stroke_width = 0,
            **kwargs)

        self.set_points_as_corners(points)
        self.add_tip(self.create_tip(tip_length = size, tip_width = size))
