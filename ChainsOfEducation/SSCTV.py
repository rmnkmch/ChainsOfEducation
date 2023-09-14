import manim as M
import random
import enum


class SSCTV(object):
    """SSCTV pictures and animations"""

    EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    en = "abcdefghijklmnopqrstuvwxyz"
    RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    PRB_NUM: int = 2
    UL_CORNER = M.LEFT * 5.5 + M.UP * 3.5

    data_saved = '''
    my - A0.2 B0.06 C0.14 D0.1 E0.47 F0.03
    Саша И - У0.13 М0.39 И0.15 Р0.05 Э0.21 А0.07

    Артём М - tv"100111110000101" 17
    М0.33 О0.27 С0.19 К0.13 В0.05 А0.03
    КОММВМКСОМСМОАМКОМВО
    МОММСОСМСМССММКОКОМС
    ВКАКАВАВВАВВВАВКАААА
    '''

    used_ps_str = "М0.33 О0.27 С0.19 К0.13 В0.05 А0.03"
    m1 = "КОММВМКСОМСМОАМКОМВО"
    m2 = "МОММСОСМСМССММКОКОМС"
    m3 = "ВКАКАВАВВАВВВАВКАААА"
    entropy = 0.0
    table_data = []
    symbol_num = 6
    mean_bit_over_symb1 = round(1.0 / 20.0, 3)
    mean_bit_over_symb2 = round(1.0 / 20.0, 3)
    mean_bit_over_symb3 = round(1.0 / 20.0, 3)

    tv1_var = 17 - 15

    new = False

    @staticmethod
    def get_all_ps_by_str(text: str):
        ret = []
        for ch_p in text.split():
            symbol = ch_p[0]
            probability = ch_p[1:]
            SSCTV.PRB_NUM = max(SSCTV.PRB_NUM, len(probability) - 2)
            ret.append(ProbabilitySymbol(symbol, probability, False, ""))
        return ret

    @staticmethod
    def check_probabilities(all_ps: list):
        p = 0.0
        for ps in all_ps:
            p += ps.probability
        return round(p, SSCTV.PRB_NUM) == 1.0

    @staticmethod
    def get_random_symbols(n: int, alphabet: str):
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
    def get_random_probabilities(n: int):
        ret = []
        sm = 0.0
        for _ in range(n):
            r = random.random()
            ret.append(r)
            sm += r
        for pbi in range(len(ret)):
            ret[pbi] = round(ret[pbi] / sm, SSCTV.PRB_NUM)
            if ret[pbi] <= 0.0001: ret[pbi] = 0.01
        return ret

    @staticmethod
    def get_random_ps(n: int):
        pb = [0.1]
        while abs(sum(pb) - 1.0) > 0.005:
            pb = SSCTV.get_random_probabilities(n)
        sm = SSCTV.get_random_symbols(n, SSCTV.RU)
        data = []
        for i in range(len(pb)):
            data.append(sm[i] + str(round(pb[i], SSCTV.PRB_NUM)))
        return " ".join(data)

    @staticmethod
    def sym_size_by_n(n: int):
        if n <= 6: return 52.0
        elif n <= 8: return 50.0
        elif n <= 10: return 44.0
        elif n <= 12: return 40.0
        elif n <= 14: return 36.0
        elif n <= 16: return 32.0
        elif n <= 18: return 28.0
        elif n <= 23: return 24.0
        else: return 20.0

    @staticmethod
    def prb_size_by_n(n: int):
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
    def zline_size_by_n(n: int):
        if n <= 6: return 0.25
        elif n <= 8: return 0.19
        elif n <= 10: return 0.14
        elif n <= 12: return 0.12
        elif n <= 14: return 0.1
        elif n <= 16: return 0.07
        elif n <= 18: return 0.05
        else: return 0.03

    @staticmethod
    def zline_stroke_width_by_n(n: int):
        if n <= 9: return 4
        elif n <= 13: return 3
        elif n <= 17: return 2
        else: return 1

    @staticmethod
    def find_ps_by_symbol(symbol: str, all_ps: list):
        for ps in all_ps:
            if ps.symbol == symbol:
                return ps

    @staticmethod
    def find_index_ps_by_symbol(symbol: str, all_ps: list):
        return all_ps.index(SSCTV.find_ps_by_symbol(symbol, all_ps))

    @staticmethod
    def get_ps_by_prb(prb: float, prb_line: list, all_ps: list):
        for i in range(len(prb_line)):
            if prb_line[i] > prb:
                return all_ps[i - 1]

    @staticmethod
    def get_prb_line(all_ps: list, lowest: float):
        prb_line = [lowest]
        for i in range(len(all_ps)):
            prb_line.append(all_ps[i].probability + prb_line[i] + lowest)
        return prb_line

    @staticmethod
    def get_main_color():
        return "#000000"

    @staticmethod
    def get_background_color():
        return "#FFFFFF"

    @staticmethod
    def make_background(scene: M.Scene):
        scene.add(M.Rectangle(
            SSCTV.get_background_color(), 9.0, 15.0, fill_opacity = 1.0))

    @staticmethod
    def make_pause(scene: M.Scene):
        scene.wait()
        scene.clear()

    @staticmethod
    def print_sp_octave(all_ps: list):
        syms = []
        prbs = []
        for i in range(len(all_ps)):
            syms.append(all_ps[i].symbol)
            prbs.append(str(round(all_ps[i].probability * 10 ** SSCTV.PRB_NUM)))
        print(", ".join(syms))
        print(", ".join(prbs))

    @staticmethod
    def print_message_20(mess_ps: list, compare_to: list):
        syms = []
        leters = []
        for ps in mess_ps:
            syms.append(str(
                SSCTV.find_index_ps_by_symbol(ps.symbol, compare_to) + 1))
            leters.append(ps.symbol)
        print(", ".join(syms))
        ret = "".join(leters)
        print(ret)
        return ret

    @staticmethod
    def get_message_20_by_str(mess_str: str, all_ps: list):
        mess = []
        for char in mess_str:
            mess.append(SSCTV.find_ps_by_symbol(char, all_ps))
        return mess

    @staticmethod
    def fill_zeros(str_to_fill, n):
        return "0" * (n - len(str_to_fill)) + str_to_fill

    @staticmethod
    def tv1_sum_mod_2(ch1: str, ch2: str):
        if (ch1 == "0" and ch2 == "0") or (ch1 == "1" and ch2 == "1"):
            return "0"
        else:
            return "1"

    @staticmethod
    def tv1_get_random_in_str(n: int):
        ret = []
        for _ in range(n):
            r = random.random()
            if r >= 0.5:
                ret.append("1")
            else:
                ret.append("0")
        return "".join(ret)

    @staticmethod
    def make_all(scene: M.Scene):
        SSCTV.random_SPIK1(SSCTV.new)
        SSCTV.make_SPIK1(scene)
        #SSCTV.make_tv1(scene)

    @staticmethod
    def random_SPIK1(new_random = False):
        pss = SSCTV.used_ps_str
        if new_random:
            pss = SSCTV.get_random_ps(SSCTV.symbol_num)
            SSCTV.used_ps_str = pss
        print(pss)
        all_ps = SSCTV.get_all_ps_by_str(pss)
        SSCTV.print_sp_octave(all_ps)
        if not SSCTV.check_probabilities(all_ps): print("prb != 1")
        n = 20
        all_ps_copy = [ProbabilitySymbol.get_full_copy(ps) for ps in all_ps]
        m1 = SSCTV.get_message_20_by_str(SSCTV.m1, all_ps_copy)
        m2 = SSCTV.get_message_20_by_str(SSCTV.m2, all_ps_copy)
        m3 = SSCTV.get_message_20_by_str(SSCTV.m3, all_ps_copy)
        if new_random:
            m1 = SSCTV.get_random_message_1(all_ps_copy, n)
            m2 = SSCTV.get_random_message_2(all_ps_copy, n)
            m3 = SSCTV.get_random_message_3(all_ps_copy, n)
        SSCTV.m1 = SSCTV.print_message_20(m1, all_ps)
        SSCTV.m2 = SSCTV.print_message_20(m2, all_ps)
        SSCTV.m3 = SSCTV.print_message_20(m3, all_ps)

    @staticmethod
    def make_SPIK1(scene: M.Scene):
        ps_full = SSCTV.make_haffman(scene)
        SSCTV.make_pause(scene)
        SSCTV.make_table_1(scene, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.make_table_2(scene, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.make_formula_1(scene, ps_full)
        SSCTV.make_pause(scene)
        m1 = SSCTV.get_message_20_by_str(SSCTV.m1, ps_full)
        m2 = SSCTV.get_message_20_by_str(SSCTV.m2, ps_full)
        m3 = SSCTV.get_message_20_by_str(SSCTV.m3, ps_full)
        SSCTV.make_messages_20(scene, m1, m2, m3, True)
        SSCTV.make_golomb(scene, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.make_table_1(scene, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.make_messages_20(scene, m1, m2, m3, True)
        num = SSCTV.make_arithm(scene, SSCTV.m1, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.make_arithm_table(scene, SSCTV.m1, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.make_count_1(scene, num)
        SSCTV.make_pause(scene)
        SSCTV.make_formula_2(scene)
        SSCTV.make_pause(scene)
        SSCTV.make_formula_3(scene)
        SSCTV.make_pause(scene)
        SSCTV.make_formula_4(scene)
        SSCTV.make_pause(scene)
        SSCTV.make_formula_5(scene)
        SSCTV.make_pause(scene)
        SSCTV.make_formula_6(scene)
        SSCTV.make_pause(scene)
        SSCTV.make_table_3(scene, SSCTV.table_data, SSCTV.entropy)
        SSCTV.make_pause(scene)

    @staticmethod
    def make_haffman(scene: M.Scene):
        SSCTV.make_background(scene)
        all_ps = SSCTV.get_all_ps_by_str(SSCTV.used_ps_str)
        all_len = len(all_ps)
        vert_offset = 8.0 / (all_len + 2)
        prb_size = SSCTV.prb_size_by_n(all_len)
        zline_size = SSCTV.zline_size_by_n(all_len)
        zline_stroke_width = SSCTV.zline_stroke_width_by_n(all_len)
        horz_offset = 12.0 / (all_len - 1)
        all_ps_old_full = all_ps.copy()
        all_ps.sort()
        all_ps.reverse()
        all_ps_old = all_ps.copy()
        for psi in range(all_len):
            scene.add(M.Text(
                all_ps[psi].symbol + ":",
                font_size = SSCTV.sym_size_by_n(all_len),
                color = SSCTV.get_main_color()).move_to(
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
                            color = SSCTV.get_main_color()
                            ).next_to(line, M.UR, max_width * 0.1)
                n0.shift(M.DOWN * n0.height)
                n1 = M.Text("1", font_size = prb_size,
                            color = SSCTV.get_main_color()
                            ).next_to(line, M.DR, max_width * 0.1)
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
        return all_ps_old_full

    @staticmethod
    def make_table_1(scene: M.Scene, all_ps: list):
        SSCTV.make_background(scene)
        table = Table(
            [[all_ps[i].symbol, all_ps[i].code]
             for i in range(len(all_ps))],
             include_outer_lines = True,
             v_buff = 0.48 * SSCTV.sym_size_by_n(len(all_ps)) / 52.0,
             h_buff = 1.8,
             element_to_mobject_config = {
                 "font_size": SSCTV.prb_size_by_n(len(all_ps)),
                 "color": SSCTV.get_main_color()},
             line_config = {"color": SSCTV.get_main_color()})
        scene.add(table)

    @staticmethod
    def make_table_2(scene: M.Scene, all_ps: list):
        from math import log2
        SSCTV.make_background(scene)
        syms = [ps.symbol for ps in all_ps]
        prbs = [str(ps.probability) for ps in all_ps]
        logs = [str(- round(log2(ps.probability), 3)) for ps in all_ps]
        prbs_logs = [str(- round(log2(ps.probability) * ps.probability, 3))
                     for ps in all_ps]
        table = Table(
            [[prbs[i], logs[i], prbs_logs[i]] for i in range(len(all_ps))],
            row_labels = [
                M.Text(rt, font_size = SSCTV.sym_size_by_n(len(all_ps)),
                       color = SSCTV.get_main_color()) for rt in syms],
            col_labels = [
                M.MathTex(
                    r"p_i", color = SSCTV.get_main_color(),
                    font_size = SSCTV.sym_size_by_n(len(all_ps))),
                M.MathTex(
                    r"-\log_2 p_i", color = SSCTV.get_main_color(),
                    font_size = SSCTV.sym_size_by_n(len(all_ps))),
                M.MathTex(
                    r"-p_i \cdot \log_2 p_i", color = SSCTV.get_main_color(),
                    font_size = SSCTV.sym_size_by_n(len(all_ps)))],
            include_outer_lines = True,
            v_buff = 0.48 * SSCTV.sym_size_by_n(len(all_ps)) / 52.0,
            h_buff = 1.8,
            element_to_mobject_config = {
                "font_size": SSCTV.prb_size_by_n(len(all_ps)),
                "color": SSCTV.get_main_color()},
            line_config = {"color": SSCTV.get_main_color()})
        scene.add(table)

    @staticmethod
    def make_formula_1(scene: M.Scene, all_ps: list):
        from math import log2
        SSCTV.make_background(scene)
        SSCTV.entropy = sum([- log2(sym.probability) * sym.probability
                        for sym in all_ps])
        tx = r"H = - \sum_{i=1}^M p_i \cdot \log_2 p_i = " + str(
            round(SSCTV.entropy, 3))
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 64.0)
        scene.add(tex)

    @staticmethod
    def get_random_message_1(all_ps: list, n: int = 20):
        all_ps.sort()
        prb_line = SSCTV.get_prb_line(all_ps, 0.0)
        mess_ps = []
        for _ in range(n):
            mess_ps.append(SSCTV.get_ps_by_prb(random.random(), prb_line, all_ps))
        return mess_ps

    @staticmethod
    def get_random_message_2(all_ps: list, n: int = 20):
        a = 0.0
        b = 0.01
        ii = 0
        while a < b:
            a = all_ps[ii].probability
            b = all_ps[- ii - 1].probability
            ii += 1
        med = (a + b) * 0.5
        for i in range(len(all_ps)):
            if all_ps[i].probability <= med:
                all_ps[i].probability *= 0.2
            else:
                all_ps[i].probability *= 5.0
        pbrs = 0.0
        for i in range(len(all_ps)):
            pbrs += all_ps[i].probability
        for i in range(len(all_ps)):
            all_ps[i].probability = all_ps[i].probability / pbrs
        prb_line = SSCTV.get_prb_line(all_ps, 0.0)
        mess_ps = []
        for i in range(n):
            mess_ps.append(SSCTV.get_ps_by_prb(random.random(), prb_line, all_ps))
        return mess_ps

    @staticmethod
    def get_random_message_3(all_ps: list, n: int = 20):
        ii = 0
        while ii < len(all_ps) // 2:
            a = all_ps[ii].probability
            b = all_ps[- ii - 1].probability
            all_ps[ii].probability = b
            all_ps[- ii - 1].probability = a
            ii += 1
        prb_line = SSCTV.get_prb_line(all_ps, 0.0)
        mess_ps = []
        for _ in range(n):
            mess_ps.append(SSCTV.get_ps_by_prb(random.random(), prb_line, all_ps))
        return mess_ps

    @staticmethod
    def make_messages_20(scene: M.Scene, m1: list, m2: list, m3: list,
                         add: bool = False):
        SSCTV.make_message_20(scene, m1, True, add)
        SSCTV.make_pause(scene)
        SSCTV.make_message_20(scene, m2, True, add)
        SSCTV.make_pause(scene)
        SSCTV.make_message_20(scene, m3, True, add)
        SSCTV.make_pause(scene)

    @staticmethod
    def make_message_20(scene: M.Scene, mess_ps: list,
                        with_text: bool = True, add: bool = False):
        SSCTV.make_background(scene)
        syms = []
        codes = []
        indexes = []
        n = 1
        len_code = 0
        for mes in mess_ps:
            syms.append(M.Text(mes.symbol, color = SSCTV.get_main_color(),
                               font_size = 30.0))
            codes.append(M.Text(mes.code, color = SSCTV.get_main_color()))
            indexes.append(M.Text(str(n), color = SSCTV.get_main_color(),
                                  font_size = 16.0))
            n += 1
            len_code += len(mes.code)
        vg = M.VGroup(*codes).arrange().move_to(1.5 * M.UP)
        scene.add(vg)
        for i in range(len(syms)):
            scene.add(syms[i].next_to(codes[i], direction = M.UP))
            scene.add(indexes[i].next_to(syms[i], direction = M.UP))
        sf = 13.5 / vg.width
        M.VGroup(*syms, *codes, *indexes).scale(sf)
        if with_text:
            bit = r"Всего бит = " + str(len_code)
            sym = r"Всего символов = " + str(len(syms))
            bit_sym = r"Бит на символ = " + str(round(len_code / len(syms), 3))
            b = M.Text(bit, color = SSCTV.get_main_color())
            s = M.Text(sym, color = SSCTV.get_main_color()).next_to(b, M.DOWN)
            bs = M.Text(bit_sym, color = SSCTV.get_main_color()).next_to(s, M.DOWN)
            scene.add(b, s, bs)
            if add:
                SSCTV.table_data.append(round(len_code / len(syms), 3))

    @staticmethod
    def decode_haffman(scene: M.Scene, mess_str: str, all_ps: list):
        SSCTV.make_background(scene)
        m = SSCTV.get_message_20_by_str(mess_str, all_ps)
        SSCTV.make_message_20(scene, m, False)

    @staticmethod
    def make_golomb(scene: M.Scene, all_ps: list):
        golomb_r = {0: "0", 1: "10", 2: "11"}
        golomb_q = {0: "0", 1: "10", 2: "110", 3: "1110", 4: "11110", 5: "111110"}
        SSCTV.make_background(scene)
        all_ps_sorted = all_ps.copy()
        all_ps_sorted.sort()
        all_ps_sorted.reverse()
        all_len = len(all_ps_sorted)
        for psi in range(all_len):
            t = str(psi + 1) + r" - " + all_ps_sorted[psi].symbol + r":"
            p = str(round(all_ps_sorted[psi].probability, SSCTV.PRB_NUM)) + ";"
            mobp = M.Text(p, font_size = 30.0,
                          color = SSCTV.get_main_color()).move_to(
                              SSCTV.UL_CORNER + M.RIGHT * 1.5 + M.UP * 0.07
                              + M.DOWN * (8.0 / (all_len + 2)) * (psi + 1))
            mobt = M.Text(
                t, font_size = 44.0,
                color = SSCTV.get_main_color()).next_to(mobp, M.LEFT)
            scene.add(mobp, mobt)
            m = 3
            q = psi // m
            r = psi - q * m
            texstr = (r"q = \left[\frac{" + str(psi + 1)
                      + r"-1}3\right] = " + str(q) + r";\ r = "
                      + str(psi + 1) + r" - 1 - " + str(q) + r"\cdot"
                      + str(m) + r" = " + str(r))
            tex = M.MathTex(texstr, color = SSCTV.get_main_color(),
                            font_size = 32.0).next_to(mobp)
            found_ps = SSCTV.find_ps_by_symbol(
                all_ps_sorted[psi].symbol, all_ps_sorted)
            found_ps.code = golomb_q[q] + golomb_r[r]
            found_text = M.Text(r" - код: " + found_ps.code,
                                color = SSCTV.get_main_color(),
                                font_size = 30.0).next_to(tex)
            scene.add(tex, found_text)

    @staticmethod
    def make_arithm(scene: M.Scene, mess_str: str, all_ps: list):
        def prb_size(cycle: int):
            if cycle <= 2: return 18.0
            elif cycle <= 4: return 16.0
            return 14.0

        left_side = M.LEFT * 6.6
        SSCTV.make_background(scene)
        mess_str = mess_str[:6]
        mes_len = len(mess_str)
        horz_offset = 12.0 / mes_len
        prb_line_old = SSCTV.get_prb_line(all_ps, 0.0)
        prb_line = SSCTV.get_prb_line(all_ps, 0.0)
        for cycle in range(mes_len + 1):
            nl = M.NumberLine(
                x_range = [0.0, 1.0, 1.0],
                length = 7.0,
                include_tip = False,
                include_numbers = False,
                rotation = 90.0 * M.DEGREES,
                color = SSCTV.get_main_color(),
                tick_size = 0.1,
                stroke_width = 3,
            ).move_to(left_side + M.RIGHT * horz_offset * cycle)
            scene.add(nl)
            if cycle != mes_len:
                for psi in range(len(all_ps) + 1):
                    new_text = M.Text(
                        str(round(prb_line[psi], (cycle + 1) * 2)),
                        font_size = prb_size(cycle), color = SSCTV.get_main_color()
                    ).next_to(nl, buff = 0.1)
                    new_text.shift(M.UP * 7.0 * (prb_line_old[psi] - 0.5))
                    new_line = M.Line(
                        left_side - M.LEFT * 0.1 + M.RIGHT * horz_offset * cycle,
                        left_side + M.LEFT * 0.1 + M.RIGHT * horz_offset * cycle,
                        color = SSCTV.get_main_color(),
                        stroke_width = 3.0
                    ).next_to(nl, buff = - 0.2)
                    new_line.shift(M.UP * 7.0 * (prb_line_old[psi] - 0.5))
                    scene.add(new_text, new_line)
                g_indx = SSCTV.find_index_ps_by_symbol(
                    mess_str[cycle], all_ps)
                p1, p2 = (prb_line[g_indx], prb_line[g_indx + 1])
                diff = p2 - p1
                for i in range(len(all_ps) + 1):
                    prb_line[i] = p1 + prb_line_old[i] * diff
                ln1 = ZLine([
                    M.UP * 7.0 * (prb_line_old[g_indx] - 0.5)
                    + left_side + M.RIGHT * horz_offset * cycle,
                    M.UP * - 3.5
                    + left_side + M.RIGHT * horz_offset * (cycle + 1)
                    ], 0.1, 2.0, SSCTV.get_main_color())
                ln2 = ZLine([
                    M.UP * 7.0 * (prb_line_old[g_indx + 1] - 0.5)
                    + left_side + M.RIGHT * horz_offset * cycle,
                    M.UP * 3.5
                    + left_side + M.RIGHT * horz_offset * (cycle + 1)
                    ], 0.1, 2.0, SSCTV.get_main_color())
                scene.add(ln1, ln2)
            else:
                num1 = str(round(prb_line[-1], (cycle + 1) * 2))
                num2 = str(round(prb_line[0], (cycle + 1) * 2))
                new_text = M.Text(
                    num1,
                    font_size = prb_size(cycle), color = SSCTV.get_main_color()
                    ).next_to(nl, buff = 0.1)
                new_text.shift(M.UP * 3.5)
                new_text2 = M.Text(
                    num2,
                    font_size = prb_size(cycle), color = SSCTV.get_main_color()
                    ).next_to(nl, buff = 0.1)
                new_text2.shift(M.UP * -3.5)
                scene.add(new_text, new_text2)
                a = 2
                ret_str = []
                while len(num1) > a and num1[a] == num2[a]:
                    ret_str.append(num2[a])
                    a += 1
                ret_str.append(str(int(num2[a]) + 1))
                return "".join(ret_str)

    @staticmethod
    def make_arithm_table(scene: M.Scene, mess_str: str, all_ps: list):
        def pop_prefix(str1, str2):
            i = 0
            while len(str1) > i and str1[i] == str2[i]:
                i += 1
            return i

        def get_sdv(p1, p2, file):
            nonlocal in_file_old
            if file > in_file_old:
                p1 = p1[file - in_file_old:] + (file - in_file_old) * "0"
                p2 = p2[file - in_file_old:] + (file - in_file_old) * "9"
                in_file_old = file
            return [p1, p2]

        SSCTV.make_background(scene)
        num_symbols = 8
        mess_str = mess_str[:6]
        mes_len = len(mess_str)
        prb_line_old = SSCTV.get_prb_line(all_ps, 0.0)
        prb_line = SSCTV.get_prb_line(all_ps, 0.0)
        data = []
        in_file = 0
        in_file_old = 0
        for cycle in range(mes_len):
            g_indx = SSCTV.find_index_ps_by_symbol(
                mess_str[cycle], all_ps)
            p1, p2 = (prb_line[g_indx], prb_line[g_indx + 1])
            diff = p2 - p1
            for i in range(len(all_ps) + 1):
                prb_line[i] = p1 + prb_line_old[i] * diff
            p1_str = SSCTV.fill_zeros(str(round(
                p1 * 10 ** (num_symbols + in_file))), num_symbols)
            p2_str = SSCTV.fill_zeros(str(round(
                p2 * 10 ** (num_symbols + in_file))), num_symbols)
            pref = pop_prefix(p1_str, p2_str)
            in_file = max(in_file, pref)
            in_file_str = p2_str[in_file_old:in_file]
            p1_str = p1_str[in_file_old:]
            p2_str = p2_str[in_file_old:]
            if cycle == mes_len - 1:
                sdv = ["-", "-"]
                in_file_str += str(int(p1_str[in_file - in_file_old]) + 1)
            else:
                sdv = get_sdv(p1_str, p2_str, in_file)
                if in_file_str == "":
                    in_file_str = "-"
            data.append([mess_str[cycle], p1_str, p2_str,
                         in_file_str, sdv[0], sdv[1]])
        fs = 20.0
        table = Table(
            data,
            col_labels = [
                M.Text("Символ", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Нижн.", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Верхн.", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("В файл", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Нижн. сдв.", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Верхн. сдв.", font_size = fs,
                       color = SSCTV.get_main_color()),
                ],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 0.8,
            element_to_mobject_config = {
                "font_size": fs,
                "color": SSCTV.get_main_color()},
            line_config = {"color": SSCTV.get_main_color()})
        scene.add(table)

    @staticmethod
    def make_count_1(scene: M.Scene, num: str):
        SSCTV.make_background(scene)
        t = num + r"_{10} = " + bin(int(num))[2:] + r"_2"
        show = M.MathTex(t, color = SSCTV.get_main_color(),
                         font_size = 54.0).move_to(2.0 * M.UP)
        bit = r"Всего бит = " + str(len(bin(int(num))[2:]))
        sym = r"Всего символов = " + str(SSCTV.symbol_num)
        bit_sym = r"Бит на символ = " + str(round(
            len(bin(int(num))[2:]) / SSCTV.symbol_num, 3))
        b = M.Text(bit, color = SSCTV.get_main_color())
        s = M.Text(sym, color = SSCTV.get_main_color()).next_to(b, M.DOWN)
        bs = M.Text(bit_sym, color = SSCTV.get_main_color()).next_to(s, M.DOWN)
        scene.add(show, b, s, bs)

    @staticmethod
    def make_formula_2(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"I_s = log_2 M"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0)
        scene.add(tex)

    @staticmethod
    def make_formula_3(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"H = - \sum_{i=1}^M p_i \cdot \log_2 p_i"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0)
        scene.add(tex)

    @staticmethod
    def make_formula_4(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"R = \log_2 M - H"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0)
        scene.add(tex)

    @staticmethod
    def make_formula_5(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"H \le n_{cp} \le H + 1"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0)
        scene.add(tex)

    @staticmethod
    def make_formula_6(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"R_c = L_{cp} - H"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0)
        scene.add(tex)

    @staticmethod
    def make_table_3(scene: M.Scene, data: list, H: float):
        SSCTV.make_background(scene)
        fs = 22.0
        data.append(SSCTV.mean_bit_over_symb1)
        data.append(SSCTV.mean_bit_over_symb2)
        data.append(SSCTV.mean_bit_over_symb3)
        table_data = []
        for i in range(3):
            table_data.append([str(data[i]), str(data[i + 3]), str(data[i + 6])])
        for i in range(0, 9, 3):
            data.append(round((data[i] + data[i + 1] + data[i + 2]) / 3.0, 3))
            data.append(round(data[- 1] - H, 3))
        table_data.append([str(data[9]), str(data[11]), str(data[13])])
        table_data.append([str(data[10]), str(data[12]), str(data[14])])
        table = Table(
            table_data,
            row_labels = [
                M.Text("Сообщение,\nсоответствующее статистике", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Сообщение,\nсостоящее из символов\nс высокими вероятностями",
                       font_size = fs, color = SSCTV.get_main_color()),
                M.Text("Сообщение,\nсостоящее из символов\nс низкими вероятностями",
                       font_size = fs, color = SSCTV.get_main_color()),
                M.Text("Cреднее количество\nбит на символ", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Избыточность", font_size = fs,
                       color = SSCTV.get_main_color())
                ],
            col_labels = [
                M.Text("Алгоритм\nХаффмана", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Алгоритм\nГоломба", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Арифметическое\nкодирование", font_size = fs,
                       color = SSCTV.get_main_color())
                ],
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.8,
            element_to_mobject_config = {
                "font_size": fs,
                "color": SSCTV.get_main_color()},
            line_config = {"color": SSCTV.get_main_color()})
        scene.add(table)

    @staticmethod
    def make_tv1(scene: M.Scene):
        key = SSCTV.fill_zeros(bin(int(SSCTV.tv1_var))[2:], 4)
        psp_str = SSCTV.tv1_make_table_1(scene, key)
        SSCTV.make_pause(scene)
        in_str = SSCTV.tv1_get_random_in_str(15)
        data01 = SSCTV.tv1_make_table_2(scene, in_str, psp_str)
        SSCTV.make_pause(scene)
        SSCTV.tv1_make_text_1(scene, data01)
        SSCTV.make_pause(scene)
        SSCTV.tv1_make_text_2(scene)
        SSCTV.make_pause(scene)

    @staticmethod
    def tv1_make_table_1(scene: M.Scene, key: str):
        def update_0_1(ch, i):
            nonlocal zeroes, ones, curr_max, max_ind, zeroes_max_ind, ones_max_ind
            nonlocal zeroes_max, ones_max, prev_ch
            if prev_ch == "":
                pass
            elif ch == "0":
                zeroes += 1
                if prev_ch == ch:
                    curr_max += 1
                    if zeroes_max < curr_max:
                        zeroes_max = curr_max
                        zeroes_max_ind = [max_ind, i]
                else:
                    max_ind = i
                    curr_max = 1
            elif ch == "1":
                ones += 1
                if prev_ch == ch:
                    curr_max += 1
                    if ones_max < curr_max:
                        ones_max = curr_max
                        ones_max_ind = [max_ind, i]
                else:
                    max_ind = i
                    curr_max = 1
            prev_ch = ch

        SSCTV.make_background(scene)
        data = []
        table_data = []
        ones_max = 0
        zeroes_max = 0
        zeroes = 0
        ones = 0
        prev_ch = ""
        curr_max = 1
        max_ind = 0
        zeroes_max_ind = []
        ones_max_ind = []
        ret_str = []
        for i in range(16):
            update_0_1(key[0], i)
            last = SSCTV.tv1_sum_mod_2(key[0], key[1])
            data.append([str(i), key[3], key[2], key[1], key[0], last])
            ret_str.append(key[0])
            key = key[1:] + last
        for i in range(len(data[0])):
            table_data.append([])
            for j in range(len(data)):
                table_data[-1].append(data[j][i])
        fs = 24.0
        table = Table(
            table_data,
            row_labels = [
                M.Text("N", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("1", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("2", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("3", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("4", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("C", font_size = fs, color = SSCTV.get_main_color()),
                ],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 0.5,
            element_to_mobject_config = {
                "font_size": fs,
                "color": SSCTV.get_main_color()},
            line_config = {"color": SSCTV.get_main_color()}
            ).next_to(M.UP * 3.8, M.DOWN)
        text_1_0 = M.Text(f"Для триггера 4: 0 - {zeroes} раз; 1 - {ones} раз",
                          font_size = 28.0, color = SSCTV.get_main_color()
                          ).next_to(table, M.DOWN, 0.6)
        t0 = f"Серия нулей - {zeroes_max} подряд "
        t0 += f"в тактах {zeroes_max_ind[0]} - {zeroes_max_ind[1]}"
        text_0 = M.Text(t0, font_size = 28.0, color = SSCTV.get_main_color()
                        ).next_to(text_1_0, M.DOWN)
        t1 = f"Серия единиц - {ones_max} подряд "
        t1 += f"в тактах {ones_max_ind[0]} - {ones_max_ind[1]}"
        text_1 = M.Text(t1, font_size = 28.0, color = SSCTV.get_main_color()
                        ).next_to(text_0, M.DOWN)
        scene.add(table, text_1_0, text_0, text_1)
        ret_str = "".join(ret_str)
        return ret_str[:-1]

    @staticmethod
    def tv1_make_table_2(scene: M.Scene, in_str: str, psp_str: str):
        def update_0_1(ch, i):
            nonlocal zeroes, ones, curr_max, max_ind, zeroes_max_ind, ones_max_ind
            nonlocal zeroes_max, ones_max, prev_ch
            if prev_ch == "":
                pass
            elif ch == "0":
                zeroes += 1
                if prev_ch == ch:
                    curr_max += 1
                    if zeroes_max < curr_max:
                        zeroes_max = curr_max
                        zeroes_max_ind = [max_ind, i]
                else:
                    max_ind = i
                    curr_max = 1
            elif ch == "1":
                ones += 1
                if prev_ch == ch:
                    curr_max += 1
                    if ones_max < curr_max:
                        ones_max = curr_max
                        ones_max_ind = [max_ind, i]
                else:
                    max_ind = i
                    curr_max = 1
            prev_ch = ch

        data = []
        table_data = []
        ones_max = 0
        zeroes_max = 0
        zeroes = 0
        ones = 0
        prev_ch = ""
        curr_max = 1
        max_ind = 0
        zeroes_max_ind = []
        ones_max_ind = []
        SSCTV.make_background(scene)
        hemming_dist = 0
        for i in range(len(psp_str)):
            skr = SSCTV.tv1_sum_mod_2(in_str[i], psp_str[i])
            dskr = SSCTV.tv1_sum_mod_2(skr, psp_str[i])
            update_0_1(skr, i)
            pcp_prev = psp_str[i - 1]
            dskr_with_prev = SSCTV.tv1_sum_mod_2(skr, pcp_prev)
            data.append([str(i), in_str[i], psp_str[i],
                         skr, dskr, pcp_prev, dskr_with_prev])
            if dskr != dskr_with_prev:
                hemming_dist += 1
        skr = SSCTV.tv1_sum_mod_2(in_str[0], psp_str[0])
        dskr = SSCTV.tv1_sum_mod_2(skr, psp_str[0])
        update_0_1(skr, 15)
        pcp_prev = psp_str[14]
        dskr_with_prev = SSCTV.tv1_sum_mod_2(skr, pcp_prev)
        data.append([str(15), in_str[0], psp_str[0],
                     skr, dskr, pcp_prev, dskr_with_prev])
        for i in range(len(data[0])):
            table_data.append([])
            for j in range(len(data)):
                table_data[-1].append(data[j][i])
        fs = 24.0
        table = Table(
            table_data,
            row_labels = [
                M.Text("N", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("Вход", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("ПСП", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("Скр", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("Дскр", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("ПСП>>", font_size = fs, color = SSCTV.get_main_color()),
                M.Text("Дскр>>", font_size = fs, color = SSCTV.get_main_color()),
                ],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 0.5,
            element_to_mobject_config = {
                "font_size": fs,
                "color": SSCTV.get_main_color()},
            line_config = {"color": SSCTV.get_main_color()}
            ).next_to(M.UP * 3.8, M.DOWN)
        scene.add(table)
        return [zeroes, ones, zeroes_max, zeroes_max_ind,
                ones_max, ones_max_ind, hemming_dist]

    @staticmethod
    def tv1_make_text_1(scene: M.Scene, data01):
        SSCTV.make_background(scene)
        zeroes, ones = (data01[0], data01[1])
        zeroes_max, zeroes_max_ind = (data01[2], data01[3])
        ones_max, ones_max_ind = (data01[4], data01[5])
        hemming_dist = data01[6]
        text_1_0 = M.Text(f"Для Скр: 0 - {zeroes} раз; 1 - {ones} раз",
                          font_size = 28.0, color = SSCTV.get_main_color()
                          ).next_to(M.UP, M.DOWN, 0.6)
        t0 = f"Серия нулей - {zeroes_max} подряд "
        t0 += f"в тактах {zeroes_max_ind[0]} - {zeroes_max_ind[1]}"
        text_0 = M.Text(t0, font_size = 28.0, color = SSCTV.get_main_color()
                        ).next_to(text_1_0, M.DOWN)
        t1 = f"Серия единиц - {ones_max} подряд "
        t1 += f"в тактах {ones_max_ind[0]} - {ones_max_ind[1]}"
        text_1 = M.Text(t1, font_size = 28.0, color = SSCTV.get_main_color()
                        ).next_to(text_0, M.DOWN)
        text_hemm = M.Text(f"Расстояние Хэмминга = {hemming_dist}",
                           font_size = 28.0, color = SSCTV.get_main_color()
                           ).next_to(text_1, M.DOWN)
        scene.add(text_1_0, text_1, text_0, text_hemm)

    @staticmethod
    def tv1_make_text_2(scene: M.Scene):
        SSCTV.make_background(scene)
        dict_vars = {1: 101, 2: 1542, 3: 3160, 4: 4422, 5: 15214,
                     6: 26700, 7: 37120, 8: 52642, 9: 48592, 10: 59306,
                     11: 61085, 12: 7706, 13: 11490, 14: 32084, 15: 41056}
        bit = dict_vars[SSCTV.tv1_var]
        max_bit = 64800
        column_bit = 64800 // 3
        str_bit = f"Бит {1}: {bit}"
        text_bit = M.Text(str_bit, font_size = 30.0,
                          color = SSCTV.get_main_color()
                          ).next_to(M.UP * (3.2) + M.LEFT * 6.0)
        scene.add(text_bit)
        for i in range(1, 10, 1):
            if bit + column_bit >= max_bit:
                str_bit = f"Бит {i + 1}: {bit} - {column_bit * 2}"
                str_bit += f" + 1 = {bit - column_bit * 2 + 1}"
                bit = bit - column_bit * 2 + 1
            else:
                str_bit = f"Бит {i + 1}: {bit} + {column_bit} = {bit + column_bit}"
                bit = bit + column_bit
            text_bit = M.Text(str_bit, font_size = 30.0,
                              color = SSCTV.get_main_color()
                              ).next_to(M.UP * (3.2 - i * 0.7) + M.LEFT * 6.0)
            scene.add(text_bit)


class ProbabilitySymbol(object):
    def __init__(self, symbol: str, probability: str, merged: bool, code: str = ""):
        self.symbol = symbol
        self.probability = float(probability)
        self.merged = merged
        self.code = code

    def __str__(self):
        return f"{self.symbol}: {round(self.probability, 3)} - {self.code}"

    def __repr__(self):
        return self.__str__() + "\n"

    def __lt__(self, other):
        if self.probability == other.probability:
            if self.merged and not other.merged: return True
            else:
                return self.symbol < other.symbol
        return self.probability < other.probability

    def __eq__(self, other):
        return self.probability == other.probability

    @staticmethod
    def get_full_copy(probability_symbol):
        return ProbabilitySymbol(probability_symbol.symbol,
                                 probability_symbol.probability,
                                 probability_symbol.merged,
                                 probability_symbol.code)


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
