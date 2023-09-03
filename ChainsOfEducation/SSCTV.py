import manim as M
import random
import enum


class SSCTV(object):
    """SSCTV pictures and animations"""

    EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    en = "abcdefghijklmnopqrstuvwxyz"
    RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    data_my = "A0.2 B0.05 C0.15 D0.1 E0.49 F0.01"
    PRB_NUM: int = 2
    UL_CORNER = M.LEFT * 5.5 + M.UP * 3.5

    data_saved = {"example": "Р0.07 Е0.21 П0.32 Л0.31 О0.09"}

    @staticmethod
    def get_symbols_and_probabilities(text: str):
        ret = []
        for ch_p in text.split():
            symbol = ch_p[0]
            probability = ch_p[1:]
            SSCTV.PRB_NUM = max(SSCTV.PRB_NUM, len(probability) - 2)
            ret.append(ProbabilitySymbol(symbol, probability, False))
        return ret

    @staticmethod
    def check_probability(all_ps):
        p = 0.0
        for ps in all_ps:
            p += ps.probability
        print(p)
        return round(p, SSCTV.PRB_NUM) == 1.0

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
            ret[pb] = round(ret[pb] / sm, SSCTV.PRB_NUM)
            if ret[pb] <= 0.0001: ret[pb] = 0.01
        return ret

    @staticmethod
    def get_random_ps(n):
        pb = [0.1]
        while abs(sum(pb) - 1.0) > 0.005:
            pb = SSCTV.get_random_probabilities(n)
        sm = SSCTV.get_random_symbols(n, SSCTV.RU)
        data = ""
        for i in range(len(pb)):
            data += sm[i] + str(round(pb[i], SSCTV.PRB_NUM)) + " "
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
    def find_ps_by_symbol(symbol, all_ps):
        for ps in all_ps:
            if ps.symbol == symbol: return ps

    @staticmethod
    def get_main_color():
        return "#000000"

    @staticmethod
    def get_background_color():
        return "#FFFFFF"

    @staticmethod
    def make_all(scene: M.Scene):
        for i in range(15, 16, 1):
            SSCTV.make_one(scene, i)

    @staticmethod
    def make_one(scene: M.Scene, nnn = 6):
        scene.add(M.Rectangle(
            SSCTV.get_background_color(), 9.0, 15.0, fill_opacity = 1.0))
        #all_ps = SSCTV.get_symbols_and_probabilities(SSCTV.get_random_ps(nnn))
        #all_ps = SSCTV.get_symbols_and_probabilities(SSCTV.data_my)
        all_ps = SSCTV.get_symbols_and_probabilities(SSCTV.data_saved["example"])
        all_len = len(all_ps)
        vert_offset = 8.0 / (all_len + 2)
        sym_size = SSCTV.sym_size_by_n(all_len)
        prb_size = SSCTV.prb_size_by_n(all_len)
        zline_size = SSCTV.zline_size_by_n(all_len)
        zline_stroke_width = SSCTV.zline_stroke_width_by_n(all_len)
        horz_offset = 12.0 / (all_len - 1)
        if not SSCTV.check_probability(all_ps): return
        all_ps_old_full = all_ps.copy()
        all_ps.sort()
        all_ps.reverse()
        all_ps_old = all_ps.copy()
        for psi in range(all_len):
            scene.add(M.Text(
                all_ps[psi].symbol + ":",
                font_size = sym_size, color = SSCTV.get_main_color()).move_to(
                    SSCTV.UL_CORNER + M.LEFT + M.UP * 0.07
                    + M.DOWN * vert_offset * (psi + 1)))
        for cycle in range(all_len):
            max_width = 0.0
            max_height = 0.0
            for psi in range(len(all_ps)):
                new_text = M.Text(
                    str(round(all_ps[psi].probability, SSCTV.PRB_NUM)),
                    font_size = prb_size, color = SSCTV.get_main_color()).move_to(
                        SSCTV.UL_CORNER
                        + M.DOWN * vert_offset * (psi + 1)
                        + M.RIGHT * horz_offset * cycle)
                max_width = max(max_width, new_text.width)
                max_height = max(max_height, new_text.height)
                scene.add(new_text)
            if cycle != all_len - 1:
                line = M.Line(
                    SSCTV.UL_CORNER
                    + M.DOWN * vert_offset * (len(all_ps) - 1 - max_height * 0.6)
                    + M.RIGHT * (horz_offset * cycle + max_width * 0.7),
                    SSCTV.UL_CORNER
                    + M.DOWN * vert_offset * (len(all_ps) + max_height * 0.6)
                    + M.RIGHT * (horz_offset * cycle + max_width * 0.7),
                    stroke_width = zline_stroke_width,
                    color = SSCTV.get_main_color())
                n0 = M.Text("0", font_size = prb_size,
                            color = SSCTV.get_main_color()).next_to(
                    line, M.UR, max_width * 0.1)
                n0.shift(M.DOWN * n0.height)
                n1 = M.Text("1", font_size = prb_size,
                            color = SSCTV.get_main_color()).next_to(
                    line, M.DR, max_width * 0.1)
                n1.shift(M.UP * n1.height)
                scene.add(line, n0, n1)
                p1 = all_ps.pop()
                p2 = all_ps.pop()
                for ch in p1.symbol:
                    SSCTV.find_ps_by_symbol(ch, all_ps_old_full).code += "1"
                for ch in p2.symbol:
                    SSCTV.find_ps_by_symbol(ch, all_ps_old_full).code += "0"
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
                        SSCTV.UL_CORNER + M.DOWN * vert_offset * (index_from + 1)
                        + M.RIGHT * (horz_offset * (cycle) + max_width * 0.7),
                        SSCTV.UL_CORNER + M.DOWN * vert_offset * (index_to + 1)
                        + M.RIGHT * (horz_offset * (cycle + 1) - max_width * 0.7)],
                               zline_size, zline_stroke_width,
                               SSCTV.get_main_color())
                    scene.add(ln)
                for psi_new in range(len(all_ps)):
                    if psi_new not in used_index:
                        index_to = psi_new
                used_index = []
                ln = ZLine([
                    SSCTV.UL_CORNER + M.DOWN * vert_offset * (len(all_ps_old) - 0.5)
                    + M.RIGHT * (horz_offset * (cycle) + max_width * 0.7),
                    SSCTV.UL_CORNER + M.DOWN * vert_offset * (len(all_ps_old) - 0.5)
                    + M.RIGHT * (horz_offset * (cycle + 0.44)),
                    SSCTV.UL_CORNER + M.DOWN * vert_offset * (index_to + 1)
                    + M.RIGHT * (horz_offset * (cycle + 0.56)),
                    SSCTV.UL_CORNER + M.DOWN * vert_offset * (index_to + 1)
                    + M.RIGHT * (horz_offset * (cycle + 1) - max_width * 0.7)],
                           zline_size, zline_stroke_width, SSCTV.get_main_color())
                scene.add(ln)
                all_ps_old = all_ps.copy()
        for i in range(len(all_ps_old_full)):
            all_ps_old_full[i].code = all_ps_old_full[i].code[::-1]
        scene.wait()
        scene.clear()
        SSCTV.make_table(scene, all_ps_old_full)
        scene.wait(1.0)

    @staticmethod
    def make_table(scene: M.Scene, all_ps_old_full):
        from math import log2
        scene.add(M.Rectangle(
            SSCTV.get_background_color(), 9.0, 15.0, fill_opacity = 1.0))
        table = Table(
            [[all_ps_old_full[i].symbol, all_ps_old_full[i].code]
             for i in range(len(all_ps_old_full))],
             include_outer_lines = True,
             v_buff = 0.48 * SSCTV.sym_size_by_n(len(all_ps_old_full)) / 54.0,
             h_buff = 2.0,
             element_to_mobject_config = {
                 "font_size": SSCTV.prb_size_by_n(len(all_ps_old_full)),
                 "color": SSCTV.get_main_color()},
             line_config = {"color": SSCTV.get_main_color()})
        scene.add(table)
        scene.wait()
        scene.clear()
        scene.add(M.Rectangle(
            SSCTV.get_background_color(), 9.0, 15.0, fill_opacity = 1.0))
        rows = [sym.symbol for sym in all_ps_old_full]
        prbs = [str(sym.probability) for sym in all_ps_old_full]
        logs = [str(- round(log2(sym.probability), 3)) for sym in all_ps_old_full]
        prbs_logs = [str(- round(log2(sym.probability) * sym.probability, 3))
                     for sym in all_ps_old_full]
        table = Table(
            [[prbs[i], logs[i], prbs_logs[i]] for i in range(len(all_ps_old_full))],
            row_labels = [M.Text(
                rt, font_size = (SSCTV.sym_size_by_n(len(all_ps_old_full) + 3)
                                 - 8.0),
                color = SSCTV.get_main_color())
                          for rt in rows],
            col_labels = [
                M.MathTex(
                    r"p_i", color = SSCTV.get_main_color(),
                    font_size = (SSCTV.sym_size_by_n(len(all_ps_old_full) + 3)
                                 - 4.0)),
                M.MathTex(
                    r"-\log_2 p_i", color = SSCTV.get_main_color(),
                    font_size = (SSCTV.sym_size_by_n(len(all_ps_old_full) + 3)
                                 - 4.0)),
                M.MathTex(
                    r"-p_i \cdot \log_2 p_i", color = SSCTV.get_main_color(),
                    font_size = (SSCTV.sym_size_by_n(len(all_ps_old_full) + 3)
                                 - 4.0))],
            include_outer_lines = True,
            v_buff = 0.48 * SSCTV.sym_size_by_n(len(all_ps_old_full)) / 54.0,
            h_buff = 2.0,
            element_to_mobject_config = {
                "font_size": SSCTV.prb_size_by_n(len(all_ps_old_full)),
                "color": SSCTV.get_main_color()},
            line_config = {"color": SSCTV.get_main_color()})
        scene.add(table)
        scene.wait()
        scene.clear()
        scene.add(M.Rectangle(
            SSCTV.get_background_color(), 9.0, 15.0, fill_opacity = 1.0))
        sum_entr = sum([- round(log2(sym.probability) * sym.probability, 3)
                    for sym in all_ps_old_full])
        tx = r"H = - \sum_{i=1}^M p_i \cdot \log_2 p_i = " + str(round(sum_entr, 3))
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 88.0)
        scene.add(tex)


class ProbabilitySymbol(object):
    def __init__(self, symbol: str, probability: str, merged: bool, code: str = ""):
        self.symbol = symbol
        self.probability = float(probability)
        self.merged = merged
        self.code = code

    def __str__(self):
        return f"{self.symbol}: {self.probability} - {self.merged} - {self.code}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if self.probability == other.probability:
            if self.merged and not other.merged: return True
            else:
                return self.symbol < other.symbol
        return self.probability < other.probability

    def __eq__(self, other):
        return self.probability == other.probability


class ZLine(M.TipableVMobject):
    def __init__(self, points, size = 0.2, stroke_width = 4,
                 color = "#FFFFFF", **kwargs):
        super().__init__(
            stroke_color = color,
            stroke_opacity = 1.0,
            stroke_width = stroke_width,
            background_stroke_color = "#000000",
            background_stroke_opacity = 1.0,
            background_stroke_width = 0,
            **kwargs)

        self.set_points_as_corners(points)
        self.add_tip(self.create_tip(tip_length = size, tip_width = size))


class PromoCode(object):

    promo_codes = [("o27739521", 100, False),
                   ("o63116012", 50, False),
                   ("o86636403", 25, False),
                   ("o15260943", 10, False),
                   ("t72539756", 20, False), #до 10.09.2023 включительно
                   ("s05050505", 50, False)]

    class PromoCodeType(enum.Enum):
        O = "One-time",
        T = "Temporary",
        S = "Special"

    def __init__(self, did: str, discount: int, used: bool):
        self.did = did
        self.discount = discount
        self.used = used

    @staticmethod
    def get_all_did(with_prefix = False):
        all_did = []
        for d in PromoCode.promo_codes:
            if with_prefix:
                all_did.append(d[0])
            else:
                all_did.append(d[0][1:])
        return all_did

    @staticmethod
    def check_promo_code(did: str):
        return did in PromoCode.get_all_did()

    @staticmethod
    def check_promo_code_full(did: str):
        ind = PromoCode.get_all_did(True).index(did)
        promo = PromoCode.promo_codes[ind]
        info = ""
        if promo[2]:
            info = f"К сожалению, промокод '{promo[0]}' уже недействителен.\
            Попробуйте другой."
        else:
            info = f"Промокод '{promo[0]}' действителен."
        print(info, promo)
        return info

    @staticmethod
    def add_prefix(did: str, type: PromoCodeType):
        prefix = ""
        if type is PromoCode.PromoCodeType.O: prefix = "o"
        elif type is PromoCode.PromoCodeType.T: prefix = "t"
        elif type is PromoCode.PromoCodeType.S: prefix = "s"
        else: print("No such type promo code")
        return prefix + did

    @staticmethod
    def get_new_promo_code(discount: int, type: PromoCodeType = PromoCodeType.O):
        r = round(random.random() * 10000000000000000.0)
        r = r // 100000000
        while PromoCode.check_promo_code(str(r)):
            r = round(random.random() * 10000000000000000.0)
            r = r // 100000000
        prcd = PromoCode.add_prefix(str(r), type)
        PromoCode.promo_codes.append((prcd, discount, False))
        return prcd


class Table(M.Table):
    def __init__(
        self, table, row_labels = None, col_labels = None,
        top_left_entry = None, v_buff: float = 0.8, h_buff: float = 0.8,
        include_outer_lines: bool = False,
        add_background_rectangles_to_entries: bool = False,
        entries_background_color = "#000000",
        include_background_rectangle: bool = False,
        background_rectangle_color = "#000000",
        element_to_mobject = M.Text,
        element_to_mobject_config: dict = {},
        arrange_in_grid_config: dict = {},
        line_config: dict = {},
        **kwargs):
        super().__init__(table, row_labels, col_labels,
            top_left_entry, v_buff, h_buff,
            include_outer_lines,
            add_background_rectangles_to_entries,
            entries_background_color,
            include_background_rectangle,
            background_rectangle_color,
            element_to_mobject,
            element_to_mobject_config,
            arrange_in_grid_config,
            line_config,
            **kwargs)
