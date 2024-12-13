import manim as M
import SIPK_SSCTV_functions as SSf


class SSCTV(object):
    """SSCTV"""

    variant = 10

    tv1_in_0_1_str = ""

    tv2_F_s = 30.0
    tv2_R2 = 7.0 / 8.0
    tv2_R2_str = r"\frac {7}{8}"
    tv2_V_p = 56.1
    tv2_b_s = 7
    tv2_data1 = [9.0, 7.0, 5.0, 3.0, 1.0]
    tv2_data2 = [10.0, 8.0, 6.0, 4.0, 2.0]
    tv2_data3 = [16.2, 13.2, 10.2, 7.2, 4.2]
    tv2_data11 = [17.45, 15.6, 13.45, 11.525, 9.4]
    tv2_data22 = [21.725, 19.825, 17.65, 15.8, 13.65]
    tv2_data33 = [29.7, 26.875, 23.7, 20.925, 17.65]
    tv2_data111 = [0.0003125, 0.003125, 0.0171875, 0.0475, 0.0915625]
    tv2_data222 = [0.00273425, 0.01117, 0.033945, 0.061485, 0.09908]
    tv2_data333 = [0.000208325, 0.00459, 0.0268225, 0.0596025, 0.0968625]

    tv2_data_4fm_12dbm_mer = [
        16.8, 16.9,
        17.0, 17.1, 17.2, 17.3, 17.4, 17.5, 17.6, 17.7, 17.8, 17.9,
        18.0, 18.1, 18.2]
    tv2_data_4fm_10db_mer = [
        14.9,
        15.0, 15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.7, 15.8, 15.9,
        16.0, 16.1, 16.2]
    tv2_data_4fm_8db_mer = [
        12.8, 12.9,
        13.0, 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8, 13.9,
        14.0]
    tv2_data_4fm_6db_mer = [
        10.9,
        11.0, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9,
        12.0, 12.1]
    tv2_data_4fm_4db_mer = [
        8.8, 8.9,
        9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9]
    
    tv2_data_4fm_12dbm_ber = [0.0, 0.00125, 0.0025]
    tv2_data_4fm_10db_ber = [
        0.0, 0.00125, 0.0025, 0.00375, 0.005, 0.00625, 0.0075, 0.00875,
        0.01, 0.01125]
    tv2_data_4fm_8db_ber = [
        0.005, 0.0075, 0.00875,
        0.01, 0.01125, 0.0125, 0.01375, 0.015, 0.01625, 0.0175, 0.01875,
        0.02, 0.02125, 0.0225, 0.02375, 0.025, 0.02625, 0.0275, 0.02875]
    tv2_data_4fm_6db_ber = [
        0.0225, 0.02375, 0.025, 0.02625, 0.0275, 0.02875,
        0.03, 0.03125, 0.0325, 0.03375, 0.035, 0.03625, 0.0375, 0.03875,
        0.04, 0.04125, 0.0425, 0.04375, 0.045, 0.04625, 0.0475, 0.04875,
        0.05, 0.05125, 0.0525, 0.05375, 0.055, 0.05625, 0.0575, 0.05875,
        0.06, 0.06125, 0.0625, 0.06375, 0.065, 0.06625, 0.0675, 0.06875,
        0.07, 0.07125]
    tv2_data_4fm_4db_ber = [
        0.06, 0.06125, 0.0625, 0.06375, 0.065, 0.06625, 0.0675, 0.06875,
        0.07, 0.07125, 0.0725, 0.07375, 0.075, 0.07625, 0.0775, 0.07875,
        0.08, 0.08125, 0.0825, 0.08375, 0.085, 0.08625, 0.0875, 0.08875,
        0.09, 0.09125, 0.0925, 0.09375, 0.095, 0.09625, 0.0975, 0.09875,
        0.10, 0.1013, 0.1025, 0.1037, 0.105, 0.1063, 0.1075, 0.1088,
        0.11, 0.1112]


    tv5_C_N_Rice = 0.0
    tv5_f_c = 0
    tv5_chanel = 0
    tv5_P_n = 0.0
    tv5_P_smin = 0.0
    tv5_E_min = 0.0
    tv5_U_smin = 0.0

    tv6_used = []
    tv6_used_data = []
    tv6_floors = -1
    tv6_flats = -1
    tv6_usilit_db = 112.8
    tv6_lines = -1
    tv6_floors_by_line = -1
    tv6_data_razv_db = {1: 0.0, 2: 4.8, 3: 7.5}

    tv7_phi = 55 / 180.0 * 3.14159265
    tv7_lambda = 3.9 / 180.0 * 3.14159265
    tv7_f = 11727
    tv7_P_EIRP = 52.0

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

    old_tv_variant = 13
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
        SSCTV.make_tv2(scene)
        # SSCTV.make_tv3(scene)
        # SSCTV.make_tv4(scene)
        # SSCTV.make_tv5(scene)
        # SSCTV.make_tv6(scene)
        # SSCTV.make_new_tv6(scene)
        # SSCTV.make_tv7(scene)
        # SSCTV.make_old_tv1(scene)
        # SSCTV.make_old_tv2(scene)
        # SSCTV.make_old_tv3(scene)
        # SSCTV.make_old_tv5(scene)
        # SSCTV.make_old_tv6(scene)
        # SSCTV.tv_ekz_1(scene)
        # SSCTV.tv_ekz_2(scene)
        # SSCTV.tv_ekz_4(scene)
        # SSCTV.tv_ekz_5(scene)

    @staticmethod
    def tv_ekz_1(scene: M.Scene):
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data_00 = [[1, 3, 2, 1, 3, 1, 3, 2, 1, 2],
                         [5, 4, 5, 5, 4, 4, 4, 4, 4, 5],
                         [7, 8, 6, 6, 7, 8, 6, 8, 7, 8],
                         [9, 10, 10, 9, 10, 10, 10, 10, 10, 10]]
        td_vals_1_1 = {1: "4К", 2: "Рек.709", 3: "Рек.601"}
        td_vals_1_2 = {1: [3840, 2160], 2: [1920, 1080], 3: [720, 576]}
        td_vals_2 = {4: 25, 5: 50}
        td_vals_3_1 = {6: "4:4:4", 7: "4:2:2", 8: "4:2:0"}
        td_vals_3_2 = {6: 1, 7: 0.5, 8: 0.25}
        td_vals_4 = {9: 12, 10: 10}
        for i in range(10):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            DUp = M.DOWN * 2.5
            info = r"Вариант: " + str(i + 1) + r"; Стандарт: "
            info += td_vals_1_1[table_data_00[0][i]]
            info += r"; n: " + str(td_vals_2[table_data_00[1][i]]) + r";"
            info2 = r"дискретиз.: " + td_vals_3_1[table_data_00[2][i]] + r"; bs: "
            info2 += str(td_vals_4[table_data_00[3][i]])
            itext1 = M.Text(info, font_size = tts, color = mc).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
            itext2 = M.Text(info2, font_size = tts, color = mc).next_to(itext1, M.DOWN)
            XY = td_vals_1_2[table_data_00[0][i]]
            razr_kvantov = td_vals_4[table_data_00[3][i]]
            f = td_vals_2[table_data_00[1][i]]
            V_Y = round(XY[0] * XY[1] * razr_kvantov / 1000000.0, 2)
            V_1 = round(V_Y * (1.0 + 2.0 * td_vals_3_2[table_data_00[2][i]]), 2)
            V = round(V_1 * f, 2)
            text3 = r"Мбит/с"
            if V > 1000.0:
                V = round(V / 1000.0, 2)
                text3 = r"Гбит/с"
            tx = r"V_Y = N_p \cdot b = " + str(XY[0]) + r" \cdot "
            tx += str(XY[1]) + r" \cdot " + str(razr_kvantov) + r" = "
            tx += str(V_Y)
            tex = M.MathTex(tx, font_size = txs, color = mc)
            txt = M.Text("Мбит", font_size = tts, color = mc)
            gr1 = M.VGroup(tex, txt)
            gr1.arrange().next_to(SSf.SIPK_SSCTV_functions.upper_side + DUp, M.DOWN)
            tx2 = r"V_1 = V_Y + V_{CB} + V_{CR} = V_Y \cdot (1 + "
            tx2 += str(td_vals_3_2[table_data_00[2][i]]) + r" + "
            tx2 += str(td_vals_3_2[table_data_00[2][i]]) + r") = "
            tx2 += str(V_1)
            tex2 = M.MathTex(tx2, font_size = txs, color = mc)
            txt2 = M.Text("Мбит", font_size = tts, color = mc)
            gr2 = M.VGroup(tex2, txt2)
            gr2.arrange().next_to(gr1, M.DOWN)
            tx3 = r"V = V_1 \cdot f = " + str(V_1) + r" \cdot " + str(f)
            tx3 += r" = " + str(V)
            tex3 = M.MathTex(tx3, font_size = txs, color = mc)
            txt3 = M.Text(text3, font_size = tts, color = mc)
            gr3 = M.VGroup(tex3, txt3)
            gr3.arrange().next_to(gr2, M.DOWN)
            scene.add(itext1, itext2, gr1, gr2, gr3)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv_ekz_2(scene: M.Scene):
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data_00 = [[1, 2, 3, 1, 2, 3, 2, 1, 1, 3],
                         [4, 7, 5, 4, 8, 5, 6, 4, 4, 5],
                         [11, 9, 11, 10, 9, 10, 9, 10, 11, 11],
                         [12, 0, 13, 13, 0, 12, 0, 14, 15, 14]]
        td_vals_1 = {1: "DVB-S", 2: "DVB-C", 3: "DVB-S2"}
        td_vals_2 = {4: "4ФМ", 5: "8ФМ", 6: "32КАМ", 7: "64КАМ", 8: "128КАМ"}
        td_vals_3 = {9: 6.97, 10: 22.5, 11: 30.0}
        td_vals_4_1 = {12: 2.0 / 3.0, 13: 3.0 / 4.0, 14: 5.0 / 6.0, 15: 7.0 / 8.0}
        td_vals_4_2 = {12: r"\frac {2}{3}", 13: r"\frac {3}{4}",
                       14: r"\frac {5}{6}", 15: r"\frac {7}{8}"}
        td_vals_5 = {1: 0.92, 2: 0.92, 3: 0.99}
        data_bs = {4: 2, 5: 3, 6: 5, 7: 6, 8: 7}
        subdata_R = {12: r"2/3", 13: r"3/4", 14: r"5/6", 15: r"7/8", 0: r"-"}
        for i in range(10):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            DUp = M.DOWN * 2.5
            info = r"Вариант: " + str(i + 1) + r"; Стандарт: "
            info += td_vals_1[table_data_00[0][i]]
            info += r"; Модуляция: " + td_vals_2[table_data_00[1][i]] + r";"
            info2 = r"Fs: " + str(td_vals_3[table_data_00[2][i]]) + r"; Rвнутр: "
            info2 += subdata_R[table_data_00[3][i]] + r"; Rвнешн: "
            info2 += str(td_vals_5[table_data_00[0][i]])
            itext1 = M.Text(info, font_size = tts, color = mc).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
            itext2 = M.Text(info2, font_size = tts, color = mc).next_to(itext1, M.DOWN)
            b_s = data_bs[table_data_00[1][i]]
            F_s = td_vals_3[table_data_00[2][i]]
            tx = r"b_s = " + str(b_s)
            tex = M.MathTex(tx, font_size = txs, color = mc)
            txt = M.Text("бит/симв", font_size = tts, color = mc)
            tx12 = r";\ F_s = " + str(F_s)
            tex12 = M.MathTex(tx12, font_size = txs, color = mc)
            txt12 = M.Text("Мсимв/с", font_size = tts, color = mc)
            gr1 = M.VGroup(tex, txt, tex12, txt12)
            gr1.arrange().next_to(SSf.SIPK_SSCTV_functions.upper_side + DUp, M.DOWN)
            scene.add(itext1, itext2, gr1)
            V_f = F_s * b_s
            if table_data_00[3][i] != 0:
                R2 = td_vals_4_1[table_data_00[3][i]]
                R2_str = td_vals_4_2[table_data_00[3][i]]
                R1 = td_vals_5[table_data_00[0][i]]
                V_in2 = V_f * R2
                tx2 = r"V_f = F_s \cdot b_s = " + str(F_s) + r" \cdot "
                tx2 += str(b_s) + r" = " + str(V_f)
                tex2 = M.MathTex(tx2, font_size = txs, color = mc)
                txt2 = M.Text("Mбит/с", font_size = tts, color = mc)
                tex22 = M.MathTex(r" = V_{out2}", font_size = txs, color = mc)
                gr2 = M.VGroup(tex2, txt2, tex22)
                gr2.arrange().next_to(gr1, M.DOWN)
                tx3 = r"V_{in2} = R_2 \cdot V_{out2} = " + R2_str + r" \cdot "
                tx3 += str(V_f) + r" = " + str(V_in2)
                tex3 = M.MathTex(tx3, font_size = txs, color = mc)
                txt3 = M.Text("Mбит/с", font_size = tts, color = mc)
                tex4 = M.MathTex(r" = V_{out1}", font_size = txs, color = mc)
                gr3 = M.VGroup(tex3, txt3, tex4)
                gr3.arrange().next_to(gr2, M.DOWN)
                tx5 = r"V_{in1} = R_1 \cdot V_{out1} = " + str(R1) + r" \cdot "
                tx5 += str(V_in2) + r" = " + str(round(V_in2 * R1, 4))
                tex5 = M.MathTex(tx5, font_size = txs, color = mc)
                txt5 = M.Text("Mбит/с", font_size = tts, color = mc)
                tex6 = M.MathTex(r" = V_p", font_size = txs, color = mc)
                gr4 = M.VGroup(tex5, txt5, tex6)
                gr4.arrange().next_to(gr3, M.DOWN)
                scene.add(gr2, gr3, gr4)
            else:
                R1 = td_vals_5[table_data_00[0][i]]
                tx2 = r"V_f = F_s \cdot b_s = " + str(F_s) + r" \cdot "
                tx2 += str(b_s) + r" = " + str(V_f)
                tex2 = M.MathTex(tx2, font_size = txs, color = mc)
                txt2 = M.Text("Mбит/с", font_size = tts, color = mc)
                tex22 = M.MathTex(r" = V_{out}", font_size = txs, color = mc)
                gr2 = M.VGroup(tex2, txt2, tex22)
                gr2.arrange().next_to(gr1, M.DOWN)
                tx5 = r"V_{in} = R \cdot V_{out} = " + str(R1) + r" \cdot "
                tx5 += str(V_f) + r" = " + str(round(V_f * R1, 4))
                tex5 = M.MathTex(tx5, font_size = txs, color = mc)
                txt5 = M.Text("Mбит/с", font_size = tts, color = mc)
                tex6 = M.MathTex(r" = V_p", font_size = txs, color = mc)
                gr4 = M.VGroup(tex5, txt5, tex6)
                gr4.arrange().next_to(gr2, M.DOWN)
                scene.add(gr2, gr4)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv_ekz_4(scene: M.Scene):
        from math import log10
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data_00 = [[48, 49, 50, 51, 52, 53, 52, 51, 50, 49],
                         [40, 41, 42, 43, 44, 40, 41, 42, 43, 44],
                         [4, 5, 6, 4, 5, 6, 4, 5, 6, 5],
                         [38300, 38400, 38500, 38600, 39600,
                          39500, 39400, 39300, 39200, 39000],
                         [12100, 12000, 11900, 11800, 11700,
                          11600, 11500, 11400, 11300, 11200],
                         [190, 195, 200, 205, 197, 202, 198, 203, 199, 204],
                         [36, 36, 36, 36, 36, 27, 27, 27, 27, 27]]
        for i in range(10):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            DUp = M.DOWN * 2.5
            info = r"Вариант: " + str(i + 1) + r"; Pэиим: "
            info += str(table_data_00[0][i])
            info += r"; Gпр: " + str(table_data_00[1][i]) + r"; bпр: "
            info += str(table_data_00[2][i]) + r"; d: " + str(table_data_00[3][i])
            info2 = r"f: " + str(table_data_00[4][i]) + r"; Tш: "
            info2 += str(table_data_00[5][i]) + r"; df: " + str(table_data_00[6][i])
            itext1 = M.Text(info, font_size = tts, color = mc).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
            itext2 = M.Text(info2, font_size = tts, color = mc).next_to(itext1, M.DOWN)
            Peiim = table_data_00[0][i]
            Gpr = table_data_00[1][i]
            bpr = table_data_00[2][i]
            d = table_data_00[3][i]
            f = table_data_00[4][i]
            Tn = table_data_00[5][i]
            df = table_data_00[6][i]
            L_0 = round(20.0 * (log10(f) + log10(d)) + 32.45, 3)
            P_r = round(Peiim + Gpr - bpr - L_0, 3)
            N_n = round(1.38 * (10 ** -3) * Tn * df, 2)
            P_r_nolog = 10 ** (P_r / 10.0)
            SNR = round(P_r_nolog / N_n * (10 ** 14), 1)
            tx1 = r"L_0 = 20 \cdot \left(\lg " + str(f) + r" + \lg " + str(d)
            tx1 += r" \right) + 32.45 = " + str(L_0)
            tex1 = M.MathTex(tx1, font_size = txs, color = mc)
            txt1 = M.Text("дБ", font_size = tts, color = mc)
            gr1 = M.VGroup(tex1, txt1).arrange().next_to(
                SSf.SIPK_SSCTV_functions.upper_side + DUp, M.DOWN)
            tx2 = r"P_r = " + str(Peiim) + r" + " + str(Gpr) + r" - "
            tx2 += str(bpr) + r" - " + str(L_0) + r" = " + str(P_r)
            tex2 = M.MathTex(tx2, font_size = txs, color = mc)
            txt2 = M.Text("дБВт", font_size = tts, color = mc)
            gr2 = M.VGroup(tex2, txt2).arrange().next_to(gr1, M.DOWN)
            tx3 = r"N_n = 1.38 \cdot 10^{-23} \cdot " + str(Tn) + r" \cdot "
            tx3 += str(df) + r"000000 = " + str(N_n) + r" \cdot 10^{-14}"
            tex3 = M.MathTex(tx3, font_size = txs, color = mc)
            txt3 = M.Text("Вт", font_size = tts, color = mc)
            gr3 = M.VGroup(tex3, txt3).arrange().next_to(gr2, M.DOWN)
            tx4 = r"P_r = 10^{\frac {P_{r \ log}}{10}} = 10^{\frac {" + str(P_r)
            tx4 += r"}{10}} = " + SSf.SIPK_SSCTV_functions.float_to_exp10(P_r_nolog)
            tex4 = M.MathTex(tx4, font_size = txs, color = mc)
            txt4 = M.Text("Вт", font_size = tts, color = mc)
            gr4 = M.VGroup(tex4, txt4).arrange().next_to(gr3, M.DOWN)
            tx5 = r"\frac {S}{N} = \frac {" + SSf.SIPK_SSCTV_functions.float_to_exp10(P_r_nolog)
            tx5 += r"}{" + str(N_n) + r" \cdot 10^{-14}" + r"} = " + str(SNR) + r" = "
            tx5 += str(round(10.0 * log10(SNR), 2))
            tex5 = M.MathTex(tx5, font_size = txs, color = mc)
            txt5 = M.Text("дБ", font_size = tts, color = mc)
            gr5 = M.VGroup(tex5, txt5).arrange().next_to(gr4, M.DOWN)
            scene.add(itext1, itext2, gr1, gr2, gr3, gr4, gr5)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv_ekz_5(scene: M.Scene):
        from math import log10, pi
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        table_data_00 = [[40, 50, 42, 49, 46, 41, 45, 48, 44, 47],
                         [10, 10.5, 11, 11.5, 12, 10, 10.5, 11, 12, 10],
                         [498, 578, 658, 738, 818, 506, 586, 746, 826, 514],
                         [3, 4, 4, 5, 5, 3, 4, 6, 6, 3],
                         [2, 3, 4, 2, 3, 4, 2, 3, 4, 3]]
        for i in range(10):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            DUp = M.DOWN * 2.5
            info = r"Вариант: " + str(i + 1)
            info += r"; E: " + str(table_data_00[0][i])
            info += r"; GD: " + str(table_data_00[1][i])
            info2 = r"f: " + str(table_data_00[2][i])
            info2 += r"; Lf: " + str(table_data_00[3][i])
            info2 += r"; F: " + str(table_data_00[4][i])
            itext1 = M.Text(info, font_size = tts, color = mc).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
            itext2 = M.Text(info2, font_size = tts, color = mc).next_to(itext1, M.DOWN)
            E = table_data_00[0][i]
            GD = table_data_00[1][i]
            f = table_data_00[2][i]
            Lf = table_data_00[3][i]
            F = table_data_00[4][i]
            lambd = round(300.0 / f, 3)
            A_a = round(GD + 10.0 * log10(1.64 * lambd * lambd / 4.0 / pi), 3)
            P_s = round(E + A_a - Lf - 145.8, 3)
            P_n = round(F + 10.0 * log10(1.38 * 290.0 * 7.61 * (10 ** -17)), 3)
            SNR = round(P_s - P_n, 3)
            tx1 = r"P_n = " + str(F) + r" + 10 \cdot \lg \left( 1.38 \cdot 10^{-23} "
            tx1 += r"\cdot 290 \cdot 7.61 \cdot 10^6 \right) = " + str(P_n)
            tex1 = M.MathTex(tx1, font_size = txs, color = mc)
            txt1 = M.Text("дБВт", font_size = tts, color = mc)
            gr1 = M.VGroup(tex1, txt1).arrange().next_to(
                SSf.SIPK_SSCTV_functions.upper_side + DUp, M.DOWN)
            tx2 = r"\lambda = \frac {3 \cdot 10^8}{" + str(f) + r" \cdot 10^6} = "
            tx2 += str(lambd)
            tex2 = M.MathTex(tx2, font_size = txs, color = mc)
            txt2 = M.Text("м", font_size = tts, color = mc)
            gr2 = M.VGroup(tex2, txt2).arrange().next_to(gr1, M.DOWN)
            tx3 = r"A_a = " + str(GD) + r" + 10 \cdot \lg \left( \frac {1.64 \cdot ("
            tx3 += str(lambd) + r")^2}{4 \cdot 3.14} \right) = " + str(A_a)
            tex3 = M.MathTex(tx3, font_size = txs, color = mc)
            txt3 = M.Text("дБм2", font_size = tts, color = mc)
            gr3 = M.VGroup(tex3, txt3).arrange().next_to(gr2, M.DOWN)
            tx4 = r"P_s = " + str(E) + r" + (" + str(A_a) + r") - " + str(Lf)
            tx4 += r" - 145.8 = " + str(P_s)
            tex4 = M.MathTex(tx4, font_size = txs, color = mc)
            txt4 = M.Text("дБВт", font_size = tts, color = mc)
            gr4 = M.VGroup(tex4, txt4).arrange().next_to(gr3, M.DOWN)
            tx5 = r"\frac {S}{N} = " + str(P_s) + r" - (" + str(P_n)
            tx5 += r") = " + str(SNR)
            tex5 = M.MathTex(tx5, font_size = txs, color = mc)
            txt5 = M.Text("дБ", font_size = tts, color = mc)
            gr5 = M.VGroup(tex5, txt5).arrange().next_to(gr4, M.DOWN)
            scene.add(itext1, itext2, gr1, gr2, gr3, gr4, gr5)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

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
                     9: 11, 10: 8, 11: 13, 12: 0, 13: 10, 14: 12, 15: 4}
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
        data = r"""17.7
0
17.1
0
17.6
0
17.8
0.00125
15.6
0.00625
15.4
0.00375
15.4
0.0025
15.4
0.0025
13.5
0.01875
13.4
0.01875
13.6
0.0175
13.1
0.015
11.5
0.04625
11.9
0.04375
11.2
0.0575
11.4
0.04875
9.3
0.08625
9.3
0.0875
9.3
0.09625
9.5
0.09
21.8
0.002188
21.7
0.001563
21.7
0.002656
21.8
0.002031
19.8
0.01203
19.8
0.01234
19.7
0.01391
19.9
0.01031
17.6
0.03547
17.5
0.03891
17.7
0.03187
17.6
0.03453
15.8
0.06156
15.9
0.06125
15.7
0.06484
15.7
0.06609
13.6
0.09922
13.7
0.09656
13.6
0.1013
13.7
0.102
29.6
0.0004427
29.7
0.0002604
29.6
0.0002083
29.6
0.0002865
26.9
0.005208
26.8
0.005208
27.0
0.004323
27.0
0.004766
23.7
0.02612
23.7
0.02674
23.6
0.02766
23.6
0.02763
20.9
0.06099
20.9
0.06016
20.8
0.06104
20.9
0.06047
17.7
0.09599
17.7
0.0969
17.7
0.09766
17.6
0.09878"""
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
    def make_tv4(scene: M.Scene):
        SSCTV.tv4_formula_1(scene)

    @staticmethod
    def tv4_formula_1(scene: M.Scene):
        data_N_by_k = {1: 853, 2: 1705, 4: 3409, 8: 6817, 16: 13633, 32: 27265}
        data_T_C_by_k = {1: 112, 2: 224, 4: 448, 8: 896, 16: 1792, 32: 3584}
        data_b_C1_by_mod = {4: 2, 16: 4, 64: 6, 256: 8}
        data = {1: [4, 8, 8, 16, 8, 8, 16],
                2: [16, 8, 8, 16, 8, 8, 16],
                3: [64, 8, 8, 16, 8, 8, 16],
                4: [256, 8, 8, 16, 8, 8, 16],
                5: [4, 2, 16, 4, 16, 2, 32],
                6: [16, 2, 16, 4, 16, 2, 32],
                7: [64, 2, 16, 4, 16, 2, 32],
                8: [256, 2, 16, 4, 16, 2, 32],
                9: [4, 32, 32, 16, 32, 32, 16],
                10: [16, 32, 32, 16, 32, 32, 16],
                11: [64, 32, 32, 16, 32, 32, 16],
                12: [256, 32, 32, 16, 32, 32, 16],
                13: [16, 4, 8, 8, 8, 4, 16],
                14: [64, 4, 8, 8, 8, 4, 16],
                15: [256, 4, 8, 8, 8, 4, 16]}
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        variant_data = data[SSCTV.variant]
        for i in range(3):
            SSf.SIPK_SSCTV_functions.make_background(scene)
            T_C = data_T_C_by_k[variant_data[1 + i * 2]]
            dT = 1.0 / variant_data[2 + i * 2]
            dT_str = r"\frac {1}{" + str(variant_data[2 + i * 2]) + r"}"
            N = data_N_by_k[variant_data[1 + i * 2]]
            b_C1 = data_b_C1_by_mod[variant_data[0]]
            b_C = b_C1 * N
            T_C3 = int(T_C * (1.0 + dT))
            V = round(b_C / T_C3, 3)
            tx = r"T_{C3} = T_C \cdot \left(1 + \Delta T_3 \right) = " + str(T_C)
            tx += r" \cdot \left(1 + " + dT_str + r"\right) = " + str(T_C3)
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
                SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
            txt = M.Text("мкс", font_size = tts, color = mc)
            tx2 = r"b_C = b_{C1} \cdot N = " + str(b_C1) + r" \cdot "
            tx2 += str(N) + r" = " + str(b_C)
            tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
            txt2 = M.Text("бит", font_size = tts, color = mc)
            tx3 = r"V = \frac {b_C}{T_{C3}} = \frac {" + str(b_C) + r"}{"
            tx3 += str(T_C3) + r"} = " + str(V)
            tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
            txt3 = M.Text("Мбит/с", font_size = tts, color = mc)
            tex.shift(M.LEFT * 0.5 * txt.width)
            txt.next_to(tex)
            tex2.shift(M.LEFT * 0.5 * txt2.width)
            txt2.next_to(tex2)
            tex3.shift(M.LEFT * 0.5 * txt3.width)
            txt3.next_to(tex3)
            scene.add(tex, txt, tex2, txt2, tex3, txt3)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_tv5(scene: M.Scene):
        SSCTV.tv5_formula_1(scene)
        SSCTV.tv5_formula_2(scene)
        SSCTV.tv5_formula_3(scene)

    @staticmethod
    def tv5_formula_1(scene: M.Scene):
        from math import floor
        data_mod_by_var = {1: 256, 2: 256, 3: 256, 4: 256,
                           5: 64, 6: 64, 7: 64, 8: 64,
                           9: 16, 10: 16, 11: 16, 12: 16,
                           13: 4, 14: 4, 15: 4}
        data_R_num_by_var = {1: 5, 2: 4, 3: 3, 4: 2, 5: 6, 6: 1, 7: 5, 8: 4,
                             9: 3, 10: 2, 11: 6, 12: 1, 13: 3, 14: 2, 15: 6}
        data_R_float_by_R_num = {1: 1.0/2.0, 2: 2.0/3.0, 3: 3.0/4.0,
                                 4: 4.0/5.0, 5: 5.0/6.0, 6: 3.0/5.0}
        data_R_str_by_R_num = {1: r"\frac{1}{2}", 2: r"\frac{2}{3}",
                               3: r"\frac{3}{4}", 4: r"\frac{4}{5}",
                               5: r"\frac{5}{6}", 6: r"\frac{3}{5}"}
        data_PP_by_var = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
                          9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7}
        data_chanel_by_var = {1: 33, 2: 24, 3: 34, 4: 44, 5: 54, 6: 64,
                              7: 25, 8: 35, 9: 45, 10: 55, 11: 65,
                              12: 26, 13: 36, 14: 46, 15: 56}
        data_C_N_Gauss_by_mod_R_num  = {
            4: {1: 1.0, 6: 2.2, 2: 3.1, 3: 4.1, 4: 4.7, 5: 5.2},
            16: {1: 6.2, 6: 7.6, 2: 8.9, 3: 10.0, 4: 10.8, 5: 11.3},
            64: {1: 10.5, 6: 12.3, 2: 13.6, 3: 15.1, 4: 16.1, 5: 16.7},
            256: {1: 14.4, 6: 16.7, 2: 18.1, 3: 20.0, 4: 21.3, 5: 22.0}}
        data_DELTA_Rice_by_mod_R_num = {
            4: {1: 0.2, 6: 0.2, 2: 0.3, 3: 0.3, 4: 0.3, 5: 0.4},
            16: {1: 0.2, 6:  0.2, 2:  0.2, 3: 0.4, 4: 0.4, 5: 0.4},
            64: {1: 0.3, 6: 0.3, 2: 0.3, 3: 0.3, 4: 0.5, 5: 0.4},
            256: {1: 0.4, 6: 0.2, 2: 0.3, 3: 0.3, 4: 0.4, 5: 0.4}}
        data_ABC_by_PP = {1: [0.1, 0.4, 2.0],
                          2: [0.1, 0.4, 2.0],
                          3: [0.1, 0.5, 1.5],
                          4: [0.1, 0.5, 1.5],
                          5: [0.1, 0.5, 1.0],
                          6: [0.1, 0.5, 1.0],
                          7: [0.1, 0.3, 1.0],
                          8: [0.1, 0.4, 1.0]}
        data_D_by_C_N_Rice_no_D = {
            15: 0.07, 16: 0.09, 17: 0.11, 18: 0.14, 19: 0.18,
            20: 0.22, 21: 0.28, 22: 0.36, 23: 0.46, 24: 0.58,
            25: 0.75, 26: 0.97, 27: 1.26, 28: 1.65, 29: 2.20,
            30: 3.02, 31: 4.33, 32: 6.87}
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        mod = data_mod_by_var[SSCTV.variant]
        R_num = data_R_num_by_var[SSCTV.variant]
        PP = data_PP_by_var[SSCTV.variant]
        chanel = data_chanel_by_var[SSCTV.variant]
        SSCTV.tv5_chanel = chanel
        f_c = 474 + (chanel - 21) * 8
        SSCTV.tv5_f_c = f_c
        C_N_Gauss = data_C_N_Gauss_by_mod_R_num[mod][R_num]
        DELTA_Rice = data_DELTA_Rice_by_mod_R_num[mod][R_num]
        ABC = data_ABC_by_PP[PP]
        round_n = 4
        C_N_Rice_no_D = round(C_N_Gauss + DELTA_Rice + ABC[0] + ABC[1] + ABC[2], round_n)
        D = 0.0
        if C_N_Rice_no_D >= 15.0:
            if C_N_Rice_no_D >= 32.0:
                D = data_D_by_C_N_Rice_no_D[32]
            else:
                D = data_D_by_C_N_Rice_no_D[floor(C_N_Rice_no_D)]
                C_N_more = C_N_Rice_no_D - floor(C_N_Rice_no_D)
                D_prop = data_D_by_C_N_Rice_no_D[floor(C_N_Rice_no_D) + 1]
                D_prop -= data_D_by_C_N_Rice_no_D[floor(C_N_Rice_no_D)]
                D += D_prop * C_N_more
                D = round(D, round_n)
        C_N_Rice = round(C_N_Rice_no_D + D, round_n)
        SSCTV.tv5_C_N_Rice = C_N_Rice
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txt0 = M.Text("дБ", font_size = tts, color = mc)
        tx = r"f_c = 474 + (N_c - 21) \cdot 8 = 474 + (" + str(chanel)
        tx += r" - 21) \cdot 8 = " + str(f_c)
        tex = M.MathTex(tx, font_size = txs, color = mc)
        txt = M.Text("МГц", font_size = tts, color = mc)
        gr = M.VGroup(tex, txt).arrange().next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"{\frac {C}{N}}_{Rice} = {\frac {C}{N}}_{Gauss} + DELTA_{Rice}"
        tx2 += r" + A + B + C + D"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc)
        gr2 = M.VGroup(tex2, txt0.copy()).arrange().next_to(gr, M.DOWN)
        tx3 = r"{\frac {C}{N}}_{Gauss} = " + str(C_N_Gauss)
        tex3 = M.MathTex(tx3, font_size = txs, color = mc)
        gr3 = M.VGroup(tex3, txt0.copy()).arrange().next_to(gr2, M.DOWN)
        tx4 = r"DELTA_{Rice} = " + str(DELTA_Rice)
        tex4 = M.MathTex(tx4, font_size = txs, color = mc)
        gr4 = M.VGroup(tex4, txt0.copy()).arrange().next_to(gr3, M.DOWN)
        tx5 = r"A = " + str(ABC[0])
        tex5 = M.MathTex(tx5, font_size = txs, color = mc)
        tx6 = r",\ B = " + str(ABC[1])
        tex6 = M.MathTex(tx6, font_size = txs, color = mc)
        tx7 = r",\ C = " + str(ABC[2])
        tex7 = M.MathTex(tx7, font_size = txs, color = mc)
        gr5 = M.VGroup(M.VGroup(tex5, txt0.copy()).arrange(),
                       M.VGroup(tex6, txt0.copy()).arrange(),
                       M.VGroup(tex7, txt0.copy()).arrange()
                       ).arrange(buff = 0.1).next_to(gr4, M.DOWN)
        tx8 = r"{\frac {C}{N}}_{'Rice} = {\frac {C}{N}}_{Gauss} + DELTA_{Rice}"
        tx8 += r" + A + B + C = "
        tex8 = M.MathTex(tx8, font_size = txs, color = mc).next_to(gr5, M.DOWN)
        tx9 = r" = " + str(C_N_Gauss) + r" + " + str(DELTA_Rice)
        tx9 += r" + " + str(ABC[0]) + r" + " + str(ABC[1]) + r" + " + str(ABC[2])
        tx9 += r" = " + str(C_N_Rice_no_D)
        tex9 = M.MathTex(tx9, font_size = txs, color = mc)
        gr6 = M.VGroup(tex9, txt0.copy()).arrange().next_to(tex8, M.DOWN)
        tx10 = r"D = " + str(D)
        tex10 = M.MathTex(tx10, font_size = txs, color = mc)
        gr7 = M.VGroup(tex10, txt0.copy()).arrange().next_to(gr6, M.DOWN)
        tx11 = r"{\frac {C}{N}}_{Rice} = " + str(C_N_Rice_no_D) + r" + "
        tx11 += str(D) + r" = " + str(C_N_Rice)
        tex11 = M.MathTex(tx11, font_size = txs, color = mc)
        gr8 = M.VGroup(tex11, txt0.copy()).arrange().next_to(gr7, M.DOWN)
        scene.add(gr, gr2, gr3, gr4, gr5, tex8, gr6, gr7, gr8)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv5_formula_2(scene: M.Scene):
        from math import log10, pi
        round_n = 4
        data_N_kff_by_var = {
            1: 3, 2: 4, 3: 3, 4: 2, 5: 4, 6: 3, 7: 2, 8: 4,
            9: 3, 10: 2, 11: 4, 12: 3, 13: 2, 14: 4, 15: 3}
        def data_f_obr_by_chanel(chanel: int):
            if chanel >= 21 and chanel <= 34:
                return 500
            elif chanel >= 35 and chanel <= 69:
                return 800
            return 0
        def data_G_D0_by_chanel(chanel: int):
            if chanel >= 21 and chanel <= 34:
                return 10.0
            elif chanel >= 35 and chanel <= 69:
                return 12.0
            return 0.0
        def data_L_f_by_chanel(chanel: int):
            if chanel >= 21 and chanel <= 34:
                return 3
            elif chanel >= 35 and chanel <= 69:
                return 5
            return 0
        tts = SSf.SIPK_SSCTV_functions.formula_text_size
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        F = data_N_kff_by_var[SSCTV.variant]
        k = 1.38 * 10.0 ** (-23)
        T_0 = 290.0
        B = 7.61 * 10.0 ** 6
        P_n = round(F + 10.0 * log10(k * T_0 * B), round_n)
        SSCTV.tv5_P_n = P_n
        P_smin = round(SSCTV.tv5_C_N_Rice + P_n, round_n)
        SSCTV.tv5_P_smin = P_smin
        f_obr = data_f_obr_by_chanel(SSCTV.tv5_chanel)
        G_D0 = data_G_D0_by_chanel(SSCTV.tv5_chanel)
        Corr = round(10.0 * log10(SSCTV.tv5_f_c / f_obr), round_n)
        G_D = round(G_D0 + Corr, round_n)
        c = 300.0
        lambd = round(c / SSCTV.tv5_f_c, round_n)
        A_a = round(G_D + 10.0 * log10(1.64 * lambd ** 2 / 4.0 / pi), round_n)
        L_f = data_L_f_by_chanel(SSCTV.tv5_chanel)
        phi_min = round(P_smin - A_a + L_f, round_n)
        E_min = round(phi_min + 120.0 + 10.0 * log10(120.0 * pi), round_n)
        SSCTV.tv5_E_min = E_min
        R = 75.0
        U_smin = round(P_smin + 120.0 + 10.0 * log10(R), round_n)
        SSCTV.tv5_U_smin = U_smin
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx = r"P_n = F + 10 \lg (k T_0 B)"
        tex = M.MathTex(tx, font_size = txs, color = mc)
        txt = M.Text("дБВт", font_size = tts, color = mc)
        gr = M.VGroup(tex, txt).arrange().next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"P_n = " + str(F) + r" + 10 \cdot "
        tx2 += str(round(log10(k * T_0 * B), round_n)) + r" = " + str(P_n)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc)
        txt2 = M.Text("дБВт", font_size = tts, color = mc)
        gr2 = M.VGroup(tex2, txt2).arrange().next_to(gr, M.DOWN)
        tx3 = r"P_{s\ min} = \frac {C}{N}}_{Rice} + P_n = "
        tx3 += str(SSCTV.tv5_C_N_Rice) + r" + " + str(P_n)
        tx3 += r" = " + str(P_smin)
        tex3 = M.MathTex(tx3, font_size = txs, color = mc)
        txt3 = M.Text("дБВт", font_size = tts, color = mc)
        gr3 = M.VGroup(tex3, txt3).arrange().next_to(gr2, M.DOWN)
        tx4 = r"A_a = G_D + 10 \lg \left( \frac {1.64 \cdot {\lambda}^2} "
        tx4 += r"{4 \pi} \right)"
        tex4 = M.MathTex(tx4, font_size = txs, color = mc)
        txt4 = M.Text("дБм", font_size = tts, color = mc)
        gr4 = M.VGroup(tex4, txt4).arrange().next_to(gr3, M.DOWN)
        txt4_2 = M.Text("2", font_size = tts - 10.0, color = mc
                        ).next_to(txt4, M.UR, 0.01)
        txt4_2.shift(M.DOWN * txt4_2.height * 0.4)
        tx5 = r"G_D^{'} = " + str(G_D0)
        tex5 = M.MathTex(tx5, font_size = txs, color = mc)
        txt5 = M.Text("дБ", font_size = tts, color = mc)
        gr5 = M.VGroup(tex5, txt5).arrange().next_to(gr4, M.DOWN)
        tx6 = r"Corr = 10 \lg \left( \frac {" + str(SSCTV.tv5_f_c)
        tx6 += r"}{" + str(f_obr) + r"} \right) = " + str(Corr)
        tex6 = M.MathTex(tx6, font_size = txs, color = mc)
        txt6 = M.Text("дБ", font_size = tts, color = mc)
        gr6 = M.VGroup(tex6, txt6).arrange().next_to(gr5, M.DOWN)
        tx7 = r"G_D = " + str(G_D)
        tex7 = M.MathTex(tx7, font_size = txs, color = mc)
        txt7 = M.Text("дБ", font_size = tts, color = mc)
        gr7 = M.VGroup(tex7, txt7).arrange().next_to(gr6, M.DOWN)
        tx8 = r"\lambda = \frac {c}{f_c} = " + str(lambd)
        tex8 = M.MathTex(tx8, font_size = txs, color = mc)
        txt8 = M.Text("м", font_size = tts, color = mc)
        gr8 = M.VGroup(tex8, txt8).arrange().next_to(gr7, M.DOWN)
        scene.add(gr, gr2, gr3, gr4, txt4_2, gr5, gr6, gr7, gr8)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx = r"A_a = " + str(G_D) + r" + 10 \lg \left( \frac {1.64 \cdot {"
        tx += str(lambd) + r"}^2}{4 \cdot 3.1415} \right) = " + str(A_a)
        tex = M.MathTex(tx, font_size = txs, color = mc)
        txt = M.Text("дБм", font_size = tts, color = mc)
        gr = M.VGroup(tex, txt).arrange().next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        txt_2 = M.Text("2", font_size = tts - 10.0, color = mc
                       ).next_to(txt, M.UR, 0.01)
        txt_2.shift(M.DOWN * txt_2.height * 0.4)
        tx2 = r"{\varphi}_{min} = P_{s\ min} - A_a + L_f"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc)
        txt2 = M.Text("дБ(Вт/м )", font_size = tts, color = mc)
        gr2 = M.VGroup(tex2, txt2).arrange().next_to(gr, M.DOWN)
        txt2_2 = M.Text("2", font_size = tts - 10.0, color = mc
                        ).next_to(txt2, M.UR, 0.01)
        txt2_2.shift(M.DOWN * txt2_2.height * 0.4)
        txt2_2.shift(M.LEFT * 0.27)
        tx3 = r"L_f = " + str(L_f)
        tex3 = M.MathTex(tx3, font_size = txs, color = mc)
        txt3 = M.Text("дБ", font_size = tts, color = mc)
        gr3 = M.VGroup(tex3, txt3).arrange().next_to(gr2, M.DOWN)
        tx4 = r"{\varphi}_{min} = " + str(P_smin) + r" + "
        tx4 += str(- A_a) + r" + " + str(L_f) + r" = " + str(phi_min)
        tex4 = M.MathTex(tx4, font_size = txs, color = mc)
        txt4 = M.Text("дБ(Вт/м )", font_size = tts, color = mc)
        gr4 = M.VGroup(tex4, txt4).arrange().next_to(gr3, M.DOWN)
        txt4_2 = M.Text("2", font_size = tts - 10.0, color = mc
                        ).next_to(txt4, M.UR, 0.01)
        txt4_2.shift(M.DOWN * txt4_2.height * 0.4)
        txt4_2.shift(M.LEFT * 0.27)
        tx5 = r"E_{min} = {\varphi}_{min} + 120 + 10 \lg (120 \pi) = "
        tex5 = M.MathTex(tx5, font_size = txs, color = mc).next_to(gr4, M.DOWN)
        tx6 = r" = " + str(phi_min) + r" + 120 + "
        tx6 += str(round(10.0 * log10(120 * pi), round_n)) + r" = " + str(E_min)
        tex6 = M.MathTex(tx6, font_size = txs, color = mc)
        txt6 = M.Text("дБ(мкВ/м)", font_size = tts, color = mc)
        gr5 = M.VGroup(tex6, txt6).arrange().next_to(tex5, M.DOWN)
        tx7 = r"U_{s\ min} = P_{s\ min} + 120 + 10 \lg (R) = "
        tex7 = M.MathTex(tx7, font_size = txs, color = mc).next_to(gr5, M.DOWN)
        tx8 = r" = " + str(P_smin) + r" + 120 + "
        tx8 += str(round(10.0 * log10(R), round_n)) + r" = " + str(U_smin)
        tex8 = M.MathTex(tx8, font_size = txs, color = mc)
        txt8 = M.Text("дБмкВ", font_size = tts, color = mc)
        gr6 = M.VGroup(tex8, txt8).arrange().next_to(tex7, M.DOWN)
        scene.add(gr, txt_2, gr2, txt2_2, gr3, gr4, txt4_2, tex5, gr5, tex7, gr6)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def tv5_formula_3(scene: M.Scene):
        round_n = 4
        tts = SSf.SIPK_SSCTV_functions.formula_text_size - 2.0
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx = r"P_{log}"
        tex = M.MathTex(tx, font_size = txs, color = mc)
        txt = M.Text("(дБВт)", font_size = tts, color = mc)
        tx2 = r" = 10 \lg P"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc)
        txt2 = M.Text("(Вт)", font_size = tts, color = mc)
        gr = M.VGroup(
            M.VGroup(tex, txt).arrange(buff = 0.04),
            M.VGroup(tex2, txt2).arrange(buff = 0.04)).arrange().next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx3 = r"P = 10^{\frac {P_{log}}{10}}"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(gr, M.DOWN)
        tx4 = r"U_{log}"
        tex4 = M.MathTex(tx4, font_size = txs, color = mc)
        txt4 = M.Text("(дБВ)", font_size = tts, color = mc)
        tx5 = r" = 20 \lg U"
        tex5 = M.MathTex(tx5, font_size = txs, color = mc)
        txt5 = M.Text("(В)", font_size = tts, color = mc)
        gr2 = M.VGroup(
            M.VGroup(tex4, txt4).arrange(buff = 0.04),
            M.VGroup(tex5, txt5).arrange(buff = 0.04)).arrange().next_to(
            tex3, M.DOWN)
        tx6 = r"U = 10^{\frac {U_{log}}{20}}"
        tex6 = M.MathTex(tx6, font_size = txs, color = mc).next_to(gr2, M.DOWN)
        tx7 = r"P_n = 10^{\frac {" + str(SSCTV.tv5_P_n) + r"}{10}} = "
        tx7 += SSf.SIPK_SSCTV_functions.float_to_exp10(
            10.0 ** (SSCTV.tv5_P_n / 10.0))
        tex7 = M.MathTex(tx7, font_size = txs, color = mc)
        txt7 = M.Text("Вт", font_size = tts, color = mc)
        gr7 = M.VGroup(tex7, txt7).arrange().next_to(tex6, M.DOWN)
        tx8 = r"P_{s\ min} = 10^{\frac {" + str(SSCTV.tv5_P_smin) + r"}{10}} = "
        tx8 += SSf.SIPK_SSCTV_functions.float_to_exp10(
            10.0 ** (SSCTV.tv5_P_smin / 10.0))
        tex8 = M.MathTex(tx8, font_size = txs, color = mc)
        txt8 = M.Text("Вт", font_size = tts, color = mc)
        gr8 = M.VGroup(tex8, txt8).arrange().next_to(gr7, M.DOWN)
        tx9 = r"E_{min} = 10^{\frac {" + str(SSCTV.tv5_E_min) + r"}{20}} = "
        tx9 += str(round(10.0 ** (SSCTV.tv5_E_min / 20.0), round_n))
        tex9 = M.MathTex(tx9, font_size = txs, color = mc)
        txt9 = M.Text("мкВ/м", font_size = tts, color = mc)
        gr9 = M.VGroup(tex9, txt9).arrange().next_to(gr8, M.DOWN)
        tx10 = r"U_{s\ min} = 10^{\frac {" + str(SSCTV.tv5_U_smin) + r"}{20}} = "
        tx10 += str(round(10.0 ** (SSCTV.tv5_U_smin / 20.0), round_n))
        tex10 = M.MathTex(tx10, font_size = txs, color = mc)
        txt10 = M.Text("мкВ", font_size = tts, color = mc)
        gr10 = M.VGroup(tex10, txt10).arrange().next_to(gr9, M.DOWN)
        scene.add(gr, tex3, gr2, tex6, gr7, gr8, gr9, gr10)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_tv6(scene: M.Scene):
        SSCTV.tv6_count_1(scene)
        SSCTV.tv6_table_1(scene)

    @staticmethod
    def tv6_count_1(scene: M.Scene):
        from random import randint
        def reccurent_count(data: dict, floor: int, db_in: float):
            ret_list = []
            inner_list = []
            for i in data:
                db_next = round(db_in - data[i], 2)
                db_flat = round(db_in - i, 2)
                if floor >= 2:
                    inner_list = reccurent_count(data, floor - 1, db_next)
                    for j in range(len(inner_list)):
                        ret_list.append([db_in, db_flat, *inner_list[j]])
                else:
                    ret_list.append([db_in, db_flat])
            return ret_list

        data_var = {1: [14, 7, 2], 2: [16, 8, 2], 3: [12, 4, 2], 4: [12, 8, 2],
                    5: [8, 6, 2], 6: [9, 8, 2], 7: [9, 7, 2], 8: [10, 6, 2],
                    9: [20, 4, 2], 10: [18, 6, 2], 11: [22, 4, 2], 12: [20, 8, 2],
                    13: [16, 4, 2], 14: [20, 6, 2], 15: [17, 4, 2]}
        data_4 = {26: 1.2,
                #   20: 1.5,
                #   18: 1.8,
                #   16: 2.5,
                #   14: 3.0,
                #   12: 4.0,
                #   10: 4.5
                  }
        data_6 = {20: 1.5,
                #   16: 2.5,
                  12: 4.5}
        data_8 = {20: 2.2,
                #   16: 4.2,
                #   12: 4.5,
                  }
        data_full = data_var[SSCTV.variant]
        SSCTV.tv6_floors = data_full[0]
        SSCTV.tv6_flats = data_full[1]
        SSCTV.tv6_lines = data_full[2]
        SSCTV.tv6_floors_by_line = round(SSCTV.tv6_floors / SSCTV.tv6_lines + 0.000001)
        SSCTV.tv6_floors += 1
        data = data_4
        if SSCTV.tv6_flats >= 5:
            data = data_6
        if SSCTV.tv6_flats >= 7:
            data = data_8
        db_in = SSCTV.tv6_usilit_db - SSCTV.tv6_data_razv_db[SSCTV.tv6_lines]
        lis = reccurent_count(data, SSCTV.tv6_floors_by_line, db_in)
        useful = []
        for i in range(len(lis)):
            show = True
            for j in range(len(lis[i]) // 2):
                if lis[i][1 + j * 2] < 70.0 or lis[i][1 + j * 2] > 83.0:
                    show = False
            if show:
                useful.append(lis[i])
                print(lis[i])
        ind = randint(0, len(useful) - 1)
        # ind = 2
        SSCTV.tv6_used = useful[ind]
        SSCTV.tv6_used_data = data

    @staticmethod
    def tv6_table_1(scene: M.Scene):
        print(SSCTV.tv6_used)
        data_razv_text = {2: "SAH\n204F", 3: "SAH\n306F"}
        data_otv_4_text = {10.0: "TAH\n410F", 12.0: "TAH\n412F",
                           14.0: "TAH\n414F", 16.0: "TAH\n416F",
                           18.0: "TAH\n418F", 20.0: "TAH\n420F",
                           22.0: "TAH\n422F", 26.0: "TAH\n426F"}
        data_otv_6_text = {20.0: "TAH\n620F", 16.0: "TAH\n616F", 12.0: "TAH\n612F"}
        data_otv_8_text = {20.0: "TAH\n820F", 16.0: "TAH\n816F", 12.0: "TAH\n812F"}
        data_otv_text = data_otv_4_text
        data_otv_wires = 4
        if SSCTV.tv6_flats >= 5:
            data_otv_text = data_otv_6_text
            data_otv_wires = 6
        if SSCTV.tv6_flats >= 7:
            data_otv_text = data_otv_8_text
            data_otv_wires = 8
        number_plane = M.NumberPlane(
            x_range = (0, 20, 1),
            y_range = (0, 10, 1),
            x_length = 13.0,
            y_length = 7.0)
        floors_done = 0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tts = 24.0
        dbs = 20.0
        useful = SSCTV.tv6_used
        while floors_done < SSCTV.tv6_floors:
            SSf.SIPK_SSCTV_functions.make_background(scene)
            line_graph1 = number_plane.plot_line_graph(
                x_values = [1, 19],
                y_values = [10, 10],
                line_color = mc,
                vertex_dot_radius = 0.0,
                stroke_width = 5)
            scene.add(line_graph1)
            floors_now = 5
            if floors_done + floors_now > SSCTV.tv6_floors:
                floors_now = SSCTV.tv6_floors - floors_done
            for j in range(floors_now):
                line_graph_j = number_plane.plot_line_graph(
                    x_values = [1, 1, 19, 19],
                    y_values = [2 * (5 - j), 2 * (4 - j), 2 * (4 - j), 2 * (5 - j)],
                    line_color = mc,
                    vertex_dot_radius = 0.0,
                    stroke_width = 5)
                if floors_done == 0:
                    to_usilit = number_plane.plot_line_graph(
                        x_values = [2, 4],
                        y_values = [9, 9],
                        line_color = mc,
                        vertex_dot_radius = 0.0,
                        stroke_width = 3)
                    to_usilit_text = M.Text("К\nантенне", font_size = tts, color = mc
                                            ).move_to(number_plane.c2p(2.6, 9, 0))
                    usilit = number_plane.plot_line_graph(
                        x_values = [4, 4, 7, 7, 4],
                        y_values = [8.2, 9.8, 9.8, 8.2, 8.2],
                        line_color = mc,
                        vertex_dot_radius = 0.0,
                        stroke_width = 4)
                    usilit_text = M.Text("Усилитель", font_size = tts, color = mc
                                         ).move_to(number_plane.c2p(5.5, 9, 0))
                    from_usilit = number_plane.plot_line_graph(
                        x_values = [7, 9],
                        y_values = [9, 9],
                        line_color = mc,
                        vertex_dot_radius = 0.0,
                        stroke_width = 3)
                    from_usilit_text = M.Text(str(SSCTV.tv6_usilit_db), font_size = dbs, color = mc
                                              ).next_to(number_plane.c2p(8, 9, 0), M.UP, 0.05)
                    scene.add(to_usilit, to_usilit_text, usilit, usilit_text,
                              from_usilit, from_usilit_text)
                    if SSCTV.tv6_lines >= 2:
                        razv = number_plane.plot_line_graph(
                            x_values = [9, 9, 11, 11, 9],
                            y_values = [8.2, 9.8, 9.8, 8.2, 8.2],
                            line_color = mc,
                            vertex_dot_radius = 0.0,
                            stroke_width = 4)
                        razv_text = M.Text(data_razv_text[SSCTV.tv6_lines],
                                           font_size = tts, color = mc
                                           ).move_to(number_plane.c2p(10, 9, 0))
                        scene.add(razv, razv_text)
                        if SSCTV.tv6_lines == 2:
                            from_razv1 = number_plane.plot_line_graph(
                                x_values = [11, 17, 17],
                                y_values = [9.33, 9.33, 8],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 3)
                            from_razv2 = number_plane.plot_line_graph(
                                x_values = [11, 13, 13],
                                y_values = [8.67, 8.67, 8],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 3)
                            from_razv_text1 = M.Text(
                                str(SSCTV.tv6_usilit_db - SSCTV.tv6_data_razv_db[SSCTV.tv6_lines]),
                                font_size = dbs, color = mc).next_to(
                                    number_plane.c2p(17, 8.3, 0), buff = 0.1)
                            from_razv_text2 = M.Text(
                                str(SSCTV.tv6_usilit_db - SSCTV.tv6_data_razv_db[SSCTV.tv6_lines]),
                                font_size = dbs, color = mc).next_to(
                                    number_plane.c2p(13, 8.3, 0), buff = 0.1)
                            scene.add(from_razv1, from_razv2, from_razv_text1, from_razv_text2)
                        if SSCTV.tv6_lines == 3:
                            from_razv1 = number_plane.plot_line_graph(
                                x_values = [11, 17, 17],
                                y_values = [9.33, 9.33, 8],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 3)
                            from_razv2 = number_plane.plot_line_graph(
                                x_values = [11, 15, 15],
                                y_values = [9, 9, 8],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 3)
                            from_razv3 = number_plane.plot_line_graph(
                                x_values = [11, 13, 13],
                                y_values = [8.67, 8.67, 8],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 3)
                            from_razv_text1 = M.Text(
                                str(SSCTV.tv6_usilit_db - SSCTV.tv6_data_razv_db[SSCTV.tv6_lines]),
                                font_size = dbs, color = mc).next_to(
                                    number_plane.c2p(17, 8.3, 0), buff = 0.1)
                            from_razv_text2 = M.Text(
                                str(SSCTV.tv6_usilit_db - SSCTV.tv6_data_razv_db[SSCTV.tv6_lines]),
                                font_size = dbs, color = mc).next_to(
                                    number_plane.c2p(15, 8.3, 0), buff = 0.1)
                            from_razv_text3 = M.Text(
                                str(SSCTV.tv6_usilit_db - SSCTV.tv6_data_razv_db[SSCTV.tv6_lines]),
                                font_size = dbs, color = mc).next_to(
                                    number_plane.c2p(13, 8.3, 0), buff = 0.1)
                            scene.add(from_razv1, from_razv2, from_razv3,
                                      from_razv_text1, from_razv_text2, from_razv_text3)
                else:
                    floor_text = M.Text("Этаж " + str(SSCTV.tv6_floors - floors_done),
                                        font_size = tts, color = mc).move_to(
                                            number_plane.c2p(3, 1 + 2 * (4 - j), 0))
                    otv_db_text = M.Text(
                        str(useful[2 * (floors_done % SSCTV.tv6_floors_by_line) - 1]) + " дБ",
                        font_size = tts, color = mc).move_to(
                            number_plane.c2p(6, 1 + 2 * (4 - j), 0))
                    if SSCTV.tv6_lines == 2:
                        if (floors_done - 1) // SSCTV.tv6_floors_by_line == 0:
                            otv = number_plane.plot_line_graph(
                                x_values = [12, 12, 14, 14, 12],
                                y_values = [0.7 + 2 * (4 - j), 1.8 + 2 * (4 - j),
                                            1.8 + 2 * (4 - j), 0.7 + 2 * (4 - j),
                                            0.7 + 2 * (4 - j)],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 4)
                            diff = useful[2 * (floors_done % SSCTV.tv6_floors_by_line) - 2]
                            diff -= useful[2 * (floors_done % SSCTV.tv6_floors_by_line) - 1]
                            otv_text = M.Text(data_otv_text[diff],
                                              font_size = tts, color = mc).move_to(
                                                  number_plane.c2p(13, 1.25 + 2 * (4 - j), 0))
                            dk = 0.9 / data_otv_wires
                            for k in range(data_otv_wires):
                                wire = number_plane.plot_line_graph(
                                    x_values = [11.5, 12],
                                    y_values = [1.8 + 2 * (4 - j) - dk * (1 + k),
                                                1.8 + 2 * (4 - j) - dk * (1 + k)],
                                    line_color = mc,
                                    vertex_dot_radius = 0.0,
                                    stroke_width = 3)
                                scene.add(wire)
                            to_otv = number_plane.plot_line_graph(
                                x_values = [13, 13],
                                y_values = [1.8 + 2 * (4 - j), 2 * (5 - j)],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 3)
                            if floors_done % SSCTV.tv6_floors_by_line != 0:
                                from_otv = number_plane.plot_line_graph(
                                    x_values = [13, 13],
                                    y_values = [0.7 + 2 * (4 - j), 2 * (4 - j)],
                                    line_color = mc,
                                    vertex_dot_radius = 0.0,
                                    stroke_width = 3)
                                from_otv_db_text = M.Text(
                                    str(useful[2 * (floors_done % SSCTV.tv6_floors_by_line)]),
                                    font_size = dbs, color = mc).next_to(
                                        number_plane.c2p(13, 0.3 + 2 * (4 - j), 0), buff = 0.1)
                                scene.add(from_otv, from_otv_db_text)
                            line_2 = number_plane.plot_line_graph(
                                x_values = [17, 17],
                                y_values = [2 * (4 - j), 2 * (5 - j)],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 3)
                            scene.add(otv, otv_text, to_otv, line_2)
                        elif (floors_done - 1) // SSCTV.tv6_floors_by_line == 1:
                            otv = number_plane.plot_line_graph(
                                x_values = [16, 16, 18, 18, 16],
                                y_values = [0.7 + 2 * (4 - j), 1.8 + 2 * (4 - j),
                                            1.8 + 2 * (4 - j), 0.7 + 2 * (4 - j),
                                            0.7 + 2 * (4 - j)],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 4)
                            diff = useful[2 * (floors_done % SSCTV.tv6_floors_by_line) - 2]
                            diff -= useful[2 * (floors_done % SSCTV.tv6_floors_by_line) - 1]
                            otv_text = M.Text(data_otv_text[diff],
                                              font_size = tts, color = mc).move_to(
                                                number_plane.c2p(17, 1.25 + 2 * (4 - j), 0))
                            dk = 0.9 / data_otv_wires
                            for k in range(data_otv_wires):
                                wire = number_plane.plot_line_graph(
                                    x_values = [15.5, 16],
                                    y_values = [1.8 + 2 * (4 - j) - dk * (1 + k),
                                                1.8 + 2 * (4 - j) - dk * (1 + k)],
                                    line_color = mc,
                                    vertex_dot_radius = 0.0,
                                    stroke_width = 3)
                                scene.add(wire)
                            to_otv = number_plane.plot_line_graph(
                                x_values = [17, 17],
                                y_values = [1.8 + 2 * (4 - j), 2 * (5 - j)],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 3)
                            if (floors_done % SSCTV.tv6_floors_by_line != 0 and
                                floors_done + 1 != SSCTV.tv6_floors):
                                from_otv = number_plane.plot_line_graph(
                                    x_values = [17, 17],
                                    y_values = [0.7 + 2 * (4 - j), 2 * (4 - j)],
                                    line_color = mc,
                                    vertex_dot_radius = 0.0,
                                    stroke_width = 3)
                                from_otv_db_text = M.Text(
                                    str(useful[2 * (floors_done % SSCTV.tv6_floors_by_line)]),
                                    font_size = dbs, color = mc).next_to(
                                        number_plane.c2p(17, 0.3 + 2 * (4 - j), 0), buff = 0.1)
                                scene.add(from_otv, from_otv_db_text)
                            scene.add(otv, otv_text, to_otv)
                    scene.add(floor_text, otv_db_text)
                floors_done += 1
                scene.add(line_graph_j)
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_new_tv6(scene: M.Scene):
        tv6_usilit_db = 95.0
        tv6_data_razv_db = {1: 0.0, 2: 4.0}
        db_minus_between_floors = 0.6
        usilit_name = "Foro\nSHA 848-121"
        data = SSCTV.new_tv6_count_1(SSCTV.variant, tv6_usilit_db, tv6_data_razv_db, db_minus_between_floors)
        SSCTV.new_tv6_table_1(scene, data[0], data[1], data[2], data[3], data[4],
                              tv6_usilit_db, tv6_data_razv_db, usilit_name, db_minus_between_floors)

    @staticmethod
    def reccurent_count(data: dict, floor: int, db_in: float, db_minus_between_floors):
        ret_list = []
        inner_list = []
        for i in data:
            db_next = round(db_in - data[i] - db_minus_between_floors, 1)
            db_flat = round(db_in - i, 1)
            if floor >= 2:
                inner_list = SSCTV.reccurent_count(data, floor - 1, db_next, db_minus_between_floors)
                for j in range(len(inner_list)):
                    ret_list.append([db_in, db_flat, *inner_list[j]])
            else:
                ret_list.append([db_in, db_flat])
        return ret_list

    @staticmethod
    def new_tv6_count_1(variant, tv6_usilit_db, tv6_data_razv_db, db_minus_between_floors):
        from random import randint
        data_var = {1: [14, 7, 2], 2: [16, 8, 2], 3: [12, 4, 2], 4: [12, 8, 2],
                    5: [8, 6, 2], 6: [9, 8, 2], 7: [9, 7, 2], 8: [10, 6, 2],
                    9: [20, 4, 2], 10: [18, 6, 2], 11: [22, 4, 2], 12: [20, 8, 2],
                    13: [16, 4, 2], 14: [20, 6, 2], 15: [17, 4, 2]}
        data_4 = {27: 1.2,
                #   24: 1.2,
                #   20: 1.5,
                  16: 2.5,
                #   12: 4.5,
                  10: 4.5
                  }
        data_6 = {24: 1.2,
                #   20: 1.5,
                #   16: 2.5,
                  12: 4.5
                  }
        data_8 = {20: 2.2,
                #   16: 4.2,
                  12: 4.5
                  }
        data_full = data_var[variant]
        tv6_floors = data_full[0]
        tv6_flats = data_full[1]
        tv6_lines = data_full[2]
        tv6_floors_by_line = round(tv6_floors / tv6_lines + 0.000001)
        data = data_4
        if tv6_flats >= 5:
            data = data_6
        if tv6_flats >= 7:
            data = data_8
        db_in = tv6_usilit_db - tv6_data_razv_db[tv6_lines]
        lis = SSCTV.reccurent_count(data, tv6_floors_by_line, db_in, db_minus_between_floors)
        useful = []
        min_floor_db = 50.5
        max_floor_db = 71.5
        for i in range(len(lis)):
            show = True
            for j in range(len(lis[i]) // 2):
                if (lis[i][1 + j * 2] - tv6_floors_by_line * (tv6_lines - 1) * db_minus_between_floors < min_floor_db or
                    lis[i][1 + j * 2] > max_floor_db):
                    show = False
            if show:
                useful.append(lis[i])
                print(lis[i])
        ind = randint(0, len(useful) - 1)
        ind = 1
        return (useful[ind], tv6_floors, tv6_flats, tv6_lines, tv6_floors_by_line)

    @staticmethod
    def new_tv6_table_1(scene: M.Scene, useful, tv6_floors, tv6_flats, tv6_lines, tv6_floors_by_line,
                        tv6_usilit_db, tv6_data_razv_db, usilit_name, db_minus_between_floors):
        print(useful)
        data_razv_text = {2: "TLC\nSAH\n204F", 3: "SAH\n306F"}
        data_otv_4_text = {10: "TAH-410F", 12: "TAH-412F", 16: "TAH-416F",
                           20: "TAH-420F", 24: "TAH-424F", 27: "TAH-427F"}
        data_otv_6_text = {12: "TAH-612F", 16: "TAH-616F", 20: "TAH-620F", 24: "TAH-624F"}
        data_otv_8_text = {12: "TAH-812F", 16: "TAH-816F", 20: "TAH-820F"}
        data_otv_text = data_otv_4_text
        data_otv_wires = 4
        if tv6_flats >= 5:
            data_otv_text = data_otv_6_text
            data_otv_wires = 6
        if tv6_flats >= 7:
            data_otv_text = data_otv_8_text
            data_otv_wires = 8
        number_plane = M.NumberPlane(
            x_range = (0, 20, 1),
            y_range = (0, 10, 1),
            x_length = 13.0,
            y_length = 7.0)
        floors_done = 0
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        tts = 18.0
        dbs = 18.0
        x_pos_1 = 17.0
        x_pos_2 = 13.0
        splitter_half_width = 1.1
        splitter_half_height = 0.4
        splitter_pos_y = 1.0
        dk = splitter_half_height * 2.0 / (data_otv_wires + 1)
        while floors_done < tv6_floors:
            SSf.SIPK_SSCTV_functions.make_background(scene)
            line_graph1 = number_plane.plot_line_graph(
                x_values = [1, 19],
                y_values = [10, 10],
                line_color = mc,
                vertex_dot_radius = 0.0,
                stroke_width = 5)
            scene.add(line_graph1)
            j = 0
            if floors_done == 0:
                j = 1
                to_usilit = number_plane.plot_line_graph(
                    x_values = [2, 4],
                    y_values = [9, 9],
                    line_color = mc,
                    vertex_dot_radius = 0.0,
                    stroke_width = 3)
                to_usilit_text = M.Text("К антенне", font_size = tts, color = mc
                                        ).move_to(number_plane.c2p(2.53, 9.35, 0))
                usilit = number_plane.plot_line_graph(
                    x_values = [4, 4, 7, 7, 4],
                    y_values = [8.2, 9.8, 9.8, 8.2, 8.2],
                    line_color = mc,
                    vertex_dot_radius = 0.0,
                    stroke_width = 4)
                usilit_text = M.Text("".join(["Усилитель\n", usilit_name]), font_size = tts, color = mc
                                     ).move_to(number_plane.c2p(5.5, 9, 0))
                from_usilit = number_plane.plot_line_graph(
                    x_values = [7, 9],
                    y_values = [9, 9],
                    line_color = mc,
                    vertex_dot_radius = 0.0,
                    stroke_width = 3)
                from_usilit_text = M.Text("".join([str(tv6_usilit_db), " дБ"]), font_size = dbs, color = mc
                                          ).next_to(number_plane.c2p(8, 9, 0), M.UP, 0.05)
                line_graph_j = number_plane.plot_line_graph(
                    x_values = [1, 1, 19, 19],
                    y_values = [10, 8, 8, 10],
                    line_color = mc,
                    vertex_dot_radius = 0.0,
                    stroke_width = 5)
                scene.add(to_usilit, to_usilit_text, usilit, usilit_text, from_usilit, from_usilit_text, line_graph_j)
                if tv6_lines >= 2:
                    razv = number_plane.plot_line_graph(
                        x_values = [9, 9, 11, 11, 9],
                        y_values = [8.2, 9.8, 9.8, 8.2, 8.2],
                        line_color = mc,
                        vertex_dot_radius = 0.0,
                        stroke_width = 4)
                    razv_text = M.Text(data_razv_text[tv6_lines], font_size = tts, color = mc
                                       ).move_to(number_plane.c2p(10, 9, 0))
                    scene.add(razv, razv_text)
                    if tv6_lines == 2:
                        from_razv1 = number_plane.plot_line_graph(
                            x_values = [11, x_pos_1, x_pos_1],
                            y_values = [9.33, 9.33, 8],
                            line_color = mc,
                            vertex_dot_radius = 0.0,
                            stroke_width = 3)
                        from_razv2 = number_plane.plot_line_graph(
                            x_values = [11, x_pos_2, x_pos_2],
                            y_values = [8.67, 8.67, 8],
                            line_color = mc,
                            vertex_dot_radius = 0.0,
                            stroke_width = 3)
                        from_razv_text1 = M.Text(
                            "".join([str(tv6_usilit_db - tv6_data_razv_db[tv6_lines]), " дБ"]),
                            font_size = dbs, color = mc).next_to(number_plane.c2p(x_pos_1, 8.3, 0), buff = 0.1)
                        from_razv_text2 = M.Text(
                            "".join([str(tv6_usilit_db - tv6_data_razv_db[tv6_lines]), " дБ"]),
                            font_size = dbs, color = mc).next_to(number_plane.c2p(x_pos_2, 8.3, 0), buff = 0.1)
                        scene.add(from_razv1, from_razv2, from_razv_text1, from_razv_text2)
            floors_now = 5
            if floors_done + floors_now > tv6_floors:
                floors_now = tv6_floors - floors_done
            while j < floors_now:
                current_line_index = floors_done // tv6_floors_by_line
                current_floor_in_line_index = floors_done % tv6_floors_by_line
                line_graph_j = number_plane.plot_line_graph(
                    x_values = [1, 1, 19, 19],
                    y_values = [2 * (5 - j), 2 * (4 - j), 2 * (4 - j), 2 * (5 - j)],
                    line_color = mc,
                    vertex_dot_radius = 0.0,
                    stroke_width = 5)
                floor_text = M.Text("Этаж " + str(tv6_floors - floors_done), font_size = 24.0, color = mc
                                    ).move_to(number_plane.c2p(3, 1 + 2 * (4 - j), 0))
                otv_db = useful[2 * current_floor_in_line_index + 1]
                otv_db -= db_minus_between_floors * (1 + current_line_index * tv6_floors_by_line)
                otv_db_text = M.Text("".join([str(round(otv_db, 1)), " дБ"]),
                                     font_size = tts, color = mc).move_to(
                                         number_plane.c2p(7, 1 + 2 * (4 - j), 0))
                scene.add(line_graph_j, floor_text, otv_db_text)
                if tv6_lines == 2:
                    if current_line_index == 0:
                        otv = number_plane.plot_line_graph(
                            x_values = [x_pos_1 - splitter_half_width,
                                        x_pos_1 - splitter_half_width,
                                        x_pos_1 + splitter_half_width,
                                        x_pos_1 + splitter_half_width,
                                        x_pos_1 - splitter_half_width],
                            y_values = [splitter_pos_y - splitter_half_height + 2 * (4 - j),
                                        splitter_pos_y + splitter_half_height + 2 * (4 - j),
                                        splitter_pos_y + splitter_half_height + 2 * (4 - j),
                                        splitter_pos_y - splitter_half_height + 2 * (4 - j),
                                        splitter_pos_y - splitter_half_height + 2 * (4 - j)],
                            line_color = mc,
                            vertex_dot_radius = 0.0,
                            stroke_width = 4)
                        diff = useful[2 * current_floor_in_line_index] - useful[2 * current_floor_in_line_index + 1]
                        otv_text = M.Text(data_otv_text[round(diff)], font_size = tts, color = mc).move_to(
                            number_plane.c2p(x_pos_1, splitter_pos_y + 2 * (4 - j), 0))
                        for k in range(data_otv_wires):
                            wire = number_plane.plot_line_graph(
                                x_values = [x_pos_1 - splitter_half_width - 0.5,
                                            x_pos_1 - splitter_half_width],
                                y_values = [splitter_pos_y + splitter_half_height + 2 * (4 - j) - dk * (1 + k),
                                            splitter_pos_y + splitter_half_height + 2 * (4 - j) - dk * (1 + k)],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 2)
                            scene.add(wire)
                        to_otv = number_plane.plot_line_graph(
                            x_values = [x_pos_1, x_pos_1],
                            y_values = [2 * (5 - j), splitter_pos_y + splitter_half_height + 2 * (4 - j)],
                            line_color = mc,
                            vertex_dot_radius = 0.0,
                            stroke_width = 3)
                        to_otv_db_1 = useful[2 * current_floor_in_line_index] - db_minus_between_floors
                        to_otv_db_2 = useful[0] - db_minus_between_floors * (1 + floors_done)
                        to_otv_db_text = M.Text("".join([str(round(to_otv_db_1, 1)), " дБ"]),
                                                font_size = dbs, color = mc).next_to(
                                                    number_plane.c2p(x_pos_1, 1.7 + 2 * (4 - j), 0), buff = 0.1)
                        to_otv_db_text_2 = M.Text("".join([str(round(to_otv_db_2, 1)), " дБ"]),
                                                  font_size = dbs, color = mc).next_to(
                                                      number_plane.c2p(x_pos_2, 1.7 + 2 * (4 - j), 0), buff = 0.1)
                        line_2 = number_plane.plot_line_graph(
                            x_values = [x_pos_2, x_pos_2],
                            y_values = [2 * (5 - j), 2 * (4 - j)],
                            line_color = mc,
                            vertex_dot_radius = 0.0,
                            stroke_width = 3)
                        scene.add(otv, otv_text, to_otv, to_otv_db_text, to_otv_db_text_2, line_2)
                        if (floors_done + 1) % tv6_floors_by_line != 0:
                            from_otv = number_plane.plot_line_graph(
                                x_values = [x_pos_1, x_pos_1],
                                y_values = [splitter_pos_y - splitter_half_height + 2 * (4 - j), 2 * (4 - j)],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 3)
                            from_otv_db = useful[2 * (current_floor_in_line_index + 1)]
                            from_otv_db_text = M.Text("".join([str(round(from_otv_db, 1)), " дБ"]),
                                                      font_size = dbs, color = mc).next_to(
                                                          number_plane.c2p(x_pos_1, 0.3 + 2 * (4 - j), 0), buff = 0.1)
                            scene.add(from_otv, from_otv_db_text)
                    elif current_line_index == 1:
                        otv = number_plane.plot_line_graph(
                            x_values = [x_pos_2 - splitter_half_width,
                                        x_pos_2 - splitter_half_width,
                                        x_pos_2 + splitter_half_width,
                                        x_pos_2 + splitter_half_width,
                                        x_pos_2 - splitter_half_width],
                            y_values = [splitter_pos_y - splitter_half_height + 2 * (4 - j),
                                        splitter_pos_y + splitter_half_height + 2 * (4 - j),
                                        splitter_pos_y + splitter_half_height + 2 * (4 - j),
                                        splitter_pos_y - splitter_half_height + 2 * (4 - j),
                                        splitter_pos_y - splitter_half_height + 2 * (4 - j)],
                            line_color = mc,
                            vertex_dot_radius = 0.0,
                            stroke_width = 4)
                        diff = useful[2 * current_floor_in_line_index] - useful[2 * current_floor_in_line_index + 1]
                        otv_text = M.Text(data_otv_text[round(diff)], font_size = tts, color = mc).move_to(
                            number_plane.c2p(x_pos_2, splitter_pos_y + 2 * (4 - j), 0))
                        for k in range(data_otv_wires):
                            wire = number_plane.plot_line_graph(
                                x_values = [x_pos_2 - splitter_half_width - 0.5,
                                            x_pos_2 - splitter_half_width],
                                y_values = [splitter_pos_y + splitter_half_height + 2 * (4 - j) - dk * (1 + k),
                                            splitter_pos_y + splitter_half_height + 2 * (4 - j) - dk * (1 + k)],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 2)
                            scene.add(wire)
                        to_otv = number_plane.plot_line_graph(
                            x_values = [x_pos_2, x_pos_2],
                            y_values = [2 * (5 - j), splitter_pos_y + splitter_half_height + 2 * (4 - j)],
                            line_color = mc,
                            vertex_dot_radius = 0.0,
                            stroke_width = 3)
                        to_otv_db_2 = useful[2 * current_floor_in_line_index]
                        to_otv_db_2 -= db_minus_between_floors * (1 + current_line_index * tv6_floors_by_line)
                        to_otv_db_text_2 = M.Text("".join([str(round(to_otv_db_2, 1)), " дБ"]),
                                                  font_size = dbs, color = mc).next_to(
                                                      number_plane.c2p(x_pos_2, 1.7 + 2 * (4 - j), 0), buff = 0.1)
                        scene.add(otv, otv_text, to_otv, to_otv_db_text_2)
                        if floors_done + 1 != tv6_floors:
                            from_otv = number_plane.plot_line_graph(
                                x_values = [x_pos_2, x_pos_2],
                                y_values = [splitter_pos_y - splitter_half_height + 2 * (4 - j), 2 * (4 - j)],
                                line_color = mc,
                                vertex_dot_radius = 0.0,
                                stroke_width = 3)
                            from_otv_db = useful[2 * (current_floor_in_line_index + 1)]
                            from_otv_db -= db_minus_between_floors * current_line_index * tv6_floors_by_line
                            from_otv_db_text = M.Text("".join([str(round(from_otv_db, 1)), " дБ"]),
                                                      font_size = dbs, color = mc).next_to(
                                                          number_plane.c2p(x_pos_2, 0.3 + 2 * (4 - j), 0), buff = 0.1)
                            scene.add(from_otv, from_otv_db_text)
                j += 1
                floors_done += 1
            SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_tv7(scene: M.Scene):
        SSCTV.tv7_formula_1(scene)

    @staticmethod
    def tv7_formula_1(scene: M.Scene):
        from math import cos, acos, sqrt, log10
        tts = SSf.SIPK_SSCTV_functions.formula_text_size - 2.0
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        SSf.SIPK_SSCTV_functions.make_background(scene)
        cos_phi = round(cos(SSCTV.tv7_phi), 3)
        cos_lambda = round(cos(SSCTV.tv7_lambda), 3)
        psi = acos(cos_phi * cos_lambda)
        psi_grad = round(psi / 3.14159265 * 180.0)
        R_3 = 6378
        R_G = 42253
        d = round(sqrt(R_3 ** 2 + R_G ** 2 - 2 * R_3 * R_G * cos(psi)))
        d = 39400
        L_0 = round(20.0 * (log10(SSCTV.tv7_f) + log10(d)) + 32.45, 3)
        P_r = round(SSCTV.tv7_P_EIRP + 40.0 - 6.0 - L_0, 3)
        K_n = round(10 ** (1/10), 3)
        T_nr = round((K_n - 1.0) * 290.0, 3)
        N_n = round(1.38 * (10 ** -9) * (198.0) * 27000000.0, 3)
        P_r_nolog = 10 ** (P_r / 10.0)
        SNR = round(P_r_nolog / N_n * (10 ** 14), 1)
        tx = r"{\psi}_{0} = \arccos(\cos {\varphi}_{C^{'}} \cdot \cos {\Delta \lambda}_{C{'}}) = "
        tx += r"\arccos(" + str(cos_phi) + r" \cdot "
        tx += str(cos_lambda) + r") = " + str(psi_grad) + r"^{\circ}"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"d = \sqrt {{R_3}^2 + {R_G}^2 - 2 R_3 R_G \cos {\psi}_0} = "
        tx2 += str(R_G) + r" \sqrt {" + str(round((R_3 / R_G) ** 2, 3)) + r" + 1 - "
        tx2 += str(round(2.0 * R_3 / R_G * cos(psi), 3)) + r"} = " + str(d)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc)
        txt2 = M.Text("км", font_size = tts, color = mc)
        gr2 = M.VGroup(tex2, txt2).arrange().next_to(tex, M.DOWN)
        tx3 = r"\frac {S}{N} = \frac {P_r}{N_n}"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(gr2, M.DOWN)
        tx4 = r"P_r = P_{EIRP} + G_r - b_r - 20 \lg \left(\frac {4 \pi d}{\lambda}\right)"
        tex4 = M.MathTex(tx4, font_size = txs, color = mc)
        txt4 = M.Text("дБВт", font_size = tts, color = mc)
        gr4 = M.VGroup(tex4, txt4).arrange().next_to(tex3, M.DOWN)
        tx5 = r"L_0 = 20 \cdot \left(\lg f + \lg d \right) + 32.45"
        tex5 = M.MathTex(tx5, font_size = txs, color = mc)
        txt5 = M.Text("дБ", font_size = tts, color = mc)
        gr5 = M.VGroup(tex5, txt5).arrange().next_to(gr4, M.DOWN)
        tx6 = r"N_n = k \cdot \left(T_{na} + T_{nr} \right) \cdot \Delta f"
        tex6 = M.MathTex(tx6, font_size = txs, color = mc)
        txt6 = M.Text("Вт", font_size = tts, color = mc)
        gr6 = M.VGroup(tex6, txt6).arrange().next_to(gr5, M.DOWN)
        tx7 = r"T_{nr} = \left( K_n - 1 \right) \cdot T_0 "
        tex7 = M.MathTex(tx7, font_size = txs, color = mc).next_to(gr6, M.DOWN)
        tx8 = r"L_0 = 20 \cdot \left(\lg " + str(SSCTV.tv7_f) + r" + \lg " + str(d) + r" \right) + 32.45"
        tx8 += r" = " + str(L_0)
        tex8 = M.MathTex(tx8, font_size = txs, color = mc)
        txt8 = M.Text("дБ", font_size = tts, color = mc)
        gr8 = M.VGroup(tex8, txt8).arrange().next_to(tex7, M.DOWN)
        tx9 = r"P_r = " + str(SSCTV.tv7_P_EIRP) + r" + 40 - 6 - " + str(L_0)
        tx9 += r" = " + str(P_r)
        tex9 = M.MathTex(tx9, font_size = txs, color = mc)
        txt9 = M.Text("дБВт", font_size = tts, color = mc)
        gr9 = M.VGroup(tex9, txt9).arrange().next_to(gr8, M.DOWN)
        scene.add(tex, gr2, tex3, gr4, gr5, gr6, tex7, gr8, gr9)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        SSf.SIPK_SSCTV_functions.make_background(scene)
        tx = r"K_n = 10^{\frac {K_{n \ log}}{10}} = 10^{\frac{1}{10}} = "
        tx += str(K_n)
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"T_{nr} = \left( " + str(K_n) + r" - 1 \right) \cdot 290 = "
        tx2 += str(T_nr)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc)
        txt2 = M.Text("К", font_size = tts, color = mc)
        gr2 = M.VGroup(tex2, txt2).arrange().next_to(tex, M.DOWN)
        tx3 = r"N_n = 1.38 \cdot 10^{-23} \cdot " + str(T_nr)
        tx3 += r" \cdot 27000000 = " + str(N_n) + r" \cdot 10^{-14}"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc)
        txt3 = M.Text("Вт", font_size = tts, color = mc)
        gr3 = M.VGroup(tex3, txt3).arrange().next_to(gr2, M.DOWN)
        tx4 = r"P_r = 10^{\frac {P_{r \ log}}{10}} = 10^{\frac {" + str(P_r) + r"}{10}} = "
        tx4 += SSf.SIPK_SSCTV_functions.float_to_exp10(P_r_nolog)
        tex4 = M.MathTex(tx4, font_size = txs, color = mc)
        txt4 = M.Text("Вт", font_size = tts, color = mc)
        gr4 = M.VGroup(tex4, txt4).arrange().next_to(gr3, M.DOWN)
        tx5 = r"\frac {S}{N} = \frac {" + SSf.SIPK_SSCTV_functions.float_to_exp10(P_r_nolog)
        tx5 += r"}{" + str(N_n) + r" \cdot 10^{-14}" + r"} = " + str(SNR) + r" = "
        tx5 += str(round(10.0 * log10(SNR), 2))
        tex5 = M.MathTex(tx5, font_size = txs, color = mc).next_to(gr4, M.DOWN)
        txt5 = M.Text("дБ", font_size = tts, color = mc)
        gr5 = M.VGroup(tex5, txt5).arrange().next_to(gr4, M.DOWN)
        scene.add(tex, gr2, gr3, gr4, gr5)
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
        SSCTV.old_tv5_formula_1(scene)

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
            line_config = {"color": mc}).next_to(table, M.DOWN, 0.5)
        table3 = SSf.Table(
            table_data3,
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.2,
            element_to_mobject_config = {"font_size": fs - 2.0, "color": mc},
            line_config = {"color": mc}).next_to(table2, M.DOWN, 0.5)
        table4 = SSf.Table(
            [["Вариант", "Кадров в 1-ой группе",
              "Кадров во 2-ой группе", "В-кадров подряд"],
             [str(SSCTV.old_tv_variant), str(dat[0]), str(dat[1]), str(dat[2])]],
            include_outer_lines = True,
            v_buff = 0.4,
            h_buff = 0.6,
            element_to_mobject_config = {"font_size": fs + 6.0, "color": mc},
            line_config = {"color": mc}).next_to(table3, M.DOWN, 0.5)
        scene.add(table, table2, table3, table4)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def old_tv5_formula_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        mb = 16
        b = 4
        res_x = 1920
        res_y = 1080
        mb_num = int(res_x * res_y / mb / mb)
        b_in_mb = int(mb * mb / b / b)
        Y_num = b_in_mb * mb_num
        tx = r"B_M = \frac {" + str(res_x) + r"}{" + str(mb) + r"} \cdot "
        tx += r"\frac {" + str(res_y) + r"}{" + str(mb) + r"} = "
        tx += str(mb_num)
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"Y = " + str(mb_num) + r" \cdot " + str(b_in_mb) + r" = "
        tx2 += str(Y_num)
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"C_R = C_B = \frac{" + str(Y_num) + r"}{4} = "
        tx3 += str(int(Y_num / 4))
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        SSf.SIPK_SSCTV_functions.make_pause(scene)

    @staticmethod
    def make_old_tv6(scene: M.Scene):
        SSCTV.old_tv6_formula_1(scene)

    @staticmethod
    def old_tv6_formula_1(scene: M.Scene):
        SSf.SIPK_SSCTV_functions.make_background(scene)
        txs = SSf.SIPK_SSCTV_functions.formula_tex_size
        mc = SSf.SIPK_SSCTV_functions.get_main_color()
        data = {1: [32, -3, -6], 2: [24, -12, -16], 3: [22, -22, -28],
                4: [25, -30, -38], 5: [28, -36, -43], 6: [18, -54, -67],
                7: [19, -45, -52], 8: [21, -39, -45], 9: [23, -31, -39],
                10: [26, -17, -23], 11: [15, -24, -33], 12: [16, -25, -29],
                13: [17, -26, -32], 14: [27, -27, -36], 15: [33, -5, -10]}
        dat = data[SSCTV.old_tv_variant]
        tx = r"N_U = 20 \cdot \lg \frac {U}{U_n}"
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(
            SSf.SIPK_SSCTV_functions.upper_side, M.DOWN)
        tx2 = r"K_r = \frac {\sqrt {U_2^2 + U_3^2}}{U_1} \cdot 100 \%"
        tex2 = M.MathTex(tx2, font_size = txs, color = mc).next_to(tex, M.DOWN)
        tx3 = r"N_U = 20 \cdot \lg \frac {U}{U_n} \Rightarrow "
        tx3 += r"\frac {N_U}{20} = \lg \frac {U}{U_n} \Rightarrow "
        tx3 += r"10^{\frac {N_U}{20}} = \frac {U}{U_n} \Rightarrow "
        tx3 += r"U = U_n \cdot 10^{\frac {N_U}{20}}"
        tex3 = M.MathTex(tx3, font_size = txs, color = mc).next_to(tex2, M.DOWN)
        scene.add(tex, tex2, tex3)
        prev = tex3
        U_is = []
        for i in range(3):
            U_i = round(0.775 * 10 ** (dat[i] / 20.0), 4)
            U_is.append(U_i)
            tx = r"U_" + str(i + 1) + r" = 0.775 \cdot 10^{\frac {"
            tx += str(dat[i]) + r"}{20}} = " + str(U_i)
            tex = M.MathTex(tx, font_size = txs, color = mc).next_to(prev, M.DOWN)
            scene.add(tex)
            prev = tex
        from math import sqrt
        K_r = round(sqrt(U_is[1] ** 2 + U_is[2] ** 2) / U_is[0] * 100.0, 4)
        tx = r"K_r = " + str(K_r)
        tex = M.MathTex(tx, font_size = txs, color = mc).next_to(prev, M.DOWN)
        scene.add(tex)
        SSf.SIPK_SSCTV_functions.make_pause(scene)
        
