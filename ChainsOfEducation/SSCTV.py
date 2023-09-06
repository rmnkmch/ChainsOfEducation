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

    data_saved = {"my": "A0.2 B0.06 C0.14 D0.1 E0.47 F0.03",
                  "exmpl": "Р0.04 Е0.24 П0.49 Л0.14 О0.09",
                  "used": "В0.11 Х0.21 Э0.03 П0.07 Н0.34 Ш0.24"}

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
        #print(p)
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
        data = []
        for i in range(len(pb)):
            data.append(sm[i] + str(round(pb[i], SSCTV.PRB_NUM)))
        return " ".join(data)

    @staticmethod
    def sym_size_by_n(n):
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
            if ps.symbol == symbol:
                return ps

    @staticmethod
    def find_index_by_symbol(symbol, all_ps):
        return all_ps.index(SSCTV.find_ps_by_symbol(symbol, all_ps))

    @staticmethod
    def get_main_color():
        return "#000000"

    @staticmethod
    def get_background_color():
        return "#FFFFFF"

    @staticmethod
    def make_background(scene):
        scene.add(M.Rectangle(
            SSCTV.get_background_color(), 9.0, 15.0, fill_opacity = 1.0))

    @staticmethod
    def make_all(scene: M.Scene):
        SSCTV.random_SPIK1()
        SSCTV.make_SPIK1(scene)

    @staticmethod
    def random_SPIK1():
        pss = SSCTV.get_random_ps(6)
        pss = SSCTV.data_saved["used"]
        print(pss)
        all_ps = SSCTV.get_symbols_and_probabilities(pss)
        SSCTV.print_sym_prb_octave(all_ps)
        if not SSCTV.check_probability(all_ps): print("prb != 1")
        n = 20
        all_ps_copy = [ProbabilitySymbol.get_full_copy(ps) for ps in all_ps]
        m1 = SSCTV.get_random_message_1(all_ps_copy, n)
        m2 = SSCTV.get_random_message_2(all_ps_copy, n)
        m3 = SSCTV.get_random_message_3(all_ps_copy, n)
        SSCTV.print_random_message_20(m1, all_ps)
        SSCTV.print_random_message_20(m2, all_ps)
        SSCTV.print_random_message_20(m3, all_ps)

    @staticmethod
    def make_SPIK1(scene: M.Scene):
        full = SSCTV.make_haffman(scene)
        scene.wait()
        scene.clear()
        SSCTV.make_table_1(scene, full)
        scene.wait()
        scene.clear()
        SSCTV.make_table_2(scene, full)
        scene.wait()
        scene.clear()
        SSCTV.make_formula_1(scene, full)
        scene.wait()
        scene.clear()
        '''full2 = [ProbabilitySymbol.get_full_copy(ps) for ps in full]
        rand = SSCTV.make_messages_20(scene, full2)
        scene.wait()
        scene.clear()
        SSCTV.make_golomb(scene, full)
        scene.wait()
        scene.clear()
        SSCTV.make_table_1(scene, full)
        scene.wait()
        scene.clear()
        full2 = [ProbabilitySymbol.get_full_copy(ps) for ps in full]
        m = SSCTV.make_messages_20(scene, full2, rand[0], rand[1], rand[2])
        scene.wait()
        scene.clear()
        num = SSCTV.make_arith(scene, m[3], full)
        scene.wait()
        scene.clear()
        SSCTV.make_count_1(scene, num)
        scene.wait()
        scene.clear()'''

    @staticmethod
    def print_sym_prb_octave(all_ps):
        syms = []
        prbs = []
        for i in range(len(all_ps)):
            syms.append(all_ps[i].symbol)
            prbs.append(str(round(all_ps[i].probability * 100)))
        print(", ".join(syms))
        print(", ".join(prbs))

    @staticmethod
    def make_haffman(scene: M.Scene):
        SSCTV.make_background(scene)
        all_ps = SSCTV.get_symbols_and_probabilities(SSCTV.data_saved["used"])
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
    def make_table_1(scene: M.Scene, all_ps):
        SSCTV.make_background(scene)
        table = Table(
            [[all_ps[i].symbol, all_ps[i].code]
             for i in range(len(all_ps))],
             include_outer_lines = True,
             v_buff = 0.48 * SSCTV.sym_size_by_n(len(all_ps)) / 54.0,
             h_buff = 2.0,
             element_to_mobject_config = {
                 "font_size": SSCTV.prb_size_by_n(len(all_ps)),
                 "color": SSCTV.get_main_color()},
             line_config = {"color": SSCTV.get_main_color()})
        scene.add(table)

    @staticmethod
    def make_table_2(scene: M.Scene, all_ps):
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
                M.Text(rt, font_size = (
                    SSCTV.sym_size_by_n(len(all_ps) + 3) - 8.0),
                       color = SSCTV.get_main_color()) for rt in syms],
            col_labels = [
                M.MathTex(
                    r"p_i", color = SSCTV.get_main_color(),
                    font_size = (
                        SSCTV.sym_size_by_n(len(all_ps) + 3) - 4.0)),
                M.MathTex(
                    r"-\log_2 p_i", color = SSCTV.get_main_color(),
                    font_size = (
                        SSCTV.sym_size_by_n(len(all_ps) + 3) - 4.0)),
                M.MathTex(
                    r"-p_i \cdot \log_2 p_i", color = SSCTV.get_main_color(),
                    font_size = (
                        SSCTV.sym_size_by_n(len(all_ps) + 3) - 4.0))],
            include_outer_lines = True,
            v_buff = 0.48 * SSCTV.sym_size_by_n(len(all_ps)) / 54.0,
            h_buff = 2.0,
            element_to_mobject_config = {
                "font_size": SSCTV.prb_size_by_n(len(all_ps)),
                "color": SSCTV.get_main_color()},
            line_config = {"color": SSCTV.get_main_color()})
        scene.add(table)

    @staticmethod
    def make_formula_1(scene: M.Scene, all_ps):
        from math import log2
        SSCTV.make_background(scene)
        sum_entr = sum([- log2(sym.probability) * sym.probability
                        for sym in all_ps])
        tx = r"H = - \sum_{i=1}^M p_i \cdot \log_2 p_i = " + str(round(sum_entr, 3))
        tex = M.MathTex(tx, color = SSCTV.get_main_color(),
                        font_size = 88.0)
        scene.add(tex)

    @staticmethod
    def ps_by_prb(prb, prb_line, all_ps):
        for i in range(len(prb_line)):
            if prb_line[i] > prb:
                return all_ps[i - 1]

    @staticmethod
    def get_prb_line(all_ps, lowest):
        prb_line = [lowest]
        for i in range(len(all_ps)):
            prb_line.append(all_ps[i].probability + prb_line[i] + lowest)
        return prb_line

    @staticmethod
    def get_random_message_1(all_ps, n = 20):
        all_ps.sort()
        prb_line = SSCTV.get_prb_line(all_ps, 0.0)
        message = []
        for _ in range(n):
            message.append(SSCTV.ps_by_prb(random.random(), prb_line, all_ps))
        return message

    @staticmethod
    def get_random_message_2(all_ps, n = 20):
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
                all_ps[i].probability *= 0.25
            else:
                all_ps[i].probability *= 4.0
        pbrs = 0.0
        for i in range(len(all_ps)):
            pbrs += all_ps[i].probability
        for i in range(len(all_ps)):
            all_ps[i].probability = all_ps[i].probability / pbrs
        prb_line = SSCTV.get_prb_line(all_ps, 0.0)
        message = []
        for i in range(n):
            message.append(SSCTV.ps_by_prb(random.random(), prb_line, all_ps))
        return message

    @staticmethod
    def get_random_message_3(all_ps, n = 20):
        ii = 0
        while ii < len(all_ps) // 2:
            a = all_ps[ii].probability
            b = all_ps[- ii - 1].probability
            all_ps[ii].probability = b
            all_ps[- ii - 1].probability = a
            ii += 1
        prb_line = SSCTV.get_prb_line(all_ps, 0.0)
        message = []
        for _ in range(n):
            message.append(SSCTV.ps_by_prb(random.random(), prb_line, all_ps))
        return message

    @staticmethod
    def print_random_message_20(mess, compr):
        syms = []
        letrs = []
        for ps in mess:
            syms.append(str(SSCTV.find_index_by_symbol(ps.symbol, compr) + 1))
            letrs.append(ps.symbol)
        print(", ".join(syms))
        print(", ".join(letrs))

    @staticmethod
    def get_message_20_by_str(mess_str, all_ps):
        mess = []
        for char in mess_str:
            mess.append(SSCTV.find_ps_by_symbol(char, all_ps))
        return mess

    @staticmethod
    def make_messages_20(scene, m1, m2, m3):
        ret_m = SSCTV.make_message(scene, m1, 1)
        scene.wait()
        SSCTV.make_message_20(scene, m2, 1)
        scene.wait()
        SSCTV.make_message_20(scene, m3, 1)
        scene.wait()
        return ret_m

    @staticmethod
    def make_message_20(scene, mess, num_rows = 1, with_text = True):
        SSCTV.make_background(scene)
        syms = []
        codes = []
        indexes = []
        n = 1
        len_code = 0
        ret_str = []
        for mes in mess:
            syms.append(M.Text(mes.symbol, color = SSCTV.get_main_color(),
                               font_size = 30.0))
            codes.append(M.Text(mes.code, color = SSCTV.get_main_color()))
            indexes.append(M.Text(str(n), color = SSCTV.get_main_color(),
                                  font_size = 16.0))
            n += 1
            len_code += len(mes.code)
            ret_str.append(mes.symbol)
        num_full = 0
        last_vg = None
        for rows in range(num_rows):
            num = round(len(codes) / num_rows)
            codes_i = []
            if rows == num_rows - 1:
                num = len(codes) - num_full
            for i in range(num):
                codes_i.append(codes[i + num_full])
            last_vg = M.VGroup(*codes_i).arrange().move_to(
                2.4 * M.UP + M.DOWN * rows * 1.9)
            scene.add(last_vg)
            num_full += num
        for i in range(len(syms)):
            scene.add(syms[i].next_to(codes[i], direction = M.UP))
            scene.add(indexes[i].next_to(syms[i], direction = M.UP))
        if num_rows == 1 and with_text:
            sf = 13.5 / last_vg.width
            M.VGroup(*syms, *codes, *indexes).scale(sf)
            bit = r"Всего бит = " + str(len_code)
            sym = r"Всего символов = " + str(len(syms))
            bit_sym = r"Бит на символ = " + str(round(len_code / len(syms), 3))
            b = M.Text(bit, color = SSCTV.get_main_color())
            s = M.Text(sym, color = SSCTV.get_main_color()).next_to(b, M.DOWN)
            bs = M.Text(bit_sym, color = SSCTV.get_main_color()).next_to(s, M.DOWN)
            scene.add(b, s, bs)
        return "".join(ret_str)

    @staticmethod
    def decode_haffman(scene, str_message, all_ps):
        SSCTV.make_background(scene)
        m = SSCTV.get_message_by_str(str_message, all_ps)
        SSCTV.make_message_20(scene, m, 1, False)
        scene.wait()

    @staticmethod
    def make_golomb(scene, all_ps_old):
        golomb_r = {0: "0", 1: "10", 2: "11"}
        golomb_q = {0: "0", 1: "10", 2: "110", 3: "1110"}
        SSCTV.make_background(scene)
        all_ps = all_ps_old.copy()
        all_ps.sort()
        all_ps.reverse()
        all_len = len(all_ps)
        for psi in range(all_len):
            t = str(psi + 1) + r" - " + all_ps[psi].symbol + r":"
            p = str(round(all_ps[psi].probability, SSCTV.PRB_NUM)) + ";"
            mobt = M.Text(
                t, font_size = 44.0,
                color = SSCTV.get_main_color()).move_to(
                    SSCTV.UL_CORNER + M.RIGHT * 0.0 + M.UP * 0.07
                    + M.DOWN * (8.0 / (all_len + 2)) * (psi + 1))
            mobp = M.Text(p, font_size = 30.0,
                          color = SSCTV.get_main_color()).next_to(mobt)
            scene.add(mobt, mobp)
            m = 3
            q = psi // m
            r = psi - q * m
            texstr = (r"q = \left[\frac{" + str(psi + 1)
                      + r"-1}3\right] = " + str(q) + r";\ r = "
                      + str(psi + 1) + r" - 1 - " + str(q) + r"\cdot"
                      + str(m) + r" = " + str(r))
            tex = M.MathTex(texstr, color = SSCTV.get_main_color(),
                            font_size = 30.0).next_to(mobt)
            scene.add(tex)
            found_ps = SSCTV.find_ps_by_symbol(
                all_ps[psi].symbol, all_ps)
            found_ps.code = golomb_q[q] + golomb_r[r]

    @staticmethod
    def make_arith(scene, str_message, all_ps):
        def prb_size(cycle):
            if cycle <= 2: return 18.0
            elif cycle <= 4: return 16.0
            return 14.0

        left_side = M.LEFT * 6.6
        SSCTV.make_background(scene)
        str_message = str_message[:6]
        mes_len = len(str_message)
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
                g_indx = SSCTV.find_index_by_symbol(
                    str_message[cycle], all_ps)
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
                return ret_str

    @staticmethod
    def make_count_1(scene, num):
        SSCTV.make_background(scene)
        s_str = num + r"_{10} = " + bin(int(num))[2:] + r"_2"
        show = M.MathTex(s_str, color = SSCTV.get_main_color(),
                         font_size = 64.0)
        scene.add(show)


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
