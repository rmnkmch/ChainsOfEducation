import manim as M
import SIPK_SSCTV_functions as SSf


class SSCTV(object):
    """SSCTV"""

    variant = 10

    tv1_in_0_1_str = ""

    tv2_F_s = 30.0#22.5
    tv2_R2 = 7.0 / 8.0
    tv2_R2_str = r"\frac {7}{8}"
    tv2_V_p = 56.10
    tv2_b_s = 7
    tv2_data1 = [9.0, 7.0, 5.0, 3.0, 1.0]
    tv2_data2 = [10.0, 8.0, 6.0, 4.0, 2.0]
    tv2_data3 = [16.2, 13.2, 10.2, 7.2, 4.2]
    tv2_data11 = [17.3, 15.425, 13.55, 11.475, 9.45]
    tv2_data22 = [21.775, 19.775, 17.725, 15.725, 13.725]
    tv2_data33 = [29.625, 26.95, 23.65, 20.875, 17.65]
    tv2_data111 = [0.0003125, 0.0034375, 0.0175, 0.048125, 0.0924875]
    tv2_data222 = [0.0028125, 0.01133, 0.03289, 0.0636325, 0.096845]
    tv2_data333 = [0.000260425, 0.00444, 0.0280025, 0.06069, 0.0979025]

    old_tv1_colors = {"Чёрный": [0, 0, 0, "#000000"],
                      "Синий": [0, 0, 1, "#0000FF"],
                      "Красный": [1, 0, 0, "#FF0000"],
                      "Пурпурный": [1, 0, 1, "#FF00FF"],
                      "Зелёный": [0, 1, 0, "#00FF00"],
                      "Голубой": [0, 1, 1, "#00FFFF"],
                      "Жёлтый": [1, 1, 0, "#FFFF00"],
                      "Белый": [1, 1, 1, "#FFFFFF"]}

    old_tv1_variants = {1: ["Пурпурный", "Чёрный", "Красный", "Голубой", "Синий"],
                        2: ["Синий", "Белый", "Пурпурный", "Жёлтый", "Зелёный"],
                        3: ["Голубой", "Красный", "Жёлтый", "Зелёный", "Чёрный"],
                        4: ["Синий", "Чёрный", "Жёлтый", "Красный", "Пурпурный"],
                        5: ["Зелёный", "Синий", "Белый", "Красный", "Голубой"],
                        6: ["Красный", "Жёлтый", "Голубой", "Чёрный", "Пурпурный"],
                        7: ["Зелёный", "Красный", "Жёлтый", "Пурпурный", "Белый"],
                        8: ["Жёлтый", "Синий", "Белый", "Красный", "Голубой"],
                        9: ["Синий", "Пурпурный", "Чёрный", "Жёлтый", "Белый"],
                        10: ["Красный", "Зелёный", "Белый", "Голубой", "Синий"],
                        11: ["Пурпурный", "Жёлтый", "Синий", "Белый", "Красный"],
                        12: ["Голубой", "Чёрный", "Зелёный", "Красный", "Жёлтый"],
                        13: ["Зелёный", "Жёлтый", "Пурпурный", "Синий", "Чёрный"],
                        14: ["Жёлтый", "Красный", "Голубой", "Чёрный", "Белый"],
                        15: ["Синий", "Зелёный", "Белый", "Голубой", "Пурпурный"]}

    old_tv_variant = 4
    old_tv1_YRB = []
    old_tv1_YRBUVCMP = []
    old_tv1_YRBDFKRB = []
    old_tv1_tex_size = 30.0

    old_tv2_YRB_DEC_BIN_HEX = []
    old_tv2_rec_for_f_kvt = []

    old_tv3_F_m_n = [[1249, 19, 3, 1, 1, 1, 0, 1],
                     [-381, 14, 3, 2, 2, 0, 0, 1],
                     [-318, -14, 3, 1, -1, 0, 1, -2],
                     [31, -45, -4, -3, -5, 0, 2, 4],
                     [154, -7, -8, -2, -2, 0, -1, 0],
                     [38, 20, -3, 2, 2, 0, -2, 2],
                     [-39, 11, 8, 3, 0, 1, 1, 0],
                     [-42, 3, 10, 1, -1, 1, 1, -1]]
    old_tv3_Q_m_n = [[8, 16, 19, 22, 26, 27, 29, 34],
                     [16, 16, 22, 24, 27, 29, 34, 37],
                     [19, 22, 26, 27, 29, 34, 34, 38],
                     [22, 22, 26, 27, 29, 34, 37, 40],
                     [22, 26, 27, 29, 32, 35, 40, 48],
                     [26, 27, 29, 32, 35, 40, 48, 58],
                     [26, 27, 29, 34, 38, 46, 56, 69],
                     [27, 29, 35, 38, 46, 56, 69, 83]]
    old_tv3_variants = {1: [16, 104], 2: [14, 96], 3: [12, 88],
                        4: [10, 80], 5: [8, 72], 6: [7, 64],
                        7: [6, 56], 8: [5, 52], 9: [4, 48],
                        10: [3, 44], 11: [2, 40], 12: [9, 75],
                        13: [11, 85], 14: [13, 91], 15: [15, 99]}
    old_tv3_Fq_values = []
    old_tv3_Fq_values_str = []
    old_tv3_N = 0
    old_tv3_Fdq = []

    @staticmethod
    def make_tv(scene: M.Scene):
        # SSCTV.make_tv1(scene)
        # SSCTV.make_tv2(scene)
        # SSCTV.make_tv3(scene)
        # SSCTV.make_old_tv1(scene)
        # SSCTV.make_old_tv2(scene)
        # SSCTV.make_old_tv3(scene)
        SSCTV.make_old_tv5(scene)

    @staticmethod
    def make_tv1(scene: M.Scene):
        psp_str = SSCTV.tv1_table_1(scene)
        if len(SSCTV.tv1_in_0_1_str) == 0:
            SSCTV.tv1_in_0_1_str = SSf.SIPK_SSCTV_functions.get_random_0_1_str(15)
        print(SSCTV.tv1_in_0_1_str)
        data01 = SSCTV.tv1_table_2(scene, psp_str)
        SSCTV.tv1_text_1(scene, data01)
        SSCTV.tv1_text_2(scene)

    @staticmethod
    def tv1_table_1(scene: M.Scene):
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

        SSf.SIPK_SSCTV_functions.make_background(scene)
        key = SSf.SIPK_SSCTV_functions.fill_zeros(bin(int(SSCTV.variant))[2:], 4)
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
            last = SSf.SIPK_SSCTV_functions.sum_mod_2(key[0], key[1])
            data.append([str(i), key[3], key[2], key[1], key[0], last])
            ret_str.append(key[0])
            key = key[1:] + last
        for i in range(len(data[0])):
            table_data.append([])
            for j in range(len(data)):
                table_data[-1].append(data[j][i])
        fs = SSf.SIPK_SSCTV_functions.table_font_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            row_labels = [
                M.Text("N", font_size = fs, color = mc),
                M.Text("1", font_size = fs, color = mc),
                M.Text("2", font_size = fs, color = mc),
                M.Text("3", font_size = fs, color = mc),
                M.Text("4", font_size = fs, color = mc),
                M.Text("C", font_size = fs, color = mc),
                ],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 0.5,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        text_1_0 = M.Text(f"Для триггера 4: 0 - {zeroes} раз; 1 - {ones} раз",
                          font_size = tts, color = mc
                          ).next_to(table, M.DOWN, 0.5)
        t0 = f"Серия нулей - {zeroes_max} подряд "
        t0 += f"в тактах {zeroes_max_ind[0]} - {zeroes_max_ind[1]}"
        text_0 = M.Text(t0, font_size = tts, color = mc
                        ).next_to(text_1_0, M.DOWN)
        t1 = f"Серия единиц - {ones_max} подряд "
        t1 += f"в тактах {ones_max_ind[0]} - {ones_max_ind[1]}"
        text_1 = M.Text(t1, font_size = tts, color = mc
                        ).next_to(text_0, M.DOWN)
        scene.add(table, text_1_0, text_0, text_1)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        ret_str = "".join(ret_str)
        return ret_str[:-1]

    @staticmethod
    def tv1_table_2(scene: M.Scene, psp_str: str):
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

        SSf.SIPK_SSCTV_functions.make_background(scene)
        in_0_1_str = SSCTV.tv1_in_0_1_str
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
        hemming_dist = 0
        for i in range(len(psp_str)):
            skr = SSf.SIPK_SSCTV_functions.sum_mod_2(in_0_1_str[i], psp_str[i])
            dskr = SSf.SIPK_SSCTV_functions.sum_mod_2(skr, psp_str[i])
            update_0_1(skr, i)
            pcp_prev = psp_str[i - 1]
            dskr_with_prev = SSf.SIPK_SSCTV_functions.sum_mod_2(skr, pcp_prev)
            table_data.append([str(i), in_0_1_str[i], psp_str[i],
                               skr, dskr, pcp_prev, dskr_with_prev])
            if dskr != dskr_with_prev: hemming_dist += 1
        skr = SSf.SIPK_SSCTV_functions.sum_mod_2(in_0_1_str[0], psp_str[0])
        dskr = SSf.SIPK_SSCTV_functions.sum_mod_2(skr, psp_str[0])
        update_0_1(skr, 15)
        pcp_prev = psp_str[14]
        dskr_with_prev = SSf.SIPK_SSCTV_functions.sum_mod_2(skr, pcp_prev)
        table_data.append([str(15), in_0_1_str[0], psp_str[0],
                           skr, dskr, pcp_prev, dskr_with_prev])
        table_data = SSf.SIPK_SSCTV_functions.transpose_list(table_data)
        fs = SSf.SIPK_SSCTV_functions.table_font_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            row_labels = [
                M.Text("N", font_size = fs, color = mc),
                M.Text("Вход", font_size = fs, color = mc),
                M.Text("ПСП", font_size = fs, color = mc),
                M.Text("Скр", font_size = fs, color = mc),
                M.Text("Дскр", font_size = fs, color = mc),
                M.Text("ПСП>>", font_size = fs, color = mc),
                M.Text("Дскр>>", font_size = fs, color = mc),
                ],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 0.5,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        return [zeroes, ones, zeroes_max, zeroes_max_ind,
                ones_max, ones_max_ind, hemming_dist]

    @staticmethod
    def tv1_text_1(scene: M.Scene, data01: list):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        zeroes, ones = (data01[0], data01[1])
        zeroes_max, zeroes_max_ind = (data01[2], data01[3])
        ones_max, ones_max_ind = (data01[4], data01[5])
        hemming_dist = data01[6]
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        text_1_0 = M.Text(f"Для Скр: 0 - {zeroes} раз; 1 - {ones} раз",
                          font_size = tts, color = mc
                          ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        t0 = f"Серия нулей - {zeroes_max} подряд "
        t0 += f"в тактах {zeroes_max_ind[0]} - {zeroes_max_ind[1]}"
        text_0 = M.Text(t0, font_size = tts, color = mc).next_to(text_1_0, M.DOWN)
        t1 = f"Серия единиц - {ones_max} подряд "
        t1 += f"в тактах {ones_max_ind[0]} - {ones_max_ind[1]}"
        text_1 = M.Text(t1, font_size = tts, color = mc).next_to(text_0, M.DOWN)
        text_hemm = M.Text(f"Расстояние Хэмминга = {hemming_dist}",
                           font_size = tts, color = mc).next_to(text_1, M.DOWN, 0.5)
        scene.add(text_1_0, text_1, text_0, text_hemm)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv1_text_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        dict_vars = {1: 101, 2: 1542, 3: 3160, 4: 4422, 5: 15214,
                     6: 26700, 7: 37120, 8: 52642, 9: 48592, 10: 59306,
                     11: 61085, 12: 7706, 13: 11490, 14: 32084, 15: 41056}
        bit = dict_vars[SSCTV.variant]
        max_bit = 64800
        column_bit = 64800 // 3
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        str_bit = f"Бит {1}: {bit}"
        text_bit = M.Text(str_bit, font_size = tts, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side + M.LEFT * 6.0 + M.DOWN * 0.7)
        scene.add(text_bit)
        for i in range(1, 10, 1):
            if bit + column_bit >= max_bit:
                str_bit = f"Бит {i + 1}: {bit} - {column_bit * 2}"
                str_bit += f" + 1 = {bit - column_bit * 2 + 1}"
                bit = bit - column_bit * 2 + 1
            else:
                str_bit = f"Бит {i + 1}: {bit} + {column_bit} = {bit + column_bit}"
                bit = bit + column_bit
            text_bit = M.Text(str_bit, font_size = tts, color = mc).next_to(
                SSf.SIPK_SSCTV_functions.upper_side + M.LEFT * 6.0
                + M.DOWN * (i + 1) * 0.7)
            scene.add(text_bit)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_tv2(scene: M.Scene):
        SSCTV.tv2_diagram(scene)
        SSCTV.tv2_formula_1(scene)
        SSCTV.tv2_formula_2(scene)
        SSCTV.tv2_count()
        SSCTV.tv2_graphs_1(scene)
        SSCTV.tv2_graphs_2(scene)
        SSCTV.tv2_graph_3(scene)
        # SSCTV.tv2_formula_3(scene)

    @staticmethod
    def tv2_diagram(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        dict_vars = {1: 14, 2: 2, 3: 1, 4: 15, 5: 3, 6: 7, 7: 9, 8: 5,
                     9: 4, 10: 8, 11: 13, 12: 0, 13: 10, 14: 12, 15: 4}
        dict_row0 = {0: "0000", 1: "0001", 2: "0101", 3: "0100"}
        dict_row1 = {0: "1000", 1: "1001", 2: "1101", 3: "1100"}
        dict_row2 = {0: "1010", 1: "1011", 2: "1111", 3: "1110"}
        dict_row3 = {0: "0010", 1: "0011", 2: "0111", 3: "0110"}
        dict_rows = {0: dict_row0, 1: dict_row1, 2: dict_row2, 3: dict_row3}
        bit_0 = dict_vars[SSCTV.variant]
        codes = []
        for i in range(16):
            codes.append("")
        for i in range(4):
            bit = bit_0 + i
            if bit // 4 != bit_0 // 4: bit -= 4
            for j in range(4):
                bit2 = (bit + j * 4) % 16
                codes[bit2] = dict_rows[j][i]
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (-6, 6, 1),
            y_range = (-6, 6, 1),
            x_length = 7.0,
            y_length = 7.0,
            color = mc,
            axis_config = {"stroke_width": 4},
            background_line_style = {"stroke_width": 0}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        number_plane.get_axes().set_color(mc)
        graphs = M.VGroup()
        for i in range(16):
            d = M.Dot(
                number_plane.c2p(- 4.5 + 3.0 * (i % 4), 4.5 - 3.0 * (i // 4), 0.0),
                color = mc)
            graphs += M.Text(codes[i], font_size = tts, color = mc
                             ).next_to(d, M.DOWN, 0.15)
            graphs += d
        scene.add(number_plane, graphs)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv2_formula_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        V_f = 2.0 * SSCTV.tv2_F_s
        V_in2 = V_f * SSCTV.tv2_R2
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"b_s = 2"
        tex = M.MathTex(tx, font_size = txs, color = mc
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        txt = M.Text("бит/симв", font_size = tts, color = mc)
        tx12 = r";\ F_s = " + str(SSCTV.tv2_F_s)
        tex12 = M.MathTex(tx12, font_size = txs, color = mc)
        txt12 = M.Text("Мсимв/с", font_size = tts, color = mc)
        tx2 = r"V_f = F_s \cdot b_s = " + str(SSCTV.tv2_F_s)
        tx2 += r" \cdot 2 = " + str(V_f)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        txt2 = M.Text("Mбит/с", font_size = tts, color = mc)
        tx22 = r" = V_{out2}"
        tex22 = M.MathTex(tx22, font_size = txs, color = mc)
        tx3 = r"V_{in2} = R_2 \cdot V_{out2} = " + SSCTV.tv2_R2_str + r" \cdot "
        tx3 += str(V_f) + r" = " + str(V_in2)
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        txt3 = M.Text("Mбит/с", font_size = tts, color = mc)
        tx4 = r" = V_{out1}"
        tex4 = M.MathTex(tx4, font_size = txs, color = mc)
        tx5 = r"V_{in1} = R_1 \cdot V_{out1} = 0.92 \cdot "
        tx5 += str(V_in2) + r" = " + str(round(V_in2 * 0.92, 5))
        tex5 = M.MathTex(tx5, font_size = txs, color = mc).next_to(tex3, M.DOWN)
        txt5 = M.Text("Mбит/с", font_size = tts, color = mc)
        tx6 = r" = V_p"
        tex6 = M.MathTex(tx6, font_size = txs, color = mc)
        tex.shift(M.LEFT * (txt.width + tex12.width + txt12.width) * 0.5)
        txt.next_to(tex)
        tex12.next_to(txt)
        txt12.next_to(tex12)
        tex2.shift(M.LEFT * (txt2.width + tex22.width) * 0.5)
        txt2.next_to(tex2)
        tex22.next_to(txt2)
        tex3.shift(M.LEFT * txt3.width * 0.5)
        txt3.next_to(tex3)
        tex4.next_to(txt3)
        tex5.shift(M.LEFT * (txt5.width + tex6.width) * 0.5)
        txt5.next_to(tex5)
        tex6.next_to(txt5)
        scene.add(tex, txt, tex12, txt12, tex2, txt2, tex22,
                  tex3, txt3, tex4, tex5, txt5, tex6)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv2_formula_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        V_f = round(SSCTV.tv2_V_p / 0.92, 3)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"b_s = " + str(SSCTV.tv2_b_s)
        tex = M.MathTex(tx, font_size = txs, color = mc
                        ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        txt = M.Text("бит/симв", font_size = tts, color = mc)
        tx12 = r";\ V_p = V_{in} = " + str(SSCTV.tv2_V_p)
        tex12 = M.MathTex(tx12, font_size = txs, color = mc)
        txt12 = M.Text("Мбит/с", font_size = tts, color = mc)
        tx2 = r"V_{out} = \frac {V_{in}}{R} = \frac {" + str(SSCTV.tv2_V_p)
        tx2 += r"}{0.92} = " + str(V_f)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        txt2 = M.Text("Mбит/с", font_size = tts, color = mc)
        tx22 = r" = V_f"
        tex22 = M.MathTex(tx22, font_size = txs, color = mc)
        tx3 = r"F_s = \frac {V_f}{b_s} = \frac {" + str(V_f)
        tx3 += r"}{" + str(SSCTV.tv2_b_s) + r"} = "
        tx3 += str(round(V_f / SSCTV.tv2_b_s, 3))
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        txt3 = M.Text("Mсимв/с", font_size = tts, color = mc)
        tex.shift(M.LEFT * (txt.width + tex12.width + txt12.width) * 0.5)
        txt.next_to(tex)
        tex12.next_to(txt)
        txt12.next_to(tex12)
        tex2.shift(M.LEFT * (txt2.width + tex22.width) * 0.5)
        txt2.next_to(tex2)
        tex22.next_to(txt2)
        tex3.shift(M.LEFT * txt3.width * 0.5)
        txt3.next_to(tex3)
        scene.add(tex, txt, tex12, txt12, tex2, txt2, tex22, tex3, txt3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv2_graphs_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (0, 17, 1),
            y_range = (6, 32, 2),
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
        line_graph1 = number_plane.plot_line_graph(
            x_values = SSCTV.tv2_data1,
            y_values = SSCTV.tv2_data11,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = "#B40097",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph2 = number_plane.plot_line_graph(
            x_values = SSCTV.tv2_data2,
            y_values = SSCTV.tv2_data22,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = "#00AA72",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph3 = number_plane.plot_line_graph(
            x_values = SSCTV.tv2_data3,
            y_values = SSCTV.tv2_data33,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = "#FFC500",
                                    stroke_color = mc),
            stroke_width = 4)
        y_label = M.MathTex("MER,", font_size = 24.0, color = mc
                            ).next_to(number_plane, M.UL)
        y_label.shift(M.RIGHT * 0.6 + M.DOWN * 0.1)
        x_label = M.MathTex(r"\frac {E_b}{N_0},", font_size = 24.0, color = mc
                            ).next_to(number_plane, M.DR)
        x_label.shift(M.LEFT * 0.35 + M.UP * 0.4)
        y_label2 = M.Text("дБ", font_size = 18.0, color = mc
                          ).next_to(y_label, M.DOWN, 0.1)
        x_label2 = M.Text("дБ", font_size = 18.0, color = mc
                          ).next_to(x_label, buff = 0.1)
        scene.add(number_plane, line_graph1, line_graph2, line_graph3,
                  y_label, x_label, y_label2, x_label2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv2_graphs_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (0, 17, 1),
            y_range = (-4, 0, 1),
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
        line_graph1 = number_plane.plot_line_graph(
            x_values = SSCTV.tv2_data1,
            y_values = SSCTV.tv2_data111,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = "#B40097",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph2 = number_plane.plot_line_graph(
            x_values = SSCTV.tv2_data2,
            y_values = SSCTV.tv2_data222,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = "#00AA72",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph3 = number_plane.plot_line_graph(
            x_values = SSCTV.tv2_data3,
            y_values = SSCTV.tv2_data333,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = "#FFC500",
                                    stroke_color = mc),
            stroke_width = 4)
        y_label = M.MathTex("BER", font_size = 24.0, color = mc
                            ).next_to(number_plane, M.UL)
        y_label.shift(M.RIGHT * 0.7 + M.DOWN * 0.1)
        x_label = M.MathTex(r"\frac {E_b}{N_0},", font_size = 24.0, color = mc
                            ).next_to(number_plane, M.DR)
        x_label.shift(M.LEFT * 0.35 + M.UP * 0.4)
        x_label2 = M.Text("дБ", font_size = 18.0, color = mc
                          ).next_to(x_label, buff = 0.1)
        scene.add(number_plane, line_graph1, line_graph2, line_graph3,
                  y_label, x_label, x_label2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv2_graph_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
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
            vertex_dot_style = dict(stroke_width = 4, fill_color = "#B40097",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph2 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [2, 2],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = "#00AA72",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph3 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [3, 3],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 4, fill_color = "#FFC500",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph4 = number_plane.plot_line_graph(
            x_values = [0.5, 0.5, 4, 4, 0.5],
            y_values = [0, 4, 4, 0, 0],
            line_color = mc,
            vertex_dot_radius = 0.0,
            vertex_dot_style = dict(stroke_width = 0),
            stroke_width = 4)
        txt1 = M.Text("4 ФМ", font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 1.0, 0.0))
        txt2 = M.Text("16 КАМ", font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 2.0, 0.0))
        txt3 = M.Text("64 КАМ", font_size = tts, color = mc).next_to(
            number_plane.c2p(2.0, 3.0, 0.0))
        scene.add(number_plane, line_graph1, line_graph2, line_graph3, line_graph4,
                  txt1, txt2, txt3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv2_formula_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"MER = 10 \lg \left[ \frac {\sum_{i=1}^N (I_i^2 + Q_i^2)}"
        tx += r"{\sum_{i=1}^N ({\delta I_i}^2 + {\delta Q_i}^2)} \right]"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        txt = M.Text("дБ", font_size = tts, color = mc)
        tex.shift(M.LEFT * 0.5 * txt.width)
        txt.next_to(tex)
        scene.add(tex, txt)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv2_count():
        data = r"""17.4
0
17.4
0
17.8
0.00125
17.5
0
15.3
0.005
15.6
0.00625
15.4
0.00125
15.7
0.0025
13.4
0.0175
13.6
0.0175
13.5
0.01875
13.2
0.01625
11.4
0.0525
11.2
0.0575
11.8
0.04625
11.3
0.04875
9.5
0.0925
9.3
0.09625
9.4
0.07875
9.3
0.095
21.7
0.003906
21.9
0.001875
21.8
0.002344
21.6
0.0025
19.8
0.01078
19.7
0.01391
19.7
0.01375
19.8
0.01109
17.6
0.03312
17.7
0.03219
17.9
0.03078
17.8
0.03203
15.8
0.06328
15.9
0.06125
16.1
0.05969
15.8
0.06188
14.0
0.09641
13.7
0.09656
13.7
0.09594
13.6
0.1031
29.7
0.0001302
29.6
0.0002604
29.7
0.0001302
29.5
0.0003646
26.9
0.004401
26.8
0.005443
26.9
0.004245
26.9
0.00474
23.6
0.02849
23.7
0.02602
23.7
0.02711
23.6
0.02755
20.8
0.06169
20.8
0.06164
20.9
0.05891
20.9
0.05971
17.7
0.09758
17.6
0.1001
17.6
0.1003
17.7
0.09687"""
        mer = 0.0
        ber = 0.0
        dat = []
        dat2 = []
        i = 0
        j = 0
        for line in data.split():
            if i % 8 == 0:
                if mer != 0.0:
                    print(round(mer * 0.25, 9))
                    print(round(ber * 0.25, 9))
                    dat.append(round(mer * 0.25, 9))
                    dat2.append(round(ber * 0.25, 9))
                    if j == 4:
                        SSCTV.tv2_data11 = dat
                        SSCTV.tv2_data111 = dat2
                        dat = []
                        dat2 = []
                    if j == 9:
                        SSCTV.tv2_data22 = dat
                        SSCTV.tv2_data222 = dat2
                        dat = []
                        dat2 = []
                    j += 1
                mer = 0.0
                ber = 0.0
            if i % 2 == 0: mer += float(line)
            else: ber += float(line)
            i += 1
        print(round(mer * 0.25, 9))
        print(round(ber * 0.25, 9))
        dat.append(round(mer * 0.25, 9))
        dat2.append(round(ber * 0.25, 9))
        SSCTV.tv2_data33 = dat
        SSCTV.tv2_data333 = dat2

    @staticmethod
    def tv3_func_part_by_2_bits(
        bits: str, part: int,
        fall: float = 20.0, amplitude: float = 2.0, zero_level: float = - 1.0):
        if bits[0] == "0" and bits[1] == "0":
            return lambda x: zero_level
        elif bits[0] == "1" and bits[1] == "1":
            return lambda x: zero_level + amplitude
        elif bits[0] == "0" and bits[1] == "1":
            if part == 1: return lambda x: SSf.SIPK_SSCTV_functions.sigmoid(
                x * fall) * amplitude + zero_level
            else: return lambda x: SSf.SIPK_SSCTV_functions.sigmoid(
                (1.0 - x) * fall) * - amplitude - zero_level
        elif bits[0] == "1" and bits[1] == "0":
            if part == 1: return lambda x: SSf.SIPK_SSCTV_functions.sigmoid(
                x * fall) * - amplitude - zero_level
            else: return lambda x: SSf.SIPK_SSCTV_functions.sigmoid(
                (1.0 - x) * fall) * amplitude + zero_level

    @staticmethod
    def tv3_func_by_3_bits(bits: str, fall: float = 20.0):
        part_1 = SSCTV.tv3_func_part_by_2_bits(bits[:2], 1, fall)
        part_2 = SSCTV.tv3_func_part_by_2_bits(bits[1:], 2, fall)
        return lambda x: (
            SSf.SIPK_SSCTV_functions.restrict_func_value(part_1(x), x, 0.0, 0.5)
            + SSf.SIPK_SSCTV_functions.restrict_func_value(part_2(x), x, 0.5, 1.0))

    @staticmethod
    def make_tv3(scene: M.Scene):
        SSCTV.tv3_diagram(scene)
        SSCTV.tv3_eye_diagram(scene)

    @staticmethod
    def tv3_diagram(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        dict_vars = {1: "011010010101", 2: "110001011011", 3: "010110100101",
                     4: "100111010100", 5: "001110101100", 6: "111000101001",
                     7: "001101001110", 8: "101100100110", 9: "010100111001",
                     10: "110011000110", 11: "011100100110", 12: "110110001010",
                     13: "010111001101", 14: "100110001011", 15: "011000111010"}
        bit = dict_vars[SSCTV.variant]
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (0, 12, 1),
            y_range = (-2, 2, 1),
            x_length = 13.0,
            y_length = 4.0,
            color = mc,
            axis_config = {
                "numbers_to_include": M.np.arange(0, 12, 1),
                "font_size": 18.0,
                "stroke_width": 3,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": 0.11,
                "label_direction": M.DR,
                "color": mc,
                },
            y_axis_config = {
                "numbers_to_include": M.np.arange(-1, 2, 1),
                "label_direction": M.LEFT},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
                },
            tips = False,
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        number_plane.get_axes().set_color(mc)
        graphs = M.VGroup()
        for i in range(len(bit) // 2):
            graphs += M.Text(str(i + 1), font_size = tts, color = mc).next_to(
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
                color = mc,
                use_smoothing = False)
        scene.add(number_plane, graphs)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv3_eye_diagram(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        dict_vars = {1: "011010010101", 2: "110001011011", 3: "010110100101",
                     4: "100111010100", 5: "001110101100", 6: "111000101001",
                     7: "001101001110", 8: "101100100110", 9: "010100111001",
                     10: "110011000110", 11: "011100100110", 12: "110110001010",
                     13: "010111001101", 14: "100110001011", 15: "011000111010"}
        dict_colors = {1: M.DARK_BROWN, 2: M.TEAL, 3: M.RED_D,
                       4: M.YELLOW, 5: M.DARK_BLUE, 6: M.ORANGE}
        dict_stroke_widths = {1: 28, 2: 23, 3: 18, 4: 13, 5: 8, 6: 3}
        bit = dict_vars[SSCTV.variant]
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (0, 17, 1),
            y_range = (-3, 3, 1),
            x_length = 13.0,
            y_length = 5.0,
            color = mc,
            axis_config = {"stroke_width": 0},
            background_line_style = {"stroke_width": 0}
            ).next_to(M.UP * 3.3, M.DOWN)
        graphs = M.VGroup()
        offset = 0.0
        for i in range(len(bit) // 2):
            graphs += M.Text(str(i + 1), font_size = tts, color = mc).next_to(
                number_plane.c2p(1.0 + i * 3.0, 3.1, 0.0), M.UP)
        for i in range(len(bit)):
            if i == 0: prev_bit = bit[i]
            else: prev_bit = bit[i - 1]
            if i == len(bit) - 1: next_bit = bit[i]
            else: next_bit = bit[i + 1]
            graphs += number_plane.plot(
                lambda x: 2.0 + SSCTV.tv3_func_by_3_bits(
                    prev_bit + bit[i] + next_bit)(x - i - offset),
                x_range = (i + offset, i + offset + 1.0, 0.0199),
                color = mc,
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
            if i % 2 == 1 and i != 0: offset += 1.0
        scene.add(number_plane, graphs)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_old_tv1(scene: M.Scene):
        SSCTV.old_tv1_formula_1(scene)
        SSCTV.old_tv1_graph_1(scene)
        SSCTV.old_tv1_graph_2(scene, [SSCTV.old_tv1_YRB[i][1] for i in range(5)])
        SSCTV.old_tv1_graph_2(scene, [SSCTV.old_tv1_YRB[i][2] for i in range(5)])
        SSCTV.old_tv1_formula_2(scene)
        # SSCTV.old_tv1_formula_3(scene)
        SSCTV.old_tv1_formula_4(scene)
        SSCTV.old_tv1_formula_5(scene)
        # SSCTV.old_tv1_formula_6(scene)
        SSCTV.old_tv1_graph_3(scene)
        SSCTV.old_tv1_table_1(scene)
        SSCTV.old_tv1_table_2(scene)

    @staticmethod
    def old_tv1_formula_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSCTV.old_tv1_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        i = 0
        for text_color in SSCTV.old_tv1_variants[SSCTV.old_tv_variant]:
            r, g, b, color = SSCTV.old_tv1_colors[text_color]
            Y = round(0.299 * r + 0.587 * g + 0.114 * b, 3)
            R = round(r - Y, 3)
            B = round(b - Y, 3)
            txt = M.Text(text_color + ": ", font_size = tts, color = mc).next_to(
                M.UP * 3.5 + M.LEFT * 6.5 + i * M.DOWN * 1.5)
            tx = r"E_Y^{'} = 0.299 \cdot " + str(r) + r" + 0.587 \cdot "
            tx += str(g) + r" + 0.114 \cdot " + str(b) + r" = "
            tx += str(Y) + r";"
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(txt)
            tx2 = r"E_{R-Y}^{'} = " + str(r) + r" - " + str(Y) + r" = "
            tx2 += str(R) + r";"
            tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(
                M.UP * 2.85 + M.LEFT * 6.5 + i * M.DOWN * 1.5)
            tx3 = r"E_{B-Y}^{'} = " + str(b) + r" - " + str(Y) + r" = "
            tx3 += str(B) + r";"
            tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(
                tex2, buff = 0.5)
            scene.add(txt, tex, tex2, tex3)
            i += 1
            SSCTV.old_tv1_YRB.append((Y, R, B))
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv1_graph_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (0, 12, 1),
            y_range = (0.0, 1.01, 0.2),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "include_numbers": False,
                "font_size": 24.0,
                "stroke_width": 6,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": 0.13,
                "color": mc},
            y_axis_config = {
                "label_direction": M.LEFT,
                "include_numbers": True},
            background_line_style = {"stroke_opacity": 0.0},
            tips = False)
        number_plane.get_axes().set_color(mc)
        background_line_style = {"stroke_color": mc,
                "stroke_width": 2,
                "stroke_opacity": 0.5}
        background_line_style2 = {"stroke_opacity": 0.0}
        background_lines, faded_lines = number_plane._get_lines()
        for i in range(1, 7, 1):
            background_lines[i].set_style(**background_line_style)
        number_plane.add_to_back(background_lines)
        for i in range(7, 18, 1):
            background_lines[i].set_style(**background_line_style2)
            number_plane.add_to_back(background_lines[i])
        scene.add(number_plane)
        for YRB in range(len(SSCTV.old_tv1_YRB)):
            line_graph = number_plane.plot_line_graph(
                x_values = [1 + YRB * 2, 1 + YRB * 2, 3 + YRB * 2,
                            3 + YRB * 2, 1 + YRB * 2],
                y_values = [0.0, SSCTV.old_tv1_YRB[YRB][0],
                            SSCTV.old_tv1_YRB[YRB][0], 0.0, 0.0],
                line_color = mc,
                vertex_dot_radius = 0.0,
                vertex_dot_style = dict(stroke_width = 0),
                stroke_width = 6)
            colr = SSCTV.old_tv1_colors[
                SSCTV.old_tv1_variants[SSCTV.old_tv_variant][YRB]][3]
            rect = M.Polygon(number_plane.c2p(1 + YRB * 2, 0.0, 0.0),
                             number_plane.c2p(
                                 1 + YRB * 2, SSCTV.old_tv1_YRB[YRB][0], 0.0),
                             number_plane.c2p(
                                 3 + YRB * 2, SSCTV.old_tv1_YRB[YRB][0], 0.0),
                             number_plane.c2p(3 + YRB * 2, 0.0, 0.0),
                             color = colr,
                             fill_color = colr,
                             fill_opacity = 1.0)
            txt = M.Text(
                SSCTV.old_tv1_variants[SSCTV.old_tv_variant][YRB],
                font_size = 22.0, color = mc).next_to(
                number_plane.c2p(2 + YRB * 2, SSCTV.old_tv1_YRB[YRB][0], 0.0), M.UP)
            scene.add(rect, line_graph, txt)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv1_graph_2(scene: M.Scene, columns: list):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (0, 12, 1),
            y_range = (-1.01, 1.01, 0.2),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "include_numbers": False,
                "font_size": 24.0,
                "stroke_width": 6,
                "include_ticks": False,
                "include_tip": False,
                "line_to_number_buff": 0.13,
                "color": mc},
            y_axis_config = {
                "label_direction": M.LEFT,
                "include_numbers": True},
            background_line_style = {"stroke_opacity": 0.0},
            tips = False)
        number_plane.get_axes().set_color(mc)
        background_line_style = {"stroke_color": mc,
                "stroke_width": 2,
                "stroke_opacity": 0.5}
        background_line_style2 = {"stroke_opacity": 0.0}
        background_lines, faded_lines = number_plane._get_lines()
        for i in range(0, 11, 1):
            background_lines[i].set_style(**background_line_style)
        number_plane.add_to_back(background_lines)
        for i in range(11, 23, 1):
            background_lines[i].set_style(**background_line_style2)
            number_plane.add_to_back(background_lines[i])
        scene.add(number_plane)
        for YRB in range(len(columns)):
            line_graph = number_plane.plot_line_graph(
                x_values = [1 + YRB * 2, 1 + YRB * 2, 3 + YRB * 2,
                            3 + YRB * 2, 1 + YRB * 2],
                y_values = [0.0, columns[YRB], columns[YRB], 0.0, 0.0],
                line_color = mc,
                vertex_dot_radius = 0.0,
                vertex_dot_style = dict(stroke_width = 0),
                stroke_width = 6)
            colr = SSCTV.old_tv1_colors[
                SSCTV.old_tv1_variants[SSCTV.old_tv_variant][YRB]][3]
            rect = M.Polygon(number_plane.c2p(1 + YRB * 2, 0.0, 0.0),
                             number_plane.c2p(1 + YRB * 2, columns[YRB], 0.0),
                             number_plane.c2p(3 + YRB * 2, columns[YRB], 0.0),
                             number_plane.c2p(3 + YRB * 2, 0.0, 0.0),
                             color = colr,
                             fill_color = colr,
                             fill_opacity = 1.0)
            to_text_y = columns[YRB]
            if to_text_y < 0.0: to_text_y = 0.0
            txt = M.Text(
                SSCTV.old_tv1_variants[SSCTV.old_tv_variant][YRB],
                font_size = 22.0, color = mc).next_to(
                number_plane.c2p(2 + YRB * 2, to_text_y, 0.0), M.UP)
            scene.add(rect, line_graph, txt)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv1_formula_2(scene: M.Scene):
        from math import sqrt, pi
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSCTV.old_tv1_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        fs = 22.0
        i = 0
        for text_color in SSCTV.old_tv1_variants[SSCTV.old_tv_variant]:
            r, g, b, color = SSCTV.old_tv1_colors[text_color]
            Y = round(0.299 * r + 0.587 * g + 0.114 * b, 3)
            R = round(r - Y, 3)
            B = round(b - Y, 3)
            U = round(B * 0.493, 3)
            V = round(R * 0.877, 3)
            U_CM = round(sqrt(U * U + V * V), 3)
            txt = M.Text(text_color + ": ", font_size = tts, color = mc).next_to(
                M.UP * 3.5 + M.LEFT * 6.5 + i * M.DOWN * 1.5)
            tx = r"U = 0.493 \cdot " + str(B) + r" = " + str(U) + r";"
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(txt)
            tx2 = r"V = 0.877 \cdot " + str(R) + r" = " + str(V) + r";"
            tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex)
            tx3 = r"U_{CM} = \sqrt{"
            if U < 0.0: tx3 += r"(" + str(U) + r")"
            else: tx3 += str(U)
            tx3 += r"^2 + "
            if V < 0.0: tx3 += r"(" + str(V) + r")"
            else: tx3 += str(V)
            tx3 += r"^2} = "
            tx3 += str(U_CM) + r";"
            tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(
                M.UP * 2.85 + M.LEFT * 6.5 + i * M.DOWN * 1.5)
            scene.add(txt, tex, tex2, tex3)
            SSCTV.old_tv1_YRBUVCMP.append([Y, R, B, U, V, U_CM, 0.0, 0.0])
            if U != 0.0:
                P_rad = round(SSf.SIPK_SSCTV_functions.get_angle_by_dx_dy(U, V), 3)
                P_grad = round(P_rad * 180.0 / pi, 1)
                tx4 = r"{\varphi}_C = \arctan \frac {"
                tx4 += str(V) + r"}{" + str(U) + r"} = "
                tx4 += str(P_rad)
                tex4 = M.MathTex(tx4, font_size = txs, color = mc).next_to(tex3)
                txt4 = M.Text("рад", font_size = fs, color = mc).next_to(
                    tex4, buff = 0.18)
                tx5 = r" = " + str(P_grad)
                tex5 = M.MathTex(tx5, font_size = txs, color = mc).next_to(txt4)
                txt5 = M.Text("град", font_size = fs, color = mc).next_to(
                    tex5, buff = 0.18)
                scene.add(tex4, txt4, tex5, txt5)
                SSCTV.old_tv1_YRBUVCMP[-1][6] = P_rad
                SSCTV.old_tv1_YRBUVCMP[-1][7] = P_grad
            i += 1
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv1_formula_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSCTV.old_tv1_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"U = 0.493 \cdot E_{B-Y}^{'};\ V = 0.877 \cdot E_{R-Y}^{'}"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"U_{CM} = \sqrt{U^2 + V^2};\ "
        tx2 += r"{\varphi}_C = \arctan \frac {V}{U}"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        scene.add(tex, tex2)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv1_formula_4(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSCTV.old_tv1_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        i = 0
        for text_color in SSCTV.old_tv1_variants[SSCTV.old_tv_variant]:
            r, g, b, color = SSCTV.old_tv1_colors[text_color]
            Y = round(0.299 * r + 0.587 * g + 0.114 * b, 3)
            R = round(r - Y, 3)
            B = round(b - Y, 3)
            D_R = round(-1.9 * R, 3)
            if R == 0.0: D_R = 0.0
            D_B = round(1.5 * B, 3)
            f_R = round(4.406 + 0.280 * D_R, 3)
            f_B = round(4.250 + 0.230 * D_B, 3)
            txt = M.Text(text_color + ": ", font_size = tts, color = mc).next_to(
                M.UP * 3.5 + M.LEFT * 6.5 + i * M.DOWN * 1.5)
            tx = r"D_R = -1.9 \cdot " + str(R) + r" = " + str(D_R) + r";"
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(txt)
            tx2 = r"D_B = 1.5 \cdot " + str(B) + r" = " + str(D_B) + r";"
            tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex)
            tx3 = r"f_R = 4.406 + 0.280 \cdot " + str(D_R)
            tx3 += r" = " + str(f_R) + r";"
            tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(
                M.UP * 2.85 + M.LEFT * 6.5 + i * M.DOWN * 1.5)
            tx4 = r"f_B = 4.250 + 0.230 \cdot " + str(D_B)
            tx4 += r" = " + str(f_B) + r";"
            tex4 = M.MathTex(tx4, font_size = txs, color = mc).next_to(tex3)
            scene.add(txt, tex, tex2, tex3, tex4)
            i += 1
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv1_formula_5(scene: M.Scene):
        from math import log10
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = 24.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        i = 0
        for text_color in SSCTV.old_tv1_variants[SSCTV.old_tv_variant]:
            r, g, b, color = SSCTV.old_tv1_colors[text_color]
            Y = round(0.299 * r + 0.587 * g + 0.114 * b, 3)
            R = round(r - Y, 3)
            B = round(b - Y, 3)
            D_R = round(-1.9 * R, 3)
            if R == 0.0: D_R = 0.0
            D_B = round(1.5 * B, 3)
            f_R = round(4.406 + 0.280 * D_R, 3)
            f_B = round(4.250 + 0.230 * D_B, 3)
            f_0 = 4.286
            K_1 = 16
            K_2 = 1.26
            F = round(f_R / f_0 - f_0 / f_R, 3)
            K = round(10.0 * log10((1 + (K_1 * F) ** 2) / (1 + (K_2 * F) ** 2)), 3)
            txt = M.Text(text_color[0] + ": ", font_size = tts, color = mc).next_to(
                M.UP * 3.5 + M.LEFT * 6.5 + i * M.DOWN * 1.5, M.LEFT, 0.0)
            tx = r"f = f_R = " + str(f_R) + r";"
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(txt)
            tx2 = r"F = \frac {" + str(f_R) + r"}{" + str(f_0) + r"} - "
            tx2 += r"\frac {" + str(f_0) + r"}{" + str(f_R) + r"} = "
            tx2 += str(F) + r";"
            tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex)
            tx3 = r"K = 10 \cdot \lg \frac {1 + (" + str(K_1) + r" \cdot "
            tx3 += str(F) + r")^2}{1 + (" + str(K_2) + r" \cdot "
            tx3 += str(F) + r")^2} = " + str(K) + r";"
            tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2)
            scene.add(txt, tex, tex2, tex3)
            SSCTV.old_tv1_YRBDFKRB.append([Y, R, B, D_R, D_B, f_R, f_B, K])
            F = round(f_B / f_0 - f_0 / f_B, 4)
            K = round(10.0 * log10((1 + (K_1 * F) ** 2) / (1 + (K_2 * F) ** 2)), 3)
            tx = r"f = f_B = " + str(f_B) + r";"
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
                M.UP * 2.79 + M.LEFT * 6.5 + i * M.DOWN * 1.5)
            tx2 = r"F = \frac {" + str(f_B) + r"}{" + str(f_0) + r"} - "
            tx2 += r"\frac {" + str(f_0) + r"}{" + str(f_B) + r"} = "
            tx2 += str(F) + r";"
            tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex)
            tx3 = r"K = 10 \cdot \lg \frac {1 + (" + str(K_1) + r" \cdot "
            tx3 += str(F) + r")^2}{1 + (" + str(K_2) + r" \cdot "
            tx3 += str(F) + r")^2} = " + str(K) + r";"
            tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2)
            scene.add(tex, tex2, tex3)
            SSCTV.old_tv1_YRBDFKRB[-1].append(K)
            i += 1
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv1_formula_6(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSCTV.old_tv1_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"E_Y^{'} = 0.299 \cdot E_R^{'}"
        tx += r" + 0.587 \cdot E_G^{'} + 0.114 \cdot E_B^{'}"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"E_{R-Y}^{'} = E_{R}^{'} - E_{Y}^{'};\ "
        tx2 += r"E_{B-Y}^{'} = E_{B}^{'} - E_{Y}^{'}"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"E_p = U \cos \omega_C t \pm V \sin \omega_C t"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        tx4 = r"D_R = -1.9 \cdot E_{R-Y}^{'}"
        tex4 = M.MathTex(tx4, font_size = txs, color = mc).next_to(tex3, M.DOWN)
        tx5 = r"D_B = 1.5 \cdot E_{B-Y}^{'}"
        tex5 = M.MathTex(tx5, font_size = txs, color = mc).next_to(tex4, M.DOWN)
        tx6 = r"f_R = 4.406 + 0.280 \cdot D_R"
        tex6 = M.MathTex(tx6, font_size = txs, color = mc).next_to(tex5, M.DOWN)
        tx7 = r"f_B = 4.250 + 0.230 \cdot D_B"
        tex7 = M.MathTex(tx7, font_size = txs, color = mc).next_to(tex6, M.DOWN)
        tx8 = r"K = 10 \cdot \lg \frac {1 + (K_1 \cdot F)^2}{1 + (K_2 \cdot F)^2}"
        tex8 = M.MathTex(tx8, font_size = txs, color = mc).next_to(tex7, M.DOWN)
        tx9 = r"K_1 = 16;\ K_2 = 1.26;\ F = \frac {f}{f_0} - \frac{f_0}{f};\ "
        tx9 += r"f_0 = 4.286;\ f = f_R,\ f = f_B"
        tex9 = M.MathTex(tx9, font_size = txs, color = mc).next_to(tex8, M.DOWN)
        scene.add(tex, tex2, tex3, tex4, tex5, tex6, tex7, tex8, tex9)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv1_graph_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (-0.7, 0.7, 0.1),
            y_range = (-0.7, 0.7, 0.1),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "include_numbers": True,
                "font_size": 18.0,
                "stroke_width": 4,
                "include_ticks": True,
                "include_tip": False,
                "line_to_number_buff": 0.1,
                "label_direction": M.DR,
                "color": mc},
            y_axis_config = {"label_direction": M.DR},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 1,
                "stroke_opacity": 0.5},
            tips = False)
        number_plane.get_axes().set_color(mc)
        scene.add(number_plane)
        for YRB in range(len(SSCTV.old_tv1_YRBUVCMP)):
            colr = SSCTV.old_tv1_colors[
                SSCTV.old_tv1_variants[SSCTV.old_tv_variant][YRB]][3]
            if SSCTV.old_tv1_YRBUVCMP[YRB][4] != 0.0:
                d = M.Dot(number_plane.c2p(
                    SSCTV.old_tv1_YRBUVCMP[YRB][3],
                    SSCTV.old_tv1_YRBUVCMP[YRB][4], 0.0),
                          0.1, stroke_width = 3, color = colr, stroke_color = mc)
                txt = M.Text(
                    "+ " + SSCTV.old_tv1_variants[SSCTV.old_tv_variant][YRB],
                    font_size = 20.0, color = mc).next_to(
                        number_plane.c2p(
                            SSCTV.old_tv1_YRBUVCMP[YRB][3],
                            SSCTV.old_tv1_YRBUVCMP[YRB][4], 0.0), M.UR, 0.15)
                d2 = M.Dot(number_plane.c2p(
                    SSCTV.old_tv1_YRBUVCMP[YRB][3],
                    - SSCTV.old_tv1_YRBUVCMP[YRB][4], 0.0),
                           0.1, stroke_width = 3, color = colr, stroke_color = mc)
                txt2 = M.Text(
                    "- " + SSCTV.old_tv1_variants[SSCTV.old_tv_variant][YRB],
                    font_size = 20.0, color = mc).next_to(
                        number_plane.c2p(
                            SSCTV.old_tv1_YRBUVCMP[YRB][3],
                            - SSCTV.old_tv1_YRBUVCMP[YRB][4], 0.0), M.UR, 0.15)
                scene.add(d, txt, d2, txt2)
            else:
                d = M.Dot(number_plane.c2p(
                    SSCTV.old_tv1_YRBUVCMP[YRB][3],
                    SSCTV.old_tv1_YRBUVCMP[YRB][4], 0.0),
                          0.1, stroke_width = 3, color = colr, stroke_color = mc)
                txt = M.Text(
                    SSCTV.old_tv1_variants[SSCTV.old_tv_variant][YRB],
                    font_size = 20.0, color = mc).next_to(
                        number_plane.c2p(
                            SSCTV.old_tv1_YRBUVCMP[YRB][3],
                            SSCTV.old_tv1_YRBUVCMP[YRB][4], 0.0), M.UR, 0.15)
                scene.add(d, txt)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv1_table_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        table_data = [["В", "В", "В", "В", "В", "В", "рад", "град"],]
        for i in range(5):
            col6 = "-"
            col7 = "-"
            if SSCTV.old_tv1_YRBUVCMP[i][6] != 0.0:
                col6 = str(SSCTV.old_tv1_YRBUVCMP[i][6])
                col7 = str(SSCTV.old_tv1_YRBUVCMP[i][7])
            table_data.append([str(SSCTV.old_tv1_YRBUVCMP[i][0]),
                               str(SSCTV.old_tv1_YRBUVCMP[i][1]),
                               str(SSCTV.old_tv1_YRBUVCMP[i][2]),
                               str(SSCTV.old_tv1_YRBUVCMP[i][3]),
                               str(SSCTV.old_tv1_YRBUVCMP[i][4]),
                               str(SSCTV.old_tv1_YRBUVCMP[i][5]),
                               col6, col7])
        fs = 22.0
        ls = 30.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            row_labels = [M.Text(""), *[
                M.Text(SSCTV.old_tv1_variants[
                    SSCTV.old_tv_variant][j],
                    color = mc, font_size = fs) for j in range(5)]],
            col_labels = [
                M.MathTex(r"E_Y^{'}", font_size = ls, color = mc),
                M.MathTex(r"E_{R-Y}^{'}", font_size = ls, color = mc),
                M.MathTex(r"E_{B-Y}^{'}", font_size = ls, color = mc),
                M.MathTex(r"U", font_size = ls, color = mc),
                M.MathTex(r"V", font_size = ls, color = mc),
                M.MathTex(r"U_{CM}", font_size = ls, color = mc),
                M.MathTex(r"{\varphi}_C", font_size = ls, color = mc),
                M.MathTex(r"{\varphi}_C", font_size = ls, color = mc)],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 0.4,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv1_table_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        table_data = [["В", "В", "В", "В", "В", "МГц", "МГц", "дБ", "дБ"],]
        for i in range(5):
            table_data.append([str(SSCTV.old_tv1_YRBDFKRB[i][0]),
                               str(SSCTV.old_tv1_YRBDFKRB[i][1]),
                               str(SSCTV.old_tv1_YRBDFKRB[i][2]),
                               str(SSCTV.old_tv1_YRBDFKRB[i][3]),
                               str(SSCTV.old_tv1_YRBDFKRB[i][4]),
                               str(SSCTV.old_tv1_YRBDFKRB[i][5]),
                               str(SSCTV.old_tv1_YRBDFKRB[i][6]),
                               str(SSCTV.old_tv1_YRBDFKRB[i][7]),
                               str(SSCTV.old_tv1_YRBDFKRB[i][8])])
        fs = 22.0
        ls = 30.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            row_labels = [M.Text(""), *[
                M.Text(SSCTV.old_tv1_variants[
                    SSCTV.old_tv_variant][j],
                    color = mc, font_size = fs) for j in range(5)]],
            col_labels = [
                M.MathTex(r"E_Y^{'}", font_size = ls, color = mc),
                M.MathTex(r"E_{R-Y}^{'}", font_size = ls, color = mc),
                M.MathTex(r"E_{B-Y}^{'}", font_size = ls, color = mc),
                M.MathTex(r"D_R", font_size = ls, color = mc),
                M.MathTex(r"D_B", font_size = ls, color = mc),
                M.MathTex(r"f_R", font_size = ls, color = mc),
                M.MathTex(r"f_B", font_size = ls, color = mc),
                M.MathTex(r"K_R", font_size = ls, color = mc),
                M.MathTex(r"K_B", font_size = ls, color = mc)],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 0.4,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv2_func_by_2_bits(
        current_bit: str, current_level: str,
        fall: float = 30.0, amplitude: float = 1.0, zero_level: float = 0.0):
        def level_by_str(current_level: str):
            if current_level == "0":
                return lambda x: zero_level
            else:
                return lambda x: zero_level + amplitude

        def fall_by_str(current_level: str):
            if current_level == "0":
                return lambda x: SSf.SIPK_SSCTV_functions.sigmoid(
                    x * fall) * amplitude + zero_level
            else:
                return lambda x: SSf.SIPK_SSCTV_functions.sigmoid(
                    x * - fall) * amplitude + zero_level

        if current_bit == "0":
            func = level_by_str(current_level)
            return lambda x: SSf.SIPK_SSCTV_functions.restrict_func_value(
                func(x), x, - 0.5, 0.5)
        else:
            func = fall_by_str(current_level)
            return lambda x: SSf.SIPK_SSCTV_functions.restrict_func_value(
                func(x), x, - 0.5, 0.5)

    @staticmethod
    def make_old_tv2(scene: M.Scene):
        SSCTV.old_tv2_formula_1(scene)
        SSCTV.old_tv2_formula_2(scene)
        SSCTV.old_tv2_table_1(scene)
        SSCTV.old_tv2_diagram_1(scene)
        SSCTV.old_tv2_diagram_2(scene)
        SSCTV.old_tv2_table_2(scene)
        SSCTV.old_tv2_table_3(scene)
        SSCTV.old_tv2_formula_3(scene)
        SSCTV.old_tv2_table_4(scene)
        SSCTV.old_tv2_formula_4(scene)

    @staticmethod
    def old_tv2_formula_1(scene: M.Scene):
        SSCTV.old_tv1_formula_1(scene)

    @staticmethod
    def old_tv2_formula_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSCTV.old_tv1_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        i = 0
        for text_color in SSCTV.old_tv1_variants[SSCTV.old_tv_variant]:
            r, g, b, color = SSCTV.old_tv1_colors[text_color]
            EY = round(0.299 * r + 0.587 * g + 0.114 * b, 3)
            ER = round(r - EY, 3)
            EB = round(b - EY, 3)
            ECR = round(ER * 0.713, 3)
            ECB = round(EB * 0.564, 3)
            Y = round((EY * 219.0 + 16.0) * 4.0)
            CR = round((ECR * 224.0 + 128.0) * 4.0)
            CB = round((ECB * 224.0 + 128.0) * 4.0)
            txt = M.Text(text_color + ": ", font_size = tts, color = mc).next_to(
                M.UP * 3.5 + M.LEFT * 7.0 + i * M.DOWN * 1.5)
            tx = r"E_{CR}^{'} = " + str(ECR)
            tx += r";\ E_{CB}^{'} = " + str(ECB) + r";\ "
            tx += r"Y = Round((219 \cdot " + str(EY) + r" + 16) \cdot 2^{10-8}) = "
            tx += str(Y) + r";"
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(txt)
            tx2 = r"CR = Round((224 \cdot " + str(ECR)
            tx2 += r" + 128) \cdot 2^{10-8}) = "
            tx2 += str(CR) + r";\ \ "
            tx2 += r"CB = Round((224 \cdot " + str(ECB)
            tx2 += r" + 128) \cdot 2^{10-8}) = "
            tx2 += str(CB) + r";"
            tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(
                M.UP * 2.8 + M.LEFT * 7.0 + i * M.DOWN * 1.5)
            scene.add(txt, tex, tex2)
            i += 1
            SSCTV.old_tv2_YRB_DEC_BIN_HEX.append(
                [str(EY), str(ER), str(EB), str(Y), str(CR), str(CB),
                 SSf.SIPK_SSCTV_functions.fill_zeros(bin(Y)[2:], 10),
                 SSf.SIPK_SSCTV_functions.fill_zeros(bin(CR)[2:], 10),
                 SSf.SIPK_SSCTV_functions.fill_zeros(bin(CB)[2:], 10),
                 SSf.SIPK_SSCTV_functions.fill_zeros(hex(Y)[2:], 3),
                 SSf.SIPK_SSCTV_functions.fill_zeros(hex(CR)[2:], 3),
                 SSf.SIPK_SSCTV_functions.fill_zeros(hex(CB)[2:], 3)])
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv2_table_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        table_data = [["В", "В", "В", "DEC", "DEC", "DEC",
                       "BIN", "BIN", "BIN", "HEX", "HEX", "HEX"],]
        for i in range(5):
            table_data.append(SSCTV.old_tv2_YRB_DEC_BIN_HEX[i])
        fs = 18.0
        ls = 28.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            row_labels = [M.Text(""), *[
                M.Text(SSCTV.old_tv1_variants[
                    SSCTV.old_tv_variant][j],
                    color = mc, font_size = fs) for j in range(5)]],
            col_labels = [
                M.MathTex(r"E_Y^{'}", font_size = ls, color = mc),
                M.MathTex(r"E_{R-Y}^{'}", font_size = ls, color = mc),
                M.MathTex(r"E_{B-Y}^{'}", font_size = ls, color = mc),
                M.MathTex(r"Y", font_size = ls, color = mc),
                M.MathTex(r"CR", font_size = ls, color = mc),
                M.MathTex(r"CB", font_size = ls, color = mc),
                M.MathTex(r"Y", font_size = ls, color = mc),
                M.MathTex(r"CR", font_size = ls, color = mc),
                M.MathTex(r"CB", font_size = ls, color = mc),
                M.MathTex(r"Y", font_size = ls, color = mc),
                M.MathTex(r"CR", font_size = ls, color = mc),
                M.MathTex(r"CB", font_size = ls, color = mc)],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 0.2,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv2_diagram_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        bit = SSCTV.old_tv2_YRB_DEC_BIN_HEX[0][8][::-1]
        bit += SSCTV.old_tv2_YRB_DEC_BIN_HEX[0][6][::-1]
        bit += SSCTV.old_tv2_YRB_DEC_BIN_HEX[0][7][::-1]
        bit += SSCTV.old_tv2_YRB_DEC_BIN_HEX[0][6][::-1]
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (-1, 40, 1),
            y_range = (0.0, 1.05, 1.0),
            x_length = 13.0,
            y_length = 1.0,
            color = mc,
            axis_config = {
                "stroke_width": 3,
                "include_ticks": False,
                "include_tip": False,
                "color": mc},
            y_axis_config = {
                "stroke_width": 0,
                "stroke_opacity": 0.0},
            background_line_style = {
                "stroke_color": mc,
                "stroke_width": 1,
                "stroke_opacity": 0.25},
            tips = False,
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side + M.DOWN, M.DOWN)
        number_plane.get_axes().set_color(mc)
        graphs = M.VGroup()
        bit_labels = ["CB", "Y", "CR", "Y"]
        for i in range(len(bit_labels)):
            graphs += M.MathTex(
                bit_labels[i], font_size = tts, color = mc
                ).next_to(number_plane.c2p(5.0 + i * 10.0, 1.1, 0.0), M.UP, 0.05)
        for i in range(3):
            graphs += M.Line(number_plane.c2p(9.5 + i * 10.0, 1.5, 0.0),
                             number_plane.c2p(9.5 + i * 10.0, - 0.6, 0.0),
                             color = mc, stroke_width = 1.0)
        for i in range(len(bit)):
            graphs += M.MathTex(bit[i], font_size = tts, color = mc).next_to(
                number_plane.c2p(i, 0.0, 0.0), M.DOWN)
        current_level = "0"
        for i in range(len(bit)):
            graphs += number_plane.plot(
                lambda x: SSCTV.old_tv2_func_by_2_bits(
                    bit[i], current_level)(x - i),
                x_range = (i - 0.5, i + 0.5, 0.0199),
                color = mc,
                use_smoothing = False)
            current_level = SSf.SIPK_SSCTV_functions.sum_mod_2(
                current_level, bit[i])
        scene.add(number_plane, graphs)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv2_diagram_2(scene: M.Scene):
        bit1 = SSCTV.old_tv2_YRB_DEC_BIN_HEX[0][8][::-1]
        bit2 = SSCTV.old_tv2_YRB_DEC_BIN_HEX[0][6][::-1]
        bit3 = SSCTV.old_tv2_YRB_DEC_BIN_HEX[0][7][::-1]
        bits = [bit1, bit2, bit3, bit2]
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        for k in range(2):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            number_plane = M.NumberPlane(
                x_range = (0.0, 4.0, 1.0),
                y_range = (-1.0, 13.0, 3.0),
                x_length = 8.0,
                y_length = 7.2,
                color = mc,
                axis_config = {
                    "stroke_width": 0,
                    "include_ticks": False,
                    "include_tip": False,
                    "color": mc},
                background_line_style = {
                    "stroke_color": mc,
                    "stroke_width": 1,
                    "stroke_opacity": 1.0},
                tips = False)
            number_plane.get_axes().set_color(mc)
            graphs = M.VGroup()
            bit_labels = ["CB", "Y", "CR", "Y"]
            for i in range(len(bit_labels)):
                graphs += M.MathTex(
                    bit_labels[i], font_size = tts, color = mc
                    ).next_to(number_plane.c2p(0.5 + i, 13.0, 0.0), M.UP, 0.1)
            for i in range(5):
                graphs += M.MathTex(
                    "U_" + str(i + k * 5), font_size = tts, color = mc
                    ).next_to(number_plane.c2p(0.0, i * 3, 0.0), M.LEFT)
            for i in range(5):
                prev_bit = "0"
                next_bit = ""
                for j in range(len(bits)):
                    if j != 0: prev_bit = bits[j - 1][i + k * 5]
                    if j == len(bits) - 1: next_bit = bits[j][i + k * 5]
                    else: next_bit = bits[j + 1][i + k * 5]
                    graphs += number_plane.plot(
                        lambda x: SSCTV.tv3_func_by_3_bits(
                            prev_bit + bits[j][i + k * 5] + next_bit, 100.0)(x - j)
                            + 3.0 * i,
                        x_range = (j, j + 1.0, 0.0099),
                        color = mc,
                        use_smoothing = False)
            scene.add(number_plane, graphs)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv2_table_2(scene: M.Scene):
        def bit_8(num: int):
            if num < 313 and num >= 1: return "0"
            else: return "1"

        def bit_7(num: int):
            if (num <= 336 and num >= 311) or num <= 23 or num >= 624: return "1"
            else: return "0"

        SSf.SIPK_SSCTV_functions.make_background(scene)
        rows_variant = {1: 2, 2: 25, 3: 172, 4: 18, 5: 250, 6: 385, 7: 500, 8: 326,
                        9: 600, 10: 315, 11: 624, 12: 8, 13: 300, 14: 616, 15: 14}
        fvh = {"000": "0000000", "001": "0011101", "010": "0101011",
               "011": "0110110", "100": "1000111", "101": "1011010",
               "110": "1101100", "111": "1110001"}
        row = rows_variant[SSCTV.old_tv_variant]
        table_data = []
        nas = "1" + fvh[bit_8(row) + bit_7(row) + "0"] + "00"
        kas = "1" + fvh[bit_8(row) + bit_7(row) + "1"] + "00"
        table_data = [[nas, hex(int(nas, base = 2))[2:]],
                      [kas, hex(int(kas, base = 2))[2:]]]
        fs = SSf.SIPK_SSCTV_functions.table_font_size
        ls = 36.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            top_left_entry = M.Text("Строка № " + str(row),
                                    font_size = fs, color = mc),
            row_labels = [
                M.MathTex("HAC", font_size = ls, color = mc),
                M.MathTex("KAC", font_size = ls, color = mc)],
            col_labels = [
                M.MathTex("BIN", font_size = ls, color = mc),
                M.MathTex("HEX", font_size = ls, color = mc)],
            include_outer_lines = True,
            v_buff = 0.8,
            h_buff = 0.8,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv2_table_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        f = 25
        if SSCTV.old_tv_variant >= 10: f = 50
        kvt = 10
        if SSCTV.old_tv_variant in [10, 11, 12]: kvt = 12
        recomend_str = {1: "601", 2: "709", 3: "2020 4K"}
        recomend = 3
        if SSCTV.old_tv_variant in [1, 3, 5]: recomend = 1
        elif SSCTV.old_tv_variant in [2, 4, 6, 13, 14, 15]: recomend = 2
        format_descr_str = {1: "4:4:4", 2: "4:2:2", 3: "4:2:0"}
        format_descr = 1
        if SSCTV.old_tv_variant in [2, 3, 8, 11, 13]: format_descr = 2
        elif SSCTV.old_tv_variant in [4, 5, 9, 12, 14]: format_descr = 3
        SSCTV.old_tv2_rec_for_f_kvt = [recomend, format_descr, f, kvt]
        table_data = [
            ["Рекоменд.", "Формат\nдискр.",
             "Частота\nкадров, Гц", "Разрядов\nквантов."],
            [recomend_str[recomend], format_descr_str[format_descr],
             str(f), str(kvt)]]
        fs = 30.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            row_labels = [
                M.Text("Вар.", font_size = fs, color = mc),
                M.Text(str(SSCTV.old_tv_variant), font_size = fs, color = mc)],
            include_outer_lines = True,
            v_buff = 0.6,
            h_buff = 0.3,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv2_formula_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        recomend, format_descr, f, kvt = SSCTV.old_tv2_rec_for_f_kvt
        format_descr_int = {1: 1, 2: 0.5, 3: 0.25}
        N_p_int = {1: [720, 576], 2: [1920, 1080], 3: [3840, 2160]}
        N_p = N_p_int[recomend]
        V_Y = round(N_p[0] * N_p[1] * kvt / 1000000.0, 2)
        V_1 = round(V_Y * (1 + 2 * format_descr_int[format_descr]), 2)
        V = round(V_1 * f / 1000.0, 2)
        tx = r"V_Y = N_p \cdot b = " + str(N_p[0]) + r" \cdot "
        tx += str(N_p[1]) + r" \cdot " + str(kvt) + r" = "
        tx += str(V_Y)
        txt = M.Text("Мбит", font_size = tts, color = mc)
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"V_1 = V_Y + V_{CB} + V_{CR} = V_Y \cdot (1 + "
        tx2 += str(format_descr_int[format_descr]) + " + "
        tx2 += str(format_descr_int[format_descr]) + ") = "
        tx2 += str(V_1)
        txt2 = M.Text("Мбит", font_size = tts, color = mc)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"V = V_1 \cdot f = " + str(V_1) + r" \cdot " + str(f)
        tx3 += r" = " + str(V)
        txt3 = M.Text("Гбит/с", font_size = tts, color = mc)
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        tex.shift(M.LEFT * txt.width * 0.5)
        tex2.shift(M.LEFT * txt2.width * 0.5)
        tex3.shift(M.LEFT * txt3.width * 0.5)
        txt.next_to(tex)
        txt2.next_to(tex2)
        txt3.next_to(tex3)
        scene.add(tex, txt, tex2, txt2, tex3, txt3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv2_table_4(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        table_data = [
            [str(i + 1) for i in range(5)],
            [SSCTV.old_tv1_variants[SSCTV.old_tv_variant][i] for i in range(5)]]
        fs = 30.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            row_labels = [
                M.Text("Вар.", font_size = fs, color = mc),
                M.Text(str(SSCTV.old_tv_variant), font_size = fs, color = mc)],
            include_outer_lines = True,
            v_buff = 0.6,
            h_buff = 0.3,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv2_formula_4(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"Y = Round((219 \cdot E_Y^{'} + 16) \cdot 2^{b-8})"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"CR = Round((224 \cdot E_{CR}^{'} + 128) \cdot 2^{b-8})"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"CB = Round((224 \cdot E_{CB}^{'} + 128) \cdot 2^{b-8})"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        tx4 = r"E_{CR}^{'} = 0.713 \cdot E_{R-Y}^{'},\ "
        tx4 += r"E_{CB}^{'} = 0.564 \cdot E_{B-Y}^{'}"
        tex4 = M.MathTex(tx4, font_size = txs, color = mc).next_to(tex3, M.DOWN)
        scene.add(tex, tex2, tex3, tex4)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_old_tv3(scene: M.Scene):
        SSCTV.old_tv3_picture(scene)
        SSCTV.old_tv3_table_1(
            scene, SSCTV.old_tv3_variants[SSCTV.old_tv_variant][0])
        SSCTV.old_tv3_number_row(scene)
        SSCTV.old_tv3_formula_1(scene)
        SSCTV.old_tv3_table_1(
            scene, SSCTV.old_tv3_variants[SSCTV.old_tv_variant][1])
        SSCTV.old_tv3_number_row(scene)
        SSCTV.old_tv3_formula_1(scene)
        SSCTV.old_tv3_table_4(
            scene, SSCTV.old_tv3_variants[SSCTV.old_tv_variant][1])
        SSCTV.old_tv3_table_2(scene)
        SSCTV.old_tv3_table_3(scene)
        SSCTV.old_tv3_formula_2(scene)
        SSCTV.old_tv3_formula_3(scene)

    @staticmethod
    def old_tv3_picture(scene: M.Scene):
        picture_Y_int = [[59, 59, 59, 60, 60, 65, 64, 64],
                         [63, 62, 62, 62, 61, 61, 61, 62],
                         [137, 123, 111, 101, 96, 89, 88, 86],
                         [237, 236, 235, 233, 231, 216, 213, 208],
                         [225, 229, 232, 232, 231, 237, 238, 239],
                         [193, 195, 197, 198, 199, 204, 204, 205],
                         [182, 182, 181, 181, 181, 180, 180, 180],
                         [183, 182, 181, 180, 179, 178, 178, 177]]
        SSf.SIPK_SSCTV_functions.make_background(scene)
        graphs = M.VGroup()
        x_len = len(picture_Y_int[0])
        y_len = len(picture_Y_int)
        number_plane = M.NumberPlane(
            x_range = (0, x_len, 1),
            y_range = (0, y_len, 1),
            x_length = 13.0,
            y_length = 7.2,
            axis_config = {
                "stroke_width": 0,
                "include_ticks": False,
                "include_tip": False},
            background_line_style = {"stroke_width": 0},
            tips = False)
        for i in range(y_len):
            for j in range(x_len):
                colr = SSf.SIPK_SSCTV_functions.fill_zeros(
                    hex(picture_Y_int[i][j])[2:], 2)
                colr *= 3
                colr = "#" + colr
                graphs += M.Polygon(
                    number_plane.c2p(j, y_len - i - 1, 0),
                    number_plane.c2p(j, y_len - i, 0),
                    number_plane.c2p(j + 1, y_len - i, 0),
                    number_plane.c2p(j + 1, y_len - i - 1, 0),
                    color = colr,
                    fill_color = colr,
                    fill_opacity = 1.0)
        scene.add(graphs)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv3_table_1(scene: M.Scene, f: int):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        kff = 16
        table_data = []
        SSCTV.old_tv3_Fq_values = []
        for i in range(len(SSCTV.old_tv3_F_m_n)):
            table_data.append([])
            SSCTV.old_tv3_Fq_values.append([])
            for j in range(len(SSCTV.old_tv3_F_m_n[0])):
                value = round(
                    kff * SSCTV.old_tv3_F_m_n[i][j] / f / SSCTV.old_tv3_Q_m_n[i][j])
                table_data[-1].append(str(value))
                SSCTV.old_tv3_Fq_values[-1].append(value)
        SSCTV.old_tv3_Fq_values_str = table_data
        fs = 30.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.8,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv3_table_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        table_data = [["f1", "f2"],
                      [str(SSCTV.old_tv3_variants[SSCTV.old_tv_variant][0]),
                       str(SSCTV.old_tv3_variants[SSCTV.old_tv_variant][1])]]
        fs = 30.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            row_labels = [
                M.Text("Вариант", font_size = fs, color = mc),
                M.Text(str(SSCTV.old_tv_variant), font_size = fs, color = mc)],
            include_outer_lines = True,
            v_buff = 0.5,
            h_buff = 3.0,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv3_number_row(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        len_x = len(SSCTV.old_tv3_Fq_values_str[0])
        len_y = len(SSCTV.old_tv3_Fq_values_str)
        full_len = len_y * len_x
        i = 0
        gp = []
        gp_RLC = []
        current_row = 0
        current_col = 0
        direction = 0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        zeros = 0
        while i < full_len:
            gp.append(M.Text(
                SSCTV.old_tv3_Fq_values_str[current_row][current_col], color = mc))
            if SSCTV.old_tv3_Fq_values_str[current_row][current_col] != "0":
                if i != 0: gp_RLC.append(M.Text(
                    str(zeros), font_size = 42.0, color = mc))
                gp_RLC.append(M.Text(
                    SSCTV.old_tv3_Fq_values_str[current_row][current_col], color = mc))
                zeros = 0
            else:
                zeros += 1
            if direction == 0:
                if current_col == len_x - 1:
                    direction = 1
                    current_row += 1
                elif current_row == 0:
                    direction = 1
                    current_col += 1
                else:
                    current_col += 1
                    current_row -= 1
            else:
                if current_row == len_y - 1:
                    direction = 0
                    current_col += 1
                elif current_col == 0:
                    direction = 0
                    current_row += 1
                else:
                    current_col -= 1
                    current_row += 1
            i += 1
        gp_RLC.append(M.Text("EOB", color = mc))
        SSCTV.old_tv3_N = len(gp_RLC)
        grp = M.VGroup(*gp).arrange(buff = 0.3)
        grp_RLC = M.VGroup(*gp_RLC).arrange(buff = 0.3).scale(14.0 / grp.width)
        grp.scale(13.5 / grp.width).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        grp_RLC.next_to(grp, M.DOWN)
        scene.add(grp, grp_RLC)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv3_formula_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"K \approx \frac {64}{N}"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"f_1 = " + str(SSCTV.old_tv3_variants[SSCTV.old_tv_variant][0])
        tx2 += r":\ K \approx \frac {64}{" + str(SSCTV.old_tv3_N) + r"} = "
        tx2 += str(round(64.0 / SSCTV.old_tv3_N, 3))
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"f_2 = " + str(SSCTV.old_tv3_variants[SSCTV.old_tv_variant][1])
        tx3 += r":\ K \approx \frac {64}{" + str(SSCTV.old_tv3_N) + r"} = "
        tx3 += str(round(64.0 / SSCTV.old_tv3_N, 3))
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv3_table_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        table_data = []
        for i in range(len(SSCTV.old_tv3_Q_m_n)):
            table_data.append([])
            for j in range(len(SSCTV.old_tv3_Q_m_n[0])):
                table_data[-1].append(str(SSCTV.old_tv3_Q_m_n[i][j]))
        fs = 30.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.8,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv3_table_4(scene: M.Scene, f: int):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        kff = 16
        table_data = []
        SSCTV.old_tv3_Fdq = []
        for i in range(len(SSCTV.old_tv3_Fq_values)):
            table_data.append([])
            SSCTV.old_tv3_Fdq.append([])
            for j in range(len(SSCTV.old_tv3_Fq_values[0])):
                value = round(
                    SSCTV.old_tv3_Fq_values[i][j]
                    * f * SSCTV.old_tv3_Q_m_n[i][j] / kff)
                table_data[-1].append(str(value))
                SSCTV.old_tv3_Fdq[-1].append(value)
        fs = 30.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.8,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(table)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv3_formula_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = 24.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        i = 0
        showed = 0
        prev = SSf.SIPK_SSCTV_functions.upper_side
        while i < 60 and showed < 6:
            if SSCTV.old_tv3_Fdq[i % 8][i // 8] != 0:
                tx = r"F(" + str(i % 8) + r", " + str(i // 8)
                tx += r") = " + str(SSCTV.old_tv3_F_m_n[i % 8][i // 8])
                tx += r",\ F_{dq}(" + str(i % 8) + r", " + str(i // 8)
                tx += r") = " + str(SSCTV.old_tv3_Fdq[i % 8][i // 8])
                tex = M.MathTex(tx, font_size = txs, color = mc
                                ).next_to(prev, M.DOWN, 0.5)
                more_less = " меньше"
                if (SSCTV.old_tv3_F_m_n[i % 8][i // 8]
                    - SSCTV.old_tv3_Fdq[i % 8][i // 8] < 0.0):
                    more_less = " больше"
                tx2 = "на " + str(round(abs(100.0 * (
                    1.0 - SSCTV.old_tv3_Fdq[i % 8][i // 8]
                    / SSCTV.old_tv3_F_m_n[i % 8][i // 8])), 1))
                tx2 += "%" + more_less
                txt = M.Text(tx2, font_size = 20.0, color = mc).next_to(tex, M.DOWN)
                scene.add(tex, txt)
                prev = txt
                showed += 1
            i += 1
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv3_formula_3(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tx = r"F_{dq}(m, n) = Round \left( \frac {F_q(m, n) \cdot f"
        tx += r" \cdot Q(m, n)}{16} \right)"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_old_tv5(scene: M.Scene):
        SSCTV.old_tv5_table_1_2_3(scene)

    @staticmethod
    def old_tv5_table_1_2_3(scene: M.Scene):
        data = {1: [9, 9, 2], 2: [8, 12, 3], 3: [6, 9, 2],
                4: [12, 8, 3], 5: [9, 6, 2], 6: [8, 8, 3],
                7: [6, 12, 2], 8: [12, 12, 3], 9: [12, 6, 2],
                10: [16, 4, 3], 11: [9, 12, 2], 12: [4, 16, 3],
                13: [12, 9, 2], 14: [8, 16, 3], 15: [6, 15, 2]}
        SSf.SIPK_SSCTV_functions.make_background(scene)
        dat = data[SSCTV.old_tv_variant]
        table_data = [[str(i + 1) for i in range(dat[0] + dat[1] + 1)], []]
        table_data3 = [[], []]
        IP_frames = 0
        for i in range(dat[0] + dat[1] + 1):
            frame = "B"
            if i == dat[0] or i == dat[0] + dat[1] or i == 0:
                frame = "I"
                IP_frames += 1
            elif i % (dat[2] + 1) == 0:
                frame = "P"
                IP_frames += 1
            table_data[1].append(frame)
            table_data3[0].append(frame + str(i + 1))
        for i in range(dat[0] + dat[1] + 1):
            if table_data3[0][i][0] == "I":
                table_data3[1].append("-")
            elif table_data3[0][i][0] == "P":
                table_data3[1].append(table_data3[0][
                    (i // (dat[2] + 1) - 1) * (dat[2] + 1)])
            else:
                table_data3[1].append(
                    table_data3[0][(i // (dat[2] + 1)) * (dat[2] + 1)]
                    + "\n"
                    + table_data3[0][(i // (dat[2] + 1) + 1) * (dat[2] + 1)])
        fs = 18.0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table = SSf.Table(
            table_data,
            include_outer_lines = True,
            v_buff = 0.33,
            h_buff = 0.33,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}
            ).next_to(SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        table_data2 = [[], []]
        table_data2[0].append(table_data[0][0])
        table_data2[1].append(table_data[1][0])
        for i in range(IP_frames - 1):
            table_data2[0].append(table_data[0][(i + 1) * (dat[2] + 1)])
            table_data2[1].append(table_data[1][(i + 1) * (dat[2] + 1)])
            for j in range(dat[2]):
                table_data2[0].append(table_data[0][i * (dat[2] + 1) + j + 1])
                table_data2[1].append(table_data[1][i * (dat[2] + 1) + j + 1])
        table2 = SSf.Table(
            table_data2,
            include_outer_lines = True,
            v_buff = 0.33,
            h_buff = 0.33,
            element_to_mobject_config = {"font_size": fs, "color": mc},
            line_config = {"color": mc}).next_to(table, M.DOWN, 1.0)
        table3 = SSf.Table(
            table_data3,
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.2,
            element_to_mobject_config = {"font_size": fs - 2.0, "color": mc},
            line_config = {"color": mc}).next_to(table2, M.DOWN, 1.0)
        scene.add(table, table2, table3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        
