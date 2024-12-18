import manim as M
import random
import SIPK_SSCTV_functions as SSf


class SIPK(object):
    """SIPK"""

    EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    en = "abcdefghijklmnopqrstuvwxyz"
    RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    sipk1_ps_str = "B0.09 V0.16 C0.26 J0.22 E0.19 M0.08"
    sipk1_m1 = "VVCMCMMCMJCCCMCVCJVE"
    sipk1_m2 = "EEECCCEJJCJCCJCCCCJE"
    sipk1_m3 = "MVMBMVVVVBMVBVVMMBVM"
    sipk1_entropy = 0.0
    sipk1_table_data = []
    sipk1_all_symbol_num = 6
    sipk1_symbol_num_arithm = 6
    sipk1_mess_all_symbol_num = 20
    sipk1_mean_bit_over_symb1 = round(59.0 / sipk1_mess_all_symbol_num, 3)
    sipk1_mean_bit_over_symb2 = round(51.0 / sipk1_mess_all_symbol_num, 3)
    sipk1_mean_bit_over_symb3 = round(72.0 / sipk1_mess_all_symbol_num, 3)
    sipk1_PRB_NUM: int = 2
    sipk1_UL = M.LEFT * 5.5 + M.UP * 3.5

    sipk2_Nhor = 25
    sipk2_Nver = 20
    sipk2_x_n = []
    sipk2_cffs = [[-4.676, -0.038, 6.786], [-0.782, -0.639, 0.558], [-0.716, -0.057, 1.487], [1.004, -0.241, 5.461]]
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
    sipk2_decode_n = [4, 14, 25]

    sipk3_R = 0.62
    sipk3_t = 4
    sipk3_check = [45, 44]
    sipk3_n = 48
    sipk3_k = 30
    sipk3_n_graph = 40

    sipk4_5_6_7_in_group_list = 26
    sipk4_fvh = ["0000000", "0011101", "0101011", "0110110",
                 "1000111", "1011010", "1101100", "1110001"]
    sipk4_matrix_fs = 30.0
    sipk4_matrix_G = []
    sipk4_matrix_H = []
    sipk4_sindromes = []

    sipk5_V_s_x_bin = ""
    sipk5_mistake_1 = 8
    sipk5_mistake_2 = 8
    sipk5_vde = ""
    sipk5_Hr = []
    sipk5_phone = 9113

    sipk6_log_p_16 = []
    sipk6_V_s_x_bin = ""
    sipk6_sindroms = []
    sipk6_sindroms_int_p1 = []
    sipk6_sigmas = []
    sipk6_group = 1

    sipk7_errs = [-1, -1]
    sipk7_soft = "2, 3; 1, -4; 2, 2; -3, 4; -4, -3; -4, -1; 2, -3; 4, 2; 2, -1; -2, -4; 4, 4"
    sipk7_final_way = ""


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
        sm = SIPK.get_random_symbols(n, SIPK.EN)
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
        # SIPK.make_sipk3(scene)
        # SIPK.make_sipk4(scene)
        # SIPK.make_sipk5(scene)
        # SIPK.make_sipk6(scene)
        SIPK.make_sipk7(scene)
        # SIPK.sipk_lr3_formula_1(scene)
        # SIPK.sipk_lr3_table_1(scene)
        # SIPK.new_sipk_lr3_graphs_1(scene)
        # SIPK.new_sipk_lr3_legend(scene)
        # SIPK.sipk_lr4_graphs_1(scene)
        # SIPK.sipk_lr4_legend(scene)

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
            for _ in range(10):
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
        # SIPK.sipk2_x_n = [8, 10, 11, 13, 15, 16, 17, 18, 18, 18, 18, 17, 16, 13, 11, 9, 6, 5, 4, 3, 2, 2, 1, 1, 1]
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
            h_buff = 0.25,
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
        h_buff = 0.28
        if X == "x": h_buff = 0.18
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
        # SIPK.sipk3_graph(scene)
        SIPK.sipk3_graph_scaled(scene, SIPK.sipk3_n_graph)
        # SIPK.sipk3_formula_1(scene)
        # SIPK.sipk3_formula_2(scene)
        for i in SIPK.sipk3_check:
            SIPK.sipk3_count_1(scene, i)
        SIPK.sipk3_count_2(scene, SIPK.sipk3_n, SIPK.sipk3_k)

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
    def sipk3_graph_scaled(scene: M.Scene, left: int):
        from math import log2, ceil
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        R_found = 0.0
        n = left
        points = []
        while n <= left + 10:
            attraction_area = 0
            for i in range(SIPK.sipk3_t + 1):
                attraction_area += SSf.SIPK_SSCTV_functions.c_n_k(n, i)
            p = ceil(log2(attraction_area))
            k = n - p
            R_found = k / n
            points.append((n, R_found))
            n += 1
        number_plane = M.NumberPlane(
            x_range = (left - 1, left + 11, 1),
            y_range = (SIPK.sipk3_R - 0.05, SIPK.sipk3_R + 0.05, 0.05),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "numbers_to_include": M.np.arange(left - 1, left + 11, 1),
                "font_size": 18.0,
                "stroke_width": 3,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": 0.08,
                "label_direction": M.DR,
                "color": mc},
            y_axis_config = {
                "numbers_to_include": M.np.arange(
                    SIPK.sipk3_R - 0.05, SIPK.sipk3_R + 0.05, 0.05),
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

    @staticmethod
    def sipk4_hemming_distance(word1: str, word2: str):
        dist = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                dist += 1
        return dist

    @staticmethod
    def sipk4_inverse_bit(word: str, bit: int):
        ret_word = word[:bit]
        if word[bit] == "1": ret_word += "0"
        else: ret_word += "1"
        ret_word += word[bit + 1:]
        return ret_word

    @staticmethod
    def sipk4_make_mistake(word: str, n_mistake: int):
        full = []
        ret = []
        ret_word = word
        for i in range(len(word)):
            full.append(i)
        for _ in range(n_mistake):
            r = round(random.random() * (len(full) - 1))
            ret.append(full[r])
            full.remove(full[r])
        for i in ret:
            ret_word = SIPK.sipk4_inverse_bit(ret_word, i)
        return ret_word

    @staticmethod
    def sipk4_str_to_list(word: str):
        ret_list = []
        for i in range(len(word)):
            ret_list.append(word[i])
        return ret_list

    @staticmethod
    def sipk4_list_to_str(word: list):
        ret_list = []
        for i in range(len(word)):
            ret_list.append(word[i])
        return "".join(ret_list)

    @staticmethod
    def sipk4_matrix_multiplication(word: str, matrix: list):
        ret_list = []
        if len(word) != len(matrix):
            print("Err!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return ret_list
        for i in range(len(matrix[0])):
            result = "0"
            for j in range(len(matrix)):
                mult = SSf.SIPK_SSCTV_functions.multiplication(
                    word[j], matrix[j][i])
                result = SSf.SIPK_SSCTV_functions.sum_mod_2(result, mult)
            ret_list.append(result)
        return ret_list

    @staticmethod
    def sipk4_matrix_concatenate(matrix1: list, matrix2: list,
                                 vertically: bool = False):
        ret_matrix = []
        def append_as_matrix(matrix: list):
            nonlocal ret_matrix
            for i in range(len(matrix)):
                ret_matrix.append(matrix[i])
        
        def append_as_list(matrix_list: list):
            nonlocal ret_matrix
            ret_matrix.append(matrix_list)

        def append(matrix: list):
            nonlocal ret_matrix
            if isinstance(matrix[0], list):
                append_as_matrix(matrix)
            else:
                append_as_list(matrix)

        if not vertically:
            matrix1 = SSf.SIPK_SSCTV_functions.transpose_list(matrix1)
            matrix2 = SSf.SIPK_SSCTV_functions.transpose_list(matrix2)
        append(matrix1)
        append(matrix2)
        if not vertically:
            ret_matrix = SSf.SIPK_SSCTV_functions.transpose_list(ret_matrix)
        return ret_matrix

    @staticmethod
    def make_sipk4(scene: M.Scene):
        var_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 3, 9: 5, 0: 7}
        SIPK.sipk3_hemming_example(scene)
        compare_row = SIPK.sipk4_fvh[var_dict[SIPK.sipk4_5_6_7_in_group_list % 10]]
        SIPK.sipk4_table_1(scene, compare_row)
        SIPK.sipk4_table_1(scene, SIPK.sipk4_make_mistake(compare_row, 1))
        SIPK.sipk4_table_1(scene, SIPK.sipk4_make_mistake(compare_row, 2))
        SIPK.sipk4_table_1(scene, SIPK.sipk4_make_mistake(compare_row, 3))
        SIPK.sipk4_table_2(scene)
        SIPK.sipk4_check_linear(scene)
        SIPK.sipk4_formula_1(scene)
        SIPK.sipk4_formula_2(scene)
        SIPK.sipk4_formula_3(scene)
        SIPK.sipk4_check_orthogonal(scene)
        SIPK.sipk4_formula_4(scene)
        SIPK.sipk4_formula_5(scene)
        SIPK.sipk4_table_3(scene)
        SIPK.sipk4_table_4(scene)

    @staticmethod
    def sipk4_table_1(scene: M.Scene, compare_row: str):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        fs = 36.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data = []
        highlighted = []
        for i in range(len(SIPK.sipk4_fvh)):
            err = 0
            table_data.append([])
            for j in range(len(SIPK.sipk4_fvh[0])):
                if compare_row[j] != SIPK.sipk4_fvh[i][j]:
                    highlighted.append((i + 2, j + 2))
                    err += 1
                table_data[-1].append(str(SIPK.sipk4_fvh[i][j]))
            table_data[-1].append(str(err))
        table = SSf.Table(
            table_data,
            row_labels = [M.MathTex(str(i), font_size = fs, color = mc)
                          for i in range(8)],
            col_labels = [
                M.MathTex("F", font_size = fs, color = mc),
                M.MathTex("V", font_size = fs, color = mc),
                M.MathTex("H", font_size = fs, color = mc),
                M.MathTex("P3", font_size = fs, color = mc),
                M.MathTex("P2", font_size = fs, color = mc),
                M.MathTex("P1", font_size = fs, color = mc),
                M.MathTex("P0", font_size = fs, color = mc),
                M.MathTex("d_n", font_size = fs, color = mc)],
            top_left_entry = M.MathTex("No", font_size = fs, color = mc),
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.8,
            element_to_mobject_config = {"font_size": 20.0, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        for cell in highlighted:
            table.add_highlighted_cell(cell, color = "#BBBBBB")
        str_code = "Кодовое слово: " + compare_row
        txt = M.Text(str_code, font_size = 30.0, color = mc).next_to(table, M.DOWN)
        scene.add(table, txt)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk4_table_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        fs = 36.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data = []
        start_word = SIPK.sipk4_5_6_7_in_group_list * 7
        if start_word > 127: start_word -= 127
        print(start_word)
        print(SSf.SIPK_SSCTV_functions.fill_zeros(bin(start_word)[2:], 7))
        for i in range(12):
            table_data.append([])
            code_word = SSf.SIPK_SSCTV_functions.fill_zeros(
                bin((start_word + i) % 128)[2:], 7)
            err = 7
            err_index = 0
            for j in range(len(SIPK.sipk4_fvh)):
                err_new = SIPK.sipk4_hemming_distance(code_word, SIPK.sipk4_fvh[j])
                if err_new < err:
                    err = err_new
                    err_index = j
            for j in range(len(code_word)):
                table_data[-1].append(code_word[j])
            if err <= 1:
                table_data[-1].append("0")
                table_data[-1].append(SIPK.sipk4_fvh[err_index][0])
                table_data[-1].append(SIPK.sipk4_fvh[err_index][1])
                table_data[-1].append(SIPK.sipk4_fvh[err_index][2])
            else:
                table_data[-1].append("1")
                table_data[-1].append("-")
                table_data[-1].append("-")
                table_data[-1].append("-")
        table = SSf.Table(
            table_data,
            row_labels = [M.MathTex(str(i), font_size = fs, color = mc)
                          for i in range(1, 13, 1)],
            col_labels = [
                M.MathTex("F", font_size = fs, color = mc),
                M.MathTex("V", font_size = fs, color = mc),
                M.MathTex("H", font_size = fs, color = mc),
                M.MathTex("P3", font_size = fs, color = mc),
                M.MathTex("P2", font_size = fs, color = mc),
                M.MathTex("P1", font_size = fs, color = mc),
                M.MathTex("P0", font_size = fs, color = mc),
                M.MathTex("Error", font_size = fs, color = mc),
                M.MathTex("F_{dec}", font_size = fs, color = mc),
                M.MathTex("V_{dec}", font_size = fs, color = mc),
                M.MathTex("H_{dec}", font_size = fs, color = mc)],
            top_left_entry = M.MathTex("No", font_size = fs, color = mc),
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.6,
            element_to_mobject_config = {"font_size": 20.0, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk4_check_linear(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        num1_2 = []
        for j in range(6):
            num1 = random.randint(1, 7)
            num2 = random.randint(1, 7)
            while (num1, num2) in num1_2 or (num2, num1) in num1_2:
                num1 = random.randint(1, 7)
                num2 = random.randint(1, 7)
            while num1 == num2:
                num2 = random.randint(1, 7)
            num1_2.append((num1, num2))
            eq_text = ""
            for i in range(7):
                eq_text += SSf.SIPK_SSCTV_functions.sum_mod_2(
                    SIPK.sipk4_fvh[num1][i], SIPK.sipk4_fvh[num2][i])
            b1 = M.Text(SIPK.sipk4_fvh[num1], font_size = tts, color = mc).next_to(
                SSf.SIPK_SSCTV_functions.upper_side + j % 3 * M.DOWN * 2.2
                + M.LEFT * 3.0 + M.RIGHT * 6.0 * (j // 3), M.DOWN)
            b2 = M.Text(SIPK.sipk4_fvh[num2], font_size = tts, color = mc
                        ).next_to(b1, M.DOWN)
            eq = M.Text(eq_text, font_size = tts, color = mc).next_to(b2, M.DOWN)
            crc = M.Text("⊕", font_size = tts, color = mc).next_to(b1, M.DL, 0.03)
            ravn = M.Text("=", font_size = tts, color = mc).next_to(b2, M.DL, 0.08)
            scene.add(b1, b2, eq, crc, ravn)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk4_formula_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SIPK.sipk4_matrix_fs
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"G = "
        tex = M.MathTex(tx, font_size = txs, color = mc)
        mx = [SIPK.sipk4_str_to_list(SIPK.sipk4_fvh[i]) for i in [4, 2, 1]]
        SIPK.sipk4_matrix_G = mx
        m = Matrix(mx, element_to_mobject_config = {"font_size": txs, "color": mc},
                   bracket_config = {"color": mc}).next_to(tex)
        g = M.VGroup(tex, m).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"v = u \cdot G"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(g, M.DOWN)
        tx3 = r"s = e \cdot H^T"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        tx4 = r"G_{k \times n} = \left( P_{k \times (n-k)}\ I_{k} \right)"
        tex4 = M.MathTex(tx4, font_size = txs, color = mc).next_to(tex3, M.DOWN)
        tx5 = r"H_{(n-k) \times k} = \left( I_{n-k}\ P_{k \times (n-k)}^T \right)"
        tex5 = M.MathTex(tx5, font_size = txs, color = mc).next_to(tex4, M.DOWN)
        tx6 = r"s = v \cdot H^T"
        tex6 = M.MathTex(tx6, font_size = txs, color = mc).next_to(tex5, M.DOWN)
        tx7 = r"s = v^{'} \cdot H^T = (v + e) \cdot H^T = "
        tx7 += r"v \cdot H^T + e \cdot H^T = e \cdot H^T"
        tex7 = M.MathTex(tx7, font_size = txs, color = mc).next_to(tex6, M.DOWN)
        tx8 = r"v = v^{'} + e"
        tex8 = M.MathTex(tx8, font_size = txs, color = mc).next_to(tex7, M.DOWN)
        scene.add(g, tex2, tex3, tex4, tex5, tex6, tex7, tex8)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk4_formula_2(scene: M.Scene):
        txs = SIPK.sipk4_matrix_fs
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        mx = SIPK.sipk4_matrix_G
        m = Matrix(mx, element_to_mobject_config = {"font_size": txs, "color": mc},
                   bracket_config = {"color": mc})
        for j in range(2):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            prev = SSf.SIPK_SSCTV_functions.upper_side
            for i in range(4):
                tex = M.MathTex(r"v_" + str(i + j * 4) + r" = ",
                                font_size = txs, color = mc)
                tx2 = r"\left( \ "
                code_v = SSf.SIPK_SSCTV_functions.fill_zeros(bin(i + j * 4)[2:], 3)
                for ch in code_v:
                    tx2 += ch + r"\ "
                tx2 += r"\right) \ \cdot "
                tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex)
                m_copy = m.copy()
                m_copy.next_to(tex2)
                tx3 = r" = \ \left( \ "
                for ch in SIPK.sipk4_matrix_multiplication(code_v, mx):
                    tx3 += ch + r"\ "
                tx3 += r"\right)"
                tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(m_copy)
                g = M.VGroup(tex, tex2, m_copy, tex3).next_to(prev, M.DOWN, 0.4)
                scene.add(g)
                prev = g
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk4_formula_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SIPK.sipk4_matrix_fs
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"H = "
        tex = M.MathTex(tx, font_size = txs, color = mc)
        mx = SSf.SIPK_SSCTV_functions.transpose_list(SIPK.sipk4_matrix_G)[3:]
        dm = SSf.SIPK_SSCTV_functions.diag_ones_matrix(4)
        mx = SIPK.sipk4_matrix_concatenate(mx, dm)
        SIPK.sipk4_matrix_H = mx
        m = Matrix(mx, element_to_mobject_config = {"font_size": txs, "color": mc},
                   bracket_config = {"color": mc}).next_to(tex)
        g = M.VGroup(tex, m).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(g)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk4_check_orthogonal(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        for i in range(len(SIPK.sipk4_matrix_G)):
            for j in range(len(SIPK.sipk4_matrix_H)):
                eq_text = ""
                for k in range(7):
                    eq_text += SSf.SIPK_SSCTV_functions.multiplication(
                        SIPK.sipk4_matrix_G[i][k], SIPK.sipk4_matrix_H[j][k])
                b1 = M.Text(
                    "".join(SIPK.sipk4_matrix_G[i]),
                    font_size = tts, color = mc).next_to(
                    SSf.SIPK_SSCTV_functions.upper_side + j * M.DOWN * 2.0
                    + M.LEFT * 3.6 + M.RIGHT * 3.6 * i, M.DOWN)
                b2 = M.Text(
                    "".join(SIPK.sipk4_matrix_H[j]),
                    font_size = tts, color = mc).next_to(b1, M.DOWN)
                eq = M.Text(eq_text, font_size = tts, color = mc
                            ).next_to(b2, M.DOWN)
                crc = M.Text("×", font_size = tts, color = mc
                             ).next_to(b1, M.DL, 0.03)
                ravn = M.Text("=", font_size = tts, color = mc
                              ).next_to(b2, M.DL, 0.08)
                scene.add(b1, b2, eq, crc, ravn)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk4_formula_4(scene: M.Scene):
        txs = SIPK.sipk4_matrix_fs
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        mht = SSf.SIPK_SSCTV_functions.transpose_list(SIPK.sipk4_matrix_H)
        m = Matrix(mht, element_to_mobject_config = {"font_size": txs, "color": mc},
                   bracket_config = {"color": mc})
        dm = SSf.SIPK_SSCTV_functions.diag_ones_matrix(7)
        for j in range(4):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            prev = SSf.SIPK_SSCTV_functions.upper_side
            for i in range(2):
                if j == 3 and i == 1: continue
                tex = M.MathTex(r"s_" + str(1 + i + j * 2) + r" = ",
                                font_size = txs, color = mc)
                tx2 = r"\left( \ "
                code_e = SIPK.sipk4_list_to_str(dm[6 - i - j * 2])
                for ch in code_e:
                    tx2 += ch + r"\ "
                tx2 += r"\right) \ \cdot "
                tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex)
                m_copy = m.copy()
                m_copy.next_to(tex2)
                tx3 = r" = \ \left( \ "
                for ch in SIPK.sipk4_matrix_multiplication(code_e, mht):
                    tx3 += ch + r"\ "
                tx3 += r"\right)"
                tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(m_copy)
                g = M.VGroup(tex, tex2, m_copy, tex3).next_to(prev, M.DOWN, 0.4)
                scene.add(g)
                prev = g
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk4_formula_5(scene: M.Scene):
        txs = SIPK.sipk4_matrix_fs
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        mht = SSf.SIPK_SSCTV_functions.transpose_list(SIPK.sipk4_matrix_H)
        m = Matrix(mht, element_to_mobject_config = {"font_size": txs, "color": mc},
                   bracket_config = {"color": mc})
        start_word = SIPK.sipk4_5_6_7_in_group_list * 7
        if start_word > 127: start_word -= 127
        SSf.SIPK_SSCTV_functions.fill_zeros(bin(start_word)[2:], 7)
        dm = [SIPK.sipk4_str_to_list(
            SSf.SIPK_SSCTV_functions.fill_zeros(bin((start_word + i) % 128)[2:], 7))
            for i in range(12)]
        for j in range(6):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            prev = SSf.SIPK_SSCTV_functions.upper_side
            for i in range(2):
                code_word = (start_word + i + j * 2) % 128
                tex = M.MathTex(r"s_{" + str(code_word) + r"} = ",
                                font_size = txs, color = mc)
                tx2 = r"\left( \ "
                code_e = SIPK.sipk4_list_to_str(dm[i + j * 2])
                for ch in code_e:
                    tx2 += ch + r"\ "
                tx2 += r"\right) \ \cdot "
                tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex)
                m_copy = m.copy()
                m_copy.next_to(tex2)
                tx3 = r" = \ \left( \ "
                mm = SIPK.sipk4_matrix_multiplication(code_e, mht)
                SIPK.sipk4_sindromes.append(mm)
                for ch in mm:
                    tx3 += ch + r"\ "
                tx3 += r"\right)"
                tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(m_copy)
                g = M.VGroup(tex, tex2, m_copy, tex3).next_to(prev, M.DOWN, 0.4)
                scene.add(g)
                prev = g
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk4_table_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        fs = 36.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data = []
        start_word = SIPK.sipk4_5_6_7_in_group_list * 7
        if start_word > 127: start_word -= 127
        mht = SSf.SIPK_SSCTV_functions.transpose_list(SIPK.sipk4_matrix_H)
        for i in range(12):
            table_data.append([])
            code_word = SSf.SIPK_SSCTV_functions.fill_zeros(
                bin((start_word + i) % 128)[2:], 7)
            table_data[-1].append(code_word)
            sindrom = SIPK.sipk4_sindromes[i]
            table_data[-1].append(SIPK.sipk4_list_to_str(sindrom))
            if sindrom in mht:
                table_data[-1].append("0")
                index = mht.index(sindrom)
                code_word = SIPK.sipk4_inverse_bit(code_word, index)
                table_data[-1].append(code_word)
            elif sindrom == ["0", "0", "0", "0"]:
                table_data[-1].append("0")
                table_data[-1].append(code_word)
            else:
                table_data[-1].append("1")
                table_data[-1].append("-")
        table = SSf.Table(
            table_data,
            row_labels = [M.MathTex(str(i), font_size = fs, color = mc)
                          for i in range(1, 13, 1)],
            col_labels = [
                M.MathTex("v^{'}", font_size = fs, color = mc),
                M.MathTex("s", font_size = fs, color = mc),
                M.MathTex("Error", font_size = fs, color = mc),
                M.MathTex("v", font_size = fs, color = mc)],
            top_left_entry = M.MathTex("No", font_size = fs, color = mc),
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.7,
            element_to_mobject_config = {"font_size": 20.0, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk4_table_4(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        fs = 36.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data = []
        mht = SSf.SIPK_SSCTV_functions.transpose_list(SIPK.sipk4_matrix_H)
        dm = SSf.SIPK_SSCTV_functions.diag_ones_matrix(7)
        for i in range(7):
            table_data.append(
                [SIPK.sipk4_list_to_str(dm[6 - i]),
                 SIPK.sipk4_list_to_str(mht[6 - i])])
        table = SSf.Table(
            table_data,
            col_labels = [M.MathTex("e", font_size = fs, color = mc),
                          M.MathTex("s", font_size = fs, color = mc)],
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.7,
            element_to_mobject_config = {"font_size": 20.0, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk5_bin_str_to_polinom(bin_str: str):
        return " + ".join(SIPK.sipk5_bin_str_to_polinom_list(bin_str))

    @staticmethod
    def sipk5_bin_str_to_polinom_list(bin_str: str):
        ret_list = []
        lb = len(bin_str)
        for i in range(lb):
            if bin_str[i] == "1":
                if i == lb - 1: ret_list.append(r"1")
                elif i == lb - 2: ret_list.append(r"x")
                else: ret_list.append(r"x^{" + str(lb - i - 1) + r"}")
            else:
                if i == lb - 1 and len(ret_list) == 0: ret_list.append(r"0")
        return ret_list

    @staticmethod
    def sipk5_polinom_to_bin_str(polinom: str):
        ret_list = []
        splited = polinom.split(r" + ")
        for i in range(len(splited)):
            lch = len(splited[i])
            if lch == 1:
                if splited[i] == "1":
                    ret_list.append(0)
                elif splited[i] == "x":
                    ret_list.append(1)
            elif lch == 5:
                ret_list.append(int(splited[i][3]))
            elif lch == 6:
                ret_list.append(int(splited[i][3:5]))
        ret_bin = ""
        for i in range(ret_list[0] + 1):
            if i in ret_list:
                ret_bin += "1"
            else:
                ret_bin += "0"
        return ret_bin[::-1]

    @staticmethod
    def sipk5_bin_str_multiplication(bin_str_1: str, bin_str_2: str):
        ret_str = ""
        lb_1 = len(bin_str_1)
        for i in range(lb_1):
            if bin_str_1[i] == "1":
                code = SSf.SIPK_SSCTV_functions.add_zeros(bin_str_2, lb_1 - i - 1)
                if ret_str == "": ret_str = code
                else:
                    ret_str = SSf.SIPK_SSCTV_functions.sum_mod_2_full(ret_str, code)
        return ret_str

    @staticmethod
    def sipk5_bin_str_division(divisible: str, divisor: str):
        polinom_list_full = []
        result_list = []
        divisor_list = SIPK.sipk5_bin_str_to_polinom_list(divisor)
        sb_divisible = SIPK.sipk5_senior_bit(divisible)
        sb_divisor = SIPK.sipk5_senior_bit(divisor)
        max_len = len(SIPK.sipk5_bin_str_to_polinom_list(divisible))
        offset = 0
        while sb_divisible >= sb_divisor:
            polinom_list_full.append([divisible, offset])
            integer_pow = sb_divisible - sb_divisor
            result_bin = SSf.SIPK_SSCTV_functions.add_zeros("1", integer_pow)
            result_list.append(SIPK.sipk5_bin_str_to_polinom_list(result_bin)[0])
            integer_part = SSf.SIPK_SSCTV_functions.add_zeros(divisor, integer_pow)
            polinom_list_full.append([integer_part, offset])
            polinom_list_len = len(SIPK.sipk5_bin_str_to_polinom_list(divisible))
            polinom_list_len2 = len(
                SIPK.sipk5_bin_str_to_polinom_list(integer_part))
            max_len = max(max_len, polinom_list_len + offset,
                          polinom_list_len2 + offset)
            divisible = SSf.SIPK_SSCTV_functions.sum_mod_2_full(
                divisible, integer_part)
            sb_divisible = SIPK.sipk5_senior_bit(divisible)
            offset += 1
        polinom_list_len = len(SIPK.sipk5_bin_str_to_polinom_list(divisible))
        max_len = max(max_len, polinom_list_len + offset) + 1
        polinom_list_full.append([divisible, max_len - polinom_list_len - 1])
        max_len_full = max_len
        if len(result_list) >= len(divisor_list):
            max_len_full += len(result_list)
            for j in range(len(result_list) - len(divisor_list)):
                divisor_list.append(r"")
        else:
            max_len_full += len(divisor_list)
            for j in range(len(divisor_list) - len(result_list)):
                result_list.append(r"")
        ret_list = []
        for i in range(len(polinom_list_full)):
            row = []
            polinom_list = SIPK.sipk5_bin_str_to_polinom_list(
                polinom_list_full[i][0])
            for j in range(polinom_list_full[i][1]):
                row.append(r"")
            for j in range(len(polinom_list)):
                if j == 0: row.append(polinom_list[j])
                else: row.append(r" + " + polinom_list[j])
            for j in range(max_len - polinom_list_full[i][1] - len(polinom_list)):
                if j == max_len - polinom_list_full[i][1] - len(polinom_list) - 1:
                    row.append(r"|")
                else:
                    row.append(r"")
            for j in range(max_len_full - max_len):
                if j == 0:
                    if i == 0:
                        row.append(divisor_list[j])
                    elif i == 1:
                        row.append(result_list[j])
                    else:
                        row.append(r"")
                else:
                    if i == 0 and divisor_list[j] != r"":
                        row.append(r"+ " + divisor_list[j])
                    elif i == 1 and result_list[j] != r"":
                        row.append(r"+ " + result_list[j])
                    else:
                        row.append(r"")
            ret_list.append(row)
        return ret_list

    @staticmethod
    def sipk5_bin_1_0_str_division(divisible: str, divisor: str):
        list_1_0_full = []
        result_list = []
        divisor_list = SIPK.sipk4_str_to_list(divisor)
        sb_divisible = SIPK.sipk5_senior_bit(divisible)
        sb_divisible_prev = sb_divisible
        sb_divisor = SIPK.sipk5_senior_bit(divisor)
        max_len = len(divisible) + 1
        offset = len(divisible) - sb_divisible - 1
        while sb_divisible >= sb_divisor:
            list_1_0_full.append([divisible, 0])
            integer_pow = sb_divisible - sb_divisor
            integer_part = SSf.SIPK_SSCTV_functions.add_zeros(divisor, integer_pow)
            list_1_0_full.append([integer_part, offset])
            divisible = SSf.SIPK_SSCTV_functions.sum_mod_2_full(
                divisible, integer_part)
            sb_divisible = SIPK.sipk5_senior_bit(divisible)
            offset += sb_divisible_prev - sb_divisible
            result_list.append("1")
            if sb_divisible >= sb_divisor:
                for i in range(sb_divisible_prev - sb_divisible - 1):
                    result_list.append("0")
            else:
                for i in range(sb_divisible_prev - 4):
                    result_list.append("0")
            sb_divisible_prev = sb_divisible
        list_1_0_full.append([divisible, 0])
        max_len_full = max_len
        max_len_full += len(result_list)
        for j in range(len(result_list) - len(divisor_list)):
            divisor_list.append(r"")
        ret_list = []
        for i in range(len(list_1_0_full)):
            row = []
            bin_list = SIPK.sipk4_str_to_list(list_1_0_full[i][0])
            for j in range(list_1_0_full[i][1]):
                row.append(r"")
            yet_1_wasnt = True
            curr_j = 0
            for j in range(len(bin_list)):
                if bin_list[j] == "0" and yet_1_wasnt:
                    if i == len(list_1_0_full) - 1 and j >= len(bin_list) - 4:
                        row.append(r"0")
                    elif i == 0:
                        row.append(r"0")
                    else:
                        row.append(r"")
                elif bin_list[j] == "1" and yet_1_wasnt:
                    yet_1_wasnt = False
                    row.append(bin_list[j])
                else:
                    if i == 0:
                        row.append(bin_list[j])
                    elif curr_j <= 3:
                        curr_j += 1
                        row.append(bin_list[j])
                    else:
                        row.append(r"")
            for j in range(max_len - list_1_0_full[i][1] - len(bin_list)):
                if j == max_len - list_1_0_full[i][1] - len(bin_list) - 1:
                    row.append(r"|")
                else:
                    row.append(r"")
            for j in range(max_len_full - max_len):
                if i == 0:
                    row.append(divisor_list[j])
                elif i == 1:
                    row.append(result_list[j])
                else:
                    row.append(r"")
            ret_list.append(row)
        return ret_list

    @staticmethod
    def sipk5_senior_bit(bin_str: str):
        for i in range(len(bin_str)):
            if bin_str[i] == "1":
                return len(bin_str) - i - 1
        return -1

    @staticmethod
    def sipk5_is_zero(bin_str: str):
        for i in range(len(bin_str)):
            if bin_str[i] == "1": return False
        return True

    @staticmethod
    def make_sipk5(scene: M.Scene):
        SIPK.sipk5_formula_1(scene)
        SIPK.sipk5_formula_2(scene)
        SIPK.sipk5_table_1(scene)
        SIPK.sipk5_formula_3(scene)
        SIPK.sipk5_table_2(scene)
        SIPK.sipk5_formula_4(scene)
        SIPK.sipk5_table_3(scene)
        SIPK.sipk5_formula_5(scene)
        SIPK.sipk5_formula_6(scene)
        SIPK.sipk5_formula_7(scene)

    @staticmethod
    def sipk5_formula_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        variant = SIPK.sipk4_5_6_7_in_group_list
        if variant >= 31: variant -= 30
        if variant >= 15: variant -= 14
        if variant >= 15: variant -= 14
        variant_bin = SSf.SIPK_SSCTV_functions.fill_zeros(bin(variant)[2:], 4)
        variant_polinom = SIPK.sipk5_bin_str_to_polinom(variant_bin)
        g_x = 11
        g_x_bin = bin(g_x)[2:]
        g_x_polinom = SIPK.sipk5_bin_str_to_polinom(g_x_bin)
        V_x_bin = SIPK.sipk5_bin_str_multiplication(variant_bin, g_x_bin)
        V_x_bin = SSf.SIPK_SSCTV_functions.fill_zeros(V_x_bin, 7)
        V_x_polinom = SIPK.sipk5_bin_str_to_polinom(V_x_bin)
        tx = str(variant) + r"_{10} = " + variant_bin + r"_{2},\ U(x) = "
        tx += variant_polinom
        tex = M.MathTex(tx, font_size = txs, color = mc
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"V(x) = U(x) \cdot g(x) = (" + variant_polinom
        tx2 += r") \cdot (" + g_x_polinom + r") = "
        tx2 += V_x_polinom
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        divisible = V_x_bin
        divisor = g_x_bin
        txt = M.Text("Число: " + divisible, font_size = 20.0, color = mc)
        table_data = SIPK.sipk5_bin_str_division(divisible, divisor)
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1})
        divisible = SIPK.sipk4_make_mistake(V_x_bin, 1)
        txt2 = M.Text("Число: " + divisible, font_size = 20.0, color = mc)
        table_data2 = SIPK.sipk5_bin_str_division(divisible, divisor)
        table2 = SSf.Table(
            table_data2,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1})
        grp = M.VGroup(table, table2).arrange(buff = 1.5).shift(M.DOWN)
        txt.next_to(table, M.UP)
        txt2.next_to(table2, M.UP)
        scene.add(tex, tex2, grp, txt, txt2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk5_formula_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        variant = SIPK.sipk4_5_6_7_in_group_list
        if variant >= 31: variant -= 30
        if variant >= 15: variant -= 14
        if variant >= 15: variant -= 14
        variant_bin = bin(variant)[2:]
        variant_bin = SSf.SIPK_SSCTV_functions.add_zeros(variant_bin, 3)
        variant_polinom = SIPK.sipk5_bin_str_to_polinom(variant_bin)
        g_x = 11
        g_x_bin = bin(g_x)[2:]
        tx = r"x^3 \cdot U(x) = " + variant_polinom
        tex = M.MathTex(tx, font_size = txs, color = mc
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        divisible = variant_bin
        divisor = g_x_bin
        table_data = SIPK.sipk5_bin_str_division(divisible, divisor)
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}
            ).next_to(tex, M.DOWN, 0.5)
        remainder_list = []
        for char in table_data[-1]:
            if char != r"" and char != r"|":
                remainder_list.append(char)
        remainder_polinom = "".join(remainder_list)
        V_s_x_polinom = variant_polinom + " + " + remainder_polinom
        tx2 = r"V_{s}(x) = " + V_s_x_polinom
        tex2 = M.MathTex(tx2, font_size = txs, color = mc
                         ).next_to(table, M.DOWN, 0.5)
        scene.add(tex, tex2, table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        V_s_x_bin = SIPK.sipk5_polinom_to_bin_str(V_s_x_polinom)
        SIPK.sipk5_V_s_x_bin = SSf.SIPK_SSCTV_functions.fill_zeros(V_s_x_bin, 7)
        table_data = SIPK.sipk5_bin_str_division(V_s_x_bin, g_x_bin)
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk5_table_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        fs = 20.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        variant = SIPK.sipk4_5_6_7_in_group_list
        if variant >= 31: variant -= 30
        if variant >= 15: variant -= 14
        if variant >= 15: variant -= 14
        variant_bin = SSf.SIPK_SSCTV_functions.fill_zeros(bin(variant)[2:], 4)
        table_data = []
        e = "0"
        d = "0"
        v = "0"
        a = "0"
        b = "0"
        g = "0"
        for i in range(5):
            e = d
            d = g
            v = b
            if i == 4:
                a = b = g = "-"
            else:
                a = variant_bin[i]
                b = SSf.SIPK_SSCTV_functions.sum_mod_2(a, e)
                g = SSf.SIPK_SSCTV_functions.sum_mod_2(b, v)
            table_data.append([a, b, v, g, d, e])
        table = SSf.Table(
            table_data,
            col_labels = [
                M.Text("а", font_size = fs, color = mc),
                M.Text("б", font_size = fs, color = mc),
                M.Text("в", font_size = fs, color = mc),
                M.Text("г", font_size = fs, color = mc),
                M.Text("д", font_size = fs, color = mc),
                M.Text("е", font_size = fs, color = mc)],
            row_labels = [
                M.Text(str(i), font_size = fs, color = mc) for i in range(5)],
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.6,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk5_formula_3(scene: M.Scene):
        g_x = 11
        g_x_bin = bin(g_x)[2:]
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        for i in range(7):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            divisible = SSf.SIPK_SSCTV_functions.add_zeros("1", i)
            tx = r"e_{" + str(i) + r"} = "
            tx += SIPK.sipk5_bin_str_to_polinom(divisible)
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
            table_data = SIPK.sipk5_bin_str_division(divisible, g_x_bin)
            table = SSf.Table(
                table_data,
                include_outer_lines = True,
                v_buff = 0.2,
                h_buff = 0.25,
                element_to_mobject = M.MathTex,
                element_to_mobject_config = {"font_size": 24.0, "color": mc},
                line_config = {"color": mc, "stroke_width": 1}
                ).next_to(tex, M.DOWN)
            scene.add(table, tex)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk5_table_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        fs = 20.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data = []
        e = SIPK.sipk5_V_s_x_bin[0]
        d = SIPK.sipk5_V_s_x_bin[1]
        v = SIPK.sipk5_V_s_x_bin[2]
        a = SIPK.sipk5_V_s_x_bin[3]
        b = SSf.SIPK_SSCTV_functions.sum_mod_2(a, e)
        g = SSf.SIPK_SSCTV_functions.sum_mod_2(v, e)
        for i in range(5):
            table_data.append([a, b, v, g, d, e])
            e = d
            d = g
            v = b
            if i >= 3:
                if i == 3: SIPK.sipk5_vde = v + d + e
                a = b = g = "-"
            else:
                a = SIPK.sipk5_V_s_x_bin[4 + i]
                b = SSf.SIPK_SSCTV_functions.sum_mod_2(a, e)
                g = SSf.SIPK_SSCTV_functions.sum_mod_2(v, e)
        table = SSf.Table(
            table_data,
            col_labels = [
                M.Text("а", font_size = fs, color = mc),
                M.Text("б", font_size = fs, color = mc),
                M.Text("в", font_size = fs, color = mc),
                M.Text("г", font_size = fs, color = mc),
                M.Text("д", font_size = fs, color = mc),
                M.Text("е", font_size = fs, color = mc)],
            row_labels = [
                M.Text(str(i), font_size = fs, color = mc) for i in range(5)],
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.6,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk5_formula_4(scene: M.Scene):
        g_x = 11
        g_x_bin = bin(g_x)[2:]
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mistake_1 = random.randint(0, 3)
        SIPK.sipk5_mistake_1 = mistake_1
        divisible = SIPK.sipk4_inverse_bit(SIPK.sipk5_V_s_x_bin, mistake_1)
        txt = M.Text(divisible, font_size = 20.0, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        table_data = SIPK.sipk5_bin_str_division(divisible, g_x_bin)
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}).next_to(txt, M.DOWN)
        scene.add(table, txt)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        sipk5_V_s_x_bin = SIPK.sipk5_V_s_x_bin
        SIPK.sipk5_V_s_x_bin = divisible
        SIPK.sipk5_table_2(scene)
        SIPK.sipk5_V_s_x_bin = sipk5_V_s_x_bin
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mistake_2 = random.randint(0, 6)
        while mistake_2 == mistake_1:
            mistake_2 = random.randint(0, 6)
        SIPK.sipk5_mistake_2 = mistake_2
        divisible = SIPK.sipk4_inverse_bit(SIPK.sipk5_V_s_x_bin, mistake_2)
        txt = M.Text(divisible, font_size = 20.0, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        table_data = SIPK.sipk5_bin_str_division(divisible, g_x_bin)
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}
            ).next_to(txt, M.DOWN)
        scene.add(table, txt)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        divisible = SIPK.sipk4_inverse_bit(SIPK.sipk5_V_s_x_bin, mistake_1)
        divisible = SIPK.sipk4_inverse_bit(divisible, mistake_2)
        txt = M.Text(divisible, font_size = 20.0, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        table_data = SIPK.sipk5_bin_str_division(divisible, g_x_bin)
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}
            ).next_to(txt, M.DOWN)
        scene.add(table, txt)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk5_table_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        fs = 20.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        V_s_x_bin_1 = SIPK.sipk4_inverse_bit(
            SIPK.sipk5_V_s_x_bin, SIPK.sipk5_mistake_1)
        table_data = []
        e = SIPK.sipk5_vde[2]
        d = SIPK.sipk5_vde[1]
        v = SIPK.sipk5_vde[0]
        j = "0"
        if e == "1" and d == "0" and v == "1": j = "1"
        a = j
        g = SSf.SIPK_SSCTV_functions.sum_mod_2(v, e)
        b = SSf.SIPK_SSCTV_functions.sum_mod_2(a, e)
        z = V_s_x_bin_1[0]
        i = SSf.SIPK_SSCTV_functions.sum_mod_2(j, z)
        for i_for in range(8):
            table_data.append([a, b, v, g, d, e, j, z, i])
            e = d
            d = g
            v = b
            j = "0"
            if e == "1" and d == "0" and v == "1": j = "1"
            a = j
            g = SSf.SIPK_SSCTV_functions.sum_mod_2(v, e)
            b = SSf.SIPK_SSCTV_functions.sum_mod_2(a, e)
            if i_for >= 6:
                z = i = "-"
            else:
                z = V_s_x_bin_1[i_for + 1]
                i = SSf.SIPK_SSCTV_functions.sum_mod_2(j, z)
        table = SSf.Table(
            table_data,
            col_labels = [
                M.Text("а", font_size = fs, color = mc),
                M.Text("б", font_size = fs, color = mc),
                M.Text("в", font_size = fs, color = mc),
                M.Text("г", font_size = fs, color = mc),
                M.Text("д", font_size = fs, color = mc),
                M.Text("е", font_size = fs, color = mc),
                M.Text("ж", font_size = fs, color = mc),
                M.Text("з", font_size = fs, color = mc),
                M.Text("и", font_size = fs, color = mc)],
            row_labels = [
                M.Text(str(i), font_size = fs, color = mc) for i in range(8)],
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.6,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk5_formula_5(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SIPK.sipk4_matrix_fs
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"H = "
        tex = M.MathTex(tx, font_size = txs, color = mc)
        mx = [["1", "1", "1", "0", "1", "0", "0"],
              ["0", "1", "1", "1", "0", "1", "0"],
              ["1", "1", "0", "1", "0", "0", "1"]]
        m = Matrix(mx, element_to_mobject_config = {"font_size": txs, "color": mc},
                   bracket_config = {"color": mc}).next_to(tex)
        g = M.VGroup(tex, m).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"H_r = "
        tex2 = M.MathTex(tx2, font_size = txs, color = mc)
        m0 = SIPK.sipk4_str_to_list("0" * len(mx))
        mh_list = SIPK.sipk4_matrix_concatenate(m0, mx)
        m1 = SIPK.sipk4_str_to_list("1" * len(mh_list[0]))
        mh_list = SIPK.sipk4_matrix_concatenate(m1, mh_list, True)
        SIPK.sipk5_Hr = mh_list
        mh = Matrix(mh_list,
                    element_to_mobject_config = {"font_size": txs, "color": mc},
                    bracket_config = {"color": mc}).next_to(tex2)
        gh = M.VGroup(tex2, mh).next_to(g, M.DOWN, 0.5)
        pcb = "0"
        for i in range(len(SIPK.sipk5_V_s_x_bin)):
            pcb = SSf.SIPK_SSCTV_functions.sum_mod_2(pcb, SIPK.sipk5_V_s_x_bin[i])
        SIPK.sipk5_V_s_x_bin = pcb + SIPK.sipk5_V_s_x_bin
        tex3 = M.MathTex(SIPK.sipk5_V_s_x_bin, font_size = txs, color = mc).next_to(
            gh, M.DOWN, 0.5)
        scene.add(g, gh, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk5_formula_6(scene: M.Scene):
        mhrt = SSf.SIPK_SSCTV_functions.transpose_list(SIPK.sipk5_Hr)
        word = SIPK.sipk5_V_s_x_bin
        SIPK.sipk_matrix_multiplication(scene, word, mhrt, r"s_0 = ")
        V_s1 = SIPK.sipk4_inverse_bit(word, SIPK.sipk5_mistake_1 + 1)
        SIPK.sipk_matrix_multiplication(scene, V_s1, mhrt, r"s_1 = ")
        V_s2 = SIPK.sipk4_inverse_bit(word, SIPK.sipk5_mistake_2 + 1)
        SIPK.sipk_matrix_multiplication(scene, V_s2, mhrt, r"s_2 = ")
        V_s12 = SIPK.sipk4_inverse_bit(V_s1, SIPK.sipk5_mistake_2 + 1)
        SIPK.sipk_matrix_multiplication(scene, V_s12, mhrt, r"s_{12} = ")

    @staticmethod
    def sipk_matrix_multiplication(
        scene: M.Scene, word: str, matrix: list, tx1: str):
        txs = SIPK.sipk4_matrix_fs
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        m = Matrix(matrix,
                   element_to_mobject_config = {"font_size": txs, "color": mc},
                   bracket_config = {"color": mc})
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tex = M.MathTex(tx1, font_size = txs, color = mc)
        tx2 = r"\left( \ "
        for ch in word:
            tx2 += ch + r"\ "
        tx2 += r"\right) \ \cdot "
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex)
        m_copy = m.copy()
        m_copy.next_to(tex2)
        tx3 = r" = \ \left( \ "
        for ch in SIPK.sipk4_matrix_multiplication(word, matrix):
            tx3 += ch + r"\ "
        tx3 += r"\right)"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(m_copy)
        g = M.VGroup(tex, tex2, m_copy, tex3).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(g)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk5_formula_7(scene: M.Scene):
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        g_x_bin = "10011"
        phone = random.randint(1, 9) * 1000 + random.randint(1, 9) * 100
        phone += random.randint(1, 9) * 10 + random.randint(1, 9)
        if SIPK.sipk5_phone != -1:
            phone = SIPK.sipk5_phone
        print(phone)
        crc_16_bit = ""
        for _ in range(4):
            num = phone % 10
            crc_16_bit = SSf.SIPK_SSCTV_functions.fill_zeros(
                bin(num)[2:], 4) + crc_16_bit
            phone = phone // 10
        print(crc_16_bit)
        divisor = g_x_bin
        for i in range(5):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            divisible = SIPK.sipk4_make_mistake(crc_16_bit, i)
            divisible_crc = r""
            for j in range(len(divisible)):
                divisible_crc += divisible[j]
                if j % 4 == 3:
                    divisible_crc += r"\ "
            tex = M.MathTex(divisible_crc, font_size = txs, color = mc
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
            table_data = SIPK.sipk5_bin_1_0_str_division(divisible, divisor)
            table = SSf.Table(
                table_data,
                include_outer_lines = True,
                v_buff = 0.16,
                h_buff = 0.32,
                element_to_mobject = M.MathTex,
                element_to_mobject_config = {"font_size": 24.0, "color": mc},
                line_config = {"color": mc, "stroke_width": 1}
                ).next_to(tex, M.DOWN)
            scene.add(tex, table)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_get_log_by_p(p: int, data_log_p: list):
        for i in range(len(data_log_p)):
            if data_log_p[i][1] == p:
                return data_log_p[i][0]
        return -1

    @staticmethod
    def sipk6_get_p_by_log(log: int, data_log_p: list):
        for i in range(len(data_log_p)):
            if data_log_p[i][0] == log:
                return data_log_p[i][1]
        return -1

    @staticmethod
    def sipk6_get_p1_by_p(p: int, data_log_p: list):
        for i in range(len(data_log_p)):
            if data_log_p[i][1] == p:
                return data_log_p[i][2]
        return -1

    @staticmethod
    def sipk6_polinom_to_log(polinom: str):
        ret_list = []
        splited = polinom.split(r" + ")
        for i in range(len(splited)):
            lch = len(splited[i])
            if lch == 1:
                if splited[i] == "1":
                    ret_list.append(0)
                elif splited[i] == "x":
                    ret_list.append(1)
            elif lch == 5:
                ret_list.append(int(splited[i][3]))
            elif lch == 6:
                ret_list.append(int(splited[i][3:5]))
        return ret_list

    @staticmethod
    def make_sipk6(scene: M.Scene):
        SIPK.sipk6_formula_1(scene)
        SIPK.sipk6_formula_2(scene)
        SIPK.sipk6_table_1(scene)
        SIPK.sipk6_table_2(scene)
        SIPK.sipk6_table_3(scene)
        SIPK.sipk6_formula_3(scene)
        SIPK.sipk6_formula_4(scene)
        SIPK.sipk6_formula_5(scene)
        SIPK.sipk6_formulas_9(scene)

    @staticmethod
    def sipk6_formula_1(scene: M.Scene):
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        variant = SIPK.sipk4_5_6_7_in_group_list
        if variant > 30: variant -= 30
        for i in range(2, 7, 1):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            prev = SSf.SIPK_SSCTV_functions.upper_side
            for j in range(7):
                number = i ** j
                tx = str(i) + r"^{" + str(j) + r"} = " + str(number)
                tx += r",\ " + str(number) + r" \bmod 7 = " + str(number % 7)
                tex = M.MathTex(tx, font_size = txs, color = mc
                                ).next_to(prev, M.DOWN)
                scene.add(tex)
                prev = tex
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_formula_2(scene: M.Scene):
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx = r"g(x) = x^8 + x^7 + x^6 + x^4 + 1"
        tex = M.MathTex(tx, font_size = txs, color = mc
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"NVar = NSp + (NGr - 1) \cdot 30"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"1 + {\sigma}_1 x + {\sigma}_2 x^2 = 0"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        mx = Matrix(
            [["S_1", "S_2"], ["S_2", "S_3"]],
            element_to_mobject_config = {"font_size": txs, "color": mc},
            bracket_config = {"color": mc})
        mx2 = Matrix(
            [[r"{\sigma}_2"], [r"{\sigma}_1"]],
            element_to_mobject_config = {"font_size": txs, "color": mc},
            bracket_config = {"color": mc})
        mx3 = Matrix(
            [[r"S_3"], [r"S_4"]],
            element_to_mobject_config = {"font_size": txs, "color": mc},
            bracket_config = {"color": mc})
        tex4 = M.MathTex(r" = ", font_size = txs, color = mc)
        gr = M.VGroup(mx, mx2, tex4, mx3).arrange().next_to(tex3, M.DOWN)
        scene.add(tex, tex2, tex3, gr)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_table_1(scene: M.Scene):
        data_log_p = [[0, 1], [1, 3], [2, 2], [3, 6], [4, 4], [5, 5], [6, 1]]
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        txs = 28.0
        txs_label = 36.0
        table_data1 = []
        table_data2 = []
        table_data3 = []
        for i in range(7):
            table_data1.append([str(data_log_p[i][0]), str(data_log_p[i][1])])
        for i in range(7):
            table_data2.append([])
            for j in range(7):
                table_data2[-1].append(str((i + j) % 7))
        for i in range(7):
            table_data3.append([])
            for j in range(7):
                if j == 0 or i == 0:
                    table_data3[-1].append("0")
                else:
                    table_data3[-1].append(
                        str(SIPK.sipk6_get_p_by_log(
                            (SIPK.sipk6_get_log_by_p(i, data_log_p)
                             + SIPK.sipk6_get_log_by_p(j, data_log_p)) % 6,
                             data_log_p)))
        table1 = SSf.Table(
            table_data1,
            col_labels = [M.MathTex(i, font_size = txs_label, color = mc)
                          for i in [r"log", r"p"]],
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.4,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": txs, "color": mc},
            line_config = {"color": mc, "stroke_width": 1})
        table2 = SSf.Table(
            table_data2,
            col_labels = [M.MathTex(str(i), font_size = txs_label, color = mc)
                          for i in range(7)],
            row_labels = [M.MathTex(str(i), font_size = txs_label, color = mc)
                          for i in range(7)],
            top_left_entry = M.MathTex(r"+", font_size = txs_label, color = mc),
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.4,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": txs, "color": mc},
            line_config = {"color": mc, "stroke_width": 1})
        table3 = SSf.Table(
            table_data3,
            col_labels = [M.MathTex(str(i), font_size = txs_label, color = mc)
                          for i in range(7)],
            row_labels = [M.MathTex(str(i), font_size = txs_label, color = mc)
                          for i in range(7)],
            top_left_entry = M.MathTex(
                r"\times", font_size = txs_label, color = mc),
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.4,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": txs, "color": mc},
            line_config = {"color": mc, "stroke_width": 1})
        gr = M.VGroup(table1, table2, table3).arrange(buff = 0.8).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(gr)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_table_2(scene: M.Scene):
        data_abc_by_var = {
            1: [1, 3, 6], 2: [2, 2, 5], 3: [3, 5, 4],
            4: [4, 6, 3], 5: [5, 4, 2], 6: [6, 5, 2],
            7: [5, 2, 3], 8: [4, 3, 4], 9: [3, 4, 5],
            10: [2, 6, 6], 11: [6, 6, 4], 12: [5, 2, 3],
            13: [4, 3, 2], 14: [3, 4, 5], 15: [2, 5, 3],
            16: [2, 6, 6], 17: [3, 5, 2], 18: [4, 4, 4],
            19: [5, 3, 5], 20: [6, 2, 6], 21: [5, 5, 3],
            22: [4, 4, 5], 23: [3, 2, 2], 24: [2, 3, 6],
            25: [6, 6, 4], 26: [5, 2, 5], 27: [4, 5, 2],
            28: [3, 3, 4], 29: [2, 6, 6], 30: [1, 4, 3]}
        data_log_p = [[0, 1], [1, 3], [2, 2], [3, 6], [4, 4], [5, 5], [6, 1]]
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        txs_label = 36.0
        variant = SIPK.sipk4_5_6_7_in_group_list
        if variant > 30: variant -= 30
        abc = data_abc_by_var[variant]
        table_data = [[r"NVar", r"a", r"b", r"c"],
                      [str(variant), *[str(i) for i in abc]]]
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.8,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": txs_label, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        bc = SIPK.sipk6_get_p_by_log(
                (SIPK.sipk6_get_log_by_p(abc[1], data_log_p)
                 + SIPK.sipk6_get_log_by_p(abc[2], data_log_p)) % 6, data_log_p)
        tx = r"d = " + str(abc[0]) + r" + " + str(abc[1]) + r" \times "
        tx += str(abc[2]) + r" = " + str(abc[0]) + r" + " + str(bc)
        tx += r" = " + str((abc[0] + bc) % 7)
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(table, M.DOWN, 0.6)
        scene.add(table, tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_table_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        txs = 24.0
        txs_label = 30.0
        table_data = [[r"-", r"0", r"0000", r"0", r"-", r"-"]]
        bin_V = r"0001"
        for i in range(15):
            table_data.append([
                r"{\alpha}^{" + str(i) + "}",
                str(SIPK.sipk5_bin_str_to_polinom(bin_V)),
                bin_V,
                str(int(bin_V, base = 2)),
                str(i)])
            SIPK.sipk6_log_p_16.append([i, int(bin_V, base = 2)])
            if i == 0:
                table_data[-1].append(r"1")
            bin_V = SSf.SIPK_SSCTV_functions.add_zeros(bin_V, 1)
            if bin_V[0] == "0":
                bin_V = bin_V[1:]
            elif bin_V[0] == "1":
                bin_V = bin_V[1:]
                bin_V = SIPK.sipk4_inverse_bit(bin_V, 2)
                bin_V = SIPK.sipk4_inverse_bit(bin_V, 3)
        SIPK.sipk6_log_p_16[0].append(int(table_data[1][3]))
        for i in range(14):
            table_data[2 + i].append(table_data[15 - i][3])
            SIPK.sipk6_log_p_16[1 + i].append(int(table_data[15 - i][3]))
        table = SSf.Table(
            table_data,
            col_labels = [M.MathTex(str(i), font_size = txs_label, color = mc)
                          for i in [r"{\alpha}^i", r"V(x)", r"Bin", r"Dec",
                                    r"log", r"{\alpha}^{-i}"]],
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.6,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": txs, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        table_data2 = []
        for i in range(15):
            table_data2.append([table_data[1 + i][0], table_data[1 + i][2]])
        table_data2 = SSf.SIPK_SSCTV_functions.transpose_list(table_data2)
        table = SSf.Table(
            table_data2,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": txs, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_formula_3(scene: M.Scene):
        data_ab_by_var = {
            1: [10, 9], 2: [11, 8], 3: [12, 7],
            4: [13, 6], 5: [14, 5], 6: [5, 14],
            7: [6, 13], 8: [7, 12], 9: [8, 11],
            10: [9, 10], 11: [5, 13], 12: [6, 13],
            13: [7, 11], 14: [8, 10], 15: [9, 9],
            16: [10, 8], 17: [11, 7], 18: [12, 6],
            19: [13, 5], 20: [14, 14], 21: [14, 7],
            22: [13, 8], 23: [12, 9], 24: [11, 10],
            25: [10, 6], 26: [9, 7], 27: [8, 14],
            28: [7, 11], 29: [6, 12], 30: [5, 13]}
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        txs_label = 36.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        variant = SIPK.sipk4_5_6_7_in_group_list
        if variant > 30: variant -= 30
        ab = data_ab_by_var[variant]
        table_data = [[r"NVar", r"a", r"b"],
                      [str(variant), *[str(i) for i in ab]]]
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.8,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": txs_label, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        a = SSf.SIPK_SSCTV_functions.fill_zeros(bin(ab[0])[2:], 4)
        b = SSf.SIPK_SSCTV_functions.fill_zeros(bin(ab[1])[2:], 4)
        a_log = SIPK.sipk6_get_log_by_p(ab[0], SIPK.sipk6_log_p_16)
        b_log = SIPK.sipk6_get_log_by_p(ab[1], SIPK.sipk6_log_p_16)
        mult = SIPK.sipk6_get_p_by_log((a_log + b_log) % 15, SIPK.sipk6_log_p_16)
        tx = r"a + b = " + str(ab[0]) + r" + " + str(ab[1])
        tx += r" = " + a + r" + " + b + r" = "
        tx += SSf.SIPK_SSCTV_functions.sum_mod_2_full(a, b) + r" = "
        tx += str(int(SSf.SIPK_SSCTV_functions.sum_mod_2_full(a, b), base = 2))
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(table, M.DOWN, 0.6)
        tx2 = r"a \times b = " + str(ab[0]) + r" \times " + str(ab[1])
        tx2 += r" = {\alpha}^{" + str(a_log) + r"} \times {\alpha}^{"
        tx2 += str(b_log) + r"} = {\alpha}^{(" + str(a_log) + r" + " + str(b_log)
        tx2 += r") \bmod 15} = {\alpha}^{" + str((a_log + b_log) % 15)
        tx2 += r"} = " + str(mult)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        scene.add(table, tex, tex2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_formula_4(scene: M.Scene):
        txs = 36.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        pows = [8, 7, 6, 4]
        for i_0 in range(2):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            prev = SSf.SIPK_SSCTV_functions.upper_side
            for i in range(2):
                matrx = []
                eql = r"0000"
                tx = r"g({\alpha}^" + str(i + i_0 * 2 + 1) + r") = "
                for j in pows:
                    tx += r"{\alpha}^{" + str((i + i_0 * 2 + 1) * j) + r"} + "
                    p = SIPK.sipk6_get_p_by_log(
                        ((i + i_0 * 2 + 1) * j) % 15, SIPK.sipk6_log_p_16)
                    p_bin = SSf.SIPK_SSCTV_functions.fill_zeros(bin(p)[2:], 4)
                    matrx.append(p_bin)
                    eql = SSf.SIPK_SSCTV_functions.sum_mod_2_full(eql, p_bin)
                tx += r" 1 = "
                p = SIPK.sipk6_get_p_by_log(0, SIPK.sipk6_log_p_16)
                p_bin = SSf.SIPK_SSCTV_functions.fill_zeros(bin(p)[2:], 4)
                matrx.append(p_bin)
                eql = SSf.SIPK_SSCTV_functions.sum_mod_2_full(eql, p_bin)
                matrx.append(eql)
                if not (i == 0 and i_0 == 0):
                    for j in pows:
                        tx += r"{\alpha}^{" + str(((i + i_0 * 2 + 1) * j) % 15)
                        tx += r"} + "
                    tx += r" 1 = "
                tex = M.MathTex(tx, font_size = txs, color = mc)
                m = Matrix(matrx,
                           element_to_mobject_config = {
                               "font_size": txs, "color": mc},
                           v_buff = 0.4, h_buff = 0.3)
                gr = M.VGroup(tex, m).arrange(buff = 0.5).next_to(prev, M.DOWN, 0.6)
                tex_eq = M.MathTex(r"=", font_size = txs, color = mc
                                   ).next_to(m, M.DL, - 0.3)
                tex_eq.shift(M.UP * 0.22)
                tex_op = M.MathTex(r"\bigoplus", font_size = 20.0, color = mc
                                   ).next_to(m, M.LEFT, - 0.3)
                tex_op.shift(M.UP * 0.2)
                prev = gr
                scene.add(gr, tex_eq, tex_op)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_formula_5(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        variant = SIPK.sipk4_5_6_7_in_group_list + 30 * (SIPK.sipk6_group - 1)
        if variant > 127: variant -= 127
        variant_bin = SSf.SIPK_SSCTV_functions.fill_zeros(bin(variant)[2:], 7)
        tx = str(variant) + r"_{10} = " + variant_bin + r"_2,\ u(x) = "
        tx += SIPK.sipk5_bin_str_to_polinom(variant_bin)
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        variant_bin = SSf.SIPK_SSCTV_functions.add_zeros(variant_bin, 8)
        variant_polinom = SIPK.sipk5_bin_str_to_polinom(variant_bin)
        g_x_bin = r"111010001"
        tx2 = r"x^8 \cdot u(x) = " + variant_polinom
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        divisible = variant_bin
        divisor = g_x_bin
        table_data = SIPK.sipk5_bin_str_division(divisible, divisor)
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}
            ).next_to(tex2, M.DOWN, 0.4)
        remainder_list = []
        for char in table_data[-1]:
            if char != r"" and char != r"|":
                remainder_list.append(char)
        remainder_polinom = "".join(remainder_list)
        V_s_x_polinom = variant_polinom + " + " + remainder_polinom
        scene.add(tex, tex2, table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx3 = r"v(x) = " + V_s_x_polinom
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        V_s_x_bin = SIPK.sipk5_polinom_to_bin_str(V_s_x_polinom)
        SIPK.sipk6_V_s_x_bin = SSf.SIPK_SSCTV_functions.fill_zeros(V_s_x_bin, 14)
        table_data = SIPK.sipk5_bin_str_division(V_s_x_bin, divisor)
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_formula_6(scene: M.Scene, V_s_x_bin: str):
        txs = 32.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        pows = SIPK.sipk6_polinom_to_log(
            SIPK.sipk5_bin_str_to_polinom(V_s_x_bin))
        SIPK.sipk6_sindroms = []
        for i in range(4):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            matrx = []
            eql = r"0000"
            str_i = str(i + 1)
            tx = r"S_" + str_i + r" = r({\alpha}^" + str_i + r") = "
            for j in pows:
                tx += r"{\alpha}^{" + str((i + 1) * j) + r"}"
                if j != pows[-1]:
                    tx += r" + "
                else:
                    tx += r" = "
                p = SIPK.sipk6_get_p_by_log(
                    ((i + 1) * j) % 15, SIPK.sipk6_log_p_16)
                p_bin = SSf.SIPK_SSCTV_functions.fill_zeros(bin(p)[2:], 4)
                matrx.append(p_bin)
                eql = SSf.SIPK_SSCTV_functions.sum_mod_2_full(eql, p_bin)
            if not (i == 0):
                tx += r"\\ = "
                for j in pows:
                    tx += r"{\alpha}^{" + str(((i  + 1) * j) % 15)
                    tx += r"}"
                    if j != pows[-1]:
                        tx += r" + "
                    else:
                        tx += r" = "
            matrx.append(eql)
            SIPK.sipk6_sindroms.append(eql)
            tex = M.MathTex(tx, font_size = txs, color = mc)
            m = Matrix(matrx,
                        element_to_mobject_config = {
                            "font_size": txs, "color": mc},
                        v_buff = 0.4, h_buff = 0.3)
            gr = M.VGroup(tex, m).arrange(buff = 0.6).next_to(
                SSf.SIPK_SSCTV_functions.upper_side + M.UP * 0.3, M.DOWN, 0.3)
            tex_eq = M.MathTex(r"=", font_size = txs, color = mc
                                ).next_to(m, M.DL, - 0.3)
            tex_eq.shift(M.UP * 0.21)
            tex_op = M.MathTex(r"\bigoplus", font_size = 20.0, color = mc
                                ).next_to(m, M.LEFT, - 0.3)
            tex_op.shift(M.UP * 0.19)
            scene.add(gr, tex_eq, tex_op)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_formula_7(scene: M.Scene, text: str):
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tex = M.MathTex(text, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_formula_8(scene: M.Scene):
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        SSf.SIPK_SSCTV_functions.make_background(scene)
        int_sindroms = []
        tx = r""
        for i in range(len(SIPK.sipk6_sindroms)):
            int_sindrom = int(SIPK.sipk6_sindroms[i], base = 2)
            int_sindroms.append(int_sindrom)
            tx += r"S_" + str(1 + i) + r" = " + str(int_sindrom)
            if i != len(SIPK.sipk6_sindroms) - 1:
                tx += r",\ "
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        mx = Matrix(
            [[str(int_sindroms[0]), str(int_sindroms[1])],
             [str(int_sindroms[1]), str(int_sindroms[2])]],
            element_to_mobject_config = {"font_size": txs, "color": mc},
            bracket_config = {"color": mc})
        mx2 = Matrix(
            [[r"{\sigma}_2"], [r"{\sigma}_1"]],
            element_to_mobject_config = {"font_size": txs, "color": mc},
            bracket_config = {"color": mc})
        mx3 = Matrix(
            [[str(int_sindroms[2])], [str(int_sindroms[3])]],
            element_to_mobject_config = {"font_size": txs, "color": mc},
            bracket_config = {"color": mc})
        tex2 = M.MathTex(r" = ", font_size = txs, color = mc)
        gr = M.VGroup(mx, mx2, tex2, mx3).arrange().next_to(tex, M.DOWN)
        tex3 = M.MathTex(r"\Delta = ", font_size = txs, color = mc)
        mx4 = Matrix(
            [[str(int_sindroms[0]), str(int_sindroms[1])],
             [str(int_sindroms[1]), str(int_sindroms[2])]],
            element_to_mobject_config = {"font_size": txs, "color": mc},
            bracket_config = {"color": mc},
            left_bracket = r"|", right_bracket = r"|")
        tx4 = r" = " + str(int_sindroms[0]) + r" \cdot " + str(int_sindroms[2])
        tx4 += r" + " + str(int_sindroms[1]) + r" \cdot " + str(int_sindroms[1])
        log_1 = SIPK.sipk6_get_log_by_p(int_sindroms[0], SIPK.sipk6_log_p_16)
        log_2 = SIPK.sipk6_get_log_by_p(int_sindroms[1], SIPK.sipk6_log_p_16)
        log_3 = SIPK.sipk6_get_log_by_p(int_sindroms[2], SIPK.sipk6_log_p_16)
        mult_1 = 0
        mult_2 = 0
        if log_1 != -1 and log_3 != -1:
            mult_1 = SIPK.sipk6_get_p_by_log(
                (log_1 + log_3) % 15, SIPK.sipk6_log_p_16)
        if log_2 != -1:
            mult_2 = SIPK.sipk6_get_p_by_log(
                (log_2 + log_2) % 15, SIPK.sipk6_log_p_16)
        summ = SSf.SIPK_SSCTV_functions.sum_mod_2_full(
            bin(mult_1)[2:], bin(mult_2)[2:])
        p = int(summ, base = 2)
        p1 = SIPK.sipk6_get_p1_by_p(p, SIPK.sipk6_log_p_16)
        tx4 += r" = " + str(mult_1) + r" + " + str(mult_2) + r" = "
        tx4 += str(p)
        tex4 = M.MathTex(tx4, font_size = txs, color = mc)
        gr2 = M.VGroup(tex3, mx4, tex4).arrange().next_to(gr, M.DOWN)
        scene.add(tex, gr, gr2)
        if p != 0:
            tx5 = r"{\Delta}^{-1} = " + str(p1)
            tex5 = M.MathTex(tx5, font_size = txs, color = mc).next_to(gr2, M.DOWN)
            scene.add(tex5)
            SIPK.sipk6_sindroms_int_p1 = [*int_sindroms, p1]
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_formulas_9(scene: M.Scene):
        data_mistake_by_var = {
            1: [13, 2], 2: [12, 3], 3: [11, 4],
            4: [10, 5], 5: [9, 6], 6: [8, 7],
            7: [7, 9], 8: [6, 10], 9: [5, 11],
            10: [4, 12], 11: [13, 6], 12: [12, 7],
            13: [11, 8], 14: [10, 9], 15: [9, 11],
            16: [8, 12], 17: [7, 13], 18: [6, 14],
            19: [5, 12], 20: [4, 13], 21: [13, 8],
            22: [12, 6], 23: [11, 4], 24: [10, 2],
            25: [9, 3], 26: [8, 5], 27: [7, 9],
            28: [6, 11], 29: [5, 13], 30: [4, 7]}
        variant = SIPK.sipk4_5_6_7_in_group_list
        if variant > 30: variant -= 30
        mistake2_nums = data_mistake_by_var[variant]
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = 36.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data = [[r"NSp", r"Err1", r"Err2"],
                      [str(variant),
                       r"x^{" + str(mistake2_nums[0]) + r"}",
                       r"x^{" + str(mistake2_nums[1]) + r"}"]]
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.8,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": txs, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SIPK.sipk6_formula_6(scene, SIPK.sipk6_V_s_x_bin)
        mistake_num = -1
        if mistake_num == -1:
            mistake_num = random.randint(0, 11)
        mistake = SIPK.sipk4_inverse_bit("0" * 15, mistake_num)
        V_s_x_bin_mistake = SSf.SIPK_SSCTV_functions.sum_mod_2_full(
            SIPK.sipk6_V_s_x_bin, mistake)
        t1 = r"e(x) = " + SIPK.sipk5_bin_str_to_polinom(mistake)
        SIPK.sipk6_formula_7(scene, t1)
        t2 = r"r(x) = " + SIPK.sipk5_bin_str_to_polinom(V_s_x_bin_mistake)
        SIPK.sipk6_formula_7(scene, t2)
        SIPK.sipk6_formula_6(scene, V_s_x_bin_mistake)
        SIPK.sipk6_formula_8(scene)
        mistake2_nums = [14 - mistake2_nums[0], 14 - mistake2_nums[1]]
        mistake2 = SIPK.sipk4_inverse_bit("0" * 15, mistake2_nums[0])
        mistake2 = SIPK.sipk4_inverse_bit(mistake2, mistake2_nums[1])
        V_s_x_bin_mistake2 = SSf.SIPK_SSCTV_functions.sum_mod_2_full(
            SIPK.sipk6_V_s_x_bin, mistake2)
        t3 = r"e(x) = " + SIPK.sipk5_bin_str_to_polinom(mistake2)
        SIPK.sipk6_formula_7(scene, t3)
        t4 = r"r(x) = " + SIPK.sipk5_bin_str_to_polinom(V_s_x_bin_mistake2)
        SIPK.sipk6_formula_7(scene, t4)
        SIPK.sipk6_formula_6(scene, V_s_x_bin_mistake2)
        SIPK.sipk6_formula_8(scene)
        SIPK.sipk6_formula_10(scene)
        SIPK.sipk6_table_4(scene)
        mistake3_nums = data_mistake_by_var[variant]
        mistake3rd = -1
        if mistake3rd == -1:
            mistake3rd = random.randint(0, 14)
            while mistake3rd == mistake3_nums[0] or mistake3rd == mistake3_nums[1]:
                mistake3rd = random.randint(0, 14)
        mistake3_nums = [14 - mistake3_nums[0],
                         14 - mistake3_nums[1],
                         14 - mistake3rd]
        mistake3 = SIPK.sipk4_inverse_bit("0" * 15, mistake3_nums[0])
        mistake3 = SIPK.sipk4_inverse_bit(mistake3, mistake3_nums[1])
        mistake3 = SIPK.sipk4_inverse_bit(mistake3, mistake3_nums[2])
        V_s_x_bin_mistake3 = SSf.SIPK_SSCTV_functions.sum_mod_2_full(
            SIPK.sipk6_V_s_x_bin, mistake3)
        t3 = r"e(x) = " + SIPK.sipk5_bin_str_to_polinom(mistake3)
        SIPK.sipk6_formula_7(scene, t3)
        t4 = r"r(x) = " + SIPK.sipk5_bin_str_to_polinom(V_s_x_bin_mistake3)
        SIPK.sipk6_formula_7(scene, t4)
        SIPK.sipk6_formula_6(scene, V_s_x_bin_mistake3)
        SIPK.sipk6_formula_8(scene)
        SIPK.sipk6_formula_10(scene)
        SIPK.sipk6_table_4(scene)

    @staticmethod
    def sipk6_formula_10(scene: M.Scene):
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        SSf.SIPK_SSCTV_functions.make_background(scene)
        sip1 = SIPK.sipk6_sindroms_int_p1
        log_1 = SIPK.sipk6_get_log_by_p(sip1[0], SIPK.sipk6_log_p_16)
        log_2 = SIPK.sipk6_get_log_by_p(sip1[1], SIPK.sipk6_log_p_16)
        log_3 = SIPK.sipk6_get_log_by_p(sip1[2], SIPK.sipk6_log_p_16)
        log_4 = SIPK.sipk6_get_log_by_p(sip1[3], SIPK.sipk6_log_p_16)
        log_5 = SIPK.sipk6_get_log_by_p(sip1[4], SIPK.sipk6_log_p_16)
        mult_1 = 0
        mult_2 = 0
        mult_3 = 0
        if log_3 != -1:
            mult_1 = SIPK.sipk6_get_p_by_log(
                (log_3 + log_3) % 15, SIPK.sipk6_log_p_16)
        if log_4 != -1 and log_2 != -1:
            mult_2 = SIPK.sipk6_get_p_by_log(
                (log_4 + log_2) % 15, SIPK.sipk6_log_p_16)
        summ = SSf.SIPK_SSCTV_functions.sum_mod_2_full(
            bin(mult_1)[2:], bin(mult_2)[2:])
        int_summ = int(summ, base = 2)
        log_summ = SIPK.sipk6_get_log_by_p(int_summ, SIPK.sipk6_log_p_16)
        if log_5 != -1 and log_summ != -1:
            mult_3 = SIPK.sipk6_get_p_by_log(
                (log_summ + log_5) % 15, SIPK.sipk6_log_p_16)
        sigma_2 = mult_3
        tex1 = M.MathTex(r"{\sigma}_2 = ", font_size = txs, color = mc)
        mx1 = Matrix(
            [[str(sip1[2]), str(sip1[1])], [str(sip1[3]), str(sip1[2])]],
            element_to_mobject_config = {"font_size": txs, "color": mc},
            bracket_config = {"color": mc},
            left_bracket = r"|", right_bracket = r"|")
        tx2 = r"\cdot \ " + str(sip1[4]) + r" = ("
        tx2 += str(sip1[2]) + r" \cdot " + str(sip1[2])
        tx2 += r" + " + str(sip1[3]) + r" \cdot " + str(sip1[1]) + r") \cdot "
        tx2 += str(sip1[4])
        tx2 += r" = (" + str(mult_1) + r" + " + str(mult_2) + r") \cdot "
        tx2 += str(sip1[4]) + r" = " + str(int_summ) + r" \cdot " + str(sip1[4])
        tx2 += r" = " + str(mult_3)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc)
        gr = M.VGroup(tex1, mx1, tex2).arrange().next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(gr)
        mult_1 = 0
        mult_2 = 0
        mult_3 = 0
        if log_1 != -1 and log_4 != -1:
            mult_1 = SIPK.sipk6_get_p_by_log((log_1 + log_4) % 15, SIPK.sipk6_log_p_16)
        if log_2 != -1 and log_3 != -1:
            mult_2 = SIPK.sipk6_get_p_by_log((log_2 + log_3) % 15, SIPK.sipk6_log_p_16)
        summ = SSf.SIPK_SSCTV_functions.sum_mod_2_full(
            bin(mult_1)[2:], bin(mult_2)[2:])
        int_summ = int(summ, base = 2)
        log_summ = SIPK.sipk6_get_log_by_p(int_summ, SIPK.sipk6_log_p_16)
        if log_5 != -1 and log_summ != -1:
            mult_3 = SIPK.sipk6_get_p_by_log((log_summ + log_5) % 15, SIPK.sipk6_log_p_16)
        sigma_1 = mult_3
        SIPK.sipk6_sigmas = [sigma_1, sigma_2]
        tex1 = M.MathTex(r"{\sigma}_1 = ", font_size = txs, color = mc)
        mx1 = Matrix(
            [[str(sip1[0]), str(sip1[2])], [str(sip1[1]), str(sip1[3])]],
            element_to_mobject_config = {"font_size": txs, "color": mc},
            bracket_config = {"color": mc},
            left_bracket = r"|", right_bracket = r"|")
        tx2 = r"\cdot \ " + str(sip1[4]) + r" = ("
        tx2 += str(sip1[0]) + r" \cdot " + str(sip1[3])
        tx2 += r" + " + str(sip1[1]) + r" \cdot " + str(sip1[2]) + r") \cdot "
        tx2 += str(sip1[4])
        tx2 += r" = (" + str(mult_1) + r" + " + str(mult_2) + r") \cdot "
        tx2 += str(sip1[4]) + r" = " + str(int_summ) + r" \cdot " + str(sip1[4])
        tx2 += r" = " + str(mult_3)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc)
        gr2 = M.VGroup(tex1, mx1, tex2).arrange().next_to(gr, M.DOWN)
        tx3 = r"1 + " + str(sigma_1) + r" \cdot x + " + str(sigma_2)
        tx3 += r" \cdot x^2 = 0"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(gr2, M.DOWN)
        scene.add(gr2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk6_table_4(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        txs = 26.0
        txs_label = 30.0
        sgs = SIPK.sipk6_sigmas
        table_data = []
        eqt = r"1 + " + str(sgs[0]) + r" \cdot x + " + str(sgs[1])
        eqt += r" \cdot x^2"
        for i in range(14):
            x = SIPK.sipk6_log_p_16[1 + i][1]
            log = SIPK.sipk6_get_log_by_p(
                x, SIPK.sipk6_log_p_16)
            log2 = (log * 2) % 15
            log_s_1 = SIPK.sipk6_get_log_by_p(sgs[0], SIPK.sipk6_log_p_16)
            log_s_2 = SIPK.sipk6_get_log_by_p(sgs[1], SIPK.sipk6_log_p_16)
            x2 = SIPK.sipk6_get_p_by_log(log2, SIPK.sipk6_log_p_16)
            mult_1 = SIPK.sipk6_get_p_by_log(
                (log_s_1 + log) % 15, SIPK.sipk6_log_p_16)
            mult_2 = SIPK.sipk6_get_p_by_log(
                (log_s_2 + log2) % 15, SIPK.sipk6_log_p_16)
            summ = SSf.SIPK_SSCTV_functions.sum_mod_2_full(
                bin(mult_1)[2:], bin(mult_2)[2:])
            summ = SSf.SIPK_SSCTV_functions.sum_mod_2_full(summ, r"0001")
            int_summ = int(summ, base = 2)
            equation = r"1 + " + str(sgs[0]) + r" \cdot " + str(x) + r" + "
            equation += str(sgs[1]) + r" \cdot " + str(x2) + r" = 1 + "
            equation += str(mult_1) + r" + " + str(mult_2) + r" = "
            equation += str(int_summ)
            table_data.append(
                [r"{\alpha}^{" + str(1 + i) + "}", str(x), str(x2), equation])
        table = SSf.Table(
            table_data,
            col_labels = [M.MathTex(i, font_size = txs_label, color = mc)
                          for i in [r"", r"x", r"x^2", eqt]],
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.6,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": txs, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_sipk7(scene: M.Scene):
        SIPK.sipk7_formula_1(scene)
        SIPK.sipk7_diagram_2(scene)

    @staticmethod
    def sipk7_get_bits_by_state_and_bit(state: int, bit: str):
        bits = ""
        curr_state = 0
        if state == 0:
            if bit == "0":
                bits = "00"
                curr_state = 0
            elif bit == "1":
                bits = "11"
                curr_state = 1
        elif state == 1:
            if bit == "0":
                bits = "01"
                curr_state = 2
            elif bit == "1":
                bits = "10"
                curr_state = 3
        elif state == 2:
            if bit == "0":
                bits = "11"
                curr_state = 0
            elif bit == "1":
                bits = "00"
                curr_state = 1
        elif state == 3:
            if bit == "0":
                bits = "10"
                curr_state = 2
            elif bit == "1":
                bits = "01"
                curr_state = 3
        return (curr_state, bits)
    
    @staticmethod
    def sipk7_code_svert(bin_str: str):
        state = 0
        bits = ""
        for i in range(len(bin_str)):
            data = SIPK.sipk7_get_bits_by_state_and_bit(state, bin_str[i])
            state = data[0]
            bits += data[1]
        return (bits, state)
    
    @staticmethod
    def sipk7_add_spaces(bin_str: str, chars_row: int = 2):
        ret_str = ""
        row = 0
        for i in range(len(bin_str)):
            ret_str += bin_str[i]
            if row % chars_row == chars_row - 1:
                ret_str += r"\ "
            row += 1
        return ret_str
    
    @staticmethod
    def sipk7_formula_1(scene: M.Scene):
        from random import randint
        data_01_by_var = {
            1: "10110110", 2: "10100011", 3: "01110010",
            4: "10001011", 5: "11010001", 6: "10111001",
            7: "11010001", 8: "01110101", 9: "11001001",
            10: "01011011", 11: "01011100", 12: "11000110",
            13: "11100101", 14: "01011101", 15: "10011001",
            16: "10011101", 17: "10010111", 18: "01111001",
            19: "11110101", 20: "01001110", 21: "01101011",
            22: "11001011", 23: "10110011", 24: "11011101",
            25: "11101101", 26: "01100101", 27: "10101110",
            28: "10110101", 29: "10011001", 30: "01100101"}
        variant = SIPK.sipk4_5_6_7_in_group_list
        first = "001000"
        second = data_01_by_var[variant] + "000"
        first_mistake = -1
        if first_mistake == -1:
            first_mistake = randint(0, 3)
        second_mistake = -1
        while second_mistake == -1 or second_mistake == first_mistake:
            second_mistake = randint(0, 3)
        second_without = SIPK.sipk7_code_svert(second)[0]
        second_with_mistake = SIPK.sipk4_inverse_bit(second, first_mistake)
        second_with_mistakes = SIPK.sipk4_inverse_bit(second_with_mistake, second_mistake)
        err1 = SIPK.sipk7_errs[0]
        err2 = SIPK.sipk7_errs[1]
        if err1 == -1:
            err1 = randint(0, 9)
        while err2 == -1 or err1 == err2:
            err2 = randint(0, 10)
        SIPK.sipk7_errs = [err1, err2]
        print(SIPK.sipk7_errs)
        print(second_without)
        second_with_errors = SIPK.sipk4_inverse_bit(second_without, err1)
        second_with_errors = SIPK.sipk4_inverse_bit(second_with_errors, err2)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = SIPK.sipk7_add_spaces(SIPK.sipk7_code_svert(first)[0])
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx22 = second
        tex22 = M.MathTex(tx22, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx2 = SIPK.sipk7_add_spaces(second_without)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex22, M.DOWN)
        tx33 = second_with_mistake
        tex33 = M.MathTex(tx33, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        tx3 = SIPK.sipk7_add_spaces(SIPK.sipk7_code_svert(second_with_mistake)[0])
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex33, M.DOWN)
        tx44 = second_with_mistakes
        tex44 = M.MathTex(tx44, font_size = txs, color = mc).next_to(tex3, M.DOWN)
        tx4 = SIPK.sipk7_add_spaces(SIPK.sipk7_code_svert(second_with_mistakes)[0])
        tex4 = M.MathTex(tx4, font_size = txs, color = mc).next_to(tex44, M.DOWN)
        tx5 = SIPK.sipk7_add_spaces(second_with_errors)
        tex5 = M.MathTex(tx5, font_size = txs, color = mc).next_to(tex4, M.DOWN)
        scene.add(tex, tex2, tex22, tex3, tex33, tex4, tex44, tex5)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SIPK.sipk7_diagram(scene, second_with_errors)
        SIPK.sipk7_perforator(scene, second_without)
        SIPK.sipk7_soft_solution(scene, second_without)

    @staticmethod
    def sipk7_get_points():
        return [2.0, 1.0, 0.0, -1.0]
    
    @staticmethod
    def sipk7_get_points_by_state_and_bit(state: int, bit: str):
        start_point = 0.0
        end_point = 0.0
        point0, point1, point2, point3 = SIPK.sipk7_get_points()
        if state == 0:
            start_point = point0
            if bit == "0":
                end_point = point0
            elif bit == "1":
                end_point = point1
        elif state == 1:
            start_point = point1
            if bit == "0":
                end_point = point2
            elif bit == "1":
                end_point = point3
        elif state == 2:
            start_point = point2
            if bit == "0":
                end_point = point0
            elif bit == "1":
                end_point = point1
        elif state == 3:
            start_point = point3
            if bit == "0":
                end_point = point2
            elif bit == "1":
                end_point = point3
        return (start_point, end_point)
    
    @staticmethod
    def sipk7_get_text_pos_by_state_and_bit(state: int, bit: str, stage_lenght: float):
        r = M.RIGHT
        u = M.UP
        x_pos = r
        y_pos = u
        point0, point1, point2, point3 = SIPK.sipk7_get_points()
        dy1 = 0.12
        dy2 = 0.18
        dy3 = 0.7
        dy4 = 1.1
        dx1 = 0.5
        dx2 = 0.36
        dx3 = 0.85
        dx4 = 0.4
        if state == 0:
            if bit == "0":
                x_pos = stage_lenght * dx1 * r
                y_pos = (point0 + dy1) * u
            elif bit == "1":
                x_pos = stage_lenght * dx2 * r
                y_pos = (point0 - dy2) * u
        elif state == 1:
            if bit == "0":
                x_pos = stage_lenght * dx3 * r
                y_pos = (point1 - dy3) * u
            elif bit == "1":
                x_pos = stage_lenght * dx4 * r
                y_pos = (point1 - dy4) * u
        elif state == 2:
            if bit == "0":
                x_pos = stage_lenght * dx4 * r
                y_pos = (point2 + dy4) * u
            elif bit == "1":
                x_pos = stage_lenght * dx3 * r
                y_pos = (point2 + dy3) * u
        elif state == 3:
            if bit == "0":
                x_pos = stage_lenght * dx2 * r
                y_pos = (point3 + dy2) * u
            elif bit == "1":
                x_pos = stage_lenght * dx1 * r
                y_pos = (point3 - dy1) * u
        return x_pos + y_pos
    
    @staticmethod
    def sipk7_diagram(scene: M.Scene, bin_str: str):
        from math import ceil

        def is_another_step(step: int):
            if step <= 11:
                return True
            return False
        
        def make_new_ways(all_ways: list):
            ret_list = []
            for way in all_ways:
                ret_list.append(way + "0")
                ret_list.append(way + "1")
            return ret_list
        
        def delete_ways_and_get_data(all_ways: list):
            nonlocal bin_str
            ret_list = []
            ways_list = []
            hemming_list = []
            way_final_state_hemming = []
            final_way = ""
            final_hemming = 22
            states_list = []
            bits_list = []
            if len(all_ways) == 2:
                for way in all_ways:
                    code = SIPK.sipk7_code_svert(way)[0]
                    hemming = SIPK.sipk4_hemming_distance(code, bin_str[:len(code)])
                    hemming_list.append(str(hemming))
                states_list.append([0,])
                bits_list.append([["00", "10"], [], [], []])
                ret_list = [all_ways, hemming_list, states_list, bits_list]
            elif len(all_ways) == 4:
                for way in all_ways:
                    code = SIPK.sipk7_code_svert(way)[0]
                    hemming = SIPK.sipk4_hemming_distance(code, bin_str[:len(code)])
                    hemming_list.append(str(hemming))
                states_list.append([0,])
                states_list.append([0, 1])
                bits_list.append([["00", "10"], [], [], []])
                bits_list.append([["00", "10"], ["00", "10"], [], []])
                ret_list = [all_ways, hemming_list, states_list, bits_list]
            else:
                for way in all_ways:
                    data = SIPK.sipk7_code_svert(way)
                    code = data[0]
                    state = data[1]
                    hemming = SIPK.sipk4_hemming_distance(code, bin_str[:len(code)])
                    way_final_state_hemming.append([way, state, hemming])
                    hemming_list.append(str(hemming))
                for i in range(len(way_final_state_hemming)):
                    for j in range(i + 1, len(way_final_state_hemming), 1):
                        if way_final_state_hemming[i][1] == way_final_state_hemming[j][1]:
                            if way_final_state_hemming[i][2] > way_final_state_hemming[j][2]:
                                ways_list.append(way_final_state_hemming[j][0])
                                if way_final_state_hemming[j][2] < final_hemming:
                                    final_way = way_final_state_hemming[j][0]
                                    final_hemming = way_final_state_hemming[j][2]
                            else:
                                ways_list.append(way_final_state_hemming[i][0])
                                if way_final_state_hemming[i][2] < final_hemming:
                                    final_way = way_final_state_hemming[i][0]
                                    final_hemming = way_final_state_hemming[i][2]
                for stage in range(len(all_ways[0])):
                    states_list_in = []
                    bits_list_in = [[], [], [], []]
                    if len(final_way) >= 11:
                        state = SIPK.sipk7_code_svert(final_way[:stage])[1]
                        bits_list_in[state].append(final_way[stage:stage + 1] + "2")
                        states_list_in.append(state)
                        if stage == 0:
                            print(final_way)
                            SIPK.sipk7_final_way = final_way
                    for way in ways_list:
                        state = SIPK.sipk7_code_svert(way[:stage])[1]
                        if (way[stage:stage + 1] + "0" not in bits_list_in[state] and
                            way[stage:stage + 1] + "2" not in bits_list_in[state]):
                            bits_list_in[state].append(way[stage:stage + 1] + "0")
                        if state not in states_list_in:
                            states_list_in.append(state)
                    for way in all_ways:
                        state = SIPK.sipk7_code_svert(way[:stage])[1]
                        if (way[stage:stage + 1] + "0" not in bits_list_in[state] and
                            way[stage:stage + 1] + "1" not in bits_list_in[state] and
                            way[stage:stage + 1] + "2" not in bits_list_in[state]):
                            bits_list_in[state].append(way[stage:stage + 1] + "1")
                        if state not in states_list_in:
                            states_list_in.append(state)
                    states_list.append(states_list_in)
                    bits_list.append(bits_list_in)
                ret_list = [ways_list, hemming_list, states_list, bits_list]
            return ret_list
        
        def get_zline_by_style(start, end, bit_style: str):
            bit = bit_style[0]
            colour = "#000000"
            if bit == "0":
                colour = "#1111DD"
            elif bit == "1":
                colour = "#11DD11"
            style = bit_style[1]
            if style == "0":
                return ZLine([start, end], 0.2, 3, colour)
            elif style == "1":
                dash_lenght = 0.05
                dash_ratio = 0.5
                zline = ZLine([start, end], 0.2, 3, colour)
                dash_number = int(ceil(zline.get_length() / dash_lenght * dash_ratio))
                return M.DashedVMobject(zline, dash_number, dash_ratio)
            elif style == "2":
                return ZLine([start, end], 0.23, 7, colour)
            
        all_ways = ["0", "1"]
        state_texts = ["00", "10", "01", "11"]
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        state_font_size = 14.0
        dots_pos = SIPK.sipk7_get_points()
        dots_radius = 0.05
        step = 1
        while is_another_step(step):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            vg = M.VGroup()
            vg.add(M.Text("Шаг " + str(step), font_size = 30.0, color = mc
                          ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN))
            for i in range(len(dots_pos)):
                vg.add(M.Dot(M.UP * dots_pos[i] + M.RIGHT * -6.5, dots_radius, color = mc))
                vg.add(M.Text(state_texts[i], font_size = 20.0, color = mc
                              ).next_to(M.UP * dots_pos[i] + M.RIGHT * -6.5, M.LEFT, 0.1))
            data_full = delete_ways_and_get_data(all_ways)
            all_ways = data_full[0]
            for stage in range(step):
                stage_lenght = min(13.0 / step, 2.0)
                vg.add(M.Text(bin_str[stage * 2:stage * 2 + 2],
                              font_size = 24.0, color = mc
                              ).move_to(M.UP * 3.0 + M.RIGHT
                                        * (-6.5 + (stage + 0.5) * stage_lenght)))
                for i in range(len(dots_pos)):
                    vg.add(M.Dot(M.UP * dots_pos[i]
                                 + M.RIGHT * (-6.5 + (stage + 1) * stage_lenght),
                                 dots_radius, color = mc))
                    if stage == step - 1:
                        if step == 1:
                            for inn in range(2):
                                vg.add(M.Text(data_full[1][inn],
                                              font_size = 20.0, color = mc).next_to(
                                                  M.UP * dots_pos[inn] + M.RIGHT
                                                  * (-6.5 + step * stage_lenght),
                                                  M.RIGHT, 0.12))
                        elif step == 2:
                            for inn in range(4):
                                vg.add(M.Text(data_full[1][inn],
                                              font_size = 20.0, color = mc).next_to(
                                                  M.UP * dots_pos[inn] + M.RIGHT
                                                  * (-6.5 + step * stage_lenght),
                                                  M.RIGHT, 0.12))
                        else:
                            for inn in range(8):
                                vg.add(M.Text(data_full[1][inn],
                                              font_size = 20.0, color = mc).next_to(
                                                  M.UP * (dots_pos[inn % 4]
                                                          - 0.3 * (inn // 4) + 0.15) + M.RIGHT
                                                  * (-6.5 + step * stage_lenght),
                                                  M.RIGHT, 0.12))
                            for inn in range(4):
                                shift_y = -0.3
                                if int(data_full[1][inn]) > int(data_full[1][inn + 4]):
                                    shift_y = 0.0
                                vg.add(M.Line(M.UP * (dots_pos[inn] + 0.22 + shift_y)
                                              + M.RIGHT * (-6.43 + step * stage_lenght),
                                              M.UP * (dots_pos[inn] + 0.08 + shift_y)
                                              + M.RIGHT * (-6.2 + step * stage_lenght),
                                              color = mc, stroke_width = 1))
                for state in data_full[2][stage]:
                    for state_bit in data_full[3][stage][state]:
                        points = SIPK.sipk7_get_points_by_state_and_bit(state, state_bit[0])
                        zline = get_zline_by_style(
                            M.UP * points[0] + M.RIGHT * (-6.5 + stage * stage_lenght),
                            M.UP * points[1] + M.RIGHT * (-6.5 + (stage + 1) * stage_lenght),
                            state_bit)
                        text = M.Text(SIPK.sipk7_get_bits_by_state_and_bit(state, state_bit[0])[1],
                                      font_size = state_font_size, color = mc)
                        text.move_to(SIPK.sipk7_get_text_pos_by_state_and_bit(
                            state, state_bit[0], stage_lenght)
                            + M.RIGHT * (-6.5 + stage * stage_lenght))
                        text.rotate(SSf.SIPK_SSCTV_functions.get_angle_by_dx_dy(
                            stage_lenght, points[1] - points[0]))
                        vg.add(zline, text)
            scene.add(vg)
            step += 1
            all_ways = make_new_ways(all_ways)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk7_diagram_2(scene: M.Scene):
        def get_zline_by_style(start, end, bit_style: str):
            bit = bit_style[0]
            colour = "#000000"
            if bit == "0":
                colour = "#1111DD"
            elif bit == "1":
                colour = "#11DD11"
            return ZLine([start, end], 0.2, 3, colour)
        
        state_texts = ["00", "10", "01", "11"]
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        state_font_size = 18.0
        dots_pos = SIPK.sipk7_get_points()
        dots_radius = 0.05
        SSf.SIPK_SSCTV_functions.make_background(scene)
        vg = M.VGroup()
        for i in range(len(dots_pos)):
            vg.add(M.Dot(M.UP * dots_pos[i] + M.RIGHT * -6.5, dots_radius, color = mc))
            vg.add(M.Text(state_texts[i], font_size = 20.0, color = mc
                          ).next_to(M.UP * dots_pos[i] + M.RIGHT * -6.5, M.LEFT, 0.1))
        for stage in range(3):
            stage_lenght = 2.0
            for i in range(len(dots_pos)):
                vg.add(M.Dot(M.UP * dots_pos[i]
                             + M.RIGHT * (-6.5 + (stage + 1) * stage_lenght),
                             dots_radius, color = mc))
            for state in range(4):
                if stage == 0 and state >= 1: continue
                if stage == 1 and state >= 2: continue
                for state_bit in ["00", "10"]:
                    points = SIPK.sipk7_get_points_by_state_and_bit(state, state_bit[0])
                    zline = get_zline_by_style(
                        M.UP * points[0] + M.RIGHT * (-6.5 + stage * stage_lenght),
                        M.UP * points[1] + M.RIGHT * (-6.5 + (stage + 1) * stage_lenght),
                        state_bit)
                    text = M.Text(SIPK.sipk7_get_bits_by_state_and_bit(state, state_bit[0])[1],
                                      font_size = state_font_size, color = mc)
                    text.move_to(SIPK.sipk7_get_text_pos_by_state_and_bit(
                        state, state_bit[0], stage_lenght)
                        + M.RIGHT * (-6.5 + stage * stage_lenght))
                    text.rotate(SSf.SIPK_SSCTV_functions.get_angle_by_dx_dy(
                        stage_lenght, points[1] - points[0]))
                    vg.add(zline, text)
        scene.add(vg.move_to(M.ORIGIN))
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk7_perforator(scene: M.Scene, bin_str: str):
        def perforate(bin_str: str, type: int):
            ret_str = ""
            perf_lits = []
            if type == 2:
                perf_lits = [2, 6, 10, 14, 18, 22]
            elif type == 3:
                perf_lits = [2, 5, 8, 11, 14, 17, 20]
            elif type == 5:
                perf_lits = [2, 5, 6, 9, 12, 15, 16, 19]
            elif type == 7:
                perf_lits = [2, 4, 6, 9, 10, 13, 16, 18, 20]
            for i in range(len(bin_str)):
                if i in perf_lits:
                    ret_str += "X"
                else:
                    ret_str += bin_str[i]
            return ret_str

        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size - 4.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        text = M.Text("Исходная\nпоследовательность:", font_size = 24.0, color = mc
                      ).next_to(M.UP * 3.0 + M.RIGHT * -2.0, M.LEFT, 0.5)
        perf2 = perforate(bin_str, 2)
        perf3 = perforate(bin_str, 3)
        perf5 = perforate(bin_str, 5)
        perf7 = perforate(bin_str, 7)
        pfs = [bin_str, perf2, perf3, perf5, perf7]
        Rs = [r"", r"R = \frac{2}{3}:", r"R = \frac{3}{4}:",
              r"R = \frac{5}{6}:", r"R = \frac{7}{8}:"]
        vg = M.VGroup(text)
        for j in range(5):
            for i in range(len(bin_str) // 2):
                tex = M.MathTex(pfs[j][2 * i:2 * i + 2], font_size = txs, color = mc)
                tex.move_to(M.UP * (3 - j) + M.RIGHT * (-2.0 + i * 0.7))
                vg.add(tex)
            tex = M.MathTex(Rs[j], font_size = txs, color = mc)
            tex.next_to(M.UP * (3 - j) + M.RIGHT * -2.0, M.LEFT, 0.7)
            vg.add(tex)
        scene.add(vg)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk7_soft_solution(scene: M.Scene, bin_str: str):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = 22.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        texts = ["Исходная\nпоследовательность",
                 "Последовательность\nс мягким решением",
                 "Преобразованная\nпоследовательность"]
        soft = SIPK.sipk7_soft
        soft_list = []
        for numbers in soft.split("; "):
            nums = numbers.split(", ")
            soft_list.append([int(nums[0]), int(nums[1])])
        soft_paired = []
        transf_to_hard = []
        for i in range(len(soft_list)):
            f = "0"
            s = "0"
            if soft_list[i][0] < 0:
                f = "1"
            if soft_list[i][1] < 0:
                s = "1"
            transf_to_hard.append(f)
            transf_to_hard.append(s)
            soft_paired.append(str(soft_list[i][0]))
            soft_paired.append(str(soft_list[i][1]))
        bins = [[bin_str[i:i + 1] for i in range(len(bin_str))],
                soft_paired, transf_to_hard]
        table_data = [[texts[0], *bins[0]],
                      [texts[1], *bins[1]],
                      [texts[2], *bins[2]]]
        highlighted = []
        for i in range(len(transf_to_hard)):
            if bins[0][i] != bins[2][i]:
                highlighted.append((3, i + 2))
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.25,
            h_buff = 0.25,
            element_to_mobject = M.Text,
            element_to_mobject_config = {"font_size": txs, "color": mc},
            line_config = {"color": mc, "stroke_width": 2}).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        for cell in highlighted:
            table.add_highlighted_cell(cell, color = "#AAAAAA")
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SIPK.sipk7_soft_table(scene, soft_list)

    @staticmethod
    def sipk7_soft_table(scene: M.Scene, soft_list: list):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = 24.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        left_part = [[" ", "C1", "00", "01", "00", "01", "10", "11", "10", "11"],
                     [" ", r"б\ч", "00", "11", "11", "00", "01", "10", "10", "01"]]
        right_part = [" ", "C2", "00", "00", "10", "10", "01", "01", "11", "11"]
        middle_part = []
        metrics_list = []
        for i in range(len(soft_list)):
            b1 = soft_list[i][0]
            b2 = soft_list[i][1]
            middle_part.append([str(i + 1), str(b1) + ", " + str(b2),
                                str( b1 + b2), str(-b1 - b2),
                                str(-b1 - b2), str( b1 + b2),
                                str( b1 - b2), str(-b1 + b2),
                                str(-b1 + b2), str( b1 - b2)])
            metrics_list.append([ b1 + b2, -b1 - b2,
                                 -b1 - b2,  b1 + b2,
                                  b1 - b2, -b1 + b2,
                                 -b1 + b2,  b1 - b2])
        left_middle_part = SIPK.sipk4_matrix_concatenate(left_part, middle_part, True)
        table_data = SIPK.sipk4_matrix_concatenate(left_middle_part, right_part, True)
        table_data = SSf.SIPK_SSCTV_functions.transpose_list(table_data)
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.3,
            element_to_mobject = M.Text,
            element_to_mobject_config = {"font_size": txs, "color": mc},
            line_config = {"color": mc, "stroke_width": 2}).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SIPK.sipk7_soft_diagram(scene, metrics_list)

    @staticmethod
    def sipk7_soft_diagram(scene: M.Scene, metrics_list: list):
        from math import ceil

        def get_text_by_stage_state_bit(stage: int, state: int, bit: str):
            nonlocal metrics_list
            i = 0
            if state == 0:
                if bit == "0": i = 0
                elif bit == "1": i = 2
            elif state == 1:
                if bit == "0": i = 4
                elif bit == "1": i = 6
            elif state == 2:
                if bit == "0": i = 1
                elif bit == "1": i = 3
            elif state == 3:
                if bit == "0": i = 5
                elif bit == "1": i = 7
            return str(metrics_list[stage][i])
        
        def get_all_data():
            def make_current_metrix_sum(previous_metrix: list, stage: int):
                nonlocal metrics_list
                if stage == 0:
                    metrixs = [metrics_list[stage][0], metrics_list[stage][2],
                               0, 0, 0, 0, 0, 0]
                    return metrixs
                elif stage == 1:
                    metrixs = [metrics_list[stage][0] + previous_metrix[0],
                               metrics_list[stage][2] + previous_metrix[0],
                               metrics_list[stage][4] + previous_metrix[1],
                               metrics_list[stage][6] + previous_metrix[1],
                               -10, -10, -10, -10]
                    return metrixs
                else:
                    max_0 = previous_metrix[0]
                    if previous_metrix[4] > max_0: max_0 = previous_metrix[4]
                    max_1 = previous_metrix[1]
                    if previous_metrix[5] > max_1: max_1 = previous_metrix[5]
                    max_2 = previous_metrix[2]
                    if previous_metrix[6] > max_2: max_2 = previous_metrix[6]
                    max_3 = previous_metrix[3]
                    if previous_metrix[7] > max_3: max_3 = previous_metrix[7]
                    metrixs = [metrics_list[stage][0] + max_0,
                               metrics_list[stage][2] + max_0,
                               metrics_list[stage][4] + max_1,
                               metrics_list[stage][6] + max_1,
                               metrics_list[stage][1] + max_2,
                               metrics_list[stage][3] + max_2,
                               metrics_list[stage][5] + max_3,
                               metrics_list[stage][7] + max_3]
                    return metrixs
                
            nonlocal metrics_list
            ret_list = []
            states_list = []
            bit_style_list = []
            sum_metrix_list = [[0, 0, 0, 0, 0, 0, 0, 0],]
            for metrix_row_i in range(len(metrics_list)):
                sum_metrix_list.append(make_current_metrix_sum(
                    sum_metrix_list[-1], metrix_row_i))
                if metrix_row_i == 0:
                    states_list.append([0,])
                elif metrix_row_i == 1:
                    states_list.append([0, 1])
                else:
                    states_list.append([0, 1, 2, 3])
                state = SIPK.sipk7_code_svert(SIPK.sipk7_final_way[:metrix_row_i])[1]
                bit_style_list.append([
                    state, SIPK.sipk7_final_way[metrix_row_i:metrix_row_i + 1] + "2"])
            ret_list = [states_list, sum_metrix_list, bit_style_list]
            return ret_list
        
        def get_zline_by_style(start, end, bit_style: str):
            bit = bit_style[0]
            colour = "#000000"
            if bit == "0":
                colour = "#1111DD"
            elif bit == "1":
                colour = "#11DD11"
            style = bit_style[1]
            if style == "0":
                return ZLine([start, end], 0.2, 2, colour)
            elif style == "1":
                dash_lenght = 0.05
                dash_ratio = 0.5
                zline = ZLine([start, end], 0.2, 2, colour)
                dash_number = int(ceil(zline.get_length() / dash_lenght * dash_ratio))
                return M.DashedVMobject(zline, dash_number, dash_ratio)
            elif style == "2":
                return ZLine([start, end], 0.23, 6, colour)
            
        data_full = get_all_data()
        state_texts = ["00", "10", "01", "11"]
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        state_font_size = 14.0
        dots_pos = SIPK.sipk7_get_points()
        dots_radius = 0.05
        SSf.SIPK_SSCTV_functions.make_background(scene)
        vg = M.VGroup()
        for i in range(len(dots_pos)):
            vg.add(M.Dot(M.UP * dots_pos[i] + M.RIGHT * -6.5, dots_radius, color = mc))
            vg.add(M.Text(state_texts[i], font_size = 20.0, color = mc
                          ).next_to(M.UP * dots_pos[i] + M.RIGHT * -6.5, M.LEFT, 0.12))
        stage_lenght = 13.0 / 11.0
        for stage in range(len(metrics_list)):
            vg.add(M.Text(str(stage + 1), font_size = 24.0, color = mc
                          ).move_to(M.UP * 3.0 + M.RIGHT * (-6.5 + (stage + 0.5) * stage_lenght)))
            for i in range(len(dots_pos)):
                vg.add(M.Dot(M.UP * dots_pos[i] + M.RIGHT * (-6.5 + (stage + 1) * stage_lenght),
                             dots_radius, color = mc))
            for i in range(8):
                if stage == 0 and i >= 2: break
                elif stage == 1 and i >= 4: break
                dir = M.UP
                if i // 4 == 1:
                    dir = M.DOWN
                vg.add(M.Text(str(data_full[1][stage + 1][i]), font_size = 18.0, color = mc
                              ).next_to(M.UP * (dots_pos[i % 4]) + M.RIGHT
                                        * (-6.5 + (stage + 1) * stage_lenght), dir, 0.13))
            for i in range(4):
                shift_y = -0.2
                if stage == 0 or stage == 1: break
                if int(data_full[1][stage + 1][i]) < int(data_full[1][stage + 1][i + 4]):
                    shift_y = 0.2
                vg.add(M.Line(M.UP * (dots_pos[i] + 0.1 + shift_y)
                              + M.RIGHT * (-6.65 + (stage + 1) * stage_lenght),
                              M.UP * (dots_pos[i] - 0.1 + shift_y)
                              + M.RIGHT * (-6.35 + (stage + 1) * stage_lenght),
                              color = mc, stroke_width = 1))
            for state in data_full[0][stage]:
                for state_bit in ["00", "10"]:
                    if [state, state_bit[0] + "2"] == data_full[2][stage]:
                        state_bit = state_bit[0] + "2"
                    points = SIPK.sipk7_get_points_by_state_and_bit(state, state_bit[0])
                    zline = get_zline_by_style(
                        M.UP * points[0] + M.RIGHT * (-6.5 + stage * stage_lenght),
                        M.UP * points[1] + M.RIGHT * (-6.5 + (stage + 1) * stage_lenght),
                        state_bit)
                    text = M.Text(get_text_by_stage_state_bit(stage, state, state_bit[0]),
                                  font_size = state_font_size, color = mc)
                    text.move_to(SIPK.sipk7_get_text_pos_by_state_and_bit(
                        state, state_bit[0], stage_lenght)
                        + M.RIGHT * (-6.5 + stage * stage_lenght))
                    text.rotate(SSf.SIPK_SSCTV_functions.get_angle_by_dx_dy(
                        stage_lenght, points[1] - points[0]))
                    vg.add(zline, text)
        scene.add(vg)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk_lr3_formula_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        variant_bin = "1001"
        variant_bin = SSf.SIPK_SSCTV_functions.add_zeros(variant_bin, 3)
        variant_polinom = SIPK.sipk5_bin_str_to_polinom(variant_bin)
        g_x = 11
        g_x_bin = bin(g_x)[2:]
        tx = r"x^3 \cdot V(x) = " + variant_polinom
        tex = M.MathTex(tx, font_size = txs, color = mc
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        divisible = variant_bin
        divisor = g_x_bin
        table_data = SIPK.sipk5_bin_str_division(divisible, divisor)
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.2,
            h_buff = 0.25,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1}
            ).next_to(tex, M.DOWN, 0.5)
        remainder_list = []
        for char in table_data[-1]:
            if char != r"" and char != r"|":
                remainder_list.append(char)
        remainder_polinom = "".join(remainder_list)
        V_s_x_polinom = variant_polinom + " + " + remainder_polinom
        tx2 = r"V_{s}(x) = " + V_s_x_polinom
        tex2 = M.MathTex(tx2, font_size = txs, color = mc
                         ).next_to(table, M.DOWN, 0.5)
        scene.add(tex, tex2, table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk_lr3_table_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        fs = 20.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data = []
        V_s_x_bin = "1000110"
        e = V_s_x_bin[0]
        d = V_s_x_bin[1]
        v = V_s_x_bin[2]
        a = V_s_x_bin[3]
        b = SSf.SIPK_SSCTV_functions.sum_mod_2(a, e)
        g = SSf.SIPK_SSCTV_functions.sum_mod_2(v, e)
        for i in range(5):
            table_data.append([a, b, v, g, d, e])
            e = d
            d = g
            v = b
            if i >= 3:
                a = b = g = "-"
            else:
                a = V_s_x_bin[4 + i]
                b = SSf.SIPK_SSCTV_functions.sum_mod_2(a, e)
                g = SSf.SIPK_SSCTV_functions.sum_mod_2(v, e)
        table = SSf.Table(
            table_data,
            col_labels = [
                M.Text("а", font_size = fs, color = mc),
                M.Text("б", font_size = fs, color = mc),
                M.Text("в", font_size = fs, color = mc),
                M.Text("г", font_size = fs, color = mc),
                M.Text("д", font_size = fs, color = mc),
                M.Text("е", font_size = fs, color = mc)],
            row_labels = [
                M.Text(str(i), font_size = fs, color = mc) for i in range(5)],
            include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.6,
            element_to_mobject = M.MathTex,
            element_to_mobject_config = {"font_size": 24.0, "color": mc},
            line_config = {"color": mc, "stroke_width": 1})
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk_lr3_graphs_1(scene: M.Scene):
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (0.0, 0.45, 0.05),
            y_range = (0, 700, 50),
            x_length = 12.5,
            y_length = 6.5,
            color = mc,
            axis_config = {
                "include_numbers": True,
                "font_size": 24.0,
                "stroke_width": 4,
                "include_ticks": False,
                "include_tip": True,
                "line_to_number_buff": 0.13,
                "label_direction": M.DOWN,
                "color": mc},
            y_axis_config = {
                "label_direction": M.LEFT},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 1,
                "stroke_opacity": 0.5},
            tips = True)
        number_plane.get_axes().set_color(mc)
        number_plane2 = M.NumberPlane(
            x_range = (0.0, 0.45, 0.05),
            y_range = (0, 150, 30),
            x_length = 12.5,
            y_length = 6.5,
            color = mc,
            axis_config = {
                "include_numbers": True,
                "font_size": 24.0,
                "stroke_width": 4,
                "include_ticks": False,
                "include_tip": True,
                "line_to_number_buff": 0.13,
                "label_direction": M.DOWN,
                "color": mc},
            y_axis_config = {
                "label_direction": M.LEFT},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 1,
                "stroke_opacity": 0.5},
            tips = True)
        number_plane2.get_axes().set_color(mc)
        data = """0.05
27
7
2
0.1
64
32
10
0.15
116
113
35
0.2
115
117
37
0.25
164
178
55
0.3
213
235
70
0.35
229
242
71
0.4
290
313
87"""
        data2 = """0.05
86
68
21
0.1
141
140
41
0.15
244
275
71
0.2
312
364
89
0.25
365
418
92
0.3
479
518
99
0.35
511
528
99
0.4
643
649
100"""
        x_range1 = []
        chanel_err1 = []
        dec_bit_err1 = []
        dec_block_err1 = []
        x_range2 = []
        chanel_err2 = []
        dec_bit_err2 = []
        dec_block_err2 = []
        i = 0
        for line in data.split():
            if i % 4 == 0:
                x_range1.append(float(line))
            elif i % 4 == 1:
                chanel_err1.append(float(line))
            elif i % 4 == 2:
                dec_bit_err1.append(float(line))
            elif i % 4 == 3:
                dec_block_err1.append(float(line))
            i += 1
        i = 0
        for line in data2.split():
            if i % 4 == 0:
                x_range2.append(float(line))
            elif i % 4 == 1:
                chanel_err2.append(float(line))
            elif i % 4 == 2:
                dec_bit_err2.append(float(line))
            elif i % 4 == 3:
                dec_block_err2.append(float(line))
            i += 1
        SSf.SIPK_SSCTV_functions.make_background(scene)
        line_graph1 = number_plane.plot_line_graph(
            x_values = x_range1,
            y_values = chanel_err1,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = "#E49148"),
            stroke_width = 4, stroke_color = "#E49148")
        line_graph2 = number_plane.plot_line_graph(
            x_values = x_range2,
            y_values = chanel_err2,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = "#71A1EE"),
            stroke_width = 4, stroke_color = "#71A1EE")
        scene.add(number_plane, line_graph1, line_graph2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        line_graph1 = number_plane.plot_line_graph(
            x_values = x_range1,
            y_values = dec_bit_err1,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = "#E49148"),
            stroke_width = 4, stroke_color = "#E49148")
        line_graph2 = number_plane.plot_line_graph(
            x_values = x_range2,
            y_values = dec_bit_err2,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = "#71A1EE"),
            stroke_width = 4, stroke_color = "#71A1EE")
        scene.add(number_plane, line_graph1, line_graph2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        line_graph1 = number_plane2.plot_line_graph(
            x_values = x_range1,
            y_values = dec_block_err1,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = "#E49148"),
            stroke_width = 4, stroke_color = "#E49148")
        line_graph2 = number_plane2.plot_line_graph(
            x_values = x_range2,
            y_values = dec_block_err2,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = "#71A1EE"),
            stroke_width = 4, stroke_color = "#71A1EE")
        scene.add(number_plane2, line_graph1, line_graph2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def new_sipk_lr3_graphs_1(scene: M.Scene):
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        col1 = "#26547c"
        col2 = "#ef476f"
        col3 = "#ffd166"
        number_plane = M.NumberPlane(
            x_range = (0.0, 0.45, 0.05),
            y_range = (0, 350, 50),
            x_length = 12.5,
            y_length = 6.5,
            color = mc,
            axis_config = {
                "include_numbers": True,
                "font_size": 24.0,
                "stroke_width": 4,
                "include_ticks": False,
                "include_tip": True,
                "line_to_number_buff": 0.13,
                "label_direction": M.DOWN,
                "color": mc},
            y_axis_config = {
                "label_direction": M.LEFT},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 1,
                "stroke_opacity": 0.5},
            tips = True)
        number_plane.get_axes().set_color(mc)
        number_plane2 = M.NumberPlane(
            x_range = (0.0, 0.45, 0.05),
            y_range = (0, 700, 50),
            x_length = 12.5,
            y_length = 6.5,
            color = mc,
            axis_config = {
                "include_numbers": True,
                "font_size": 24.0,
                "stroke_width": 4,
                "include_ticks": False,
                "include_tip": True,
                "line_to_number_buff": 0.13,
                "label_direction": M.DOWN,
                "color": mc},
            y_axis_config = {
                "label_direction": M.LEFT},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 1,
                "stroke_opacity": 0.5},
            tips = True)
        number_plane2.get_axes().set_color(mc)
        data = """0.05
36
15
5
0.1
67
51
16
0.15
87
72
23
0.2
146
144
43
0.25
186
185
56
0.3
205
207
61
0.35
254
279
77
0.4
257
279
82"""
        data2 = """0.05
81
55
17
0.1
134
126
36
0.15
236
250
70
0.2
343
389
91
0.25
398
448
95
0.3
461
483
98
0.35
523
545
97
0.4
597
611
100"""
        x_range1 = []
        chanel_err1 = []
        dec_bit_err1 = []
        dec_block_err1 = []
        x_range2 = []
        chanel_err2 = []
        dec_bit_err2 = []
        dec_block_err2 = []
        i = 0
        for line in data.split():
            if i % 4 == 0:
                x_range1.append(float(line))
            elif i % 4 == 1:
                chanel_err1.append(float(line))
            elif i % 4 == 2:
                dec_bit_err1.append(float(line))
            elif i % 4 == 3:
                dec_block_err1.append(float(line))
            i += 1
        i = 0
        for line in data2.split():
            if i % 4 == 0:
                x_range2.append(float(line))
            elif i % 4 == 1:
                chanel_err2.append(float(line))
            elif i % 4 == 2:
                dec_bit_err2.append(float(line))
            elif i % 4 == 3:
                dec_block_err2.append(float(line))
            i += 1
        SSf.SIPK_SSCTV_functions.make_background(scene)
        line_graph1 = number_plane.plot_line_graph(
            x_values = x_range1,
            y_values = chanel_err1,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = col1),
            stroke_width = 4, stroke_color = col1)
        line_graph2 = number_plane.plot_line_graph(
            x_values = x_range1,
            y_values = dec_bit_err1,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = col2),
            stroke_width = 4, stroke_color = col2)
        line_graph3 = number_plane.plot_line_graph(
            x_values = x_range1,
            y_values = dec_block_err1,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = col3),
            stroke_width = 4, stroke_color = col3)
        scene.add(number_plane, line_graph1, line_graph2, line_graph3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        line_graph1 = number_plane2.plot_line_graph(
            x_values = x_range2,
            y_values = chanel_err2,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = col1),
            stroke_width = 4, stroke_color = col1)
        line_graph2 = number_plane2.plot_line_graph(
            x_values = x_range2,
            y_values = dec_bit_err2,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = col2),
            stroke_width = 4, stroke_color = col2)
        line_graph3 = number_plane2.plot_line_graph(
            x_values = x_range2,
            y_values = dec_block_err2,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = col3),
            stroke_width = 4, stroke_color = col3)
        scene.add(number_plane2, line_graph1, line_graph2, line_graph3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk_lr3_legend(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tts = 22.0
        number_plane = M.NumberPlane(
            x_range = (0, 12, 1),
            y_range = (0, 10, 1),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "stroke_width": 0,
                "color": mc},
            background_line_style = {
                "stroke_width": 0},
            tips = False)
        line_graph1 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [1, 1],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = "#E49148"),
            stroke_width = 4, stroke_color = "#E49148")
        line_graph2 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [2, 2],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = "#71A1EE"),
            stroke_width = 4, stroke_color = "#71A1EE")
        line_graph4 = number_plane.plot_line_graph(
            x_values = [0.5, 0.5, 3.5, 3.5, 0.5],
            y_values = [0, 3, 3, 0, 0],
            line_color = mc,
            vertex_dot_radius = 0.0,
            vertex_dot_style = dict(stroke_width = 0),
            stroke_width = 4)
        txt1 = M.Text("(7,4)",
                      font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 1.0, 0.0))
        txt2 = M.Text("(15,11)",
                      font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 2.0, 0.0))
        scene.add(number_plane, line_graph1, line_graph2, line_graph4, txt1, txt2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def new_sipk_lr3_legend(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        col1 = "#26547c"
        col2 = "#ef476f"
        col3 = "#ffd166"
        tts = 22.0
        number_plane = M.NumberPlane(
            x_range = (0, 12, 1),
            y_range = (0, 10, 1),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "stroke_width": 0,
                "color": mc},
            background_line_style = {
                "stroke_width": 0},
            tips = False)
        line_graph1 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [1, 1],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = col1),
            stroke_width = 4, stroke_color = col1)
        line_graph2 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [1.5, 1.5],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = col2),
            stroke_width = 4, stroke_color = col2)
        line_graph3 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [2, 2],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = mc,
                                    stroke_color = col3),
            stroke_width = 4, stroke_color = col3)
        line_graph4 = number_plane.plot_line_graph(
            x_values = [0.5, 0.5, 7.0, 7.0, 0.5],
            y_values = [0, 3, 3, 0, 0],
            line_color = mc,
            vertex_dot_radius = 0.0,
            vertex_dot_style = dict(stroke_width = 0),
            stroke_width = 4)
        txt1 = M.Text("Ошибки в канале", font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 1.0, 0.0))
        txt2 = M.Text("Битовые ошибки декодера", font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 1.5, 0.0))
        txt3 = M.Text("Блоковые ошибки декодера", font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 2.0, 0.0))
        scene.add(number_plane, line_graph1, line_graph2, line_graph3, line_graph4, txt1, txt2, txt3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk_lr4_graphs_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (0, 10, 1),
            y_range = (-7, 0, 1),
            x_length = 12.5,
            y_length = 6.5,
            color = mc,
            axis_config = {
                "include_numbers": True,
                "font_size": 24.0,
                "stroke_width": 4,
                "include_ticks": False,
                "include_tip": True,
                "line_to_number_buff": 0.13,
                "label_direction": M.DOWN,
                "color": mc},
            y_axis_config = {
                "label_direction": M.LEFT,
                "scaling": M.LogBase(custom_labels = True)},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 1,
                "stroke_opacity": 0.5},
            tips = True)
        number_plane.get_axes().set_color(mc)
        data1 = """1
2
3
4
5
6
7
8
9"""
        data2 = """5.62e-2
3.74e-2
2.29e-2
1.25e-2
5.97e-3
2.39e-3
7.74e-4
1.91e-4
3.42e-5"""
        data3 = """1.42e-1
1.05e-1
5.43e-2
1.45e-2
1.46e-3
4.18e-5"""
        data4 = """1.5e-2"""
        data5 = """1.3e-2
1.3e-3
4.0e-5
3.9e-7"""
        x_range = []
        ber2 = []
        ber3 = []
        ber4 = []
        ber5 = []
        for i in data1.split():
            x_range.append(float(i))
        for i in data2.split():
            ber2.append(float(i))
        for i in data3.split():
            ber3.append(float(i))
        for i in data4.split():
            ber4.append(float(i))
        for i in data5.split():
            ber5.append(float(i))
        line_graph1 = number_plane.plot_line_graph(
            x_values = x_range,
            y_values = ber2,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 3, fill_color = "#B41297",
                                    stroke_color = mc),
            stroke_width = 3)
        line_graph2 = number_plane.plot_line_graph(
            x_values = x_range,
            y_values = ber3,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 3, fill_color = "#09EA72",
                                    stroke_color = mc),
            stroke_width = 3)
        line_graph3 = number_plane.plot_line_graph(
            x_values = x_range[3:],
            y_values = ber4,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 3, fill_color = "#9FC500",
                                    stroke_color = mc),
            stroke_width = 3)
        line_graph4 = number_plane.plot_line_graph(
            x_values = x_range[3:],
            y_values = ber5,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 3, fill_color = "#3F55E0",
                                    stroke_color = mc),
            stroke_width = 3)
        y_label = M.MathTex("BER", font_size = 24.0, color = mc
                            ).next_to(number_plane, M.UL)
        y_label.shift(M.RIGHT * 0.7 + M.DOWN * 0.1)
        x_label = M.MathTex(r"\frac {E_b}{N_0},", font_size = 24.0, color = mc
                            ).next_to(number_plane, M.DR)
        x_label.shift(M.LEFT * 0.35 + M.UP * 0.4)
        x_label2 = M.Text("дБ", font_size = 18.0, color = mc
                          ).next_to(x_label, buff = 0.1)
        scene.add(number_plane, line_graph1, line_graph2,
                #   line_graph3,
                  line_graph4,
                  y_label, x_label, x_label2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def sipk_lr4_legend(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tts = 22.0
        number_plane = M.NumberPlane(
            x_range = (0, 12, 1),
            y_range = (0, 10, 1),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "stroke_width": 0,
                "color": mc},
            background_line_style = {
                "stroke_width": 0},
            tips = False)
        line_graph1 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [1, 1],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 3, fill_color = "#B41297",
                                    stroke_color = mc),
            stroke_width = 3)
        line_graph2 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [2, 2],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 3, fill_color = "#09EA72",
                                    stroke_color = mc),
            stroke_width = 3)
        line_graph3 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [3, 3],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 3, fill_color = "#9FC500",
                                    stroke_color = mc),
            stroke_width = 3)
        line_graph4 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [3, 3],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 3, fill_color = "#3F55E0",
                                    stroke_color = mc),
            stroke_width = 3)
        line_graph0 = number_plane.plot_line_graph(
            x_values = [0.5, 0.5, 5.0, 5.0, 0.5],
            y_values = [0, 4, 4, 0, 0],
            line_color = mc,
            vertex_dot_radius = 0.0,
            vertex_dot_style = dict(stroke_width = 0),
            stroke_width = 4)
        txt1 = M.Text("BERкан.ср.", font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 1.0, 0.0))
        txt2 = M.Text("BERдекод.ср.", font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 2.0, 0.0))
        txt3 = M.Text("BERдекод.спр.", font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 3.0, 0.0))
        txt4 = M.Text("BERдекод.макс.", font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 3.0, 0.0))
        scene.add(number_plane, line_graph1, line_graph2,
                #   line_graph3,
                  line_graph4,
                  line_graph0, txt1, txt2,
                #   txt3,
                  txt4
                  )
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
        self.add_tip(self.create_tip(tip_length = size, tip_width = size * 0.5))


class Matrix(M.Matrix):
    """Matrix"""

    def __init__(self, matrix, v_buff: float = 0.45, h_buff: float = 0.6,
                 bracket_h_buff: float = 0.15, bracket_v_buff: float = 0.15,
                 add_background_rectangles_to_entries: bool = False,
                 include_background_rectangle: bool = False,
                 element_to_mobject_config: dict = {},
                 left_bracket: str = "(", right_bracket: str = ")",
                 stretch_brackets: bool = True,
                 bracket_config: dict = {}, **kwargs):
        super().__init__(matrix, v_buff, h_buff, bracket_h_buff, bracket_v_buff,
                         add_background_rectangles_to_entries,
                         include_background_rectangle,
                         element_to_mobject_config = element_to_mobject_config,
                         left_bracket = left_bracket, right_bracket = right_bracket,
                         stretch_brackets = stretch_brackets,
                         bracket_config =bracket_config, **kwargs)
        
