import manim as M
import random
import SIPK_SSCTV_functions as SSf


class SIPK(object):
    """SIPK"""

    EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    en = "abcdefghijklmnopqrstuvwxyz"
    RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    sipk1_ps_str = ""
    sipk1_m1 = ""
    sipk1_m2 = ""
    sipk1_m3 = ""
    sipk1_entropy = 0.0
    sipk1_table_data = []
    sipk1_all_symbol_num = 8
    sipk1_symbol_num_arithm = 6
    sipk1_mess_all_symbol_num = 22
    sipk1_mean_bit_over_symb1 = round(1.0 / sipk1_mess_all_symbol_num, 3)
    sipk1_mean_bit_over_symb2 = round(1.0 / sipk1_mess_all_symbol_num, 3)
    sipk1_mean_bit_over_symb3 = round(1.0 / sipk1_mess_all_symbol_num, 3)
    sipk1_PRB_NUM: int = 2
    sipk1_UL = M.LEFT * 5.5 + M.UP * 3.5

    sipk2_Nhor = 24
    sipk2_Nver = 24
    sipk2_x_n = []
    sipk2_cffs = []
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
    sipk2_decode_n = [3, 12, 24]

    sipk3_R = 0.85
    sipk3_t = 3

    @staticmethod
    def get_all_ps_by_str(text: str):
        ret = []
        for ch_p in text.split():
            symbol = ch_p[0]
            probability = ch_p[1:]
            SIPK.sipk1_PRB_NUM = max(SIPK.sipk1_PRB_NUM, len(probability) - 2)
            ret.append(ProbabilitySymbol(symbol, probability, False, ""))
        return ret

    @staticmethod
    def check_probabilities(all_ps: list):
        p = 0.0
        for ps in all_ps:
            p += ps.probability
        return round(p, SIPK.sipk1_PRB_NUM) == 1.0

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
            ret[pbi] = round(ret[pbi] / sm, SIPK.sipk1_PRB_NUM)
            if ret[pbi] <= 0.0001: ret[pbi] = 0.01
        return ret

    @staticmethod
    def get_random_ps(n: int):
        pb = [0.1]
        while abs(sum(pb) - 1.0) > 0.005:
            pb = SIPK.get_random_probabilities(n)
        sm = SIPK.get_random_symbols(n, SIPK.en)
        data = []
        for i in range(len(pb)):
            data.append(sm[i] + str(round(pb[i], SIPK.sipk1_PRB_NUM)))
        return " ".join(data)

    @staticmethod
    def find_ps_by_symbol(symbol: str, all_ps: list):
        for ps in all_ps:
            if ps.symbol == symbol:
                return ps

    @staticmethod
    def find_index_ps_by_symbol(symbol: str, all_ps: list):
        for i in range(len(all_ps)):
            if all_ps[i].symbol == symbol:
                return i

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
    def print_sp_octave(all_ps: list):
        syms = []
        prbs = []
        for i in range(len(all_ps)):
            syms.append(all_ps[i].symbol)
            prbs.append(str(round(
                all_ps[i].probability * 10 ** SIPK.sipk1_PRB_NUM)))
        print(", ".join(syms))
        print(", ".join(prbs))

    @staticmethod
    def print_message_20(mess_ps: list, compare_to: list):
        syms = []
        leters = []
        for ps in mess_ps:
            syms.append(str(
                SIPK.find_index_ps_by_symbol(ps.symbol, compare_to) + 1))
            leters.append(ps.symbol)
        print(", ".join(syms))
        ret = "".join(leters)
        print(ret)
        return ret

    @staticmethod
    def get_message_20_by_str(mess_str: str, all_ps: list):
        mess = []
        for char in mess_str:
            mess.append(SIPK.find_ps_by_symbol(char, all_ps))
        return mess

    @staticmethod
    def make_sipk(scene: M.Scene):
        # SIPK.random_sipk1()
        # SIPK.make_sipk1(scene)
        # SIPK.make_sipk2(scene)
        SIPK.make_sipk3(scene)

    @staticmethod
    def random_sipk1():
        if len(SIPK.sipk1_ps_str) == 0:
            SIPK.sipk1_ps_str = SIPK.get_random_ps(SIPK.sipk1_all_symbol_num)
        print(SIPK.sipk1_ps_str)
        all_ps = SIPK.get_all_ps_by_str(SIPK.sipk1_ps_str)
        SIPK.print_sp_octave(all_ps)
        if not SIPK.check_probabilities(all_ps): print("prb != 1")
        all_ps_copy = [ProbabilitySymbol.get_full_copy(ps) for ps in all_ps]
        m1 = SIPK.get_message_20_by_str(SIPK.sipk1_m1, all_ps_copy)
        m2 = SIPK.get_message_20_by_str(SIPK.sipk1_m2, all_ps_copy)
        m3 = SIPK.get_message_20_by_str(SIPK.sipk1_m3, all_ps_copy)
        if len(m1) == 0:
            m1 = SIPK.get_random_message_1(
                all_ps_copy, SIPK.sipk1_mess_all_symbol_num)
            m2 = SIPK.get_random_message_2(
                all_ps_copy, SIPK.sipk1_mess_all_symbol_num)
            m3 = SIPK.get_random_message_3(
                all_ps_copy, SIPK.sipk1_mess_all_symbol_num)
        SIPK.sipk1_m1 = SIPK.print_message_20(m1, all_ps)
        SIPK.sipk1_m2 = SIPK.print_message_20(m2, all_ps)
        SIPK.sipk1_m3 = SIPK.print_message_20(m3, all_ps)

    @staticmethod
    def make_sipk1(scene: M.Scene):
        ps_full = SIPK.sipk1_haffman(scene)
        SIPK.sipk1_table_1(scene, ps_full)
        SIPK.sipk1_table_2(scene, ps_full)
        SIPK.sipk1_formula_1(scene, ps_full)
        m1 = SIPK.get_message_20_by_str(SIPK.sipk1_m1, ps_full)
        m2 = SIPK.get_message_20_by_str(SIPK.sipk1_m2, ps_full)
        m3 = SIPK.get_message_20_by_str(SIPK.sipk1_m3, ps_full)
        SIPK.sipk1_messages_20(scene, m1, m2, m3)
        SIPK.sipk1_golomb(scene, ps_full)
        SIPK.sipk1_table_1(scene, ps_full)
        SIPK.sipk1_messages_20(scene, m1, m2, m3)
        num = SIPK.sipk1_arithm(scene, SIPK.sipk1_m1, ps_full)
        SIPK.sipk1_arithm_table(scene, SIPK.sipk1_m1, ps_full)
        SIPK.sipk1_count_1(scene, num)
        # SIPK.sipk1_formula_2(scene)
        # SIPK.sipk1_formula_3(scene)
        # SIPK.sipk1_formula_4(scene)
        # SIPK.sipk1_formula_5(scene)
        # SIPK.sipk1_formula_6(scene)
        SIPK.sipk1_table_3(scene, SIPK.sipk1_table_data, SIPK.sipk1_entropy)

    @staticmethod
    def sipk1_haffman(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        all_ps = SIPK.get_all_ps_by_str(SIPK.sipk1_ps_str)
        all_len = len(all_ps)
        vert_offset = 8.0 / (all_len + 2)
        prb_size = 24.0
        zline_size = 0.2
        zline_stroke_width = 3
        horz_offset = 12.0 / (all_len - 1)
        all_ps_old_full = all_ps.copy()
        all_ps.sort()
        all_ps.reverse()
        all_ps_old = all_ps.copy()
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        for psi in range(all_len):
            scene.add(M.Text(all_ps[psi].symbol + ":", font_size = 44.0, color = mc
                             ).move_to(SIPK.sipk1_UL + M.LEFT + M.UP * 0.07
                                       + M.DOWN * vert_offset * (psi + 1)))
        for cycle in range(all_len):
            max_width = 0.0
            max_height = 0.0
            for psi in range(len(all_ps)):
                new_text = M.Text(
                    str(round(all_ps[psi].probability, SIPK.sipk1_PRB_NUM)),
                    font_size = prb_size, color = mc).move_to(
                        SIPK.sipk1_UL
                        + M.DOWN * vert_offset * (psi + 1)
                        + M.RIGHT * horz_offset * cycle)
                max_width = max(max_width, new_text.width)
                max_height = max(max_height, new_text.height)
                scene.add(new_text)
            if cycle != all_len - 1:
                line = M.Line(
                    SIPK.sipk1_UL
                    + M.DOWN * vert_offset * (len(all_ps) - 1 - max_height * 0.6)
                    + M.RIGHT * (horz_offset * cycle + max_width * 0.7),
                    SIPK.sipk1_UL
                    + M.DOWN * vert_offset * (len(all_ps) + max_height * 0.6)
                    + M.RIGHT * (horz_offset * cycle + max_width * 0.7),
                    stroke_width = zline_stroke_width, color = mc)
                n0 = M.Text("0", font_size = prb_size, color = mc
                            ).next_to(line, M.UR, max_width * 0.1)
                n0.shift(M.DOWN * n0.height)
                n1 = M.Text("1", font_size = prb_size, color = mc
                            ).next_to(line, M.DR, max_width * 0.1)
                n1.shift(M.UP * n1.height)
                scene.add(line, n0, n1)
                p1 = all_ps.pop()
                p2 = all_ps.pop()
                for ch in p1.symbol:
                    SIPK.find_ps_by_symbol(ch, all_ps_old_full).code += "1"
                for ch in p2.symbol:
                    SIPK.find_ps_by_symbol(ch, all_ps_old_full).code += "0"
                all_ps.append(ProbabilitySymbol(
                    p1.symbol + p2.symbol, p1.probability + p2.probability, True))
                all_ps.sort()
                all_ps.reverse()
                used_index = []
                index_to = 1
                for index_from in range(len(all_ps_old) - 2):
                    index_to = -1
                    for psi_new in range(len(all_ps)):
                        if all_ps_old[index_from].symbol == all_ps[psi_new].symbol:
                            used_index.append(psi_new)
                            index_to = psi_new
                            break
                    ln = ZLine([
                        SIPK.sipk1_UL + M.DOWN * vert_offset * (index_from + 1)
                        + M.RIGHT * (horz_offset * (cycle) + max_width * 0.7),
                        SIPK.sipk1_UL + M.DOWN * vert_offset * (index_to + 1)
                        + M.RIGHT * (horz_offset * (cycle + 1) - max_width * 0.7)],
                        zline_size, zline_stroke_width, mc)
                    scene.add(ln)
                for psi_new in range(len(all_ps)):
                    if psi_new not in used_index:
                        index_to = psi_new
                used_index = []
                ln = ZLine([
                    SIPK.sipk1_UL + M.DOWN * vert_offset * (len(all_ps_old) - 0.5)
                    + M.RIGHT * (horz_offset * (cycle) + max_width * 0.7),
                    SIPK.sipk1_UL + M.DOWN * vert_offset * (len(all_ps_old) - 0.5)
                    + M.RIGHT * (horz_offset * (cycle + 0.44)),
                    SIPK.sipk1_UL + M.DOWN * vert_offset * (index_to + 1)
                    + M.RIGHT * (horz_offset * (cycle + 0.56)),
                    SIPK.sipk1_UL + M.DOWN * vert_offset * (index_to + 1)
                    + M.RIGHT * (horz_offset * (cycle + 1) - max_width * 0.7)],
                    zline_size, zline_stroke_width, mc)
                scene.add(ln)
                all_ps_old = all_ps.copy()
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        for i in range(len(all_ps_old_full)):
            all_ps_old_full[i].code = all_ps_old_full[i].code[::-1]
        return all_ps_old_full

    @staticmethod
    def sipk1_table_1(scene: M.Scene, all_ps: list):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            [[all_ps[i].symbol, all_ps[i].code]
             for i in range(len(all_ps))],
             include_outer_lines = True,
             v_buff = 0.5,
             h_buff = 1.8,
             element_to_mobject_config = {"font_size": 24.0, "color": mc},
             line_config = {"color": mc}
             ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk1_table_2(scene: M.Scene, all_ps: list):
        from math import log2
        SSf.SIPK_SSCTV_functions.make_background(scene)
        syms = [ps.symbol for ps in all_ps]
        prbs = [str(ps.probability) for ps in all_ps]
        logs = [str(- round(log2(ps.probability), 3)) for ps in all_ps]
        prbs_logs = [str(- round(log2(ps.probability) * ps.probability, 3))
                     for ps in all_ps]
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            [[prbs[i], logs[i], prbs_logs[i]] for i in range(len(all_ps))],
            row_labels = [M.Text(rt, font_size = 36.0, color = mc) for rt in syms],
            col_labels = [
                M.MathTex(r"p_i", font_size = 36.0, color = mc),
                M.MathTex(r"-\log_2 p_i", font_size = 36.0, color = mc),
                M.MathTex(r"-p_i \cdot \log_2 p_i", font_size = 36.0, color = mc)],
            include_outer_lines = True,
            v_buff = 0.44,
            h_buff = 1.8,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk1_formula_1(scene: M.Scene, all_ps: list):
        from math import log2
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        SIPK.sipk1_entropy = sum([- log2(sym.probability) * sym.probability
                                  for sym in all_ps])
        tx = r"H = - \sum_{i=1}^M p_i \cdot \log_2 p_i = "
        tx += str(round(SIPK.sipk1_entropy, 3))
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        txt = M.Text("бит/символ", font_size = tts, color = mc)
        tex.shift(M.LEFT * 0.5 * txt.width)
        txt.next_to(tex)
        scene.add(tex, txt)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def get_random_message_1(all_ps: list, n: int = 20):
        all_ps.sort()
        prb_line = SIPK.get_prb_line(all_ps, 0.0)
        mess_ps = []
        for _ in range(n):
            mess_ps.append(SIPK.get_ps_by_prb(random.random(), prb_line, all_ps))
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
        prb_line = SIPK.get_prb_line(all_ps, 0.0)
        mess_ps = []
        for i in range(n):
            mess_ps.append(SIPK.get_ps_by_prb(random.random(), prb_line, all_ps))
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
        prb_line = SIPK.get_prb_line(all_ps, 0.0)
        mess_ps = []
        for _ in range(n):
            mess_ps.append(SIPK.get_ps_by_prb(random.random(), prb_line, all_ps))
        return mess_ps

    @staticmethod
    def sipk1_messages_20(scene: M.Scene, m1: list, m2: list, m3: list):
        SIPK.sipk1_message_20(scene, m1)
        SIPK.sipk1_message_20(scene, m2)
        SIPK.sipk1_message_20(scene, m3)

    @staticmethod
    def sipk1_message_20(scene: M.Scene, mess_ps: list):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        syms = []
        codes = []
        indexes = []
        n = 1
        len_code = 0
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        for mes in mess_ps:
            syms.append(M.Text(mes.symbol, font_size = 30.0, color = mc))
            codes.append(M.Text(mes.code, color = mc))
            indexes.append(M.Text(str(n), font_size = 16.0, color = mc))
            n += 1
            len_code += len(mes.code)
        vg = M.VGroup(*codes).arrange()
        for i in range(len(syms)):
            vg += syms[i].next_to(codes[i], M.UP)
            vg += indexes[i].next_to(syms[i], M.UP)
        vg.scale(13.5 / vg.width).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        bit = r"Всего бит в сообщении = " + str(len_code)
        sym = r"Всего символов в сообщении = " + str(len(syms))
        bit_sym = r"Среднее значение = " + str(round(len_code / len(syms), 3))
        bit_sym += r" (бит/символ)"
        b = M.Text(bit, font_size = tts, color = mc).next_to(vg, M.DOWN, 0.5)
        s = M.Text(sym, font_size = tts, color = mc).next_to(b, M.DOWN)
        bs = M.Text(bit_sym, font_size = tts, color = mc).next_to(s, M.DOWN)
        scene.add(vg, b, s, bs)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SIPK.sipk1_table_data.append(round(len_code / len(syms), 3))

    @staticmethod
    def sipk1_golomb(scene: M.Scene, all_ps: list):
        golomb_r = {0: "0", 1: "10", 2: "11"}
        golomb_q = {0: "0", 1: "10", 2: "110", 3: "1110", 4: "11110", 5: "111110"}
        SSf.SIPK_SSCTV_functions.make_background(scene)
        all_ps_sorted = all_ps.copy()
        all_ps_sorted.sort()
        all_ps_sorted.reverse()
        all_len = len(all_ps_sorted)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = 24.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        for psi in range(all_len):
            t = str(psi + 1) + r" - " + all_ps_sorted[psi].symbol + r":"
            p = str(round(all_ps_sorted[psi].probability, SIPK.sipk1_PRB_NUM)) + ";"
            mobp = M.Text(p, font_size = tts, color = mc).move_to(
                SIPK.sipk1_UL + M.RIGHT * 1.5 + M.UP * 0.07
                + M.DOWN * (8.0 / (all_len + 2)) * (psi + 1))
            mobt = M.Text(t, font_size = 44.0, color = mc).next_to(mobp, M.LEFT)
            scene.add(mobp, mobt)
            m = 3
            q = psi // m
            r = psi - q * m
            texstr = (r"q = \left[\frac{" + str(psi + 1)
                      + r"-1}3\right] = " + str(q) + r";\ r = "
                      + str(psi + 1) + r" - 1 - " + str(q) + r"\cdot"
                      + str(m) + r" = " + str(r))
            tex = M.MathTex(texstr, font_size = txs, color = mc).next_to(mobp)
            found_ps = SIPK.find_ps_by_symbol(
                all_ps_sorted[psi].symbol, all_ps_sorted)
            found_ps.code = golomb_q[q] + golomb_r[r]
            found_text = M.Text(r" - код: " + found_ps.code,
                                font_size = tts, color = mc).next_to(tex)
            scene.add(tex, found_text)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk1_arithm(scene: M.Scene, mess_str: str, all_ps: list):
        def prb_size(cycle: int):
            if cycle <= 2: return 18.0
            elif cycle <= 4: return 16.0
            return 14.0

        SSf.SIPK_SSCTV_functions.make_background(scene)
        left_side = M.LEFT * 6.6
        mess_str = mess_str[:SIPK.sipk1_symbol_num_arithm]
        mes_len = len(mess_str)
        horz_offset = 12.0 / mes_len
        prb_line_old = SIPK.get_prb_line(all_ps, 0.0)
        prb_line = SIPK.get_prb_line(all_ps, 0.0)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        for cycle in range(mes_len + 1):
            nl = M.NumberLine(
                x_range = [0.0, 1.0, 1.0],
                length = 7.0,
                include_tip = False,
                include_numbers = False,
                rotation = 90.0 * M.DEGREES,
                color = mc,
                tick_size = 0.1,
                stroke_width = 3,
            ).move_to(left_side + M.RIGHT * horz_offset * cycle)
            scene.add(nl)
            if cycle != mes_len:
                for psi in range(len(all_ps) + 1):
                    new_text = M.Text(
                        str(round(prb_line[psi], (cycle + 1) * 2)),
                        font_size = prb_size(cycle), color = mc
                        ).next_to(nl, buff = 0.1)
                    new_text.shift(M.UP * 7.0 * (prb_line_old[psi] - 0.5))
                    new_line = M.Line(
                        left_side - M.LEFT * 0.1 + M.RIGHT * horz_offset * cycle,
                        left_side + M.LEFT * 0.1 + M.RIGHT * horz_offset * cycle,
                        color = mc, stroke_width = 3.0).next_to(nl, buff = - 0.2)
                    new_line.shift(M.UP * 7.0 * (prb_line_old[psi] - 0.5))
                    scene.add(new_text, new_line)
                g_indx = SIPK.find_index_ps_by_symbol(mess_str[cycle], all_ps)
                p1, p2 = (prb_line[g_indx], prb_line[g_indx + 1])
                diff = p2 - p1
                for i in range(len(all_ps) + 1):
                    prb_line[i] = p1 + prb_line_old[i] * diff
                ln1 = ZLine([
                    M.UP * 7.0 * (prb_line_old[g_indx] - 0.5)
                    + left_side + M.RIGHT * horz_offset * cycle,
                    M.UP * - 3.5
                    + left_side + M.RIGHT * horz_offset * (cycle + 1)
                    ], 0.1, 2, mc)
                ln2 = ZLine([
                    M.UP * 7.0 * (prb_line_old[g_indx + 1] - 0.5)
                    + left_side + M.RIGHT * horz_offset * cycle,
                    M.UP * 3.5
                    + left_side + M.RIGHT * horz_offset * (cycle + 1)
                    ], 0.1, 2, mc)
                scene.add(ln1, ln2)
            else:
                num1 = str(round(prb_line[-1], (cycle + 1) * 2))
                num2 = str(round(prb_line[0], (cycle + 1) * 2))
                new_text = M.Text(num1, font_size = prb_size(cycle), color = mc
                                  ).next_to(nl, buff = 0.1)
                new_text.shift(M.UP * 3.5)
                new_text2 = M.Text(num2, font_size = prb_size(cycle), color = mc
                                   ).next_to(nl, buff = 0.1)
                new_text2.shift(M.UP * -3.5)
                scene.add(new_text, new_text2)
                SSf.SIPK_SSCTV_functions.make_pause(scene)
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

        SSf.SIPK_SSCTV_functions.make_background(scene)
        num_symbols = 4
        mess_str = mess_str[:SIPK.sipk1_symbol_num_arithm]
        mes_len = len(mess_str)
        prb_line_old = SIPK.get_prb_line(all_ps, 0.0)
        prb_line = SIPK.get_prb_line(all_ps, 0.0)
        data = []
        in_file = 0
        in_file_old = 0
        pow_10 = 0
        pref_zeroes = 0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        for cycle in range(mes_len):
            g_indx = SIPK.find_index_ps_by_symbol(mess_str[cycle], all_ps)
            p1, p2 = (prb_line[g_indx], prb_line[g_indx + 1])
            diff = p2 - p1
            for i in range(len(all_ps) + 1):
                prb_line[i] = p1 + prb_line_old[i] * diff
            p1_str_emp = str(round(p1 * 10 ** (num_symbols + pow_10)))
            p1_str = SSf.SIPK_SSCTV_functions.fill_zeros(p1_str_emp, num_symbols)
            p2_str_emp = str(round(p2 * 10 ** (num_symbols + pow_10)))
            p2_str = SSf.SIPK_SSCTV_functions.fill_zeros(p2_str_emp, num_symbols)
            pref = pop_prefix(p1_str, p2_str)
            if pref > in_file:
                if in_file == 0 and p2_str[0] == "0":
                    pref_zeroes += 1
                    if p2_str[1] == "0": pref_zeroes += 1
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
                if in_file_str == "": in_file_str = "-"
            data.append([mess_str[cycle], p1_str, p2_str,
                         in_file_str, sdv[0], sdv[1]])
        fs = 24.0
        table = SSf.Table(
            data,
            col_labels = [
                M.Text("Символ", font_size = fs, color = mc),
                M.Text("Нижн.", font_size = fs, color = mc),
                M.Text("Верхн.", font_size = fs, color = mc),
                M.Text("В файл", font_size = fs, color = mc),
                M.Text("Нижн. сдв.", font_size = fs, color = mc),
                M.Text("Верхн. сдв.", font_size = fs, color = mc),
                ],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 0.8,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk1_count_1(scene: M.Scene, num: str):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        t = num + r"_{10} = "
        bin_s = ""
        if num[0] == "0":
            bin_s += "0"
            if num[1] == "0": bin_s += "0"
        bin_s += bin(int(num))[2:]
        t += bin_s + r"_2"
        show = M.MathTex(t, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        bit = r"Всего бит в сообщении = " + str(len(bin_s))
        sym = r"Всего символов в сообщении = " + str(SIPK.sipk1_symbol_num_arithm)
        bit_sym = r"Среднее значение = "
        bit_sym += str(round(len(bin_s) / SIPK.sipk1_symbol_num_arithm, 3))
        bit_sym += r" (бит/символ)"
        b = M.Text(bit, font_size = tts, color = mc).next_to(show, M.DOWN)
        s = M.Text(sym, font_size = tts, color = mc).next_to(b, M.DOWN)
        bs = M.Text(bit_sym, font_size = tts, color = mc).next_to(s, M.DOWN)
        scene.add(show, b, s, bs)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk1_formula_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx = r"I_s = log_2 M"
        tex = M.MathTex(tx, font_size = SSf.SIPK_SSCTV_functions.formula_tex_size,
                        color = SSf.SIPK_SSCTV_functions.get_main_color()
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk1_formula_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx = r"H = - \sum_{i=1}^M p_i \cdot \log_2 p_i"
        tex = M.MathTex(tx, font_size = SSf.SIPK_SSCTV_functions.formula_tex_size,
                        color = SSf.SIPK_SSCTV_functions.get_main_color()
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk1_formula_4(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx = r"R = \log_2 M - H"
        tex = M.MathTex(tx, font_size = SSf.SIPK_SSCTV_functions.formula_tex_size,
                        color = SSf.SIPK_SSCTV_functions.get_main_color()
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk1_formula_5(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx = r"H \le n_{cp} \le H + 1"
        tex = M.MathTex(tx, font_size = SSf.SIPK_SSCTV_functions.formula_tex_size,
                        color = SSf.SIPK_SSCTV_functions.get_main_color()
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk1_formula_6(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx = r"R_c = L_{cp} - H"
        tex = M.MathTex(tx, font_size = SSf.SIPK_SSCTV_functions.formula_tex_size,
                        color = SSf.SIPK_SSCTV_functions.get_main_color()
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk1_table_3(scene: M.Scene, data: list, H: float):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        fs = SSf.SIPK_SSCTV_functions.table_font_size
        data.append(SIPK.sipk1_mean_bit_over_symb1)
        data.append(SIPK.sipk1_mean_bit_over_symb2)
        data.append(SIPK.sipk1_mean_bit_over_symb3)
        table_data = []
        for i in range(3):
            table_data.append([str(data[i]), str(data[i + 3]), str(data[i + 6])])
        for i in range(0, 9, 3):
            data.append(round((data[i] + data[i + 1] + data[i + 2]) / 3.0, 3))
            data.append(round(data[- 1] - H, 3))
        table_data.append([str(data[9]), str(data[11]), str(data[13])])
        table_data.append([str(data[10]), str(data[12]), str(data[14])])
        table = SSf.Table(
            table_data,
            row_labels = [
                M.Text("Сообщение №1", font_size = fs, color = mc),
                M.Text("Сообщение №2", font_size = fs, color = mc),
                M.Text("Сообщение №3", font_size = fs, color = mc),
                M.Text("Cреднее значение\nбит/символ", font_size = fs, color = mc),
                M.Text("Избыточность", font_size = fs, color = mc)],
            col_labels = [
                M.Text("Код\nХаффмана", font_size = fs, color = mc),
                M.Text("Код\nГоломба", font_size = fs, color = mc),
                M.Text("Арифметический\nкод", font_size = fs, color = mc)],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 0.8,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

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
    def sipk2_scale_center_graph(graph):
        accuracy: int = 10
        Nver = SIPK.sipk2_Nver
        Nhor = SIPK.sipk2_Nhor
        min_g = 100.0
        max_g = -100.0
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
        if len(SIPK.sipk2_cffs) == 0:
            for _ in range(5):
                SIPK.sipk2_num_plane(scene)
            return
        SIPK.sipk2_num_plane(scene)
        SIPK.sipk2_table_1(scene)
        SIPK.sipk2_decode_1(scene, SIPK.sipk2_x_n)
        SIPK.sipk2_decode_2(scene, SIPK.sipk2_x_n)
        SIPK.sipk2_table_2(scene, SIPK.sipk2_x_n, "x")
        SIPK.sipk2_table_2(scene, SIPK.sipk2_e1, "e_1")
        SIPK.sipk2_table_2(scene, SIPK.sipk2_e2, "e_2")
        SIPK.sipk2_table_2(scene, SIPK.sipk2_e2_opt, "e_{2opt}")
        # SIPK.sipk2_formula_1(scene)
        # SIPK.sipk2_formula_2(scene)
        # SIPK.sipk2_formula_3(scene)
        # SIPK.sipk2_formula_4(scene)
        # SIPK.sipk2_formula_5(scene)
        # SIPK.sipk2_formula_6(scene)
        SIPK.sipk2_formula_7(scene)
        SIPK.sipk2_formula_8(scene)
        # SIPK.sipk2_formula_9(scene)
        # SIPK.sipk2_formula_10(scene)
        # SIPK.sipk2_formula_11(scene)
        # SIPK.sipk2_formula_12(scene)
        # SIPK.sipk2_formula_13(scene)
        # SIPK.sipk2_formula_14(scene)

    @staticmethod
    def sipk2_num_plane(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (0, SIPK.sipk2_Nhor, 1),
            y_range = (0, SIPK.sipk2_Nver, 1),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "numbers_to_include": M.np.arange(0, SIPK.sipk2_Nhor + 1, 1),
                "font_size": 18.0,
                "stroke_width": 3,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": 0.11,
                "label_direction": M.DOWN,
                "color": mc},
            y_axis_config = {
                "numbers_to_include": M.np.arange(0, SIPK.sipk2_Nver + 1, 1),
                "label_direction": M.LEFT},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 2,
                "stroke_opacity": 0.5},
            tips = False)
        number_plane.get_axes().set_color(mc)
        graphs = M.VGroup()
        gr = SIPK.sipk2_cffs
        if len(gr) == 0: gr = SIPK.sipk2_random_graph_cffs()
        gr = SIPK.sipk2_scale_center_graph(SIPK.sipk2_graph_by_cffs(gr))
        graphs += number_plane.plot(
            gr, x_range = (0, SIPK.sipk2_Nhor, 0.1),
            color = mc, use_smoothing = False)
        x_n = []
        for i in range(SIPK.sipk2_Nhor + 1):
            graphs += M.Dot(number_plane.c2p(i, round(gr(i)), 0), 0.05, color = mc)
            x_n.append(round(gr(i)))
        SIPK.sipk2_x_n = x_n
        scene.add(number_plane, graphs)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_table_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        fs = 24.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        x_n_1: int = 0
        x_n_2: int = 0
        sum_x_x1_n1 = 0
        sum_x1_x1_n1 = 0
        sum_x_x1_n2 = 0
        sum_x_x2_n2 = 0
        sum_x1_x2_n2 = 0
        sum_x1_x1_n2 = 0
        sum_x2_x2_n2 = 0
        for i in range(len(SIPK.sipk2_x_n)):
            sum_x_x1_n1 += SIPK.sipk2_x_n[i] * x_n_1
            sum_x1_x1_n1 += x_n_1 * x_n_1
            if i >= 2:
                sum_x_x1_n2 += SIPK.sipk2_x_n[i] * x_n_1
                sum_x_x2_n2 += SIPK.sipk2_x_n[i] * x_n_2
                sum_x1_x2_n2 += x_n_1 * x_n_2
                sum_x1_x1_n2 += x_n_1 * x_n_1
                sum_x2_x2_n2 += x_n_2 * x_n_2
            x_n_2 = x_n_1
            x_n_1 = SIPK.sipk2_x_n[i]
        SIPK.sipk2_a22 = (
            (sum_x_x2_n2 * sum_x1_x1_n2 - sum_x_x1_n2 * sum_x1_x2_n2)
            / (sum_x2_x2_n2 * sum_x1_x1_n2 - sum_x1_x2_n2 * sum_x1_x2_n2))
        SIPK.sipk2_a21 = ((sum_x_x1_n2 - SIPK.sipk2_a22 * sum_x1_x2_n2)
                          / sum_x1_x1_n2)
        SIPK.sipk2_a1 = sum_x_x1_n1 / sum_x1_x1_n1
        SIPK.sipk2_sum_x_x1_n1 = sum_x_x1_n1
        SIPK.sipk2_sum_x1_x1_n1 = sum_x1_x1_n1
        SIPK.sipk2_sum_x_x1_n2 = sum_x_x1_n2
        SIPK.sipk2_sum_x_x2_n2 = sum_x_x2_n2
        SIPK.sipk2_sum_x1_x2_n2 = sum_x1_x2_n2
        SIPK.sipk2_sum_x1_x1_n2 = sum_x1_x1_n2
        SIPK.sipk2_sum_x2_x2_n2 = sum_x2_x2_n2
        table_data = []
        x_n_1 = 0
        x_n_2 = 0
        y_n_1 = 0
        y_n_2 = 0
        SIPK.sipk2_e1.clear()
        SIPK.sipk2_e2.clear()
        SIPK.sipk2_e2_opt.clear()
        highlighted = []
        for i in range(len(SIPK.sipk2_x_n)):
            p1 = x_n_1
            p2 = 2 * x_n_1 - x_n_2
            p2_opt = round(SIPK.sipk2_a21 * x_n_1 + SIPK.sipk2_a22 * x_n_2)
            if i == 1:
                p2 = x_n_1
                p2_opt = x_n_1
            if p2 != p2_opt: highlighted.append((9, 2 + i))
            e1 = SIPK.sipk2_x_n[i] - p1
            e2 = SIPK.sipk2_x_n[i] - p2
            e2_opt = SIPK.sipk2_x_n[i] - p2_opt
            y1 = y_n_1 + e1
            y2 = 2 * y_n_1 - y_n_2 + e2
            if i == 1: y2 = y_n_1 + e2
            table_data.append([str(i), str(SIPK.sipk2_x_n[i]),
                               str(p1), str(e1), str(y1),
                               str(p2), str(e2), str(y2),
                               str(p2_opt), str(e2_opt)])
            y_n_2 = y_n_1
            y_n_1 = y1
            x_n_2 = x_n_1
            x_n_1 = SIPK.sipk2_x_n[i]
            SIPK.sipk2_e1.append(e1)
            SIPK.sipk2_e2.append(e2)
            SIPK.sipk2_e2_opt.append(e2_opt)
        table_data = SSf.SIPK_SSCTV_functions.transpose_list(table_data)
        table = SSf.Table(
            table_data,
            row_labels = [
                M.MathTex("n", font_size = fs, color = mc),
                M.MathTex("x(n)", font_size = fs, color = mc),
                M.MathTex("p_1(n)", font_size = fs, color = mc),
                M.MathTex("e_1(n)", font_size = fs, color = mc),
                M.MathTex("y_1(n)", font_size = fs, color = mc),
                M.MathTex("p_2(n)", font_size = fs, color = mc),
                M.MathTex("e_2(n)", font_size = fs, color = mc),
                M.MathTex("y_2(n)", font_size = fs, color = mc),
                M.MathTex("p_{2opt}(n)", font_size = fs, color = mc),
                M.MathTex("e_{2opt}(n)", font_size = fs, color = mc)],
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.3,
            element_to_mobject_config = {"font_size": 14.0, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        for cell in highlighted:
            table.add_highlighted_cell(cell, color = "#999999")
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_table_2(scene: M.Scene, data: list, X: str):
        from math import log2
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        fs_title = 24.0
        h_buff = 0.3
        if X == "x": h_buff = 0.24
        table_data = []
        data_dict = {}
        data.sort()
        for i in range(len(data)):
            if data[i] not in data_dict:
                data_dict[data[i]] = 1
            else:
                data_dict[data[i]] += 1
        SIPK.sipk1_entropy = 0.0
        for i in data_dict:
            pb = data_dict[i] / len(data)
            table_data.append([str(i),
                               str(data_dict[i]),
                               str(round(pb, 3)),
                               str(- round(log2(pb), 3)),
                               str(- round(log2(pb) * pb, 3))])
            SIPK.sipk1_entropy += - log2(pb) * pb
        table_data = SSf.SIPK_SSCTV_functions.transpose_list(table_data)
        table = SSf.Table(
            table_data,
            row_labels = [
                M.MathTex(f"{X}", font_size = fs_title, color = mc),
                M.MathTex(f"N({X})", font_size = fs_title, color = mc),
                M.MathTex(f"p({X})", font_size = fs_title, color = mc),
                M.MathTex(r"-\log_2 p(" + X + r")",
                          font_size = fs_title, color = mc),
                M.MathTex(r"-p(" + X + r") \cdot \log_2 p(" + X + r")",
                          font_size = fs_title, color = mc)],
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = h_buff,
            element_to_mobject_config = {"font_size": 14.0, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx = r"H = - \sum_{i=1}^M p_i \cdot \log_2 p_i = "
        tx += str(round(SIPK.sipk1_entropy, 3))
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(table, M.DOWN)
        txt = M.Text("бит/символ", font_size = tts, color = mc)
        tex.shift(M.LEFT * txt.width * 0.5)
        txt.next_to(tex)
        scene.add(table, tex, txt)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"E = \overline{s^2(n)} = \overline{\left["
        tx += r"x(n) - \sum_{m=1}^M a_m x(n-m) \right]^2}"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"\frac{\partial E}{\partial a_i} = \overline{2 \left["
        tx2 += r"x(n) - \sum_{m=1}^M a_m x(n-m) \right] x(n-m)} = 0;\ "
        tx2 += r"i = 1, \ldots , M"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"\sum_{m=1}^M a_m R(i,m) = R(m,0);\ "
        tx3 += r"i = 1, \ldots , M"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"E_1 = \overline{\left[x(n) - a_1 x(n-1) \right]^2}"
        tx += r" = \frac 1 N \sum_{n=1}^N [x(n) - a_1 x(n-1) \right]^2"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"E_2 = \overline{\left[x(n) - a_{21} x(n-1) "
        tx2 += r"- a_{22} x(n-2) \right]^2} ="
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"= \frac 1 {N-1} \sum_{n=2}^N \left[x(n) - a_{21} x(n-1)"
        tx3 += r" - a_{22} x(n-2) \right]^2"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"\frac{\partial E_1}{\partial a_1} = "
        tx += r"\frac {-2} N \sum_{n=1}^N \big(\left[x(n) - "
        tx += r"a_1 x(n-1) \right] x(n-1) \big) = 0"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"\frac{\partial E_2}{\partial a_{21}} = "
        tx2 += r"\frac {-2} {N-1} \sum_{n=2}^N \big(\left[x(n) - "
        tx2 += r"a_{21} x(n-1) - a_{22} x(n-2) \right] x(n-1) \big) = 0"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"\frac{\partial E_2}{\partial a_{22}} = "
        tx3 += r"\frac {-2} {N-1} \sum_{n=2}^N \big(\left[x(n) - "
        tx3 += r"a_{21} x(n-1) - a_{22} x(n-2) \right] x(n-2) \big) = 0"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_4(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"\frac{\partial E_1}{\partial a_1} = "
        tx += r"\frac {-2} N \sum_{n=1}^N \big(x(n) x(n-1) - "
        tx += r"a_1 (x(n-1))^2 \big) = 0"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"\frac{\partial E_2}{\partial a_{21}} = "
        tx2 += r"\frac {-2} {N-1} \sum_{n=2}^N \big(x(n) x(n-1) - "
        tx2 += r"a_{21} (x(n-1))^2 - a_{22} x(n-2) x(n-1)\big) = 0"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"\frac{\partial E_2}{\partial a_{22}} = "
        tx3 += r"\frac {-2} {N-1} \sum_{n=2}^N \big(x(n) x(n-2) - "
        tx3 += r"a_{21} x(n-1) x(n-2) - a_{22} (x(n-2))^2 \big) = 0"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_5(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"\sum_{n=1}^N x(n) x(n-1) - "
        tx += r"a_1 \sum_{n=1}^N (x(n-1))^2 = 0"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"\sum_{n=2}^N x(n) x(n-1) - "
        tx2 += r"a_{21} \sum_{n=2}^N (x(n-1))^2 -"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx22 = r"- a_{22} \sum_{n=2}^N x(n-2) x(n-1) = 0"
        tex22 = M.MathTex(tx22, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        tx3 = r"\sum_{n=2}^N x(n) x(n-2) - "
        tx3 += r"a_{21} \sum_{n=2}^N x(n-1) x(n-2) -"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex22, M.DOWN)
        tx32 = r"- a_{22} \sum_{n=2}^N (x(n-2))^2 = 0"
        tex32 = M.MathTex(tx32, font_size = txs, color = mc).next_to(tex3, M.DOWN)
        scene.add(tex, tex2, tex3, tex22, tex32)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_6(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"a_1 = \frac {\sum_{n=1}^N x(n) x(n-1)}"
        tx += r"{\sum_{n=1}^N (x(n-1))^2}"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"a_{21} = \frac {\sum_{n=2}^N x(n) x(n-1) - "
        tx2 += r"a_{22} \sum_{n=2}^N x(n-2) x(n-1)}"
        tx2 += r"{\sum_{n=2}^N (x(n-1))^2}"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"a_{22} = \frac {\sum_{n=2}^N x(n) x(n-2) - "
        tx3 += r"a_{21} \sum_{n=2}^N x(n-1) x(n-2)}"
        tx3 += r"{\sum_{n=2}^N (x(n-2))^2}"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_7(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"a_1 = " + str(round(SIPK.sipk2_a1, 3))
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        more_less = " меньше"
        if 1.0 - SIPK.sipk2_a1 < 0.0: more_less = " больше"
        tx2 = "на " + str(round(abs(100.0 * (1.0 - SIPK.sipk2_a1)), 1))
        tx2 += "%" + more_less
        tex2 = M.Text(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        scene.add(tex, tex2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_8(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"a_{21} = " + str(round(SIPK.sipk2_a21, 3))
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"a_{22} = " + str(round(SIPK.sipk2_a22, 3))
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        more_less = " меньше"
        if 2.0 - SIPK.sipk2_a21 < 0.0: more_less = " больше"
        tx3 = "на " + str(round(abs(100.0 * (1.0 - SIPK.sipk2_a21 * 0.5)), 1))
        tx3 += "%" + more_less
        tex3 = M.Text(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        more_less = " меньше"
        if -1.0 - SIPK.sipk2_a22 > 0.0: more_less = " больше"
        tx4 = "на " + str(round(abs(100.0 * (1.0 + SIPK.sipk2_a22)), 1))
        tx4 += "%" + more_less
        tex4 = M.Text(tx4, font_size = txs, color = mc).next_to(tex3, M.DOWN)
        scene.add(tex, tex2, tex3, tex4)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_9(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"H(X_1, X_2) = - \sum_{i=1}^M \sum_{j=1}^M "
        tx += r"p(x_i, x_j) \cdot \log_2 p(x_i, x_j)"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_10(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"p(n) = \sum_{m=1}^M a_m x(n - m)"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_11(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"f_1 = \sum_{n=2}^N x(n) x(n-1);\ f_2 = \sum_{n=2}^N x(n) x(n-2);"
        tx2 = r"f_{11} = \sum_{n=2}^N (x(n-1))^2;"
        tx2 += r"\ f_{22} = \sum_{n=2}^N (x(n-2))^2;"
        tx3 = r"f_{12} = \sum_{n=2}^N x(n-1) x(n-2)"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_12(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"a_{21} = \frac {f_1 - a_{22} f_{12}}{f_{11}}"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"a_{22} = \frac {f_2 - a_{21} f_{12}}{f_{22}}"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"a_{22} = \frac {f_2 - (\frac {f_1 - a_{22} f_{12}}{f_{11}}) "
        tx3 += r"f_{12}}{f_{22}}"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        tx4 = r"a_{22} f_{22} = f_2 - \frac {f_1 f_{12} - a_{22} f_{12}^2}{f_{11}}"
        tex4 = M.MathTex(tx4, font_size = txs, color = mc).next_to(tex3, M.DOWN)
        tx5 = r"a_{22} f_{22} f_{11} = f_2 f_{11} - f_1 f_{12} + a_{22} f_{12}^2"
        tex5 = M.MathTex(tx5, font_size = txs, color = mc).next_to(tex4, M.DOWN)
        tx6 = r"a_{22} = \frac {f_2 f_{11} - f_1 f_{12}}{f_{22} f_{11} - f_{12}^2}"
        tex6 = M.MathTex(tx6, font_size = txs, color = mc).next_to(tex5, M.DOWN)
        scene.add(tex, tex2, tex3, tex4, tex5, tex6)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_13(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"a_{21} = \frac {\sum_{n=2}^N x(n) x(n-1) - "
        tx += r"a_{22} \sum_{n=2}^N x(n-2) x(n-1)}"
        tx += r"{\sum_{n=2}^N (x(n-1))^2}"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"a_{22} = \frac {(\sum_{n=2}^N x(n) x(n-2))"
        tx2 += r"(\sum_{n=2}^N (x(n-1))^2) - "
        tx2 += r"(\sum_{n=2}^N x(n) x(n-1))"
        tx2 += r"(\sum_{n=2}^N x(n-1) x(n-2))}"
        tx2 += r"{(\sum_{n=2}^N (x(n-2))^2)"
        tx2 += r"{(\sum_{n=2}^N (x(n-1))^2) - "
        tx2 += r"(\sum_{n=2}^N x(n-1) x(n-2))^2}"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"\left\{ \frac {\frac {\displaystyle \sum_{n=2}^N}{ \sum_{n=2}^N}}"
        tx3 += r"{\displaystyle \sum_{n=2}^N} \right\}"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_formula_14(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"p(X) = \frac {N(X)}{N}"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_decode_1(scene: M.Scene, data: list):
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        for i in SIPK.sipk2_decode_n:
            SSf.SIPK_SSCTV_functions.make_background(scene)
            tx0 = r"n = " + str(i) + r":\ x(" + str(i) + r") = " + str(data[i])
            tx0 += r";\ x(" + str(i - 1) + r") = " + str(data[i - 1])
            tex0 = M.MathTex(tx0, font_size = txs, color = mc).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
            tx = r"y_1(" + str(i) + r") = y_1(" + str(i - 1) + r") + "
            tx += r"e_1(" + str(i) + r")"
            tx += r" = " + str(data[i - 1]) + r" + " + str(data[i] - data[i - 1])
            tx += r" = " + str(data[i])
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(tex0, M.DOWN)
            tx2 = r"y_1(" + str(i - 1) + r") = " + str(data[i - 1])
            tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
            tx3 = r"e_1(" + str(i) + r") = x("
            tx3 += str(i) + r") - p_1(" + str(i) + r")"
            tx3 += r" = x(" + str(i) + r") - x(" + str(i - 1) + r")"
            tx3 += r" = " + str(data[i]) + r" - " + str(data[i - 1])
            tx3 += r" = " + str(data[i] - data[i - 1])
            tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
            scene.add(tex0, tex, tex2, tex3)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk2_decode_2(scene: M.Scene, data: list):
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        for i in SIPK.sipk2_decode_n:
            SSf.SIPK_SSCTV_functions.make_background(scene)
            tx0 = r"n = " + str(i) + r":\ x(" + str(i) + r") = " + str(data[i])
            tx0 += r";\ x(" + str(i - 1) + r") = " + str(data[i - 1])
            tx0 += r";\ x(" + str(i - 2) + r") = " + str(data[i - 2])
            tex0 = M.MathTex(tx0, font_size = txs, color = mc).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
            tx = r"y_2(" + str(i) + r") = 2 \cdot y_2(" + str(i - 1) + r") - "
            tx += r"y_2(" + str(i - 2) + r") + "
            tx += r"e_2(" + str(i) + r")"
            tx += r" = " + str(2 * data[i - 1]) + r" - " + str(data[i - 2])
            tx += r" + " + str(data[i] - 2 * data[i - 1] + data[i - 2])
            tx += r" = " + str(data[i])
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(tex0, M.DOWN)
            tx2 = r"y_2(" + str(i - 1) + r") = " + str(data[i - 1])
            tx2 += r";\ y_2(" + str(i - 2) + r") = " + str(data[i - 2])
            tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
            tx3 = r"e_2(" + str(i) + r") = x("
            tx3 += str(i) + r") - p_2(" + str(i) + r")"
            tx3 += r" = x(" + str(i) + r") - (2 \cdot x(" + str(i - 1) + r")"
            tx3 += r" - x(" + str(i - 2) + r"))"
            tx3 += r" = " + str(data[i]) + r" - (" + str(2 * data[i - 1])
            tx3 += r" - " + str(data[i - 2]) + r")"
            tx3 += r" = " + str(data[i] - 2 * data[i - 1] + data[i - 2])
            tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
            scene.add(tex0, tex, tex2, tex3)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_sipk3(scene: M.Scene):
        SIPK.sipk3_hemming_example(scene)
        SIPK.sipk3_graph(scene)
        SIPK.sipk3_graph_scaled(scene)
        SIPK.sipk3_formula_1(scene)
        SIPK.sipk3_formula_2(scene)
        check = [127, 126]
        for i in check:
            SIPK.sipk3_count_1(scene, i)
        SIPK.sipk3_count_2(scene, 127, 108)

    @staticmethod
    def sipk3_hemming_example(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        num1 = random.randint(0, 255)
        num2 = random.randint(0, 255)
        bin1 = SSf.SIPK_SSCTV_functions.fill_zeros(bin(num1)[2:], 8)
        bin2 = SSf.SIPK_SSCTV_functions.fill_zeros(bin(num2)[2:], 8)
        eq_text = ""
        for i in range(8):
            eq_text += SSf.SIPK_SSCTV_functions.sum_mod_2(bin1[i], bin2[i])
        print(bin1, bin2)
        b1 = M.Text(bin1, font_size = tts, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        b2 = M.Text(bin2, font_size = tts, color = mc).next_to(b1, M.DOWN)
        eq = M.Text(eq_text, font_size = tts, color = mc).next_to(b2, M.DOWN)
        crc = M.Text("⊕", font_size = tts, color = mc).next_to(b1, M.DL, 0.03)
        ravn = M.Text("=", font_size = tts, color = mc).next_to(b2, M.DL, 0.08)
        scene.add(b1, b2, eq, crc, ravn)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk3_graph(scene: M.Scene):
        from math import log2, ceil
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        n = 25
        points = []
        while n <= 185:
            attraction_area = 0
            for i in range(SIPK.sipk3_t + 1):
                attraction_area += SSf.SIPK_SSCTV_functions.c_n_k(n, i)
            p = ceil(log2(attraction_area))
            k = n - p
            R_found = k / n
            points.append((n, R_found))
            n += 1
        number_plane = M.NumberPlane(
            x_range = (20, 190, 10),
            y_range = (0.5, 0.9, 0.05),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "numbers_to_include": M.np.arange(20, 190, 10),
                "font_size": 18.0,
                "stroke_width": 3,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": 0.08,
                "label_direction": M.DR,
                "color": mc},
            y_axis_config = {
                "numbers_to_include": M.np.arange(0.5, 0.9, 0.05),
                "label_direction": M.LEFT},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 1,
                "stroke_opacity": 0.5},
            tips = False,
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        number_plane.get_axes().set_color(mc)
        graphs = M.VGroup()
        for i in points:
            graphs += M.Dot(number_plane.c2p(i[0], i[1], 0.0),
                            0.04, color = mc)
        scene.add(number_plane, graphs)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk3_graph_scaled(scene: M.Scene):
        from math import log2, ceil
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        R_found = 0.0
        n = 120
        points = []
        while n <= 130:
            attraction_area = 0
            for i in range(SIPK.sipk3_t + 1):
                attraction_area += SSf.SIPK_SSCTV_functions.c_n_k(n, i)
            p = ceil(log2(attraction_area))
            k = n - p
            R_found = k / n
            points.append((n, R_found))
            n += 1
        number_plane = M.NumberPlane(
            x_range = (119, 131, 1),
            y_range = (0.84, 0.86, 0.005),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "numbers_to_include": M.np.arange(119, 131, 1),
                "font_size": 18.0,
                "stroke_width": 3,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": 0.08,
                "label_direction": M.DR,
                "color": mc},
            y_axis_config = {
                "numbers_to_include": M.np.arange(0.84, 0.86, 0.005),
                "label_direction": M.LEFT},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 1,
                "stroke_opacity": 0.5},
            tips = False,
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        number_plane.get_axes().set_color(mc)
        graphs = M.VGroup()
        for i in points:
            graphs += M.Dot(number_plane.c2p(i[0], i[1], 0.0),
                            0.1, color = mc)
        scene.add(number_plane, graphs)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk3_formula_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"p \ge \log_2 (C_n^0 + C_n^1 + C_n^2 + C_n^3 + C_n^4)"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"C_n^k = \frac {n!}{k!(n-k)!}"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        scene.add(tex, tex2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk3_formula_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"p = n - k \ge \log_2 \left(\sum_{i=0}^t C_n^i \right)"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk3_count_1(scene: M.Scene, n: int):
        from math import log2, ceil
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"n = " + str(n) + r": \ p \ge \log_2 (C_{" + str(n) + r"}^0 + C_{"
        tx += str(n) + r"}^1 + C_{" + str(n) + r"}^2 + C_{" + str(n) + r"}^3"
        if SIPK.sipk3_t == 4: tx += r" + C_{" + str(n) + r"}^4"
        tx += r")"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"C_{" + str(n) + r"}^0 = 1;\ "
        tx2 += r"C_{" + str(n) + r"}^1 = " + str(n) + r";\ "
        tx2 += r"C_{" + str(n) + r"}^2 = "
        tx2 += str(SSf.SIPK_SSCTV_functions.c_n_k(n, 2)) + r";\ "
        tx2 += r"C_{" + str(n) + r"}^3 = "
        tx2 += str(SSf.SIPK_SSCTV_functions.c_n_k(n, 3))
        attraction_area = 1 + n + SSf.SIPK_SSCTV_functions.c_n_k(n, 2)
        attraction_area += SSf.SIPK_SSCTV_functions.c_n_k(n, 3)
        if SIPK.sipk3_t == 4:
            tx2 += r";\ C_{" + str(n) + r"}^4 = "
            tx2 += str(SSf.SIPK_SSCTV_functions.c_n_k(n, 4))
            attraction_area += SSf.SIPK_SSCTV_functions.c_n_k(n, 4)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN, 0.4)
        tx3 = r"\log_2 (" + str(attraction_area)
        tx3 += r") = " + str(round(log2(attraction_area), 2))
        tex3 = M.MathTex(tx3, font_size = txs, color = mc
                         ).next_to(tex2, M.DOWN, 0.4)
        p = ceil(log2(attraction_area))
        tx4 = r"p = " + str(p)
        tx4 += r";\ k = n - p = " + str(n - p)
        tx4 += r";\ R = \frac {k}{n} = " + str(round((n - p) / n, 4))
        tex4 = M.MathTex(tx4, font_size = txs, color = mc
                         ).next_to(tex3, M.DOWN, 0.4)
        scene.add(tex, tex2, tex3, tex4)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk3_count_2(scene: M.Scene, n: int, k: int):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"N_r = 2^k = 2^{" + str(k) + r"} = "
        tx += SSf.SIPK_SSCTV_functions.int_to_exp10(2 ** k)
        tx += r";\ N_p = 2^n = 2^{" + str(n) + r"} = "
        tx += SSf.SIPK_SSCTV_functions.int_to_exp10(2 ** n)
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"2^k \cdot n = "
        tx2 += SSf.SIPK_SSCTV_functions.int_to_exp10((2 ** k) * n)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"2^n \cdot (k + 1) = "
        tx3 += SSf.SIPK_SSCTV_functions.int_to_exp10((2 ** n) * (k + 1))
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)


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
        
