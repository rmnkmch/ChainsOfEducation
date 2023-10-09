import manim as M
import SIPK_SSCTV_functions as SSf


class SSCTV(object):
    """SSCTV"""

    variant = 7

    tv1_in_0_1_str = ""

    tv2_F_s = 30.0#22.5
    tv2_R2 = 2.0 / 3.0
    tv2_R2_str = r"\frac {2}{3}"
    tv2_V_p = 16.03
    tv2_b_s = 5
    tv2_data1 = [9.0, 7.0, 5.0, 3.0, 1.0]
    tv2_data2 = [10.0, 8.0, 6.0, 4.0, 2.0]
    tv2_data3 = [16.2, 13.2, 10.2, 7.2, 4.2]
    tv2_data11 = [17.375, 15.625, 13.475, 11.475, 9.55]
    tv2_data22 = [21.7, 19.8, 17.725, 15.775, 13.575]
    tv2_data33 = [29.675, 26.875, 23.7, 20.875, 17.675]
    tv2_data111 = [0.0001, 0.0046875, 0.0175, 0.05, 0.09]
    tv2_data222 = [0.0028125, 0.011015, 0.0327725, 0.0625375, 0.0981775]
    tv2_data333 = [0.00028645, 0.00479175, 0.0263725, 0.0609525, 0.0968975]
    tv2_pool_4fm_mer = {12: [17.0, 18.2], 10: [15.1, 16.3],
                        8: [13.0, 13.9], 6: [11.0, 12.2], 4: [8.9, 9.9]}
    tv2_pool_16kam_mer = {16: [21.5, 22.0], 14: [19.5, 20.1],
                          12: [17.4, 18.0], 10: [15.4, 16.0], 8: [13.4, 13.9]}
    tv2_pool_64kam_mer = {24: [29.5, 29.8], 21: [26.8, 27.0],
                          18: [23.5, 23.8], 15: [20.8, 21.0], 12: [17.5, 17.8]}
    tv2_pool_4fm_ber = {12: [0.0, 0.00125, 0.0025],
                        10: [0.0, 0.00125, 0.0025, 0.00375, 0.005,
                             0.00625, 0.0075, 0.00875, 0.01],
                        8: [0.01, 0.01125, 0.0125, 0.01375, 0.015,
                            0.01625, 0.0175, 0.01875, 0.02, 0.02125,
                            0.0225, 0.02375, 0.02625],
                        6: [0.02875, 0.03125, 0.035, 0.03625, 0.375,
                            0.03875, 0.04, 0.04125, 0.0425, 0.04375, 0.045,
                            0.04625, 0.0475, 0.04875, 0.5, 0.05125, 0.05375,
                            0.055, 0.0575, 0.05875, 0.06125, 0.06875],
                        4: []
                        }

    @staticmethod
    def make_tv(scene: M.Scene):
        # SSCTV.make_tv1(scene)
        SSCTV.make_tv2(scene)
        # SSCTV.make_tv3(scene)

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
        SSCTV.tv2_graphs_1(scene)
        SSCTV.tv2_graphs_2(scene)
        # SSCTV.tv2_graph_3(scene)
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
        tx3 += r"}{" + str(SSCTV.tv2_b_s) + r"} = " + str(V_f / SSCTV.tv2_b_s)
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
            y_range = (8, 31, 1),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "include_numbers": True,
                "font_size": 24.0,
                "stroke_width": 4,
                "include_ticks": False,
                "include_tip": True,
                "line_to_number_buff": 0.12,
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
            vertex_dot_style = dict(stroke_width = 2, fill_color = "#f30c2c",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph2 = number_plane.plot_line_graph(
            x_values = SSCTV.tv2_data2,
            y_values = SSCTV.tv2_data22,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 2, fill_color = "#0c2cf3",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph3 = number_plane.plot_line_graph(
            x_values = SSCTV.tv2_data3,
            y_values = SSCTV.tv2_data33,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 2, fill_color = "#2cf30c",
                                    stroke_color = mc),
            stroke_width = 4)
        scene.add(number_plane, line_graph1, line_graph2, line_graph3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv2_graphs_2(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        number_plane = M.NumberPlane(
            x_range = (0, 17, 1),
            y_range = (-5, 0, 1),
            x_length = 13.0,
            y_length = 7.0,
            color = mc,
            axis_config = {
                "include_numbers": True,
                "font_size": 24.0,
                "stroke_width": 4,
                "include_ticks": False,
                "include_tip": True,
                "line_to_number_buff": 0.12,
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
            vertex_dot_style = dict(stroke_width = 2, fill_color = "#f30c2c",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph2 = number_plane.plot_line_graph(
            x_values = SSCTV.tv2_data2,
            y_values = SSCTV.tv2_data222,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 2, fill_color = "#0c2cf3",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph3 = number_plane.plot_line_graph(
            x_values = SSCTV.tv2_data3,
            y_values = SSCTV.tv2_data333,
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 2, fill_color = "#2cf30c",
                                    stroke_color = mc),
            stroke_width = 4)
        scene.add(number_plane, line_graph1, line_graph2, line_graph3)
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
            vertex_dot_style = dict(stroke_width = 2, fill_color = "#f30c2c",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph2 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [2, 2],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 2, fill_color = "#0c2cf3",
                                    stroke_color = mc),
            stroke_width = 4)
        line_graph3 = number_plane.plot_line_graph(
            x_values = [1, 2],
            y_values = [3, 3],
            line_color = mc,
            vertex_dot_style = dict(stroke_width = 2, fill_color = "#2cf30c",
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
    def tv3_func_part_by_2_bits(bits: str, part: int):
        fall = 22.0
        amp = 2.0
        if bits[0] == "0" and bits[1] == "0":
            return lambda x: - 1.0
        elif bits[0] == "1" and bits[1] == "1":
            return lambda x: 1.0
        elif bits[0] == "0" and bits[1] == "1":
            if part == 1: return lambda x: SSf.SIPK_SSCTV_functions.sigmoid(
                x * fall) * amp - 1.0
            else: return lambda x: SSf.SIPK_SSCTV_functions.sigmoid(
                (1.0 - x) * fall) * - amp + 1.0
        elif bits[0] == "1" and bits[1] == "0":
            if part == 1: return lambda x: SSf.SIPK_SSCTV_functions.sigmoid(
                x * fall) * - amp + 1.0
            else: return lambda x: SSf.SIPK_SSCTV_functions.sigmoid(
                (1.0 - x) * fall) * amp - 1.0

    @staticmethod
    def tv3_func_by_3_bits(bits: str):
        part_1 = SSCTV.tv3_func_part_by_2_bits(bits[:2], 1)
        part_2 = SSCTV.tv3_func_part_by_2_bits(bits[1:], 2)
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
        
