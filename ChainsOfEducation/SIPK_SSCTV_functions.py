import manim as M
import random
import enum


class SIPK_SSCTV_functions(object):
    """SIPK_SSCTV_functions"""

    data_saved = r"""pkg load communications"""

    table_font_size = 24.0
    formula_tex_size = 40.0
    formula_text_size = 30.0
    upper_side = M.UP * 4.0

    @staticmethod
    def get_main_color():
        return "#000000"

    @staticmethod
    def get_background_color():
        return "#FFFFFF"

    @staticmethod
    def make_background(scene: M.Scene):
        scene.add(M.Rectangle(
            SIPK_SSCTV_functions.get_background_color(),
            9.0, 15.0, fill_opacity = 1.0))

    @staticmethod
    def make_pause(scene: M.Scene):
        scene.wait()
        scene.clear()

    @staticmethod
    def fill_zeros(str_to_fill: str, n: int):
        return "0" * (n - len(str_to_fill)) + str_to_fill

    @staticmethod
    def add_zeros(str_to_add: str, n: int, left: bool = False):
        if left: return "0" * n + str_to_add
        else: return str_to_add + "0" * n

    @staticmethod
    def sum_mod_2(bit1: str, bit2: str):
        if (bit1 == "0" and bit2 == "0") or (bit1 == "1" and bit2 == "1"):
            return "0"
        else:
            return "1"

    @staticmethod
    def sum_mod_2_full(bin_str_1: str, bin_str_2: str):
        len_max = max(len(bin_str_1), len(bin_str_2))
        bin_str_1 = SIPK_SSCTV_functions.fill_zeros(bin_str_1, len_max)
        bin_str_2 = SIPK_SSCTV_functions.fill_zeros(bin_str_2, len_max)
        sm2_full = ""
        for i in range(len_max):
            sm2_full += SIPK_SSCTV_functions.sum_mod_2(bin_str_1[i], bin_str_2[i])
        return sm2_full

    @staticmethod
    def multiplication(bit1: str, bit2: str):
        if bit1 == "1" and bit2 == "1":
            return "1"
        else:
            return "0"

    @staticmethod
    def diag_ones_matrix(n: int):
        ret_matrix = []
        for i in range(n):
            ret_matrix.append([])
            for j in range(n):
                if i == j:
                    ret_matrix[-1].append("1")
                else:
                    ret_matrix[-1].append("0")
        return ret_matrix

    @staticmethod
    def get_random_0_1_str(n: int = 8):
        ret = []
        for _ in range(n):
            r = random.random()
            if r >= 0.5:
                ret.append("1")
            else:
                ret.append("0")
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
    def c_n_k(n: int, k: int):
        numerator = 1
        denominator = 1
        if k > n // 2: k = n - k
        for i in range(n, n - k, -1):
            numerator *= i
        for i in range(1, k + 1, 1):
            denominator *= i
        return numerator // denominator

    @staticmethod
    def int_to_exp10(n: int):
        s = "{:e}".format(n)
        if n >= 10000000000: s = s[:4] + r" \cdot 10^{" + s[-2:] + r"}"
        else: s = s[:4] + r" \cdot 10^{" + s[-1:] + r"}"
        return s

    @staticmethod
    def float_to_exp10(n: float):
        s = "{:e}".format(n)
        power = ""
        ch = s[-1]
        i = -1
        while ch != "e" and i > -20:
            power = ch + power
            i -= 1
            ch = s[i]
        s = s[:4] + r" \cdot 10^{" + power + r"}"
        return s

    @staticmethod
    def sigmoid(x: float):
        from math import exp
        return 1.0 / (1.0 + exp(- x))

    @staticmethod
    def restrict_func_value(
        func_value: float, x: float, left: float, right: float,
        left_border: bool = False, right_border: bool = False):
        if (x > right or x < left
            or (x == right and right_border)
            or (x == left and left_border)):
            return 0.0
        else:
            return func_value

    @staticmethod
    def get_angle_by_dx_dy(dx: float, dy: float):
        from math import atan, pi
        if dx > 0.0:
            if dy > 0.0: return atan(abs(dy / dx))
            elif dy < 0.0: return - atan(abs(dy / dx))
            else: return 0.0
        elif dx < 0.0:
            if dy > 0.0: return pi - atan(abs(dy / dx))
            elif dy < 0.0: return - pi + atan(abs(dy / dx))
            else: return pi
        else:
            if dy > 0.0: return 0.5 * pi
            elif dy < 0.0: return -0.5 * pi
            else: return 0.0


class PromoCode(object):
    promo_codes = [("o27739521", 90, True),
                   ("o63116012", 50, True),
                   ("o86636403", 25, True),
                   ("o15260943", 10, False),
                   ("t72539756", 20, True),
                   ("s05050505", 50, True)]

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
        
