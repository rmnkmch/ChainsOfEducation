﻿import manim as M
import random
import enum


class SSCTV(object):
    """SSCTV and SiPK"""

    EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    en = "abcdefghijklmnopqrstuvwxyz"
    RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    PRB_NUM: int = 2
    UL_CORNER = M.LEFT * 5.5 + M.UP * 3.5

    data_saved = '''
    my_spik1
    A0.2 B0.06 C0.14 D0.1 E0.47 F0.03
    EEEDCAEEEAEACDAECEAE
    ECAEEEEEAEAEEAECEEEE
    FDFFFBFBFFFFFFFFFFBD
    my_spik2
    [[2.624, -0.475, 6.535], [-3.482, 0.422, 6.106],
    [-0.156, 0.49, 1.542], [-0.763, 1.139, 3.568]]
    Артём М - 17
    Алексей Г - 4
    [[3.013, 0.47, 4.333], [-0.506, 0.6, 4.464],
    [-0.165, -0.765, 2.938], [-0.858, -0.284, 5.776]]
    Данила Л - 14
    pkg load communications
    '''

    used_ps_str = ""
    m1 = ""
    m2 = ""
    m3 = ""
    entropy = 0.0
    table_data = []
    symbol_num = 7
    symbol_num_arithm = 6
    mess_symbol_num = 21
    mean_bit_over_symb1 = round(1.0 / mess_symbol_num, 3)
    mean_bit_over_symb2 = round(1.0 / mess_symbol_num, 3)
    mean_bit_over_symb3 = round(1.0 / mess_symbol_num, 3)

    tv_var = 7
    tv1_in_str = ""

    sipk2_Nhor = 24
    sipk2_Nver = 21
    sipk2_x_n = []
    sipk2_cffs = [[2.624, -0.475, 6.535], [-3.482, 0.422, 6.106],
                  [-0.156, 0.49, 1.542], [-0.763, 1.139, 3.568]]
    # sipk2_cffs = []
    sipk2_e1 = []
    sipk2_e2 = []
    sipk2_e2_opt = []
    sipk2_x_n_A = []
    sipk2_sum_x_x1_n1 = 0
    sipk2_sum_x1_x1_n1 = 0
    sipk2_sum_x_x1_n2 = 0
    sipk2_sum_x_x2_n2 = 0
    sipk2_sum_x1_x2_n2 = 0
    sipk2_sum_x1_x1_n2 = 0
    sipk2_sum_x2_x2_n2 = 0
    sipk2_a1 = 0.0
    sipk2_a21 = 0.0
    sipk2_a22 = 0.0
    sipk2_texsize = 40.0

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
        print("".join(ret))
        return "".join(ret)

    @staticmethod
    def transpose_list(used_list: list):
        ret_list: list = []
        for i in range(len(used_list[0])):
            ret_list.append([])
            for j in range(len(used_list)):
                ret_list[-1].append(used_list[j][i])
        return ret_list

    @staticmethod
    def make_all(scene: M.Scene):
        #SSCTV.random_sipk1()
        #SSCTV.make_sipk1(scene)
        #SSCTV.make_tv1(scene)
        SSCTV.make_sipk2(scene)
        #SSCTV.make_tv3(scene)

    @staticmethod
    def random_sipk1():
        pss = SSCTV.used_ps_str
        if len(pss) == 0:
            pss = SSCTV.get_random_ps(SSCTV.symbol_num)
            SSCTV.used_ps_str = pss
        print(pss)
        all_ps = SSCTV.get_all_ps_by_str(pss)
        SSCTV.print_sp_octave(all_ps)
        if not SSCTV.check_probabilities(all_ps): print("prb != 1")
        all_ps_copy = [ProbabilitySymbol.get_full_copy(ps) for ps in all_ps]
        m1 = SSCTV.get_message_20_by_str(SSCTV.m1, all_ps_copy)
        m2 = SSCTV.get_message_20_by_str(SSCTV.m2, all_ps_copy)
        m3 = SSCTV.get_message_20_by_str(SSCTV.m3, all_ps_copy)
        if len(m1) == 0:
            m1 = SSCTV.get_random_message_1(all_ps_copy, SSCTV.mess_symbol_num)
            m2 = SSCTV.get_random_message_2(all_ps_copy, SSCTV.mess_symbol_num)
            m3 = SSCTV.get_random_message_3(all_ps_copy, SSCTV.mess_symbol_num)
        SSCTV.m1 = SSCTV.print_message_20(m1, all_ps)
        SSCTV.m2 = SSCTV.print_message_20(m2, all_ps)
        SSCTV.m3 = SSCTV.print_message_20(m3, all_ps)

    @staticmethod
    def make_sipk1(scene: M.Scene):
        ps_full = SSCTV.sipk1_haffman(scene)
        SSCTV.make_pause(scene)
        SSCTV.sipk1_table_1(scene, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.sipk1_table_2(scene, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.sipk1_formula_1(scene, ps_full)
        SSCTV.make_pause(scene)
        m1 = SSCTV.get_message_20_by_str(SSCTV.m1, ps_full)
        m2 = SSCTV.get_message_20_by_str(SSCTV.m2, ps_full)
        m3 = SSCTV.get_message_20_by_str(SSCTV.m3, ps_full)
        SSCTV.sipk1_messages_20(scene, m1, m2, m3, True)
        SSCTV.sipk1_golomb(scene, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.sipk1_table_1(scene, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.sipk1_messages_20(scene, m1, m2, m3, True)
        num = SSCTV.sipk1_arithm(scene, SSCTV.m1, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.sipk1_arithm_table(scene, SSCTV.m1, ps_full)
        SSCTV.make_pause(scene)
        SSCTV.sipk1_count_1(scene, num)
        SSCTV.make_pause(scene)
        # SSCTV.sipk1_formula_2(scene)
        # SSCTV.make_pause(scene)
        # SSCTV.sipk1_formula_3(scene)
        # SSCTV.make_pause(scene)
        # SSCTV.sipk1_formula_4(scene)
        # SSCTV.make_pause(scene)
        # SSCTV.sipk1_formula_5(scene)
        # SSCTV.make_pause(scene)
        # SSCTV.sipk1_formula_6(scene)
        # SSCTV.make_pause(scene)
        SSCTV.sipk1_table_3(scene, SSCTV.table_data, SSCTV.entropy)
        SSCTV.make_pause(scene)

    @staticmethod
    def sipk1_haffman(scene: M.Scene):
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
    def sipk1_table_1(scene: M.Scene, all_ps: list):
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
    def sipk1_table_2(scene: M.Scene, all_ps: list):
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
    def sipk1_formula_1(scene: M.Scene, all_ps: list):
        from math import log2
        SSCTV.make_background(scene)
        SSCTV.entropy = sum([- log2(sym.probability) * sym.probability
                        for sym in all_ps])
        tx = r"H = - \sum_{i=1}^M p_i \cdot \log_2 p_i = " + str(
            round(SSCTV.entropy, 3))
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0).move_to(M.LEFT * 2.0)
        txt = M.Text("бит/символ", color = SSCTV.get_main_color(),
                     font_size = 40.0).next_to(tex)
        scene.add(tex, txt)

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
    def sipk1_messages_20(scene: M.Scene, m1: list, m2: list, m3: list,
                         add: bool = False):
        SSCTV.sipk1_message_20(scene, m1, True, add)
        SSCTV.make_pause(scene)
        SSCTV.sipk1_message_20(scene, m2, True, add)
        SSCTV.make_pause(scene)
        SSCTV.sipk1_message_20(scene, m3, True, add)
        SSCTV.make_pause(scene)

    @staticmethod
    def sipk1_message_20(scene: M.Scene, mess_ps: list,
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
    def sipk1_golomb(scene: M.Scene, all_ps: list):
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
    def sipk1_arithm(scene: M.Scene, mess_str: str, all_ps: list):
        def prb_size(cycle: int):
            if cycle <= 2: return 18.0
            elif cycle <= 4: return 16.0
            return 14.0

        left_side = M.LEFT * 6.6
        SSCTV.make_background(scene)
        mess_str = mess_str[:SSCTV.symbol_num_arithm]
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
                    ], 0.1, 2, SSCTV.get_main_color())
                ln2 = ZLine([
                    M.UP * 7.0 * (prb_line_old[g_indx + 1] - 0.5)
                    + left_side + M.RIGHT * horz_offset * cycle,
                    M.UP * 3.5
                    + left_side + M.RIGHT * horz_offset * (cycle + 1)
                    ], 0.1, 2, SSCTV.get_main_color())
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
    def sipk1_arithm_table(scene: M.Scene, mess_str: str, all_ps: list):
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
        num_symbols = 5
        mess_str = mess_str[:SSCTV.symbol_num_arithm]
        mes_len = len(mess_str)
        prb_line_old = SSCTV.get_prb_line(all_ps, 0.0)
        prb_line = SSCTV.get_prb_line(all_ps, 0.0)
        data = []
        in_file = 0
        in_file_old = 0
        pow_10 = 0
        pref_zeroes = 0
        for cycle in range(mes_len):
            g_indx = SSCTV.find_index_ps_by_symbol(
                mess_str[cycle], all_ps)
            p1, p2 = (prb_line[g_indx], prb_line[g_indx + 1])
            diff = p2 - p1
            for i in range(len(all_ps) + 1):
                prb_line[i] = p1 + prb_line_old[i] * diff
            p1_str_emp = str(round(p1 * 10 ** (num_symbols + pow_10)))
            p1_str = SSCTV.fill_zeros(p1_str_emp, num_symbols)
            p2_str_emp = str(round(p2 * 10 ** (num_symbols + pow_10)))
            p2_str = SSCTV.fill_zeros(p2_str_emp, num_symbols)
            pref = pop_prefix(p1_str, p2_str)
            if pref > in_file:
                if in_file == 0 and p2_str[0] == "0":
                    pref_zeroes += 1
                    if p2_str[1] == "0":
                        pref_zeroes += 1
                    in_file = pref
                    pow_10 = pref
                else:
                    in_file = pref
                    pow_10 = pref
            if pref_zeroes > 0 and in_file_old > 0:
                in_file_old -= pref_zeroes
                pow_10 += pref_zeroes
                pref_zeroes = 0
            in_file_str = p1_str[in_file_old : in_file]
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
        fs = 24.0
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
    def sipk1_count_1(scene: M.Scene, num: str):
        SSCTV.make_background(scene)
        t = num + r"_{10} = "
        bin_s = ""
        if num[0] == "0":
            bin_s += "0"
            if num[1] == "0":
                bin_s += "0"
        bin_s += bin(int(num))[2:]
        t += bin_s + r"_2"
        show = M.MathTex(t, color = SSCTV.get_main_color(),
                         font_size = 54.0).move_to(2.0 * M.UP)
        bit = r"Всего бит = " + str(len(bin_s))
        sym = r"Всего символов = " + str(SSCTV.symbol_num_arithm)
        bit_sym = r"Бит на символ = " + str(round(
            len(bin_s) / SSCTV.symbol_num_arithm, 3))
        b = M.Text(bit, color = SSCTV.get_main_color())
        s = M.Text(sym, color = SSCTV.get_main_color()).next_to(b, M.DOWN)
        bs = M.Text(bit_sym, color = SSCTV.get_main_color()).next_to(s, M.DOWN)
        scene.add(show, b, s, bs)

    @staticmethod
    def sipk1_formula_2(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"I_s = log_2 M"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0)
        scene.add(tex)

    @staticmethod
    def sipk1_formula_3(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"H = - \sum_{i=1}^M p_i \cdot \log_2 p_i"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0)
        scene.add(tex)

    @staticmethod
    def sipk1_formula_4(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"R = \log_2 M - H"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0)
        scene.add(tex)

    @staticmethod
    def sipk1_formula_5(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"H \le n_{cp} \le H + 1"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0)
        scene.add(tex)

    @staticmethod
    def sipk1_formula_6(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"R_c = L_{cp} - H"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 54.0)
        scene.add(tex)

    @staticmethod
    def sipk1_table_3(scene: M.Scene, data: list, H: float):
        SSCTV.make_background(scene)
        fs = 24.0
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
                M.Text("Сообщение №1", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Сообщение №2",
                       font_size = fs, color = SSCTV.get_main_color()),
                M.Text("Сообщение №3",
                       font_size = fs, color = SSCTV.get_main_color()),
                M.Text("Cреднее значение\nбит на символ", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Избыточность", font_size = fs,
                       color = SSCTV.get_main_color())
                ],
            col_labels = [
                M.Text("Код\nХаффмана", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Код\nГоломба", font_size = fs,
                       color = SSCTV.get_main_color()),
                M.Text("Арифметический\nкод", font_size = fs,
                       color = SSCTV.get_main_color())
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
    def make_tv1(scene: M.Scene):
        key = SSCTV.fill_zeros(bin(int(SSCTV.tv_var))[2:], 4)
        psp_str = SSCTV.tv1_table_1(scene, key)
        SSCTV.make_pause(scene)
        in_str = SSCTV.tv1_in_str
        if len(in_str) == 0:
            in_str = SSCTV.tv1_get_random_in_str(15)
        data01 = SSCTV.tv1_table_2(scene, in_str, psp_str)
        SSCTV.make_pause(scene)
        SSCTV.tv1_text_1(scene, data01)
        SSCTV.make_pause(scene)
        SSCTV.tv1_text_2(scene)
        SSCTV.make_pause(scene)

    @staticmethod
    def tv1_table_1(scene: M.Scene, key: str):
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
    def tv1_table_2(scene: M.Scene, in_str: str, psp_str: str):
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
    def tv1_text_1(scene: M.Scene, data01):
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
    def tv1_text_2(scene: M.Scene):
        SSCTV.make_background(scene)
        dict_vars = {1: 101, 2: 1542, 3: 3160, 4: 4422, 5: 15214,
                     6: 26700, 7: 37120, 8: 52642, 9: 48592, 10: 59306,
                     11: 61085, 12: 7706, 13: 11490, 14: 32084, 15: 41056}
        bit = dict_vars[SSCTV.tv_var]
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

    @staticmethod
    def sipk2_graph_by_cffs(cffs: list):
        from math import sin
        return (lambda x:
                cffs[0][0] * sin(cffs[0][1] * x + cffs[0][2])
                + cffs[1][0] * sin(cffs[1][1] * x + cffs[1][2])
                + cffs[2][0] * sin(cffs[2][1] * x + cffs[2][2])
                + cffs[3][0] * sin(cffs[3][1] * x + cffs[3][2]))

    @staticmethod
    def sipk2_random_graph_cffs():
        ret = []
        for i in range(4):
            sin_a = round((random.random() - 0.5) * (10.0 - 2.0 * i), 3)
            sin_f = round((random.random() - 0.5) * (1.0 + i), 3)
            sin_p = round(random.random() * 7.0, 3)
            ret.append([sin_a, sin_f, sin_p])
        print(ret)
        return ret

    @staticmethod
    def sipk2_scale_center_graph(graph, Nver: int = 0, Nhor: int = 0):
        accuracy: int = 10
        if Nver == 0: Nver = SSCTV.sipk2_Nver
        if Nhor == 0: Nhor = SSCTV.sipk2_Nhor
        min_g = 100.0
        max_g = - 100.0
        for i in range(Nhor):
            for j in range(accuracy):
                y = graph(i + j / accuracy)
                min_g = min(min_g, y)
                max_g = max(max_g, y)
        amp = Nver / abs(max_g - min_g) * 0.98
        corr_vert = (max_g + min_g) * 0.5
        return lambda x: (graph(x) - corr_vert) * amp + Nver * 0.5

    @staticmethod
    def make_sipk2(scene: M.Scene):
        repetitions = 1
        for _ in range(repetitions):
            SSCTV.sipk2_num_plane(scene)
            SSCTV.make_pause(scene)
            SSCTV.sipk2_table_1(scene)
            SSCTV.make_pause(scene)
            SSCTV.sipk2_table_2(scene, SSCTV.sipk2_x_n, "x")
            SSCTV.make_pause(scene)
            SSCTV.sipk2_table_2(scene, SSCTV.sipk2_e1, "e_1")
            SSCTV.make_pause(scene)
            SSCTV.sipk2_table_2(scene, SSCTV.sipk2_e2, "e_2")
            SSCTV.make_pause(scene)
            SSCTV.sipk2_table_2(scene, SSCTV.sipk2_e2_opt, "e_{2opt}")
            SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_1(scene)
            # SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_2(scene)
            # SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_3(scene)
            # SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_4(scene)
            # SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_5(scene)
            # SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_6(scene)
            # SSCTV.make_pause(scene)
            SSCTV.sipk2_formula_7(scene)
            SSCTV.make_pause(scene)
            SSCTV.sipk2_formula_8(scene)
            SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_9(scene)
            # SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_10(scene)
            # SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_11(scene)
            # SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_12(scene)
            # SSCTV.make_pause(scene)
            # SSCTV.sipk2_formula_13(scene)
            # SSCTV.make_pause(scene)
            SSCTV.sipk2_Nhor = random.randint(24, 26)
            SSCTV.sipk2_Nver = random.randint(20, 30)

    @staticmethod
    def sipk2_num_plane(scene: M.Scene):
        SSCTV.make_background(scene)
        number_plane = M.NumberPlane(
            x_range = (0, SSCTV.sipk2_Nhor, 1),
            y_range = (0, SSCTV.sipk2_Nver, 1),
            x_length = 13.0,
            y_length = 7.0,
            color = SSCTV.get_main_color(),
            axis_config = {
                "numbers_to_include": M.np.arange(0, SSCTV.sipk2_Nhor + 1, 1),
                "font_size": 18.0,
                "stroke_width": 3,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": 0.11,
                "label_direction": M.DOWN,
                "color": SSCTV.get_main_color(),
                },
            y_axis_config = {
                "numbers_to_include": M.np.arange(0, SSCTV.sipk2_Nver + 1, 1),
                "label_direction": M.LEFT},
            background_line_style = {
                "stroke_color": SSCTV.get_main_color(),
                "stroke_width": 2,
                "stroke_opacity": 0.5,
                },
            tips = False,
            )
        number_plane.get_axes().set_color(SSCTV.get_main_color())
        graphs = M.VGroup()
        gr = SSCTV.sipk2_cffs
        if len(gr) == 0: gr = SSCTV.sipk2_random_graph_cffs()
        gr = SSCTV.sipk2_scale_center_graph(SSCTV.sipk2_graph_by_cffs(gr))
        graphs += number_plane.plot(
            gr, x_range = (0, SSCTV.sipk2_Nhor, 0.1),
            color = SSCTV.get_main_color(), use_smoothing = False)
        x_n = []
        for i in range(SSCTV.sipk2_Nhor + 1):
            graphs += M.Dot(number_plane.c2p(i, round(gr(i)), 0), 0.05,
                            color = SSCTV.get_main_color())
            x_n.append(round(gr(i)))
        SSCTV.sipk2_x_n = x_n
        scene.add(number_plane, graphs)

    @staticmethod
    def sipk2_table_1(scene: M.Scene):
        SSCTV.make_background(scene)
        x_n_1: int = 0
        x_n_2: int = 0
        sum_x_x1_n1 = 0
        sum_x1_x1_n1 = 0
        sum_x_x1_n2 = 0
        sum_x_x2_n2 = 0
        sum_x1_x2_n2 = 0
        sum_x1_x1_n2 = 0
        sum_x2_x2_n2 = 0
        for i in range(len(SSCTV.sipk2_x_n)):
            sum_x_x1_n1 += SSCTV.sipk2_x_n[i] * x_n_1
            sum_x1_x1_n1 += x_n_1 * x_n_1
            if i >= 2:
                sum_x_x1_n2 += SSCTV.sipk2_x_n[i] * x_n_1
                sum_x_x2_n2 += SSCTV.sipk2_x_n[i] * x_n_2
                sum_x1_x2_n2 += x_n_1 * x_n_2
                sum_x1_x1_n2 += x_n_1 * x_n_1
                sum_x2_x2_n2 += x_n_2 * x_n_2
            x_n_2 = x_n_1
            x_n_1 = SSCTV.sipk2_x_n[i]
        SSCTV.sipk2_a22 = ((sum_x_x2_n2 * sum_x1_x1_n2 - sum_x_x1_n2 * sum_x1_x2_n2)
               / (sum_x2_x2_n2 * sum_x1_x1_n2 - sum_x1_x2_n2 * sum_x1_x2_n2))
        SSCTV.sipk2_a21 = ((sum_x_x1_n2 - SSCTV.sipk2_a22 * sum_x1_x2_n2)
                           / sum_x1_x1_n2)
        SSCTV.sipk2_a1 = sum_x_x1_n1 / sum_x1_x1_n1
        SSCTV.sipk2_sum_x_x1_n1 = sum_x_x1_n1
        SSCTV.sipk2_sum_x1_x1_n1 = sum_x1_x1_n1
        SSCTV.sipk2_sum_x_x1_n2 = sum_x_x1_n2
        SSCTV.sipk2_sum_x_x2_n2 = sum_x_x2_n2
        SSCTV.sipk2_sum_x1_x2_n2 = sum_x1_x2_n2
        SSCTV.sipk2_sum_x1_x1_n2 = sum_x1_x1_n2
        SSCTV.sipk2_sum_x2_x2_n2 = sum_x2_x2_n2
        table_data = []
        x_n_1 = 0
        x_n_2 = 0
        y_n_1 = 0
        y_n_2 = 0
        SSCTV.sipk2_e1.clear()
        SSCTV.sipk2_e2.clear()
        SSCTV.sipk2_e2_opt.clear()
        highlighted = []
        for i in range(len(SSCTV.sipk2_x_n)):
            p1 = x_n_1
            p2 = 2 * x_n_1 - x_n_2
            p2_opt = round(SSCTV.sipk2_a21 * x_n_1 + SSCTV.sipk2_a22 * x_n_2)
            if i == 1:
                p2 = x_n_1
                p2_opt = x_n_1
            if p2 != p2_opt: highlighted.append((9, 2 + i))
            e1 = SSCTV.sipk2_x_n[i] - p1
            e2 = SSCTV.sipk2_x_n[i] - p2
            e2_opt = SSCTV.sipk2_x_n[i] - p2_opt
            y1 = y_n_1 + e1
            y2 = 2 * y_n_1 - y_n_2 + e2
            if i == 1: y2 = y_n_1 + e2
            table_data.append([str(i), str(SSCTV.sipk2_x_n[i]),
                               str(p1), str(e1), str(y1),
                               str(p2), str(e2), str(y2),
                               str(p2_opt), str(e2_opt),
                               ])
            y_n_2 = y_n_1
            y_n_1 = y1
            x_n_2 = x_n_1
            x_n_1 = SSCTV.sipk2_x_n[i]
            SSCTV.sipk2_e1.append(e1)
            SSCTV.sipk2_e2.append(e2)
            SSCTV.sipk2_e2_opt.append(e2_opt)
        table_data = SSCTV.transpose_list(table_data)
        fs = 14.0
        table = Table(
            table_data,
            row_labels = [
                M.MathTex("n", color = SSCTV.get_main_color(), font_size = 24.0),
                M.MathTex("x(n)", color = SSCTV.get_main_color(),
                          font_size = 24.0),
                M.MathTex("p_1(n)", color = SSCTV.get_main_color(),
                          font_size = 24.0),
                M.MathTex("e_1(n)", color = SSCTV.get_main_color(),
                          font_size = 24.0),
                M.MathTex("y_1(n)", color = SSCTV.get_main_color(),
                          font_size = 24.0),
                M.MathTex("p_2(n)", color = SSCTV.get_main_color(),
                          font_size = 24.0),
                M.MathTex("e_2(n)", color = SSCTV.get_main_color(),
                          font_size = 24.0),
                M.MathTex("y_2(n)", color = SSCTV.get_main_color(),
                          font_size = 24.0),
                M.MathTex("p_{2opt}(n)", color = SSCTV.get_main_color(),
                          font_size = 24.0),
                M.MathTex("e_{2opt}(n)", color = SSCTV.get_main_color(),
                          font_size = 24.0),
                ],
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.3,
            element_to_mobject_config = {
                "font_size": fs,
                "color": SSCTV.get_main_color()},
            line_config = {"color": SSCTV.get_main_color()}
            ).next_to(M.UP * 3.8, M.DOWN)
        for cell in highlighted:
            table.add_highlighted_cell(cell, color = "#999999")
        scene.add(table)

    @staticmethod
    def sipk2_table_2(scene: M.Scene, data: list, X: str):
        from math import log2
        SSCTV.make_background(scene)
        table_data = []
        data_dict = {}
        data.sort()
        for i in range(len(data)):
            if data[i] not in data_dict:
                data_dict[data[i]] = 1
            else:
                data_dict[data[i]] += 1
        SSCTV.entropy = 0.0
        for i in data_dict:
            pb = data_dict[i] / len(data)
            table_data.append([str(i),
                               str(data_dict[i]),
                               str(round(pb, 3)),
                               str(- round(log2(pb), 3)),
                               str(- round(log2(pb) * pb, 3)),
                               ])
            SSCTV.entropy += - log2(pb) * pb
        table_data = SSCTV.transpose_list(table_data)
        fs = 14.0
        table = Table(
            table_data,
            row_labels = [
                M.MathTex(
                    f"{X}", color = SSCTV.get_main_color(),
                    font_size = 24.0),
                M.MathTex(
                    f"N({X})", color = SSCTV.get_main_color(),
                    font_size = 24.0),
                M.MathTex(
                    f"p({X})", color = SSCTV.get_main_color(),
                    font_size = 24.0),    
                M.MathTex(r"-\log_2 p(" + X + r")",
                          color = SSCTV.get_main_color(), font_size = 24.0),
                M.MathTex(r"-p(" + X + r") \cdot \log_2 p(" + X + r")",
                          color = SSCTV.get_main_color(), font_size = 24.0),
                ],
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.3,
            element_to_mobject_config = {
                "font_size": fs,
                "color": SSCTV.get_main_color()},
            line_config = {"color": SSCTV.get_main_color()}
            ).next_to(M.UP * 3.8, M.DOWN)
        tx = r"H = - \sum_{i=1}^M p_i \cdot \log_2 p_i = " + str(
            round(SSCTV.entropy, 3))
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(table, M.DOWN)
        txt = M.Text("бит/символ", color = SSCTV.get_main_color(),
                     font_size = 30.0)
        tex.shift(M.LEFT * txt.width * 0.5)
        txt.next_to(tex)
        scene.add(table, tex, txt)

    @staticmethod
    def sipk2_formula_1(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"E = \overline{s^2(n)} = \overline{\left["
        tx += r"x(n) - \sum_{m=1}^M a_m x(n-m) \right]^2}"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        tx2 = r"\frac{\partial E}{\partial a_i} = \overline{2 \left["
        tx2 += r"x(n) - \sum_{m=1}^M a_m x(n-m) \right] x(n-m)} = 0;\ "
        tx2 += r"i = 1, \ldots , M"
        tex2 = M.MathTex(tx2, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex, M.DOWN)
        tx3 = r"\sum_{m=1}^M a_m R(i,m) = R(m,0);\ "
        tx3 += r"i = 1, \ldots , M"
        tex3 = M.MathTex(tx3, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)

    @staticmethod
    def sipk2_formula_2(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"E_1 = \overline{\left[x(n) - a_1 x(n-1) \right]^2}"
        tx += r" = \frac 1 N \sum_{n=1}^N [x(n) - a_1 x(n-1) \right]^2"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        tx2 = r"E_2 = \overline{\left[x(n) - a_{21} x(n-1) "
        tx2 += r"- a_{22} x(n-2) \right]^2} ="
        tex2 = M.MathTex(tx2, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex, M.DOWN)
        tx3 = r"= \frac 1 {N-1} \sum_{n=2}^N \left[x(n) - a_{21} x(n-1)"
        tx3 += r" - a_{22} x(n-2) \right]^2"
        tex3 = M.MathTex(tx3, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)

    @staticmethod
    def sipk2_formula_3(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"\frac{\partial E_1}{\partial a_1} = "
        tx += r"\frac {-2} N \sum_{n=1}^N \big(\left[x(n) - "
        tx += r"a_1 x(n-1) \right] x(n-1) \big) = 0"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        tx2 = r"\frac{\partial E_2}{\partial a_{21}} = "
        tx2 += r"\frac {-2} {N-1} \sum_{n=2}^N \big(\left[x(n) - "
        tx2 += r"a_{21} x(n-1) - a_{22} x(n-2) \right] x(n-1) \big) = 0"
        tex2 = M.MathTex(tx2, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex, M.DOWN)
        tx3 = r"\frac{\partial E_2}{\partial a_{22}} = "
        tx3 += r"\frac {-2} {N-1} \sum_{n=2}^N \big(\left[x(n) - "
        tx3 += r"a_{21} x(n-1) - a_{22} x(n-2) \right] x(n-2) \big) = 0"
        tex3 = M.MathTex(tx3, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)

    @staticmethod
    def sipk2_formula_4(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"\frac{\partial E_1}{\partial a_1} = "
        tx += r"\frac {-2} N \sum_{n=1}^N \big(x(n) x(n-1) - "
        tx += r"a_1 (x(n-1))^2 \big) = 0"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        tx2 = r"\frac{\partial E_2}{\partial a_{21}} = "
        tx2 += r"\frac {-2} {N-1} \sum_{n=2}^N \big(x(n) x(n-1) - "
        tx2 += r"a_{21} (x(n-1))^2 - a_{22} x(n-2) x(n-1)\big) = 0"
        tex2 = M.MathTex(tx2, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex, M.DOWN)
        tx3 = r"\frac{\partial E_2}{\partial a_{22}} = "
        tx3 += r"\frac {-2} {N-1} \sum_{n=2}^N \big(x(n) x(n-2) - "
        tx3 += r"a_{21} x(n-1) x(n-2) - a_{22} (x(n-2))^2 \big) = 0"
        tex3 = M.MathTex(tx3, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)

    @staticmethod
    def sipk2_formula_5(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"\sum_{n=1}^N x(n) x(n-1) - "
        tx += r"a_1 \sum_{n=1}^N (x(n-1))^2 = 0"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        tx2 = r"\sum_{n=2}^N x(n) x(n-1) - "
        tx2 += r"a_{21} \sum_{n=2}^N (x(n-1))^2 -"
        tex2 = M.MathTex(tx2, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex, M.DOWN)
        tx22 = r"- a_{22} \sum_{n=2}^N x(n-2) x(n-1) = 0"
        tex22 = M.MathTex(tx22, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex2, M.DOWN)
        tx3 = r"\sum_{n=2}^N x(n) x(n-2) - "
        tx3 += r"a_{21} \sum_{n=2}^N x(n-1) x(n-2) -"
        tex3 = M.MathTex(tx3, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex22, M.DOWN)
        tx32 = r"- a_{22} \sum_{n=2}^N (x(n-2))^2 = 0"
        tex32 = M.MathTex(tx32, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex3, M.DOWN)
        scene.add(tex, tex2, tex3, tex22, tex32)

    @staticmethod
    def sipk2_formula_6(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"a_1 = \frac {\sum_{n=1}^N x(n) x(n-1)}"
        tx += r"{\sum_{n=1}^N (x(n-1))^2}"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        tx2 = r"a_{21} = \frac {\sum_{n=2}^N x(n) x(n-1) - "
        tx2 += r"a_{22} \sum_{n=2}^N x(n-2) x(n-1)}"
        tx2 += r"{\sum_{n=2}^N (x(n-1))^2}"
        tex2 = M.MathTex(tx2, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex, M.DOWN)
        tx3 = r"a_{22} = \frac {\sum_{n=2}^N x(n) x(n-2) - "
        tx3 += r"a_{21} \sum_{n=2}^N x(n-1) x(n-2)}"
        tx3 += r"{\sum_{n=2}^N (x(n-2))^2}"
        tex3 = M.MathTex(tx3, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)

    @staticmethod
    def sipk2_formula_7(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"a_1 = " + str(round(SSCTV.sipk2_a1, 3))
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        more_less = " меньше"
        if 1.0 - SSCTV.sipk2_a1 < 0.0: more_less = " больше"
        tx2 = "на " + str(round(
            abs(100.0 * (1.0 - SSCTV.sipk2_a1)), 1)) + "%" + more_less
        tex2 = M.Text(tx2, color = SSCTV.get_main_color(),
                     font_size = 36.0).next_to(tex, M.DOWN)
        scene.add(tex, tex2)

    @staticmethod
    def sipk2_formula_8(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"a_{21} = " + str(round(SSCTV.sipk2_a21, 3))
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        more_less = " меньше"
        if 2.0 - SSCTV.sipk2_a21 < 0.0: more_less = " больше"
        tx2 = "на " + str(round(
            abs(100.0 * (1.0 - SSCTV.sipk2_a21 * 0.5)), 1)) + "%" + more_less
        tex2 = M.Text(tx2, color = SSCTV.get_main_color(),
                     font_size = 36.0).next_to(tex, M.DOWN)
        tx3 = r"a_{22} = " + str(round(SSCTV.sipk2_a22, 3))
        tex3 = M.MathTex(tx3, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(tex2, M.DOWN)
        more_less = " меньше"
        if -1.0 - SSCTV.sipk2_a22 > 0.0: more_less = " больше"
        tx4 = "на " + str(round(
            abs(100.0 * (1.0 + SSCTV.sipk2_a22)), 1)) + "%" + more_less
        tex4 = M.Text(tx4, color = SSCTV.get_main_color(),
                     font_size = 36.0).next_to(tex3, M.DOWN)
        scene.add(tex, tex2, tex3, tex4)

    @staticmethod
    def sipk2_formula_9(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"H(X_1, X_2) = - \sum_{i=1}^M \sum_{j=1}^M "
        tx += r"p(x_i, x_j) \cdot \log_2 p(x_i, x_j)"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        scene.add(tex)

    @staticmethod
    def sipk2_formula_10(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"p(n) = \sum_{m=1}^M a_m x(n - m)"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        scene.add(tex)

    @staticmethod
    def sipk2_formula_11(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"f_1 = \sum_{n=2}^N x(n) x(n-1);\ f_2 = \sum_{n=2}^N x(n) x(n-2);"
        tx2 = r"f_{11} = \sum_{n=2}^N (x(n-1))^2;"
        tx2 += r"\ f_{22} = \sum_{n=2}^N (x(n-2))^2;"
        tx3 = r"f_{12} = \sum_{n=2}^N x(n-1) x(n-2)"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        tex2 = M.MathTex(tx2, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex, M.DOWN)
        tex3 = M.MathTex(tx3, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)

    @staticmethod
    def sipk2_formula_12(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"a_{21} = \frac {f_1 - a_{22} f_{12}}{f_{11}}"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = SSCTV.sipk2_texsize).next_to(M.UP * 3.8, M.DOWN)
        tx2 = r"a_{22} = \frac {f_2 - a_{21} f_{12}}{f_{22}}"
        tex2 = M.MathTex(tx2, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex, M.DOWN)
        tx3 = r"a_{22} = \frac {f_2 - (\frac {f_1 - a_{22} f_{12}}{f_{11}}) "
        tx3 += r"f_{12}}{f_{22}}"
        tex3 = M.MathTex(tx3, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex2, M.DOWN)
        tx4 = r"a_{22} f_{22} = f_2 - \frac {f_1 f_{12} - a_{22} f_{12}^2}{f_{11}}"
        tex4 = M.MathTex(tx4, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex3, M.DOWN)
        tx5 = r"a_{22} f_{22} f_{11} = f_2 f_{11} - f_1 f_{12} + a_{22} f_{12}^2"
        tex5 = M.MathTex(tx5, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex4, M.DOWN)
        tx6 = r"a_{22} = \frac {f_2 f_{11} - f_1 f_{12}}{f_{22} f_{11} - f_{12}^2}"
        tex6 = M.MathTex(tx6, color = SSCTV.get_main_color(),
                         font_size = SSCTV.sipk2_texsize).next_to(tex5, M.DOWN)
        scene.add(tex, tex2, tex3, tex4, tex5, tex6)

    @staticmethod
    def sipk2_formula_13(scene: M.Scene):
        SSCTV.make_background(scene)
        tx = r"a_{21} = \frac {\sum_{n=2}^N x(n) x(n-1) - "
        tx += r"a_{22} \sum_{n=2}^N x(n-2) x(n-1)}"
        tx += r"{\sum_{n=2}^N (x(n-1))^2}"
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 30.0).next_to(M.UP * 3.8, M.DOWN)
        tx2 = r"a_{22} = \frac {(\sum_{n=2}^N x(n) x(n-2))"
        tx2 += r"(\sum_{n=2}^N (x(n-1))^2) - "
        tx2 += r"(\sum_{n=2}^N x(n) x(n-1))"
        tx2 += r"(\sum_{n=2}^N x(n-1) x(n-2))}"
        tx2 += r"{(\sum_{n=2}^N (x(n-2))^2)"
        tx2 += r"{(\sum_{n=2}^N (x(n-1))^2) - "
        tx2 += r"(\sum_{n=2}^N x(n-1) x(n-2))^2}"
        tex2 = M.MathTex(tx2, color = SSCTV.get_main_color(),
                        font_size = 30.0).next_to(tex, M.DOWN)
        tx3 = r"\left\{ \frac {\frac {\displaystyle \sum_{n=2}^N}{ \sum_{n=2}^N}}"
        tx3 += r"{\displaystyle \sum_{n=2}^N} \right\}"
        tex3 = M.MathTex(tx3, color = SSCTV.get_main_color(),
                        font_size = 30.0).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)

    @staticmethod
    def tv3_sigmoid(x: float):
        from math import exp
        return 1.0 / (1.0 + exp(- x))

    @staticmethod
    def tv3_restrict_func_value(
        func_value: float, x: float, left: float, right: float,
        left_border: bool = False, right_border: bool = False):
        if (x > right or x < left
            or (x == right and right_border)
            or (x == left and left_border)):
            return 0.0
        else:
            return func_value

    @staticmethod
    def tv3_func_part_by_2_bits(bits: str, part: int):
        fall = 25.0
        amp = 2.0
        if bits[0] == "0" and bits[1] == "0":
            return lambda x: - 1.0
        elif bits[0] == "1" and bits[1] == "1":
            return lambda x: 1.0
        elif bits[0] == "0" and bits[1] == "1":
            if part == 1: return lambda x: SSCTV.tv3_sigmoid(x * fall) * amp - 1.0
            else: return lambda x: SSCTV.tv3_sigmoid((1.0 - x) * fall) * - amp + 1.0
        elif bits[0] == "1" and bits[1] == "0":
            if part == 1: return lambda x: SSCTV.tv3_sigmoid(x * fall) * - amp + 1.0
            else: return lambda x: SSCTV.tv3_sigmoid((1.0 - x) * fall) * amp - 1.0

    @staticmethod
    def tv3_func_by_3_bits(bits: str):
        part_1 = SSCTV.tv3_func_part_by_2_bits(bits[:2], 1)
        part_2 = SSCTV.tv3_func_part_by_2_bits(bits[1:], 2)
        return lambda x: (
            SSCTV.tv3_restrict_func_value(part_1(x), x, 0.0, 0.5)
            + SSCTV.tv3_restrict_func_value(part_2(x), x, 0.5, 1.0))

    @staticmethod
    def make_tv3(scene: M.Scene):
        SSCTV.tv3_diagram(scene)
        SSCTV.make_pause(scene)
        SSCTV.tv3_eye_diagram(scene)
        SSCTV.make_pause(scene)

    @staticmethod
    def tv3_diagram(scene: M.Scene):
        SSCTV.make_background(scene)
        dict_vars = {1: "011010010101", 2: "110001011011", 3: "010110100101",
                     4: "100111010100", 5: "001110101100", 6: "111000101001",
                     7: "001101001110", 8: "101100100110", 9: "010100111001",
                     10: "110011000110", 11: "011100100110", 12: "110110001010",
                     13: "010111001101", 14: "100110001011", 15: "011000111010"}
        bit = dict_vars[SSCTV.tv_var]
        number_plane = M.NumberPlane(
            x_range = (0, 12, 1),
            y_range = (-2, 2, 1),
            x_length = 13.0,
            y_length = 4.0,
            color = SSCTV.get_main_color(),
            axis_config = {
                "numbers_to_include": M.np.arange(0, 12, 1),
                "font_size": 18.0,
                "stroke_width": 3,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": 0.11,
                "label_direction": M.DR,
                "color": SSCTV.get_main_color(),
                },
            y_axis_config = {
                "numbers_to_include": M.np.arange(-1, 2, 1),
                "label_direction": M.LEFT},
            background_line_style = {
                "stroke_color": SSCTV.get_main_color(),
                "stroke_width": 1,
                "stroke_opacity": 0.5,
                },
            tips = False,
            ).next_to(M.UP * 3.8, M.DOWN)
        number_plane.get_axes().set_color(SSCTV.get_main_color())
        graphs = M.VGroup()
        for i in range(len(bit) // 2):
            graphs += M.Text(
                str(i + 1), font_size = 30.0,
                color = SSCTV.get_main_color()).next_to(
                    number_plane.c2p(1.0 + i * 2.0, 1.2, 0.0), M.UP)
        prev_bit = ""
        next_bit = ""
        for i in range(len(bit)):
            if i == 0: prev_bit = bit[i]
            else: prev_bit = bit[i - 1]
            if i == len(bit) - 1: next_bit = bit[i]
            else: next_bit = bit[i + 1]
            graphs += number_plane.plot(
                lambda x: SSCTV.tv3_func_by_3_bits(
                    prev_bit + bit[i] + next_bit)(x - i),
                x_range = (i, i + 1.0, 0.0199),
                color = SSCTV.get_main_color(),
                use_smoothing = False)
        scene.add(number_plane, graphs)

    @staticmethod
    def tv3_eye_diagram(scene: M.Scene):
        SSCTV.make_background(scene)
        dict_vars = {1: "011010010101", 2: "110001011011", 3: "010110100101",
                     4: "100111010100", 5: "001110101100", 6: "111000101001",
                     7: "001101001110", 8: "101100100110", 9: "010100111001",
                     10: "110011000110", 11: "011100100110", 12: "110110001010",
                     13: "010111001101", 14: "100110001011", 15: "011000111010"}
        dict_colors = {1: M.DARK_BROWN, 2: M.TEAL, 3: M.RED_D,
                       4: M.ORANGE, 5: M.YELLOW, 6: M.DARK_BLUE}
        dict_stroke_widths = {1: 28, 2: 23, 3: 18, 4: 13, 5: 8, 6: 3}
        bit = dict_vars[SSCTV.tv_var]
        number_plane = M.NumberPlane(
            x_range = (0, 17, 1),
            y_range = (-3, 3, 1),
            x_length = 13.0,
            y_length = 5.0,
            color = SSCTV.get_main_color(),
            axis_config = {"stroke_width": 0},
            background_line_style = {"stroke_width": 0}
            ).next_to(M.UP * 3.3, M.DOWN)
        graphs = M.VGroup()
        offset = 0.0
        for i in range(len(bit) // 2):
            graphs += M.Text(str(i + 1),
                             font_size = 30.0,
                             color = SSCTV.get_main_color()
                             ).next_to(number_plane.c2p(1.0 + i * 3.0, 3.1, 0.0), M.UP)
        for i in range(len(bit)):
            if i == 0: prev_bit = bit[i]
            else: prev_bit = bit[i - 1]
            if i == len(bit) - 1: next_bit = bit[i]
            else: next_bit = bit[i + 1]
            graphs += number_plane.plot(
                lambda x: 2.0 + SSCTV.tv3_func_by_3_bits(
                    prev_bit + bit[i] + next_bit)(x - i - offset),
                x_range = (i + offset, i + offset + 1.0, 0.0199),
                color = SSCTV.get_main_color(),
                use_smoothing = False)
            offset_inner = 0.0
            for j in range((len(bit) - i + 1) // 2):
                graphs += number_plane.plot(
                    lambda x: - 1.0 + SSCTV.tv3_func_by_3_bits(
                        prev_bit + bit[i] + next_bit
                        )(x - i - offset_inner - offset),
                    x_range = (i + offset_inner + offset,
                               i + offset_inner + offset + 1.0, 0.0199),
                    use_smoothing = False,
                    stroke_width = 1 + dict_stroke_widths[i // 2 + 1],
                    background_stroke_width = 3 + dict_stroke_widths[i // 2 + 1],
                    stroke_color = dict_colors[i // 2 + 1])
                offset_inner += 3.0
            if i % 2 == 1 and i != 0:
                offset += 1.0
        scene.add(number_plane, graphs)


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

    promo_codes = [("o27739521", 90, True),
                   ("o63116012", 50, False),
                   ("o86636403", 25, False),
                   ("o15260943", 10, False),
                   ("t72539756", 20, False),
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
