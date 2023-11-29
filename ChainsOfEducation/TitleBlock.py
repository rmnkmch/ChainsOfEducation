﻿import manim


c_1 = "1⃣"
c_2 = "2⃣"
c_3 = "3⃣"
c_4 = "4⃣"
c_5 = "5⃣"
c_6 = "6⃣"
c_7 = "7⃣"
c_8 = "8⃣"
c_9 = "9⃣"
c_0 = "0⃣"
c_off = "🏢"
c_cap = "🏛"
c_lang = "👅"
c_mon = "💰"


class TitleBlock(manim.RoundedRectangle):
    """None now, jpn, geo"""

    @staticmethod
    def resplit_to_post_geo(text: str):
        lines = text.split("\n")
        num_line = 0
        ln = ""
        rus = ""
        for line in lines:
            if num_line == 0:
                num_line = 1
                print("#Geography")
                rus = line.split("; ")
                ln = rus[0] + " - "
            elif num_line == 1:
                num_line = 2
                ln += line
                print(ln)
            elif num_line == 2:
                num_line = 3
                eng = line.split("; ")
                ln = c_off + " - "
                for word_num in range(len(eng)):
                    ln += rus[word_num] + " (" + eng[word_num] + ")"
                    if word_num < len(eng) - 1: ln += " / "
                print(ln)
            elif num_line == 3:
                num_line = 4
                wr = line.split("; ")
                print(c_cap + " - " + wr[0] + " (" + wr[1] + ")")
            elif num_line == 4:
                num_line = 5
                part = line.split("; ")
                ln = c_lang + " - " + part[0] + " (" + part[1] + ")"
                print(ln)
            elif num_line == 5:
                num_line = 0
                part = line.split("; ")
                lower = part[0][:5] + part[0][5].lower() + part[0][6:]
                ln = c_mon + " - " + lower + " (" + part[1] + ")"
                print(ln)

    @staticmethod
    def resplit_to_z_name_geo(text: str):
        lines = text.split("\n")
        num_line = 0
        num = 125
        for line in lines:
            if num_line == 2:
                num_line = 3
                eng = line.split("; ")
                print("#" + str(num) + " z_" + eng[0])
                num += 1
            elif num_line == 5: num_line = 0
            else: num_line += 1

    @staticmethod
    def resplit_to_post_examples(text: str):
        lines = text.split("\n")
        ln = ""
        for line in lines:
            if line[0].isnumeric():
                continue
            elif len(line) > 1 and line[0] == " ":
                parts = line.split()
                ln = parts[0] + " (" + parts[1] + ") - "
            elif not line[0].isupper():
                if ";" in line:
                    s = line.split("; ")
                    print(ln + ", ".join(s) + ".")
                else:
                    print(ln + line + ".")

    @staticmethod
    def resplit_to_post_kanji(text: str):
        lines = text.split("\n")
        ln = ""
        trlt = ""
        num = 271
        mod3 = 0
        for line in lines:
            if len(line) == 1:
                if mod3 % 3 == 0: print("#Japanese")
                ln = TitleBlock.num2sticker(num) + " " + line + " - "
                num += 1
                mod3 += 1
            elif len(line) > 1 and not line[0].isupper(): trlt = line
            elif line.startswith("Kun: "):
                kuns = line.removeprefix("Kun: ")
                kuns = kuns.split("、 ")
                for kun in kuns:
                    ln += kun
                    if kuns.index(kun) < len(kuns) - 1:
                        ln += ", "
            elif line.startswith("On: "):
                ons = line.removeprefix("On: ")
                ons = ons.split("、 ")
                ln += "; "
                for on in ons:
                    ln += on
                    if ons.index(on) < len(ons) - 1:
                        ln += ", "
                ln += " - " + trlt
                print(ln)

    @staticmethod
    def resplit_to_JP_read_kanji(text: str):
        lines = text.split("\n")
        ln = ""
        for line in lines:
            if len(line) == 1: ln = line + ",-. / "
            elif line.startswith("Kun: "):
                kuns = line.removeprefix("Kun: ")
                kuns = kuns.split("、 ")
                for kun in kuns:
                    ln += kun + ",-. "
            elif line.startswith("On: "):
                ons = line.removeprefix("On: ")
                ons = ons.split("、 ")
                ln += " / "
                for on in ons:
                    ln += on + ",-. "
                print(ln)

    @staticmethod
    def resplit_to_RU_read_kanji(text: str):
        lines = text.split("\n")
        ln = ""
        for line in lines:
            if len(line) > 1 and not line[0].isupper() and not line[0].isnumeric():
                words = line.split(", ")
                for word in words:
                    ln += word + ",-. "
                print(ln)
                ln = ""

    @staticmethod
    def resplit_to_menu_kanji(text: str):
        lines = text.split("\n")
        for line in lines:
            if len(line) == 1: print(line, end = " ")

    @staticmethod
    def num2sticker(num: int):
        dct: dict = {1: c_1, 2: c_2, 3: c_3, 4: c_4, 5: c_5,
                     6: c_6, 7: c_7, 8: c_8, 9: c_9, 0: c_0}
        st = ""
        while num > 0:
            st = dct[int(num % 10)] + st
            num = int(num / 10)
        return st

    @staticmethod
    def print_symbols(scene: manim.Scene, symbol: str):
        fonts = ['Sans', 'Malgun Gothic', 'Malgun Gothic Semilight',
                 'Microsoft JhengHei Light', 'Microsoft YaHei Light',
                 'UD Digi Kyokasho N-R', 'Yu Mincho Demibold', 'MS Mincho', 'Serif']
        rect = manim.Rectangle("#2a2a2a", 16.0, 16.0, fill_opacity = 1.0)
        size = 3.8
        line_color = "#4a4a4a"
        line1 = manim.Line(manim.UP * 1.5 * size + manim.RIGHT * - 0.5 * size,
                           manim.UP * - 1.5 * size + manim.RIGHT * - 0.5 * size,
                           stroke_color = line_color)
        line2 = manim.Line(manim.UP * 1.5 * size + manim.RIGHT * 0.5 * size,
                           manim.UP * - 1.5 * size + manim.RIGHT * 0.5 * size,
                           stroke_color = line_color)
        line3 = manim.Line(manim.UP * 0.5 * size + manim.RIGHT * - 1.5 * size,
                           manim.UP * 0.5 * size + manim.RIGHT * 1.5 * size,
                           stroke_color = line_color)
        line4 = manim.Line(manim.UP * - 0.5 * size + manim.RIGHT * - 1.5 * size,
                           manim.UP * - 0.5 * size + manim.RIGHT * 1.5 * size,
                           stroke_color = line_color)
        scene.add(rect, line1, line2, line3, line4)
        for i in range(len(fonts)):
            sym = manim.Text(
                symbol, font_size = 210.0, color = "#eaeaea", font = fonts[i]
                ).move_to(manim.UP * size * (1 - i // 3)
                          + manim.RIGHT * size * (1 - i % 3))
            scene.add(sym)
        scene.wait(0.1/6.0)
        scene.clear()

    @staticmethod
    def print_symbol(scene: manim.Scene, symbol: str):
        font = 'Microsoft YaHei Light'
        rect = manim.Rectangle("#2a2a2a", 16.0, 16.0, fill_opacity = 1.0)
        sym = manim.Text(symbol, font_size = 700.0, color = "#eaeaea", font = font)
        scene.add(rect, sym)
        scene.wait(0.1/6.0)
        scene.clear()

    @staticmethod
    def make_symbols(scene: manim.Scene):
        kanji = "向 君 味 命 和 品 員 商 問 坂 央 始 委 守 安 定 実 客 宮 宿 寒 対 局 屋 岸 島 州 帳 平 幸"
        for kj in kanji.split():
            TitleBlock.print_symbols(scene, kj)
        for kj in kanji.split():
            TitleBlock.print_symbol(scene, kj)

    @staticmethod
    def Jpn_Geo(scene: manim.Scene):
        # TitleBlock.make_symbols(scene)
        native_examples = """ 校長 	 こうちょう 
директор школы
33
 校服 	 こうふく 
школьная форма
19
 校庭 	 こうてい 
территория университета, колледжа
4
 日本語 	 にほんご 
японский язык (2 урок; 5 урок)
7
 本気 	 ほんき 
серьёзность
100
 評判が本当かどうか解らない 	 ひょうばんがほんとうかどうかわからない 
верны ли эти слухи или нет, не знаю;
7
 天文台 	 てんもんだい 
обсерватория
61
 非文明 	 ひぶんめい 
нецивилизованный
67
 三人寄れば文殊の知恵 	 さんにんよればもんじゅのちえ  
две головы лучше одной
7
 習字 	 しゅうじ 
каллиграфия
13
 太字 	 ふとじ 
жирный шрифт
53
 嘘字 	 うそじ 
неправильно написанный иероглиф;
5
 名所 	 めいしょ 
достопримечательность
51
 無名指 	  むめいし 
безымянный палец
103
 後世に名を残す 	 こうせいになをのこす 
прославить своё имя в веках
5
 大学生 	 だいがくせい 
студент
25
 地理学 	 ちりがく 
география
180
 化学的作用 	 かがくてきさよう 
химический процесс
13
 鼻先 	 はなさき 
кончик носа
61
 時代の先端を行く 	 じだいのせんたんをいく 
идти в ногу со временем;
62
 今の先 	 いまのさき 
только что
26
 歯が立たない 	 はがたたない 
быть не по зубам
49
 独立 	 どくりつ 
независимость
97
 条理の立った 	 じょうりのたった 
логичный, последовательный
5
 早期 	 そうき 
ранняя стадия
34
 大層早く 	 たいそうはやく 
очень рано;
17
 遅かれ早かれ 	 おそかれはやかれ 
рано или позно
5
 夏休み 	 なつやすみ 
летние каникулы
24
 年中無休 	 ねんじゅうむきゅう 
открытый круглый год; без выходных
22
 休みの日 	 休みのひ 
выходной день
6
 港町 	 みなとまち 
портовый город
2
 市町村 	 しちょうそん 
города, городки и деревни (как административные единицы)
4
 町長 	 ちょうちょう 
городской голова, правитель города, мэр
4
 村人 	 むらびと 
селянин; деревенский житель
13
 村雨 	 むらさめ 
короткий ливень
6
 村八分 	 むらはちぶ 
остракизм; изгнание
11
 王座 	 おうざ 
трон
24
 百獣の王 	 ひゃくじゅうのおう 
царь зверей, лев
3
 王子 	 おうじ 
принц
99
 亀の甲より年の効 	 かめのこうよりねんのこう 
мудрость приходит с годами (поговорка)
80
 年中行事 	 ねんじゅうぎょうじ 
ежегодное событие
86
 恭賀新年 	 きょうがしんねん 
с новым годом!
10
 救急車 	 きゅうきゅうしゃ 
машина скорой помощи
70
 駐車禁止 	 ちゅうしゃきんし 
стоянка запрещена
87
 無賃乗車 	 むちんじょうしゃ 
бесплатный проезд
6
 出入口 	 でいりぐち 
вход и выход
64
 入伸 	 にゅうしん 
дар, талант, мастерство, гений
104
 立入禁止 	 たちいりきんし 
Не входить!; Посторонним вход воспрещён!
7
 見出 	 みだし 
заголовок, указатель
14
 出来栄え 	 できばえ 
результат, эффект
36
 導き出す 	 みちびきだす 
приходить к выводу, докопаться до истины
20
 金科玉条 	 きんかぎょくじょう 
золотое правило; девиз
21
 善玉悪玉 	 ぜんだまあくだま 
добрые и злые, хорошие и дурные
25
 逸れ玉 	 それだま 
шальная пуля
9
 真空 	 しんくう 
вакуум; безвоздушное пространство; абсолютная пустота;
47
 関数空間 	 かんすうくうかん 
функциональное пространство
63
 航空港 	 こうくうこう 
аэропорт
13
 糸瓜 	 へちま 
тыква
1
 細い糸 	 ほそいいと 
тонкая нить
7
 綿糸 	 めんし 
хлопчатобумажная пряжа"""
        native_kun_on_2191_2220 = """"""
        native_kun_on_2161_2190 = """"""
        native_kun_on_2131_2160 = """"""
        native_kun_on_2101_2130 = """"""
        native_kun_on_2071_2100 = """"""
        native_kun_on_2041_2070 = """"""
        native_kun_on_2011_2040 = """"""
        native_kun_on_1981_2010 = """"""
        native_kun_on_1951_1980 = """"""
        native_kun_on_1921_1950 = """"""
        native_kun_on_1891_1920 = """"""
        native_kun_on_1861_1890 = """"""
        native_kun_on_1831_1860 = """"""
        native_kun_on_1801_1830 = """"""
        native_kun_on_1771_1800 = """"""
        native_kun_on_1741_1770 = """"""
        native_kun_on_1711_1740 = """"""
        native_kun_on_1681_1710 = """"""
        native_kun_on_1651_1680 = """"""
        native_kun_on_1621_1650 = """"""
        native_kun_on_1591_1620 = """"""
        native_kun_on_1561_1590 = """"""
        native_kun_on_1531_1560 = """"""
        native_kun_on_1501_1530 = """"""
        native_kun_on_1471_1500 = """"""
        native_kun_on_1441_1470 = """"""
        native_kun_on_1411_1440 = """"""
        native_kun_on_1381_1410 = """"""
        native_kun_on_1351_1380 = """"""
        native_kun_on_1321_1350 = """"""
        native_kun_on_1291_1320 = """"""
        native_kun_on_1261_1290 = """"""
        native_kun_on_1231_1260 = """"""
        native_kun_on_1201_1230 = """"""
        native_kun_on_1171_1200 = """"""
        native_kun_on_1141_1170 = """"""
        native_kun_on_1111_1140 = """"""
        native_kun_on_1081_1110 = """"""
        native_kun_on_1051_1080 = """"""
        native_kun_on_1021_1050 = """"""
        native_kun_on_991_1020 = """"""
        native_kun_on_961_990 = """"""
        native_kun_on_931_960 = """"""
        native_kun_on_901_930 = """"""
        native_kun_on_871_900 = """"""
        native_kun_on_841_870 = """"""
        native_kun_on_811_840 = """"""
        native_kun_on_781_810 = """"""
        native_kun_on_751_780 = """"""
        native_kun_on_721_750 = """"""
        native_kun_on_691_720 = """序
7 strokes
Radical: house on cliff 广
Parts: 一 亅 マ 子 广
предисловие, начало, порядок, приоритет, случай, случайность, кстати
Kun: つい.で、 ついで
On: ジョ
弁
5 strokes
Radical: two hands, twenty 廾
Parts: 厶 廾
Variants: 辨 辧 瓣 辯 辮
клапан, лепесток, коса, речь, диалект, дискриминация, утилизация, различать
Kun: かんむり、 わきま.える、 わ.ける、 はなびら、 あらそ.う
On: ベン、 ヘン
張
11 strokes
Radical: bow 弓
Parts: 弓 長
счетчик для луков и струнных инструментов, растяжка, раскладывание, поставленная (палатка)
Kun: は.る、 -は.り、 -ば.り
On: チョウ
往
8 strokes
Radical: step 彳
Parts: 丶 彳 王
Variants: 徃
путешествие, путешествовать, прогонять, отпустить, идти, раньше, раньше
Kun: い.く、 いにしえ、 さき.に、 ゆ.く
On: オウ
復
12 strokes
Radical: step 彳
Parts: 一 ノ 人 夂 彳 日 乞
восстановить, вернуться, возобновить
Kun: また
On: フク
徳
14 strokes
Radical: step 彳
Parts: 十 彳 心 買
Variants: 悳 德
этика, нравственность, добродетель
On: トク
志
7 strokes
Radical: heart 心 (忄, ⺗)
Parts: 士 心
намерение, план, разрешать, стремиться, мотив, надежды, шиллинг
Kun: シリング、 こころざ.す、 こころざし
On: シ
応
7 strokes
Radical: heart 心 (忄, ⺗)
Parts: 广 心
Variants: 應
отвчать, да, реагирование
Kun: あた.る、 まさに、 こた.える
On: オウ、 ヨウ、 -ノウ
快
7 strokes
Radical: heart 心 (忄, ⺗)
Parts: 二 人 ユ 大 忙
веселый, приятный, приятный, удобный
Kun: こころよ.い
On: カイ
性
8 strokes
Radical: heart 心 (忄, ⺗)
Parts: 忙 生
пол, природа
Kun: さが
On: セイ、 ショウ
恩
10 strokes
Radical: heart 心 (忄, ⺗)
Parts: 囗 大 心
Variants:
благодать, доброта, благосклонность, милосердие, благословение, выгода
On: オン
情
11 strokes
Radical: heart 心 (忄, ⺗)
Parts: 二 亠 土 忙 月 青
чувства, эмоции, страсть, симпатия, обстоятельства, факты
Kun: なさ.け
On: ジョウ、 セイ
態
14 strokes
Radical: heart 心 (忄, ⺗)
Parts: 匕 厶 心 月
отношение, состояние, фигура, внешний вид
Kun: わざ.と
On: タイ
慣
14 strokes
Radical: heart 心 (忄, ⺗)
Parts: ハ 忙 毋 目 母 貝
Variants:
привык, привыкай, становись опытным
Kun: な.れる、 な.らす
On: カン
承
8 strokes
Radical: hand 手 (扌龵)
Parts: ノ 亅 二 手
Variants:
уступать, слышать, слушать, быть в курсе, получать
Kun: うけたまわ.る、 う.ける
On: ショウ、 ジョウ
技
7 strokes
Radical: hand 手 (扌龵)
Parts: 十 又 扎 支
Variants:
умение, искусство, ремесло, способности, подвиг, перформанс, призвание
Kun: わざ
On: ギ
招
8 strokes
Radical: hand 手 (扌龵)
Parts: 刀 口 扎
манить, приглашать, вызывать, заниматься
Kun: まね.く
On: ショウ
授
11 strokes
Radical: hand 手 (扌龵)
Parts: 冖 又 扎 爪
давать
Kun: さず.ける、 さず.かる
On: ジュ
採
11 strokes
Radical: hand 手 (扌龵)
Parts: 扎 木 爪
Variants:
брать
Kun: と.る
On: サイ
接
11 strokes
Radical: hand 手 (扌龵)
Parts: 女 扎 立
Variants: 擑
прикосновение, контакт, примыкание, кусок воедино
Kun: つ.ぐ
On: セツ、 ショウ
提
12 strokes
Radical: hand 手 (扌龵)
Parts: 扎 日 疋
предлагать, брать с собой, носить с собой в руки
Kun: さ.げる
On: テイ、 チョウ、 ダイ
損
13 strokes
Radical: hand 手 (扌龵)
Parts: ハ 口 扎 目 貝
повреждение, потеря, невыгодность, ранить, повредить
Kun: そこ.なう、 そこな.う、 -そこ.なう、 そこ.ねる、 -そこ.ねる
On: ソン
支
4 strokes
Radical: branch 支
Parts: 十 又 支
ветвь, поддержка, сустейн
Kun: ささ.える、 つか.える、 か.う
On: シ
政
9 strokes
Radical: rap 攴 (攵)
Parts: 一 止 乞 攵
политика, правительство
Kun: まつりごと、 まん
On: セイ、 ショウ
故
9 strokes
Radical: rap 攴 (攵)
Parts: 十 口 乞 攵
случайность, особенно намеренно, разум, причина, обстоятельства, поздняя, поэтому, следовательно
Kun: ゆえ、 ふる.い、 もと
On: コ
敵
15 strokes
Radical: rap 攴 (攵)
Parts: 亠 并 冂 十 口 立 滴 乞 攵
враг, противник
Kun: かたき、 あだ、 かな.う
On: テキ
断
11 strokes
Radical: axe 斤
Parts: 一 ｜ 斤 米
Variants: 斷
выходное пособие, отказываться, отказывать, извиняться, предостерегать, увольнять, запрещать, решение, судебное решение, сокращение
Kun: た.つ、 ことわ.る、 さだ.める
On: ダン
旧
5 strokes
Radical: sun, day 日
Parts: ｜ 日
Variants: 舊
старые времена, старые вещи, старый друг, бывший
Kun: ふる.い、 もと
On: キュウ
易
8 strokes
Radical: sun, day 日
Parts: ノ 勹 日 勿
Легко, готово, просто, гадания
Kun: やさ.しい、 やす.い
On: エキ、 イ
暴
15 strokes
Radical: sun, day 日
Parts: 一 ｜ 二 ハ 日 水 井
вспышка, рейв, лад, сила, насилие, жестокость, возмущение
Kun: あば.く、 あば.れる
On: ボウ、 バク"""
        native_kun_on_661_690 = """効
8 strokes
Radical: power, force 力
Parts: 亠 力 父
Variants: 效
эффект, достоинство, действенность, результативность, выгода
Kun: き.く、 ききめ、 なら.う
On: コウ
務
11 strokes
Radical: power, force 力
Parts: 力 矛 攵
задача, обязанности
Kun: つと.める
On: ム
勢
13 strokes
Radical: power, force 力
Parts: 丶 儿 力 九 土
силы, энергия, военная мощь
Kun: いきお.い、 はずみ
On: セイ、 ゼイ
厚
9 strokes
Radical: cliff 厂
Parts: 厂 子 日
Variants: 垕
толстый, тяжелый, богатый, добрый, сердечный, наглый, бесстыдный
Kun: あつ.い、 あか
On: コウ
句
5 strokes
Radical: mouth, opening 口
Parts: 勹 口
фраза, клаузула, предложение, отрывок, абзац, счетчик для хайку
On: ク
可
5 strokes
Radical: mouth, opening 口
Parts: 一 亅 口
одобрять, могу, сносно, не должен, не следует, не делай
Kun: -べ.き、 -べ.し
On: カ、 コク
営
12 strokes
Radical: mouth, opening 口
Parts: ノ 冖 口 尚
Variants: 營
разбивать лагерь, выступать, строить, вести (бизнес)
Kun: いとな.む、 いとな.み
On: エイ
因
6 strokes
Radical: enclosure 囗
Parts: 囗 大
Variants: 囙
причина, фактор, быть связанным с, зависеть от, ограничиваться
Kun: よ.る、 ちな.む
On: イン
団
6 strokes
Radical: enclosure 囗
Parts: 囗 寸
Variants: 團
группа, ассоциация
Kun: かたまり、 まる.い
On: ダン、 トン
圧
5 strokes
Radical: earth 土
Parts: 厂 土
Variants: 壓
давить, давить, подавлять, угнетать, доминировать
Kun: お.す、 へ.す、 おさ.える、 お.さえる
On: アツ、 エン、 オウ
在
6 strokes
Radical: earth 土
Parts: 一 ｜ ノ 土
существуют окраины, пригороды, расположенные в
Kun: あ.る
On: ザイ
均
7 strokes
Radical: earth 土
Parts: 二 冫 勹 土
уровень, средний
Kun: なら.す
On: キン
基
11 strokes
Radical: earth 土
Parts: 一 ハ 土 甘
основы, радикал (химия), счетчик для машин, фундамент
Kun: もと、 もとい
On: キ
報
12 strokes
Radical: earth 土
Parts: 亠 十 卩 又 土 立 辛
отчет, новости, награда, возмездие
Kun: むく.いる
On: ホウ
境
14 strokes
Radical: earth 土
Parts: 儿 土 日 立 音
граница, приграничье, регион
Kun: さかい
On: キョウ、 ケイ
墓
13 strokes
Radical: earth 土
Parts: 土 大 艾 日
могила, надгробие
Kun: はか
On: ボ
増
14 strokes
Radical: earth 土
Parts: 并 土 日 田
увеличивать, добавлять, приумножать, завоевывать, продвигать
Kun: ま.す、 ま.し、 ふ.える、 ふ.やす
On: ゾウ
夢
13 strokes
Radical: evening, sunset 夕
Parts: 冖 夕 艾 買
Variants: 梦 夣
сон, видение, иллюзия
Kun: ゆめ、 ゆめ.みる、 くら.い
On: ム、 ボウ
妻
8 strokes
Radical: woman, female 女
Parts: 一 ｜ 女 ヨ
жена, супруг
Kun: つま
On: サイ
婦
11 strokes
Radical: woman, female 女
Parts: 冖 女 巾 ヨ
леди, женщина, жена, невеста
Kun: よめ
On: フ
容
10 strokes
Radical: roof 宀
Parts: 个 ハ 口 宀 穴 谷
содержать, формировать, выглядеть
Kun: い.れる
On: ヨウ
寄
11 strokes
Radical: roof 宀
Parts: 一 亅 口 大 宀
приблизиться, остановиться, приблизить, собрать, коллекционировать, отправить, переслать вперед
Kun: よ.る、 -よ.り、 よ.せる
On: キ
富
12 strokes
Radical: roof 宀
Parts: 一 口 宀 田
Variants: 冨
богатство, обогащение, изобилие
Kun: と.む、 とみ
On: フ、 フウ
導
15 strokes
Radical: thumb, inch 寸
Parts: 并 込 寸 自 首
руководство, ведущий, дирижер, привратник
Kun: みちび.く
On: ドウ
居
8 strokes
Radical: corpse 尸
Parts: 十 口 尸
Variants: 凥
проживать, быть, существовать, жить с
Kun: い.る、 -い、 お.る
On: キョ、 コ
属
12 strokes
Radical: corpse 尸
Parts: ノ 尸 禹
Variants: 屬
принадлежность, род, подчиненное должностное лицо, аффилированный
Kun: さかん、 つく、 やから
On: ゾク、 ショク
布
5 strokes
Radical: turban, scarf 巾
Parts: 一 ノ 巾
лен, ткань, расстилать, распределять
Kun: ぬの、 し.く、 きれ
On: フ、 ホ
師
10 strokes
Radical: turban, scarf 巾
Parts: 一 ｜ 口 巾
эксперт, учитель, мастер, модель, образец для подражания, армия (вкл. счетчик), война
Kun: いくさ
On: シ
常
11 strokes
Radical: turban, scarf 巾
Parts: 冖 口 尚 巾
обычный, ординарный, нормальный, распространенный, регулярный, постоянно, всегда, продолжительный
Kun: つね、 とこ-
On: ジョウ
幹
13 strokes
Radical: pestle 干
Parts: 个 十 干 日
Variants: 榦
ствол дерева, основная часть, талант, способности
Kun: みき
On: カン"""
        native_kun_on_631_660 = """陸
11 strokes
Radical: mound, dam (阝 left) 阜 (阝)
Parts: 儿 土 阡
земля, шесть
Kun: おか
On: リク、 ロク
隊
12 strokes
Radical: mound, dam (阝 left) 阜 (阝)
Parts: 并 阡 豕
полк, партия, рота, отделение
On: タイ
静
14 strokes
Radical: blue 青 (靑)
Parts: 亅 二 亠 勹 土 ヨ 月 青
Variants: 靜
тихий
Kun: しず-、 しず.か、 しず.まる、 しず.める
On: セイ、 ジョウ
順
12 strokes
Radical: leaf 頁
Parts: ハ 川 目 貝 頁
подчиняться, приказывать, поворачиваться, направо, покорность, случай
On: ジュン
願
19 strokes
Radical: leaf 頁
Parts: ハ 厂 小 白 目 貝 頁
прошение, просьба, обет, желание
Kun: ねが.う、 -ねがい
On: ガン
類
18 strokes
Radical: leaf 頁
Parts: ハ 大 目 米 貝 頁
сорт, разновидность, разновидность, класс, род
Kun: たぐ.い
On: ルイ
飛
9 strokes
Radical: fly 飛
Parts: 飛
летать, пропускать (страницы), разбрасываться
Kun: と.ぶ、 と.ばす、 -と.ばす
On: ヒ
飯
12 strokes
Radical: eat, food 食 (飠)
Parts: 厂 又 食
блюдо из отварного риса
Kun: めし
On: ハン
養
15 strokes
Radical: eat, food 食 (飠)
Parts: 并 王 羊 食
Variants: 羪
опекать, воспитывать, растить, развивать, лелеять
Kun: やしな.う
On: ヨウ、 リョウ
験
18 strokes
Radical: horse 馬
Parts: 人 个 口 杰 馬
Variants: 驗 騐
проверка, эффект, тестирование
Kun: あかし、 しるし、 ため.す、 ためし
On: ケン、 ゲン
久
3 strokes
Radical: slash 丿
Parts: 入 ノ 久
давняя, старая история
Kun: ひさ.しい
On: キュウ、 ク
仏
4 strokes
Radical: man, human 人 (亻)
Parts: 化 厶
Variants: 佛
Будда, мертвый, Франция
Kun: ほとけ
On: ブツ、 フツ
仮
6 strokes
Radical: man, human 人 (亻)
Parts: 化 厂 又
Variants: 假
фиктивный, временный, промежуточный, вымышленный (имя), неофициальный
Kun: かり、 かり-
On: カ、 ケ
件
6 strokes
Radical: man, human 人 (亻)
Parts: 化 牛
дело, кейс, материя, предмет
Kun: くだん
On: ケン
任
6 strokes
Radical: man, human 人 (亻)
Parts: ノ 化 士 王
ответственность, долг, срок, поручать, назначать
Kun: まか.せる、 まか.す
On: ニン
似
7 strokes
Radical: man, human 人 (亻)
Parts: 丶 人 化
Variants: 佀
становиться, походить, подделывать, имитировать, подходить
Kun: に.る、 ひ.る
On: ジ
余
7 strokes
Radical: man, human 人 (亻)
Parts: 一 亅 二 个 ハ 小 示
Variants: 餘
слишком много, я сам, излишек, другой, остаток
Kun: あま.る、 あま.り、 あま.す、 あんま.り
On: ヨ
価
8 strokes
Radical: man, human 人 (亻)
Parts: 化 西
Variants: 價
ценность, цена
Kun: あたい
On: カ、 ケ
保
9 strokes
Radical: man, human 人 (亻)
Parts: 化 口 木
защищать, гарантировать, оберегать, сберегать, поддерживать, опора
Kun: たも.つ
On: ホ、 ホウ
修
10 strokes
Radical: man, human 人 (亻)
Parts: ｜ 化 彡 乞 攵
Variants: 俢
дисциплинировать, хорошо себя вести, учиться, овладевать
Kun: おさ.める、 おさ.まる
On: シュウ、 シュ
俵
10 strokes
Radical: man, human 人 (亻)
Parts: 二 亠 化 土 士 衣
сумка, тюк, мешковина, прилавок для мешков
Kun: たわら
On: ヒョウ
個
10 strokes
Radical: man, human 人 (亻)
Parts: 化 十 口 囗
Variants:
индивидуальный прилавок для товаров
On: コ、 カ
備
12 strokes
Radical: man, human 人 (亻)
Parts: 化 厂 艾 用
Variants: 僃
оснащение, обеспечение, подготовка
Kun: そな.える、 そな.わる、 つぶさ.に
On: ビ
備
12 strokes
Radical: man, human 人 (亻)
Parts: 化 厂 艾 用
Variants: 僃
оснащение, обеспечение, подготовка
Kun: そな.える、 そな.わる、 つぶさ.に
On: ビ
再
6 strokes
Radical: open country 冂
Parts: 一 ｜ 冂 王
снова, дважды, во второй раз
Kun: ふたた.び
On: サイ、 サ
刊
5 strokes
Radical: knife, sword 刀 (刂)
Parts: 刈 干
публиковать, вырезать, гравировать
On: カン
判
7 strokes
Radical: knife, sword 刀 (刂)
Parts: ｜ 二 并 刈 十
решение суда, судебное решение, подпись, штамп, печать
Kun: わか.る
On: ハン、 バン
制
8 strokes
Radical: knife, sword 刀 (刂)
Parts: ノ 二 刈 巾 牛
система, закон, правило
On: セイ
券
8 strokes
Radical: knife, sword 刀 (刂)
Parts: 一 二 人 并 刀 大
билет
On: ケン
則
9 strokes
Radical: knife, sword 刀 (刂)
Parts: ハ 刈 目 貝
правило, закон, следовать, на основе, по образцу
Kun: のっと.る、 のり、 すなわち
On: ソク"""
        native_kun_on_601_630 = """芽
8 strokes
Radical: grass 艸 (艹)
Parts: 艾 牙
почка, росток, острие, зародыш
Kun: め
On: ガ
英
8 strokes
Radical: grass 艸 (艹)
Parts: ノ 冖 大 艾
Variants: 偀
Англия, английский, герой, выдающийся
Kun: はなぶさ
On: エイ
菜
11 strokes
Radical: grass 艸 (艹)
Parts: 艾 木 爪
овощ, гарнир, зелень
Kun: な
On: サイ
街
12 strokes
Radical: go, do 行
Parts: 土 彳 行
бульвар, улица, город
Kun: まち
On: ガイ、 カイ
衣
6 strokes
Radical: clothes 衣 (衤)
Parts: 亠 衣
предмет одежды, одежда для переодевания
Kun: ころも、 きぬ、 -ぎ
On: イ、 エ
要
9 strokes
Radical: west 西 (襾, 覀)
Parts: 女 西
потребность, главный момент, суть, стержень, ключ к
Kun: い.る、 かなめ
On: ヨウ
覚
12 strokes
Radical: see 見
Parts: 冖 尚 見
Variants: 覺 覐
запоминай, учись, запоминай, просыпайся, протрезвевай
Kun: おぼ.える、 さ.ます、 さ.める、 さと.る
On: カク
観
18 strokes
Radical: see 見
Parts: 矢 見 隹 乞
Variants: 觀
внешний вид, состояние, вид
Kun: み.る、 しめ.す
On: カン
訓
10 strokes
Radical: speech 言 (訁)
Parts: 川 言
инструкция, чтение японских иероглифов, объяснение, читать
Kun: おし.える、 よ.む、 くん.ずる
On: クン、 キン
試
13 strokes
Radical: speech 言 (訁)
Parts: 工 弋 言
проверять, пробовать, покушаться, экспериментировать, суровое испытание
Kun: こころ.みる、 ため.す
On: シ
説
14 strokes
Radical: speech 言 (訁)
Parts: 儿 并 口 言
мнение, теория, объяснение, слух
Kun: と.く
On: セツ、 ゼイ
課
15 strokes
Radical: speech 言 (訁)
Parts: 木 田 言
глава, урок, раздел, кафедра, деление, счетчик глав 
On: カ
議
20 strokes
Radical: speech 言 (訁)
Parts: 一 亅 并 手 戈 王 羊 言
обсуждение, консультация, прения, рассмотрение
On: ギ
象
12 strokes
Radical: pig 豕
Parts: 一 勹 口 豕
слон, образец после, подражать, образ, форма
Kun: かたど.る
On: ショウ、 ゾウ
貨
11 strokes
Radical: shell 貝
Parts: 化 ハ 匕 目 貝
фрахт, товары, имущество
Kun: たから
On: カ
貯
12 strokes
Radical: shell 貝
Parts: 一 亅 ハ 宀 目 貝
сберегать, хранить, откладывать, беречь, носить усы
Kun: た.める、 たくわ.える
On: チョ
費
12 strokes
Radical: shell 貝
Parts: ｜ ハ 弓 目 貝
расход, себестоимость, тратить, потребитель, отходы
Kun: つい.やす、 つい.える
On: ヒ
賞
15 strokes
Radical: shell 貝
Parts: ハ 冖 口 尚 目 貝
приз, награда, похвала
Kun: ほ.める
On: ショウ
軍
9 strokes
Radical: cart, car 車
Parts: 冖 車
армия, сила, войска, война, сражение
Kun: いくさ
On: グン
輪
15 strokes
Radical: cart, car 車
Parts: 一 ｜ 个 廾 冊 車
колесо, кольцо, окружность, звено, петля
Kun: わ
On: リン
辞
13 strokes
Radical: bitter 辛
Parts: 十 口 立 舌 辛
Variants: 辭 辝 辤
уйти в отставку, слово, термин, выражение
Kun: や.める、 いな.む
On: ジ
辺
5 strokes (also 4)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 刀 込
Variants: 邊 邉
окрестности, граница, приграничье
Kun: あた.り、 ほと.り、 -べ
On: ヘン
連
10 strokes (also 9)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 込 車
бери с собой, веди за собой, присоединяйся, соединяйся, вечеринка, банда, клика
Kun: つら.なる、 つら.ねる、 つ.れる、 -づ.れ
On: レン
達
12 strokes (also 11)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 并 込 土 王 羊
Variants: 逹
свершенный, достигающий, прибывающий, постигающий
Kun: -たち
On: タツ、 ダ
選
15 strokes (also 14)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: ｜ 二 ハ 込 已
избирать, отбирать, выбирать, предпочитать
Kun: えら.ぶ、 え.る、 よ.る
On: セン
郡
10 strokes (also 9)
Radical: town (阝 right) 邑 (阝)
Parts: 一 ノ 口 ヨ 邦
округ, дистрикт
Kun: こおり
On: グン
量
12 strokes
Radical: village, mile 里
Parts: 一 日 里
количество, мера, вес, количество, рассматривать, оценивать, предполагать
Kun: はか.る
On: リョウ
録
16 strokes
Radical: metal, gold 金 (釒)
Parts: ヨ 水 金 隶
рекорд
Kun: しる.す、 と.る
On: ロク
鏡
19 strokes
Radical: metal, gold 金 (釒)
Parts: 儿 日 立 金 音
Variants: 獍
зеркало, отражатель, бочкообразная головка, круглая рисовая лепешка
Kun: かがみ
On: キョウ、 ケイ
関
14 strokes
Radical: gate 門
Parts: 一 二 人 ハ 并 大 門
Variants: 關
соединение, барьер, шлюз, вовлекать, касающийся
Kun: せき、 -ぜき、 かか.わる、 からくり、 かんぬき
On: カン"""
        native_kun_on_571_600 = """照
13 strokes
Radical: fire 火 (灬)
Parts: 刀 口 日 杰
Variants: 曌 瞾
освещать, сиять, сравнивать, застенчивый
Kun: て.る、 て.らす、 て.れる
On: ショウ
熱
15 strokes
Radical: fire 火 (灬)
Parts: 丶 儿 九 土 杰
жар, температура, лихорадка, мания, страсть
Kun: あつ.い
On: ネツ
牧
8 strokes
Radical: cow 牛 (牜)
Parts: 牛 乞 攵
разводить, ухаживать, пасти, кормить, выпасать
Kun: まき
On: ボク
特
10 strokes
Radical: cow 牛 (牜)
Parts: 土 寸 牛
особый
On: トク
産
11 strokes
Radical: life 生
Parts: ノ 亠 并 厂 生 立
продукты, выносить, рожать, приносить доход, роды, родной, собственность
Kun: う.む、 う.まれる、 うぶ-、 む.す
On: サン
的
8 strokes
Radical: white 白
Parts: 丶 勹 白
яблочко, метка, мишень, объект, окончание прилагательного
Kun: まと
On: テキ
省
9 strokes
Radical: eye 目
Parts: ノ 小 目
государственное служение, сохранить, опустить
Kun: かえり.みる、 はぶ.く
On: セイ、 ショウ
祝
9 strokes
Radical: sign 示 (礻)
Parts: 儿 口 礼
празднуйте, поздравляйте
Kun: いわ.う
On: シュク、 シュウ
票
11 strokes
Radical: sign 示 (礻)
Parts: 二 小 示 西
избирательный бюллетень, этикетка, билет, вывеска
On: ヒョウ
種
14 strokes
Radical: grain 禾
Parts: ｜ ノ 日 禾 里
вид, разновидность, класс
Kun: たね、 -ぐさ
On: シュ
積
16 strokes
Radical: grain 禾
Parts: 二 亠 ハ 土 目 禾 貝
объем, площадь, содержимое, складывать, накапливать
Kun: つ.む、 -づ.み、 つ.もる、 つ.もり
On: セキ
競
20 strokes
Radical: stand, erect 立
Parts: 儿 口 立
подражать, соревноваться, предлагать цену, продавать на аукционе, бое, состязании, гонке
Kun: きそ.う、 せ.る、 くら.べる
On: キョウ、 ケイ
笑
10 strokes
Radical: bamboo 竹 (⺮)
Parts: 大 禾 竹 乞
смеяться
Kun: わら.う、 え.む
On: ショウ
管
14 strokes
Radical: bamboo 竹 (⺮)
Parts: ｜ 口 宀 竹 乞
труба, тубус, духовой инструмент, пьяные разговоры, контроль, юрисдикция
Kun: くだ
On: カン
節
13 strokes
Radical: bamboo 竹 (⺮)
Parts: 卩 竹 艮 乞
узел, время года, период, повод, стих, предложение, строфа
Kun: ふし、 -ぶし、 のっと
On: セツ、 セチ
粉
10 strokes
Radical: rice 米
Parts: ハ 并 刀 米
мука, порошок, пыль
Kun: デシメートル、 こ、 こな
On: フン
紀
9 strokes
Radical: silk 糸 (糹)
Parts: 小 已 幺 糸
хроника, отчет, повествование, история
On: キ
約
9 strokes
Radical: silk 糸 (糹)
Parts: 丶 勹 小 幺 糸
обещать, примерно, сжаться
Kun: つづ.まる、 つづ.める、 つづま.やか
On: ヤク
結
12 strokes
Radical: silk 糸 (糹)
Parts: 口 士 小 幺 糸
завязывать, связывать, сжимать, соединять, организовывать, делать прическу, закреплять
Kun: むす.ぶ、 ゆ.う、 ゆ.わえる
On: ケツ、 ケチ
給
12 strokes
Radical: silk 糸 (糹)
Parts: 一 个 口 小 幺 糸
зарплата, оклад, подарок, позволять, даровать, одаривать
Kun: たま.う、 たも.う、 -たま.え
On: キュウ
続
13 strokes
Radical: silk 糸 (糹)
Parts: 儿 冖 士 小 幺 糸
Variants: 續 賡
продолжение, сериал, сиквел
Kun: つづ.く、 つづ.ける、 つぐ.ない
On: ゾク、 ショク、 コウ、 キョウ
置
13 strokes
Radical: net 网 (罒, ⺲, 罓, ⺳)
Parts: 一 ｜ 十 目 買
размещение, класть, комплектовать, депонировать, оставлять после себя, хранить, нанимать на работу, закладывать
Kun: お.く、 -お.き
On: チ
老
6 strokes
Radical: old 老 (耂)
Parts: 匕 老
старик, старость, стареть
Kun: お.いる、 ふ.ける
On: ロウ
胃
9 strokes
Radical: meat 肉 (⺼)
Parts: 月 田
желудок, брюшко, зоб, зобок
On: イ
脈
10 strokes
Radical: meat 肉 (⺼)
Parts: 厂 斤 月
Variants: 脉
вена, пульс, надежда
Kun: すじ
On: ミャク
腸
13 strokes
Radical: meat 肉 (⺼)
Parts: 一 日 月 勿
Variants: 膓
кишки, потроха, недра, внутренности
Kun: はらわた、 わた
On: チョウ
臣
7 strokes
Radical: minster, official 臣
Parts: 匚 臣
фиксатор, подлежащий
On: シン、 ジン
航
10 strokes
Radical: boat 舟
Parts: 亠 几 舟
ориентироваться, плыть под парусом, совершать круиз, летать
On: コウ
良
7 strokes
Radical: stopping 艮
Parts: 艮
хороший, приятный, умелый
Kun: よ.い、 -よ.い、 い.い、 -い.い
On: リョウ
芸
7 strokes
Radical: grass 艸 (艹)
Parts: 二 厶 艾
Variants: 藝 秇
техника, искусство, ремесло, перформанс, актерская игра, трюк, каскадерша
Kun: う.える、 のり、 わざ
On: ゲイ、 ウン"""
        native_kun_on_541_570 = """束
7 strokes
Radical: tree 木
Parts: 一 ｜ ハ 口 木
связывать, сноп, стопка, связывать в пучки, управлять, управляешь, контролируешь
Kun: たば、 たば.ねる、 つか、 つか.ねる
On: ソク
松
8 strokes
Radical: tree 木
Parts: ハ 厶 木
Variants: 枩 柗 梥
сосна
Kun: まつ
On: ショウ
果
8 strokes
Radical: tree 木
Parts: ｜ 木 田
плодоносить, вознаграждать, осуществлять, достигать, завершать, заканчивать, заканчивать успешно
Kun: は.たす、 はた.す、 -は.たす、 は.てる、 -は.てる、 は.て
On: カ
栄
9 strokes
Radical: tree 木
Parts: 冖 尚 木
Variants: 榮
расцвет, процветание, честь, слава, великолепие
Kun: さか.える、 は.え、 -ば.え、 は.える、 え
On: エイ、 ヨウ
案
10 strokes
Radical: tree 木
Parts: 女 宀 木
план, предложение, черновик, обдумывание, страх, пропозиция, идея, ожидание, беспокойство, стол, скамья
Kun: つくえ
On: アン
梅
10 strokes
Radical: tree 木
Parts: 木 毋 母 乞
Variants: 楳 槑 梅
слива
Kun: うめ
On: バイ
械
11 strokes
Radical: tree 木
Parts: 廾 戈 木
механизм, хитроумное устройство, оковы, машина, инструмент
Kun: かせ
On: カイ
極
12 strokes (also 13)
Radical: tree 木
Parts: 一 又 口 木
столбы, поселение, заключение, конец, наивысший ранг, электрические столбы, очень, чрезвычайно
Kun: きわ.める、 きわ.まる、 きわ.まり、 きわ.み、 き.める、 -ぎ.め、 き.まる
On: キョク、 ゴク
標
15 strokes
Radical: tree 木
Parts: 二 小 木 示 西
указатель, печать, клеймо, штемпель, оттиск, символ, эмблема, товарный знак, улика, сувенир, мишень
Kun: しるべ、 しるし
On: ヒョウ
機
16 strokes
Radical: tree 木
Parts: 丶 ノ 幺 戈 木
ткацкий станок, механизм, машина, самолет, возможность, мощь, действенность, случай
Kun: はた
On: キ
欠
4 strokes
Radical: lack, yawn 欠
Parts: 人 勹 欠
Variants: 缺 缼
недостаток, пробел, неудача
Kun: か.ける、 か.く
On: ケツ、 ケン
歴
14 strokes
Radical: stop 止
Parts: 厂 广 木 止 麻
учебный план, продолжение, течение времени
On: レキ、 レッキ
残
10 strokes
Radical: death, decay 歹 (歺)
Parts: 二 戈 歹
Variants: 殘
остаток, пережиток, баланс
Kun: のこ.る、 のこ.す、 そこな.う、 のこ.り
On: ザン、 サン
殺
10 strokes
Radical: weapon, lance 殳
Parts: 丶 ノ 几 又 木 殳
Variants: 煞
убивать, умерщвлять, разделывать, отрезать, расщеплять, уменьшать, редуцировать, портить
Kun: ころ.す、 -ごろ.し、 そ.ぐ、 あや.める
On: サツ、 サイ、 セツ
毒
8 strokes
Radical: mother, do not 毋 (母, ⺟)
Parts: 二 亠 土 毋 母
яд, вирус, ядовитость, микроб, вред, увечье, злоба
On: ドク
氏
4 strokes
Radical: clan 氏
Parts: 氏
семейное имя, фамилия, клан
Kun: うじ、 -うじ
On: シ
民
5 strokes
Radical: clan 氏
Parts: 口 尸 氏
люди, нация, подданные
Kun: たみ
On: ミン
求
7 strokes
Radical: water 水 (氵, 氺)
Parts: 一 丶 水
просить, хотеть, желать чего-либо, требовать, востребованность
Kun: もと.める
On: キュウ、 グ
治
8 strokes
Radical: water 水 (氵, 氺)
Parts: 厶 口 汁
царствуй, будь в мире, успокойся, подчиняй, усмиряй, управляй, лечи, исцели, правь, сохраняй
Kun: おさ.める、 おさ.まる、 なお.る、 なお.す
On: ジ、 チ
法
8 strokes
Radical: water 水 (氵, 氺)
Parts: 厶 土 汁
Variants: 佱 灋
метод, закон, правило, принцип, модель, система
Kun: のり
On: ホウ、 ハッ、 ホッ、 フラン
泣
8 strokes
Radical: water 水 (氵, 氺)
Parts: 汁 立
плакать, рыдать
Kun: な.く
On: キュウ
浅
9 strokes
Radical: water 水 (氵, 氺)
Parts: 二 汁 戈
Variants: 淺
мелкий, поверхностный, легкомысленный, жалкий, постыдный
Kun: あさ.い
On: セン
浴
10 strokes
Radical: water 水 (氵, 氺)
Parts: 个 ハ 口 汁 谷
купаться, быть любимым, нежиться в
Kun: あ.びる、 あ.びせる
On: ヨク
清
11 strokes
Radical: water 水 (氵, 氺)
Parts: 二 亠 土 汁 月 青
очищать, расчищать
Kun: きよ.い、 きよ.まる、 きよ.める
On: セイ、 ショウ、 シン
満
12 strokes
Radical: water 水 (氵, 氺)
Parts: 一 ｜ 二 冂 山 汁 艾
Variants: 滿
полный, наполненность, достаточное количество, удовлетворяющий
Kun: み.ちる、 み.つ、 み.たす
On: マン、 バン
漁
14 strokes
Radical: water 水 (氵, 氺)
Parts: 汁 杰 田 魚
рыбалка, рыболовный промысел
Kun: あさ.る
On: ギョ、 リョウ
灯
6 strokes
Radical: fire 火 (灬)
Parts: 一 亅 火
Variants: 燈
лампа, светильник, подсветка, счетчик для ламп
Kun: ひ、 ほ-、 ともしび、 とも.す、 あかり
On: トウ
無
12 strokes
Radical: fire 火 (灬)
Parts: 一 ｜ ノ 杰 無 乞
ничто, никто, не существует, ничего, ноль, не
Kun: な.い
On: ム、 ブ
然
12 strokes
Radical: fire 火 (灬)
Parts: 夕 杰 犬
что-то в этом роде, так что, если это так, в таком случае, что ж
Kun: しか、 しか.り、 しか.し、 さ
On: ゼン、 ネン
焼
12 strokes
Radical: fire 火 (灬)
Parts: 儿 十 火
Variants: 燒
запекать, обжигать
Kun: や.く、 や.き、 や.き-、 -や.き、 や.ける
On: ショウ"""
        native_kun_on_511_540 = """席
10 strokes
Radical: turban, scarf 巾
Parts: 一 巾 广 凵
сиденье, коврик, повод, место
Kun: むしろ
On: セキ
帯
10 strokes
Radical: turban, scarf 巾
Parts: 一 ｜ 冖 巾
Variants: 帶
кушак, пояс, оби, зона, регион
Kun: お.びる、 おび
On: タイ
底
8 strokes
Radical: house on cliff 广
Parts: 广 氏
дно, подошва, глубина, нижняя цена, основа, вид, сортировка
Kun: そこ
On: テイ
府
8 strokes
Radical: house on cliff 广
Parts: 化 寸 广
район, городская префектура, правительственный офис, представительный орган, склад
On: フ
康
11 strokes
Radical: house on cliff 广
Parts: 广 ヨ 水 隶
легкость, умиротворение
On: コウ
建
9 strokes
Radical: long stride 廴
Parts: 廴 聿
строить
Kun: た.てる、 た.て、 -だ.て、 た.つ
On: ケン、 コン
径
8 strokes
Radical: step 彳
Parts: 又 土 彳
Variants: 徑 逕
диаметр, траектория, способ
Kun: みち、 こみち、 さしわたし、 ただちに
On: ケイ
徒
10 strokes
Radical: step 彳
Parts: 土 彳 走
пустота, тщеславие, тщетность, бесполезность
Kun: いたずら、 あだ
On: ト
得
11 strokes
Radical: step 彳
Parts: 一 寸 彳 日
приобретать, добывать, находить, зарабатывать
Kun: え.る、 う.る
On: トク
必
5 strokes
Radical: heart 心 (忄, ⺗)
Parts: ノ 心
неизменно, неоспоримо, неотвратимо
Kun: かなら.ず
On: ヒツ
念
8 strokes
Radical: heart 心 (忄, ⺗)
Parts: 一 ｜ 个 心
желание, смысл, идея, мысль, чувство, вожделение, внимание
On: ネン
愛
13 strokes
Radical: heart 心 (忄, ⺗)
Parts: 冖 夂 心 爪
любовь, привязанность, любимый
Kun: いと.しい、 かな.しい、 め.でる、 お.しむ、 まな
On: アイ
成
6 strokes
Radical: spear, halberd 戈
Parts: ノ 戈
превращаться, становиться, получать, расти, истекать, достигать
Kun: な.る、 な.す、 -な.す
On: セイ、 ジョウ
戦
13 strokes
Radical: spear, halberd 戈
Parts: 十 尚 戈 田
Variants: 戰
война, сражение, поединок
Kun: いくさ、 たたか.う、 おのの.く、 そよ.ぐ、 わなな.く
On: セン
折
7 strokes
Radical: hand 手 (扌龵)
Parts: 扎 斤
сгибать, ломать, разламывать, сгибать, уступать, подчиняться
Kun: お.る、 おり、 お.り、 -お.り、 お.れる
On: セツ、 シャク
挙
10 strokes
Radical: hand 手 (扌龵)
Parts: ハ 尚 手
Variants: 擧 舉
воспитание, план, проект, поведение, действия
Kun: あ.げる、 あ.がる、 こぞ.る
On: キョ
改
7 strokes
Radical: rap 攴 (攵)
Parts: 已 乞 攵
реформировать, изменять, модифицировать, чинить, обновлять, изучать, инспектировать, искать
Kun: あらた.める、 あらた.まる
On: カイ
救
11 strokes
Radical: rap 攴 (攵)
Parts: 丶 水 乞 攵
спасать, помогать, возвращать
Kun: すく.う
On: キュウ
敗
11 strokes
Radical: rap 攴 (攵)
Parts: ハ 目 貝 乞 攵
Variants: 贁
неудача, поражение, разворот
Kun: やぶ.れる
On: ハイ
散
12 strokes
Radical: rap 攴 (攵)
Parts: 二 廾 月 乞 攵
разбрасывать, рассеивать, тратить, растрачивать впустую
Kun: ち.る、 ち.らす、 -ち.らす、 ち.らかす、 ち.らかる、 ち.らばる、 ばら、 ばら.ける
On: サン
料
10 strokes
Radical: dipper 斗
Parts: 斗 米
плата, материалы
On: リョウ
旗
14 strokes
Radical: square 方
Parts: ハ 方 甘 乞
национальный флаг, знамя, штандарт
Kun: はた
On: キ
昨
9 strokes
Radical: sun, day 日
Parts: ｜ ノ 日
вчерашний, предыдущий
On: サク
景
12 strokes
Radical: sun, day 日
Parts: 亠 口 小 日
пейзаж, вид
On: ケイ
最
12 strokes
Radical: say 曰
Parts: 一 又 日 耳
Variants: 冣
предельный, самый, экстремальный
Kun: もっと.も、 つま
On: サイ、 シュ
望
11 strokes
Radical: moon, month 月
Parts: 亡 月 王
амбиции, полнолуние, надежда, желание, стремлюсь к, ожидаю
Kun: のぞ.む、 もち
On: ボウ、 モウ
未
5 strokes
Radical: tree 木
Parts: ｜ 二 亠 ハ 木
не-, еще нет, доселе, все еще, даже сейчас, знак овна
Kun: いま.だ、 ま.だ、 ひつじ
On: ミ、 ビ
末
5 strokes
Radical: tree 木
Parts: 一 ｜ 亠 ハ 木
конец, закрытие, наконечник, пудра, потомство
Kun: すえ、 うら、 うれ
On: マツ、 バツ
札
5 strokes
Radical: tree 木
Parts: 乙 木
бирка, бумажные деньги, счетчик для облигаций, плакат, заявка
Kun: ふだ
On: サツ
材
7 strokes
Radical: tree 木
Parts: 一 ノ 亅 木
бревно, пиломатериалы, древесина, материалы, ингредиенты, талант
On: ザイ"""
        native_kun_on_481_510 = """博
12 strokes
Radical: ten, complete 十
Parts: 丶 十 寸 田
Доктор, команда, уважение, завоевание признания, доктор философии, экспозиция, ярмарка
On: ハク、 バク
印
6 strokes
Radical: kneel 卩
Parts: ｜ 卩
штамп, печать, клеймо, оттиск, символ, эмблема, товарный знак, вещественное доказательство, сувенир, Индия
Kun: しるし、 -じるし、 しる.す
On: イン
参
8 strokes
Radical: private 厶
Parts: 一 厶 彡
Variants: 參 叅
cбитый с толку, навестить, потерпеть поражение, умереть, быть безумно влюбленным, участвовать, принимать участие в
Kun: まい.る、 まい-、 まじわる、 みつ
On: サン、 シン
史
5 strokes
Radical: mouth, opening 口
Parts: ノ 口
история, хроника
On: シ
司
5 strokes
Radical: mouth, opening 口
Parts: 一 亅 口
директор, должностное лицо, правительственный офис, править, администрировать
Kun: つかさど.る
On: シ
各
6 strokes
Radical: mouth, opening 口
Parts: 口 夂 攵
каждый, либо
Kun: おのおの
On: カク
告
7 strokes
Radical: mouth, opening 口
Parts: ノ 口 土
откровение, рассказывать, информировать, объявлять
Kun: つ.げる
On: コク
周
8 strokes
Radical: mouth, opening 口
Parts: 冂 口 土
окружность, контур, круг
Kun: まわ.り
On: シュウ
唱
11 strokes
Radical: mouth, opening 口
Parts: 口 日
Variants: 誯
пойте, декламируйте, взывайте, кричите
Kun: とな.える
On: ショウ
喜
12 strokes
Radical: mouth, opening 口
Parts: 并 口 士 豆
радуйтесь, получайте удовольствие от
Kun: よろこ.ぶ、 よろこ.ばす
On: キ
器
15 strokes
Radical: mouth, opening 口
Parts: 口 大
Variants: 噐
посуда, сосуд, вместилище, приспособление, инструмент, способность, контейнер, инструментарий, набор
Kun: うつわ
On: キ
囲
7 strokes
Radical: enclosure 囗
Parts: 囗 井
Variants: 圍
окружать, осаждать, хранить, обносить частоколом, ограждать, окружать, сохранять, оберегать
Kun: かこ.む、 かこ.う、 かこ.い
On: イ
固
8 strokes
Radical: enclosure 囗
Parts: 十 口 囗
Variants:
затвердевать, схватываться, сворачиваться в комок
Kun: かた.める、 かた.まる、 かた.まり、 かた.い
On: コ
型
9 strokes
Radical: earth 土
Parts: 一 ノ 二 刈 土 廾
форма, тип, модель
Kun: かた、 -がた
On: ケイ
堂
11 strokes
Radical: earth 土
Parts: 冖 口 土 尚
общественная палата, зал
On: ドウ
塩
13 strokes
Radical: earth 土
Parts: 一 ノ 人 口 土 皿 乞
Variants: 鹽
соль
Kun: しお
On: エン
士
3 strokes
Radical: scholar, bachelor 士
Parts: 士
джентльмен, ученый, самурай
Kun: さむらい
On: シ
変
9 strokes
Radical: go 夂
Parts: 亠 夂
Variants: 變
необычное, переменчивое, странное
Kun: か.わる、 か.わり、 か.える
On: ヘン
夫
4 strokes
Radical: big, very 大
Parts: 二 亠 人 大
муж
Kun: おっと、 それ
On: フ、 フウ、 ブ
失
5 strokes
Radical: big, very 大
Parts: ノ 二 人 大
проигрыш, ошибка, неисправность, недостаток, потеря
Kun: うしな.う、 う.せる
On: シツ
好
6 strokes
Radical: woman, female 女
Parts: 女 子
нежный, приятный, похожий на что-то
Kun: この.む、 す.く、 よ.い、 い.い
On: コウ
季
8 strokes
Radical: child, seed 子
Parts: 子 禾
времена года
On: キ
孫
10 strokes
Radical: child, seed 子
Parts: ノ 子 小 幺 糸
внук, потомки
Kun: まご
On: ソン
完
7 strokes
Radical: roof 宀
Parts: 二 儿 宀 元
совершенство, завершение, конец
On: カン
官
8 strokes
Radical: roof 宀
Parts: ｜ 口 宀
бюрократ, правительство, орган
On: カン
害
10 strokes
Radical: roof 宀
Parts: 二 亠 口 土 宀
вред, увечье
On: ガイ
察
14 strokes
Radical: roof 宀
Parts: ノ 二 宀 小 癶 示
угадывать, предполагать, догадываться, судить, понимать
On: サツ
巣
11 strokes
Radical: river 巛 (川, 巜)
Parts: 尚 木 田
Variants: 巢
гнездо, лежбище, улей, паутина, берлога
Kun: す、 す.くう
On: ソウ
差
10 strokes
Radical: work 工
Parts: ノ 并 工 王 羊
различие, разность, вариация, расхождение, запас, баланс
Kun: さ.す、 さ.し
On: サ
希
7 strokes
Radical: turban, scarf 巾
Parts: 一 ノ 巾
редкий, немногочисленный, феноменальный, Греция
Kun: まれ、 こいねが.う
On: キ、 ケ"""
        native_kun_on_451_480 = """便
9 strokes
Radical: man, human 人 (亻)
Parts: 一 ｜ ノ 化 日 田
удобство, возможность, экскременты, фекалии, письмо, шанс
Kun: たよ.り
On: ベン、 ビン
信
9 strokes
Radical: man, human 人 (亻)
Parts: 化 言
Variants: 訫
вера, истина, верность, доверие
On: シン
倉
10 strokes
Radical: man, human 人 (亻)
Parts: 一 ノ 个 口 尸
богадельня, склад, кладовая, погреб, сокровищница
Kun: くら
On: ソウ
候
10 strokes
Radical: man, human 人 (亻)
Parts: ｜ 化 ユ 矢 乞
климат, время года, погода, ждать, ожидать
Kun: そうろう
On: コウ
借
10 strokes
Radical: man, human 人 (亻)
Parts: 二 化 廾 日
брать взаймы, сдавать в аренду
Kun: か.りる
On: シャク
停
11 strokes
Radical: man, human 人 (亻)
Parts: 一 亅 亠 化 冖 口
стоп, остановка
Kun: と.める、 と.まる
On: テイ
健
11 strokes
Radical: man, human 人 (亻)
Parts: 化 廴 聿
Variants: 徤
здоровый, крепкое здоровье, сила, настойчивость
Kun: すこ.やか
On: ケン
側
11 strokes
Radical: man, human 人 (亻)
Parts: 化 ハ 刈 目 貝
вставать на сторону, склоняться, возражать, сожалеть
Kun: かわ、 がわ、 そば
On: ソク
働
13 strokes
Radical: man, human 人 (亻)
Parts: 一 ｜ ノ 化 力 日
Variants: 仂
работать
Kun: はたら.く
On: ドウ
億
15 strokes
Radical: man, human 人 (亻)
Parts: 化 心 日 立 音
сто миллионов
On: オク
兆
6 strokes
Radical: legs 儿
Parts: 儿 冫
предзнаменование, триллион, знак, предзнаменование
Kun: きざ.す、 きざ.し
On: チョウ
児
7 strokes
Radical: legs 儿
Parts: ｜ 儿 日
Variants: 兒
новорожденный младенец, ребенок, детеныш животных
Kun: こ、 -こ、 -っこ
On: ジ、 ニ、 ゲイ
共
6 strokes
Radical: eight 八
Parts: 一 ｜ 二 ハ
вместе, оба, ни то, ни другое, все и, одинаково
Kun: とも、 とも.に、 -ども
On: キョウ
兵
7 strokes
Radical: eight 八
Parts: 一 ハ 斤
солдат, рядовой, войска, армия, война, стратегия, тактика
Kun: つわもの
On: ヘイ、 ヒョウ
典
8 strokes
Radical: eight 八
Parts: 一 ｜ ハ 日
кодекс, церемония, закон, правило
Kun: ふみ、 のり
On: テン、 デン
冷
7 strokes
Radical: ice 冫
Parts: 一 个 冫 卩
прохладный, холодный
Kun: つめ.たい、 ひ.える、 ひ.や、 ひ.ややか、 ひ.やす、 ひ.やかす、 さ.める、 さ.ます
On: レイ
初
7 strokes
Radical: knife, sword 刀 (刂)
Parts: 刀 初
Variants:
первое время, начинание
Kun: はじ.め、 はじ.めて、 はつ、 はつ-、 うい-、 -そ.める、 -ぞ.め
On: ショ
別
7 strokes
Radical: knife, sword 刀 (刂)
Parts: 刈 力 勹 口
отделять, ответвляться, расходиться, разветвляться, другой, дополнительный, специально
Kun: わか.れる、 わ.ける
On: ベツ
利
7 strokes
Radical: knife, sword 刀 (刂)
Parts: 刈 禾
прибыль, преимущество, выгода
Kun: き.く
On: リ
刷
8 strokes
Radical: knife, sword 刀 (刂)
Parts: 刈 尸 巾
печать, оттиск, кисть
Kun: す.る、 -ず.り、 -ずり、 は.く
On: サツ
副
11 strokes
Radical: knife, sword 刀 (刂)
Parts: 一 刈 口 田
заместитель, ассистент, помощница, дубликат, копия
On: フク
功
5 strokes
Radical: power, force 力
Parts: 力 工
достижение, заслуги, успех, честь, кредит
Kun: いさお
On: コウ、 ク
加
5 strokes
Radical: power, force 力
Parts: 力 口
добавить, сложение, увеличение, присоединение, включение, Канада
Kun: くわ.える、 くわ.わる
On: カ
努
7 strokes
Radical: power, force 力
Parts: 力 又 女
Variants: 伮
усердно трудиться, насколько это возможно
Kun: つと.める
On: ド
労
7 strokes
Radical: power, force 力
Parts: 冖 力 尚
Variants: 勞
труд, благодарность за, награда за, тяжкий труд, неприятности
Kun: ろう.する、 いたわ.る、 いた.ずき、 ねぎら、 つか.れる、 ねぎら.う
On: ロウ
勇
9 strokes
Radical: power, force 力
Parts: 力 マ 田
Variants: 勈
смелость, не унывай, будь в приподнятом настроении, отвага, героизм
Kun: いさ.む
On: ユウ
包
5 strokes
Radical: wrap, embrace 勹
Parts: 勹 已
заворачивать, упаковывать, накрывать, скрывать
Kun: つつ.む、 くる.む
On: ホウ
卒
8 strokes
Radical: ten, complete 十
Parts: 亠 人 十
Variants: 卆
выпускник, солдат, рядовой, умри
Kun: そっ.する、 お.える、 お.わる、 ついに、 にわか
On: ソツ、 シュツ
協
8 strokes
Radical: ten, complete 十
Parts: 力 十
сотрудничество
On: キョウ
単
9 strokes
Radical: ten, complete 十
Parts: 十 尚 田
Variants: 單 嘽
простой, единый, незамысловатый, просто
Kun: ひとえ
On: タン"""
        native_kun_on_421_450 = """遊
12 strokes (also 11)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 込 子 方 乞
развлекаться
Kun: あそ.ぶ、 あそ.ばす
On: ユウ、 ユ
運
12 strokes (also 11)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 冖 込 車
судьба, участь, нести, тащить
Kun: はこ.ぶ
On: ウン
部
11 strokes (also 10)
Radical: town (阝 right) 邑 (阝)
Parts: 口 邦 立
Variants: 郶
часть, сектор
Kun: -べ
On: ブ
都
11 strokes (also 10)
Radical: town (阝 right) 邑 (阝)
Parts: 邦 老 日
Variants: 都
мегаполис, столица
Kun: みやこ
On: ト、 ツ
配
10 strokes
Radical: wine, alcohol 酉
Parts: 已 酉
распределять, супруг, изгнание, нормирование
Kun: くば.る
On: ハイ
酒
10 strokes
Radical: wine, alcohol 酉
Parts: 汁 酉
саке, алкоголь
Kun: さけ、 さか-
On: シュ
重
9 strokes
Radical: village, mile 里
Parts: 一 ｜ ノ 日 里
тяжелый, важный, почитаемый, складывать
Kun: え、 おも.い、 おも.り、 おも.なう、 かさ.ねる、 かさ.なる、 おも
On: ジュウ、 チョウ
鉄
13 strokes
Radical: metal, gold 金 (釒)
Parts: ノ 二 大 矢 金 乞
Variants: 銕 鐵 鐡 鋨
железо
Kun: くろがね
On: テツ
銀
14 strokes
Radical: metal, gold 金 (釒)
Parts: 艮 金
серебро
Kun: しろがね
On: ギン
開
12 strokes
Radical: gate 門
Parts: 一 ノ 二 廾 門
Variants:
открывать, открываться
Kun: ひら.く、 ひら.き、 -びら.き、 ひら.ける、 あ.く、 あ.ける
On: カイ
院
10 strokes
Radical: mound, dam (阝 left) 阜 (阝)
Parts: 二 儿 宀 阡 元
учреждение, школа
On: イン
陽
12 strokes
Radical: mound, dam (阝 left) 阜 (阝)
Parts: 一 阡 日 勿
Variants: 阦 阳
солнце, солнечный свет, принцип ян, позитив, мужчина, небеса, дневное время
Kun: ひ
On: ヨウ
階
12 strokes
Radical: mound, dam (阝 left) 阜 (阝)
Parts: 阡 比 白
Variants: 堦
этаж, лестница, счетчик этажей здания
Kun: きざはし
On: カイ
集
12 strokes
Radical: small bird 隹
Parts: 木 隹
собираться, встречаться, скапливаться, роиться, слетаться стаей
Kun: あつ.まる、 あつ.める、 つど.う
On: シュウ
面
9 strokes
Radical: face 面 (靣)
Parts: 面
Variants: 靣
маска, лицо, черты лица, поверхность
Kun: おも、 おもて、 つら
On: メン、 ベン
題
18 strokes
Radical: leaf 頁
Parts: ハ 日 疋 目 貝 頁
тема, предмет, заглавие
On: ダイ
飲
12 strokes
Radical: eat, food 食 (飠)
Parts: 欠 食
Variants: 飮
пить, курить, принимать
Kun: の.む、 -の.み
On: イン、 オン
館
16 strokes
Radical: eat, food 食 (飠)
Parts: ｜ 口 宀 食
Variants: 舘
здание, особняк, большое здание, дворец
Kun: やかた、 たて
On: カン
駅
14 strokes
Radical: horse 馬
Parts: 丶 尸 杰 馬
Variants: 驛
станция
On: エキ
鼻
14 strokes
Radical: nose 鼻
Parts: 廾 田 目 自 鼻
нос
Kun: はな
On: ビ
不
4 strokes
Radical: one 一
Parts: 一 ｜ 丶 ノ
не, не-
On: フ、 ブ
争
6 strokes
Radical: hook 亅
Parts: 一 亅 勹 ヨ
Variants: 爭
бороться, препираться, оспаривать, аргументировать
Kun: あらそ.う、 いか.でか
On: ソウ
付
5 strokes
Radical: man, human 人 (亻)
Parts: 化 寸
придерживаться, присоединять, ссылаться на, дополнять
Kun: つ.ける、 -つ.ける、 -づ.ける、 つ.け、 つ.け-、 -つ.け、 -づ.け、 -づけ、 つ.く、 -づ.く、 つ.き、 -つ.き、 -つき、 -づ.き、 -づき
On: フ
令
5 strokes
Radical: man, human 人 (亻)
Parts: 一 个 卩
приказы, законы, повеление
On: レイ
以
5 strokes
Radical: man, human 人 (亻)
Parts: ｜ 丶 人
посредством, потому что, принимая во внимание, по сравнению с
Kun: もっ.て
On: イ
仲
6 strokes
Radical: man, human 人 (亻)
Parts: ｜ 化 口
посредник, отношения
Kun: なか
On: チュウ
伝
6 strokes
Radical: man, human 人 (亻)
Parts: 二 化 厶
Variants: 傳
передавать, продолжать, прогуливаться, следовать
Kun: つた.わる、 つた.える、 つた.う、 つだ.う、 -づた.い、 つて
On: デン、 テン
位
7 strokes
Radical: man, human 人 (亻)
Parts: 化 立
звание, ранг, трон, корона, примерно, какой-то
Kun: くらい、 ぐらい
On: イ
低
7 strokes
Radical: man, human 人 (亻)
Parts: 一 化 氏
Variants: 仾
низкий
Kun: ひく.い、 ひく.める、 ひく.まる
On: テイ
例
8 strokes
Radical: man, human 人 (亻)
Parts: 化 刈 歹
пример, обычай, использование, прецедент
Kun: たと.える
On: レイ"""
        native_kun_on_391_420 = """緑
14 strokes
Radical: silk 糸 (糹)
Parts: 小 幺 ヨ 水 糸 隶
Variants: 綠
зелёный
Kun: みどり
On: リョク、 ロク
練
14 strokes
Radical: silk 糸 (糹)
Parts: ｜ ハ 小 幺 日 木 田 糸
Variants: 練
практикуйся, наводи лоск, тренируй, сверли, полируй, облагораживай
Kun: ね.る、 ね.り
On: レン
羊
6 strokes
Radical: sheep 羊 (⺶)
Parts: 并 王 羊
овца, баран
Kun: ひつじ
On: ヨウ
美
9 strokes
Radical: sheep 羊 (⺶)
Parts: 并 大 王 羊
красивый, красота
Kun: うつく.しい
On: ビ、 ミ
習
11 strokes
Radical: feather 羽
Parts: 冫 白 羽
учиться
Kun: なら.う、 なら.い
On: シュウ、 ジュ
者
8 strokes
Radical: old 老 (耂)
Parts: 老 日
Variants: 者
человек, некто
Kun: もの
On: シャ
育
8 strokes
Radical: meat 肉 (⺼)
Parts: 亠 厶 月
Variants: 毓
воспитывать, взрослеть, растить, лелеять
Kun: そだ.つ、 そだ.ち、 そだ.てる、 はぐく.む
On: イク
苦
8 strokes
Radical: grass 艸 (艹)
Parts: 十 口 艾
страдание, испытание, беспокойство, трудности, чувствовать горечь, хмуриться
Kun: くる.しい、 -ぐる.しい、 くる.しむ、 くる.しめる、 にが.い、 にが.る
On: ク
荷
10 strokes
Radical: grass 艸 (艹)
Parts: 一 亅 化 口 艾
багаж, нагрузка на плечо, нагрузка, груз
Kun: に
On: カ
落
12 strokes
Radical: grass 艸 (艹)
Parts: 口 夂 汁 艾
падать, спускайся вниз, деревня, хутор
Kun: お.ちる、 お.ち、 お.とす
On: ラク
葉
12 strokes
Radical: grass 艸 (艹)
Parts: 艾 木 世
лист, плоскость, лепесток, игла, лезвие, копье
Kun: は
On: ヨウ
薬
16 strokes
Radical: grass 艸 (艹)
Parts: 冫 艾 日 木
Variants: 藥
лекарство, медицина, химия, эмаль, порох, польза
Kun: くすり
On: ヤク
血
6 strokes
Radical: blood 血
Parts: 皿 血
кровь
Kun: ち
On: ケツ
表
8 strokes
Radical: clothes 衣 (衤)
Parts: 二 亠 土 士 衣
поверхность, таблица, график, диаграмма
Kun: おもて、 -おもて、 あらわ.す、 あらわ.れる、 あら.わす
On: ヒョウ
詩
13 strokes
Radical: speech 言 (訁)
Parts: 土 寸 言
стихи, поэзия
Kun: うた
On: シ
調
15 strokes
Radical: speech 言 (訁)
Parts: 冂 口 土 言
мелодия, тон, метр, тональность
Kun: しら.べる、 しら.べ、 ととの.う、 ととの.える
On: チョウ
談
15 strokes
Radical: speech 言 (訁)
Parts: 火 言
разговор, беседа
On: ダン
豆
7 strokes
Radical: bean 豆
Parts: 并 口 豆
боб, горох
Kun: まめ、 まめ-
On: トウ、 ズ
負
9 strokes
Radical: shell 貝
Parts: ハ 勹 目 貝
поражение, негатив, нести, быть обязанным, брать на себя ответственность
Kun: ま.ける、 ま.かす、 お.う
On: フ
起
10 strokes
Radical: run 走 (赱)
Parts: 土 已 走
просыпаться, вставать
Kun: お.きる、 お.こる、 お.こす、 おこ.す、 た.つ
On: キ
路
13 strokes
Radical: foot 足 (⻊)
Parts: 口 夂 止 足
Variants:
дорога, путь
Kun: -じ、 みち
On: ロ、 ル
身
7 strokes
Radical: body 身
Parts: 身
персона, тело
Kun: み
On: シン
転
11 strokes
Radical: cart, car 車
Parts: 二 厶 車
Variants: 轉
поворачиваться, падать, изменять
Kun: ころ.がる、 ころ.げる、 ころ.がす、 ころ.ぶ、 まろ.ぶ、 うたた、 うつ.る、 くる.めく
On: テン
軽
12 strokes
Radical: cart, car 車
Parts: 又 土 車
Variants: 輕
легкий, легкомысленный, пустяковый, неважный
Kun: かる.い、 かろ.やか、 かろ.んじる
On: ケイ、 キョウ、 キン
農
13 strokes
Radical: morning 辰
Parts: 一 ｜ 厂 日 衣 辰
земледелие
On: ノウ
返
7 strokes (also 6)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 厂 又 込
возвращать, ответ
Kun: かえ.す、 -かえ.す、 かえ.る、 -かえ.る
On: ヘン
追
9 strokes (also 8)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: ｜ 込 口
преследовать, гнать, выгонять
Kun: お.う
On: ツイ
送
9 strokes (also 8)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 一 二 并 込 大
посылать, отправлять
Kun: おく.る
On: ソウ
速
10 strokes (also 9)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 一 ｜ ハ 込 口 木
Variants:
скорость, быстрый, немедленно
Kun: はや.い、 はや-、 はや.める、 すみ.やか
On: ソク
進
11 strokes (also 10)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 込 隹
продвигаться, продолжать, прогрессировать, продвигать
Kun: すす.む、 すす.める
On: シン"""
        native_kun_on_361_390 = """由
5 strokes
Radical: field 田
Parts: ｜ 日 田
причина
Kun: よし、 よ.る
On: ユ、 ユウ、 ユイ
申
5 strokes
Radical: field 田
Parts: ｜ 日 田
докладывать, говорить
Kun: もう.す、 もう.し-、 さる
On: シン
界
9 strokes
Radical: field 田
Parts: 个 儿 田
мир, сфера
On: カイ
畑
9 strokes
Radical: field 田
Parts: 火 田
ферма, поле, сад
Kun: はた、 はたけ、 -ばたけ
病
10 strokes
Radical: sickness 疒
Parts: 一 人 冂 疔
болеть, болезнь
Kun: や.む、 -や.み、 やまい
On: ビョウ、 ヘイ
発
9 strokes
Radical: footsteps 癶
Parts: 二 儿 癶
Variants: 發
испускать, отправление, разрядка, публикация, выброс, начало, раскрытие, счетчик выстрелов
Kun: た.つ、 あば.く、 おこ.る、 つか.わす、 はな.つ
On: ハツ、 ホツ
登
12 strokes
Radical: footsteps 癶
Parts: 并 口 癶 豆
Variants: 僜
подниматься, карабкаться вверх
Kun: のぼ.る、 あ.がる
On: トウ、 ト、 ドウ、 ショウ、 チョウ
皮
5 strokes
Radical: skin 皮
Parts: 又 皮
кожа
Kun: かわ
On: ヒ
皿
5 strokes
Radical: dish 皿
Parts: 皿
блюдо, порция, тарелка
Kun: さら
On: ベイ
相
9 strokes
Radical: eye 目
Parts: 木 目
взаимный, вместе, друг с другом
Kun: あい-
On: ソウ、 ショウ
県
9 strokes
Radical: eye 目
Parts: 小 目
Variants: 縣
префектура
Kun: か.ける
On: ケン
真
10 strokes
Radical: eye 目
Parts: 一 ハ 十 目
Variants: 眞
правда, истина
Kun: ま、 ま-、 まこと
On: シン
着
12 strokes
Radical: eye 目
Parts: ノ 并 王 目 羊
надевать, прибывать
Kun: き.る、 き.せる、 つ.く、 つ.ける
On: チャク、 ジャク
短
12 strokes
Radical: arrow 矢
Parts: 并 口 矢 豆 乞
короткий, лаконичность, недостаток, дефект, слабое место
Kun: みじか.い
On: タン
研
9 strokes
Radical: stone 石
Parts: 一 ｜ ノ 亅 二 口 廾 石
точить
Kun: と.ぐ
On: ケン
礼
5 strokes
Radical: sign 示 (礻)
Parts: 乙 礼
Variants: 禮
приветствие, поклон, церемония, благодарность, вознаграждение
On: レイ、 ライ
神
9 strokes
Radical: sign 示 (礻)
Parts: ｜ 日 礼 田
божество, боги, разум, душа
Kun: かみ、 かん-、 こう-
On: シン、 ジン
祭
11 strokes
Radical: sign 示 (礻)
Parts: 二 个 小 癶 示
праздник, праздничество, поклоняться
Kun: まつ.る、 まつ.り、 まつり
On: サイ
福
13 strokes
Radical: sign 示 (礻)
Parts: 一 口 礼 田
счастье, благословение, удача, везение, богатство
On: フク
秒
9 strokes
Radical: grain 禾
Parts: ノ 小 禾
секунда
On: ビョウ
究
7 strokes
Radical: cave 穴
Parts: 儿 九 宀 穴
Variants:
осваивать
Kun: きわ.める
On: キュウ、 ク
章
11 strokes
Radical: stand, erect 立
Parts: 十 日 立 音
эмблема, значок, глава, композиция, стихотворение, дизайн
On: ショウ
童
12 strokes
Radical: stand, erect 立
Parts: 立 里
дитя
Kun: わらべ
On: ドウ
笛
11 strokes
Radical: bamboo 竹 (⺮)
Parts: ｜ 日 田 竹 乞
флейта, кларнет
Kun: ふえ
On: テキ
第
11 strokes
Radical: bamboo 竹 (⺮)
Parts: 弓 竹 乞
префикс числительных
On: ダイ、 テイ
筆
12 strokes
Radical: bamboo 竹 (⺮)
Parts: 竹 聿 乞
Variants: 笔
кисть для письма, письмо, кисть для рисования, почерк
Kun: ふで
On: ヒツ
等
12 strokes
Radical: bamboo 竹 (⺮)
Parts: 土 寸 竹 乞
разряд, и так далее, класс (первый), качество, равный, подобный
Kun: ひと.しい、 など、 -ら
On: トウ
箱
15 strokes
Radical: bamboo 竹 (⺮)
Parts: 木 目 竹 乞
ящик, коробка
Kun: はこ
On: ソウ
級
9 strokes
Radical: silk 糸 (糹)
Parts: ノ 小 幺 及 糸
класс, разряд
On: キュウ
終
11 strokes
Radical: silk 糸 (糹)
Parts: 夂 小 幺 糸
конец, заканчиваться
Kun: お.わる、 -お.わる、 おわ.る、 お.える、 つい、 つい.に
On: シュウ"""
        native_kun_on_331_360 = """期
12 strokes
Radical: moon, month 月
Parts: ハ 月 甘
Variants: 朞
период, время, дата, срок
On: キ、 ゴ
板
8 strokes
Radical: tree 木
Parts: 厂 又 木
планка, дощечка, плита, сцена
Kun: いた
On: ハン、 バン
柱
9 strokes
Radical: tree 木
Parts: 丶 木 王
стойка, столбик, цилиндр, опора
Kun: はしら
On: チュウ
根
10 strokes
Radical: tree 木
Parts: 木 艮
корень, прикорневая часть
Kun: ね、 -ね
On: コン
植
12 strokes
Radical: tree 木
Parts: 十 木 目
сажать растения
Kun: う.える、 う.わる
On: ショク
業
13 strokes
Radical: tree 木
Parts: 一 ｜ 并 木 王 羊 耒
бизнес, призвание, искусство, перформанс
Kun: わざ
On: ギョウ、 ゴウ
様
14 strokes
Radical: tree 木
Parts: 并 木 水 王 羊
Variants: 樣
способ, манера поведения, ситуация, вежливый суффикс, вид, положение
Kun: さま、 さん
On: ヨウ、 ショウ
横
15 strokes
Radical: tree 木
Parts: ｜ 二 ハ 廾 日 木 田 黄
горизонтальный, ширина
Kun: よこ
On: オウ
橋
16 strokes
Radical: tree 木
Parts: ノ 冂 口 木
Variants: 槗
мост
Kun: はし
On: キョウ
次
6 strokes
Radical: lack, yawn 欠
Parts: 冫 欠
следующий, далее, порядок, последовательность
Kun: つ.ぐ、 つぎ
On: ジ、 シ
歯
12 strokes
Radical: stop 止
Parts: 凵 止 米 歯
Variants: 齒
зуб
Kun: よわい、 は、 よわ.い、 よわい.する
On: シ
死
6 strokes
Radical: death, decay 歹 (歺)
Parts: 一 匕 夕 歹
смерть, умирать
Kun: し.ぬ、 し.に-
On: シ
氷
5 strokes
Radical: water 水 (氵, 氺)
Parts: 丶 水
Variants: 冰
сосулька, лед, град, замерзание, застывание
Kun: こおり、 ひ、 こお.る
On: ヒョウ
決
7 strokes
Radical: water 水 (氵, 氺)
Parts: 二 人 ユ 大 汁
Variants: 决
решать, фиксировать, согласовывать, назначать
Kun: き.める、 -ぎ.め、 き.まる、 さ.く
On: ケツ
油
8 strokes
Radical: water 水 (氵, 氺)
Parts: ｜ 汁 日 田
масло
Kun: あぶら
On: ユ、 ユウ
波
8 strokes
Radical: water 水 (氵, 氺)
Parts: 又 汁 皮
волна
Kun: なみ
On: ハ
注
8 strokes
Radical: water 水 (氵, 氺)
Parts: 丶 汁 王
лить, примечание, изливать, орошать, проливать (слезы), вливаться, концентрироваться, отмечать, комментировать, аннотировать
泳
8 strokes
Radical: water 水 (氵, 氺)
Parts: 丶 汁 水
плавать
Kun: およ.ぐ
On: エイ
洋
9 strokes
Radical: water 水 (氵, 氺)
Parts: 并 汁 王 羊
океан, море
On: ヨウ
流
10 strokes
Radical: water 水 (氵, 氺)
Parts: 亠 厶 川 汁
течь, течение, сток, поток, неустойка
Kun: なが.れる、 なが.れ、 なが.す、 -なが.す
On: リュウ、 ル
消
10 strokes
Radical: water 水 (氵, 氺)
Parts: 尚 汁 月
гаснуть, задуть, погасить, задуть, выключить, нейтрализовать, отменить
Kun: き.える、 け.す
On: ショウ
深
11 strokes
Radical: water 水 (氵, 氺)
Parts: 儿 冖 汁 木
глубокий, углублять, усиливать, интенсифицировать, укреплять
Kun: ふか.い、 -ぶか.い、 ふか.まる、 ふか.める、 み-
On: シン
温
12 strokes
Radical: water 水 (氵, 氺)
Parts: 汁 日 皿
Variants: 溫
тёплый
Kun: あたた.か、 あたた.かい、 あたた.まる、 あたた.める、 ぬく
On: オン
港
12 strokes
Radical: water 水 (氵, 氺)
Parts: ハ 已 汁 井
порт
Kun: みなと
On: コウ
湖
12 strokes
Radical: water 水 (氵, 氺)
Parts: 十 口 汁 月
озеро
Kun: みずうみ
On: コ
湯
12 strokes
Radical: water 水 (氵, 氺)
Parts: 一 ｜ 汁 日 勿
горячая вода, ванна, горячий источник
Kun: ゆ
On: トウ
漢
13 strokes
Radical: water 水 (氵, 氺)
Parts: 一 二 口 大 汁 艾
китайский
On: カン
炭
9 strokes
Radical: fire 火 (灬)
Parts: 厂 山 火
древесный уголь, каменный уголь
Kun: すみ
On: タン
物
8 strokes
Radical: cow 牛 (牜)
Parts: ノ 勹 牛 勿
вещь, предмет
Kun: もの、 もの-
On: ブツ、 モツ
球
11 strokes
Radical: jade (king) 玉 (王)
Parts: 丶 水 王
мяч, шар
Kun: たま
On: キュウ"""
        native_kun_on_301_330 = """度
9 strokes
Radical: house on cliff 广
Parts: 一 又 广 凵
степени, вхождение, время, счетчик вхождений, рассмотрение, отношение
Kun: たび、 -た.い
On: ド、 ト、 タク
庫
10 strokes
Radical: house on cliff 广
Parts: 广 車
склад, кладовая
Kun: くら
On: コ、 ク
庭
10 strokes
Radical: house on cliff 广
Parts: 广 廴 王
внутренний двор, сад, дворик
Kun: にわ
On: テイ
式
6 strokes
Radical: shoot, arrow 弋
Parts: 工 弋
стиль, церемония, обряд, функция, метод, система, форма, выражение
On: シキ
役
7 strokes
Radical: step 彳
Parts: 几 又 彳 殳
долг, война, кампания, призывной труд, должность, служба, роль
On: ヤク、 エキ
待
9 strokes
Radical: step 彳
Parts: 土 寸 彳
ждать
Kun: ま.つ、 -ま.ち
On: タイ
急
9 strokes
Radical: heart 心 (忄, ⺗)
Parts: 勹 ヨ 心
спешить, чрезвычайная ситуация, внезапный
Kun: いそ.ぐ、 いそ.ぎ、 せ.く
On: キュウ
息
10 strokes
Radical: heart 心 (忄, ⺗)
Parts: 心 目 自
дыхание, одышка
Kun: いき
On: ソク
悪
11 strokes
Radical: heart 心 (忄, ⺗)
Parts: 一 ｜ 口 心
Variants: 惡
плохой, порочный, негодяй, лживый, злой, неправильный
Kun: わる.い、 わる-、 あ.し、 にく.い、 -にく.い、 ああ、 いずくに、 いずくんぞ、 にく.む
On: アク、 オ
悲
12 strokes
Radical: heart 心 (忄, ⺗)
Parts: 心 非
печальный, грустный
Kun: かな.しい、 かな.しむ
On: ヒ
想
13 strokes
Radical: heart 心 (忄, ⺗)
Parts: 心 木 目
концепция, мышление, идея, размышление
Kun: おも.う
On: ソウ、 ソ
意
13 strokes
Radical: heart 心 (忄, ⺗)
Parts: 心 日 立 音
идея, разум, сердце, вкус, мысль, желание, забота, симпатия
On: イ
感
13 strokes
Radical: heart 心 (忄, ⺗)
Parts: ノ 口 心 戈
эмоция, чувство, сенсация
On: カン
所
8 strokes
Radical: door, house 戶 (户, 戸)
Parts: 一 尸 戸 斤
место
Kun: ところ、 -ところ、 どころ、 とこ
On: ショ
打
5 strokes
Radical: hand 手 (扌龵)
Parts: 亅 扎
ударять, бить
Kun: う.つ、 う.ち-、 ぶ.つ
On: ダ、 ダース
投
7 strokes
Radical: hand 手 (扌龵)
Parts: 几 又 扎 殳
бросать, отбрасывать, отрекаться, пускаться в дело
Kun: な.げる、 -な.げ
On: トウ
拾
9 strokes
Radical: hand 手 (扌龵)
Parts: 一 个 口 扎
подбирать, собирать, находить, идти пешком, десять
Kun: ひろ.う
On: シュウ、 ジュウ
持
9 strokes
Radical: hand 手 (扌龵)
Parts: 土 寸 扎
держать, иметь
Kun: も.つ、 -も.ち、 も.てる
On: ジ
指
9 strokes
Radical: hand 手 (扌龵)
Parts: 匕 扎 日
палец, указывать
Kun: ゆび、 さ.す、 -さ.し
On: シ
放
8 strokes
Radical: rap 攴 (攵)
Parts: 方 乞 攵
отпускать, бросать
Kun: はな.す、 -っぱな.し、 はな.つ、 はな.れる、 こ.く、 ほう.る
On: ホウ
整
16 strokes
Radical: rap 攴 (攵)
Parts: 一 ｜ 口 木 止 乞 攵
Variants:
организовать, аранжировка, настройка, тон, метр
Kun: ととの.える、 ととの.う
On: セイ
旅
10 strokes
Radical: square 方
Parts: ノ 方 乞
путешествие
Kun: たび
On: リョ
族
11 strokes
Radical: square 方
Parts: 方 矢 乞
племя, семья
On: ゾク
昔
8 strokes
Radical: sun, day 日
Parts: 一 ｜ 二 日
прошлое, давным-давно, древность, старые времена
Kun: むかし
On: セキ、 シャク
昭
9 strokes
Radical: sun, day 日
Parts: 刀 口 日
сияющий, яркий
On: ショウ
暑
12 strokes
Radical: sun, day 日
Parts: 老 日
Variants:
жаркий
Kun: あつ.い
On: ショ
暗
13 strokes
Radical: sun, day 日
Parts: 日 立 音
темный, темнота, исчезновение, тень, неформальность, темнеть, быть ослепленным
Kun: くら.い、 くら.む、 くれ.る
On: アン
曲
6 strokes
Radical: say 曰
Parts: ｜ 日
изгиб, музыка, мелодия, композиция, удовольствие, несправедливость, вина, изгиб, кривобокий, извращенный, худой
Kun: ま.がる、 ま.げる、 くま
On: キョク
有
6 strokes
Radical: moon, month 月
Parts: 一 ノ 月
обладать, иметь, существовать, случаться, протекать
Kun: あ.る
On: ユウ、 ウ
服
8 strokes
Radical: moon, month 月
Parts: 卩 又 月
одежда, одеваться, впускать, подчиняться, увольнять
On: フク"""
        native_kun_on_271_300 = """向
6 strokes
Radical: mouth, opening 口
Parts: 冂 口
лицом к лицу, за пределами, противостоять, бросать вызов, стремиться к, приближаться
Kun: む.く、 む.い、 -む.き、 む.ける、 -む.け、 む.かう、 む.かい、 む.こう、 む.こう-、 むこ、 むか.い
On: コウ
君
7 strokes
Radical: mouth, opening 口
Parts: 一 ノ 口 ヨ
господин, правитель, суффикс мужского имени
Kun: きみ、 -ぎみ
On: クン
味
8 strokes
Radical: mouth, opening 口
Parts: ｜ 二 亠 ハ 口 木
аромат, вкус
Kun: あじ、 あじ.わう
On: ミ
命
8 strokes
Radical: mouth, opening 口
Parts: 一 个 卩 口
судьба, приказ, декрет, предназначение, жизнь, назначать
Kun: いのち
On: メイ、 ミョウ
和
8 strokes
Radical: mouth, opening 口
Parts: 口 禾
Variants: 龢
гармония, японский стиль, умиротворение, смягчение, Япония
Kun: やわ.らぐ、 やわ.らげる、 なご.む、 なご.やか、 あ.える
On: ワ、 オ、 カ
品
9 strokes
Radical: mouth, opening 口
Parts: 口 品
товары, изысканность, достоинство, изделие, стойка для подачи блюд
Kun: しな
On: ヒン、 ホン
員
10 strokes
Radical: mouth, opening 口
Parts: ハ 口 目 貝
сотрудник, участник, номер, ответственный
On: イン
商
11 strokes
Radical: mouth, opening 口
Parts: 亠 儿 并 冂 口 立
заключать сделку, продавать, заниматься торговлей, коммерсант
Kun: あきな.う
On: ショウ
問
11 strokes
Radical: mouth, opening 口
Parts: 口 門
Variants:
вопрос, проси, проблема
Kun: と.う、 と.い、 とん
On: モン
坂
7 strokes
Radical: earth 土
Parts: 厂 又 土
Variants: 阪
склон, уклон, возвышенность
Kun: さか
On: ハン
央
5 strokes
Radical: big, very 大
Parts: 一 ノ 冖 大
центр, середина
On: オウ
始
8 strokes
Radical: women, female 女
Parts: 厶 口 女
Variants: 乨 兘
начинать
Kun: はじ.める、 -はじ.める、 はじ.まる
On: シ
委
8 strokes
Radical: woman, female 女
Parts: 女 禾
комитировать, поручать, оставлять, посвящать, отбрасывать
Kun: ゆだ.ねる
On: イ
守
6 strokes
Radical: roof 宀
Parts: 宀 寸
Variants: 垨
охранять, оберегать, обороняться, подчиняться
Kun: まも.る、 まも.り、 もり、 -もり、 かみ
On: シュ、 ス
安
6 strokes
Radical: roof 宀
Parts: 女 宀
расслабленный, дешевый, низкопробный, тихий, отдохнувший, довольный, умиротворенный
Kun: やす.い、 やす.まる、 やす、 やす.らか
On: アン
定
8 strokes
Radical: roof 宀
Parts: 宀 疋
определять, фиксировать, устанавливать, решать
Kun: さだ.める、 さだ.まる、 さだ.か
On: テイ、 ジョウ
実
8 strokes
Radical: roof 宀
Parts: 士 大 宀
Variants: 實
реальность, истина, семя, фрукт, орех
Kun: み、 みの.る、 まこと、 みの、 みち.る
On: ジツ、 シツ
客
9 strokes
Radical: roof 宀
Parts: 口 夂 宀
гость, посетительница, заказчик, клиентка
On: キャク、 カク
宮
10 strokesRadical: roof 宀
Parts: ノ 口 宀
Синтоистский храм, созвездия, дворец, принцесса
Kun: みや
On: キュウ、 グウ、 ク、 クウ
宿
11 strokes
Radical: roof 宀
Parts: 化 宀 白
гостиница, ночлег, ретрансляционная станция, обитать, сторожка, быть беременной, дом, жилище
Kun: やど、 やど.る、 やど.す
On: シュク
寒
12 strokes
Radical: roof 宀
Parts: 一 丶 ハ 宀 井
холод
Kun: さむ.い
On: カン
対
7 strokes
Radical: thumb, inch 寸
Parts: 寸 文
Variants: 對
противоположный, четный, равный, по сравнению, сравнивать
Kun: あいて、 こた.える、 そろ.い、 つれあ.い、 なら.ぶ、 むか.う
On: タイ、 ツイ
局
7 strokes
Radical: corpse 尸
Parts: 口 尸
бюро, правление, контора, дело, заключение, придворная дама, фрейлина, ее квартира
Kun: つぼね
On: キョク
屋
9 strokes
Radical: corpse 尸
Parts: 厶 土 尸 至
крыша, дом, магазин, дилер, продавец
Kun: や
On: オク
岸
8 strokes
Radical: mountain 山
Parts: 厂 山 干
пляж, берег
Kun: きし
On: ガン
島
10 strokes
Radical: mountain 山
Parts: 山 白 鳥
Variants: 嶋 嶌 嶹
остров
Kun: しま
On: トウ
州
6 strokes
Radical: river 巛 (川, 巜)
Parts: ｜ 丶 川
Variants:
провинция, область
Kun: す
On: シュウ、 ス
帳
11 strokes
Radical: turban, scarf 巾
Parts: 巾 長
Variants: 賬
блокнот, учетная книга, альбом, занавеска, вуаль, сетка, палатка
Kun: とばり
On: チョウ
平
5 strokes
Radical: pestle 干
Parts: 并 干
плоский, ровный, плоский, умиротворенный
Kun: たい.ら、 たい.らげる、 ひら
On: ヘイ、 ビョウ、 ヒョウ
幸
8 strokes
Radical: pestle 干
Parts: 亠 十 立 辛
счастье, благословение, удача
Kun: さいわ.い、 さち、 しあわ.せ
On: コウ"""
        native_kun_on_241_270 = """丁
2 strokes
Radical: one 一
Parts: 一 亅
улица, район, город, прилавок, чётный
Kun: ひのと
On: チョウ、 テイ、 チン、 トウ、 チ
世
5 strokes
Radical: one 一
Parts: 一 ｜ 世
Variants: 丗 卋
поколение, мир, эпоха, общество, общественность
Kun: よ
On: セイ、 セ、 ソウ
両
6 strokes
Radical: one 一
Parts: 一 ｜ 冂 山
Variants: 兩 两
и то, и другое, старинная японская монета, оба
Kun: てる、 ふたつ
On: リョウ
主
5 strokes
Radical: dot 丶
Parts: 丶 王
господин, вождь, повелитель, главный, хозяин, принципиальный
Kun: ぬし、 おも、 あるじ
On: シュ、 ス、 シュウ
乗
9 strokes
Radical: slash 丿
Parts: 一 ｜ ノ ハ 禾
Variants: 乘 椉
ехать, поездка, мощность, умножение, запись, счетчик транспортных средств, доска, крепление, соединение
Kun: の.る、 -の.り、 の.せる
On: ジョウ、 ショウ
予
4 strokes
Radical: hook 亅
Parts: 一 亅 マ
Variants: 豫
заранее, предыдущий, я сам, я
Kun: あらかじ.め
On: ヨ、 シャ
事
8 strokes
Radical: hook 亅
Parts: 一 亅 口 ヨ
Variants: 亊 叓
случай, материя, вещь, факт, бизнес, причина, возможно
Kun: こと、 つか.う、 つか.える
On: ジ、 ズ
仕
5 strokes
Radical: man, human 人 (亻)
Parts: 化 士
присутствовать, делать, официально, служить
Kun: つか.える
On: シ、 ジ
他
5 strokes
Radical: man, human 人 (亻)
Parts: 化 也
другой, еще один, остальные
Kun: ほか
On: タ
代
5 strokes
Radical: man, human 人 (亻)
Parts: 化 弋
заменять, изменять, конвертировать, заменять, период, возраст, счетчик
Kun: か.わる、 かわ.る、 かわ.り、 か.わり、 -がわ.り、 -が.わり、 か.える、 よ、 しろ
On: ダイ、 タイ
住
7 strokes
Radical: man, human 人 (亻)
Parts: 丶 化 王
обитать, пребывать, жить, населять
Kun: す.む、 す.まう、 -ず.まい
On: ジュウ、 ヂュウ、 チュウ
使
8 strokes
Radical: man, human 人 (亻)
Parts: 一 ノ 化 口
использовать, отправлять на задание, приказывать
Kun: つか.う、 つか.い、 -つか.い、 -づか.い
On: シ
係
9 strokes
Radical: man, human 人 (亻)
Parts: ノ 化 小 幺 糸
ответственность, ответственный человек, связь, долг, забота о себе
Kun: かか.る、 かかり、 -がかり、 かか.わる
On: ケイ
倍
10 strokes
Radical: man, human 人 (亻)
Parts: 化 口 立
удваивать, дважды, раз, складывать
On: バイ
全
6 strokes
Radical: enter 入
Parts: 个 ハ 王
целый, цельный, все, завершающий, исполняющий, полностью, абсолютно
Kun: まった.く、 すべ.て
On: ゼン
具
8 strokes
Radical: eight 八
Parts: 一 ハ 目
инструмент, посуда, средства, имущество, ингредиенты, прилавок, оборудовать, орудие
Kun: そな.える、 つぶさ.に
On: グ
写
5 strokes
Radical: cover 冖
Parts: 一 冖 勹
Variants: 冩 寫
копировать, фотографироваться, описывать
Kun: うつ.す、 うつ.る、 うつ-、 うつ.し
On: シャ、 ジャ
列
6 strokes
Radical: knife, sword 刀 (刂)
Parts: 刈 歹
ряд, файл, строка, ранг, уровень, столбец
On: レツ、 レ
助
7 strokes
Radical: power, force 力
Parts: 力 目
помогите, спасите, ассистируйте
Kun: たす.ける、 たす.かる、 す.ける、 すけ
On: ジョ
勉
10 strokes
Radical: power, force 力
Parts: 儿 力 勹 免
напрягаться, прилагать усилия, поощрять, стремиться, прилагать усилия, прилежный
Kun: つと.める
On: ベン
動
11 strokes
Radical: power, force 力
Parts: 一 ｜ ノ 力 日 里
движение, подвижность, изменение, путаница, сдвиг, встряска
Kun: うご.く、 うご.かす
On: ドウ
勝
12 strokes
Radical: power, force 力
Parts: 二 人 并 力 大 月
победа, побеждать, превозмогать, преуспевать
Kun: か.つ、 -が.ち、 まさ.る、 すぐ.れる、 かつ
On: ショウ
化
4 strokes
Radical: spoon 匕
Parts: 化 匕
изменять, принимать форму, влиять, очаровывать, вводить в заблуждение
Kun: ば.ける、 ば.かす、 ふ.ける、 け.する
On: カ、 ケ
区
4 strokes
Radical: hiding enclosure 匸
Parts: 丶 ノ 匚
Variants: 區
район города, приход, округ
On: ク、 オウ、 コウ
医
7 strokes
Radical: hiding enclosure 匸
Parts: 匚 矢 乞
Variants: 醫
врач, медицина
Kun: い.やす、 い.する、 くすし
On: イ
去
5 strokes
Radical: private 厶
Parts: 厶 土
Variants: 厺
уходить, покидать, ушедший, прошедший, уволившийся, оставляющий, истекающий, устраняющий, разводящийся
Kun: さ.る、 -さ.る
On: キョ、 コ
反
4 strokes
Radical: right hand 又
Parts: 厂 又
против, изгибаться
Kun: そ.る、 そ.らす、 かえ.す、 かえ.る、 -かえ.る
On: ハン、 ホン、 タン、 ホ
取
8 strokes
Radical: right hand 又
Parts: 又 耳
брать, получать, приноси, поднимай
Kun: と.る、 と.り、 と.り-、 とり、 -ど.り
On: シュ
受
8 strokes
Radical: right hand 又
Parts: 冖 又 爪
принимать, претерпевать, отвечать (по телефону), брать, доставать, улавливать, получать
Kun: う.ける、 -う.け、 う.かる
On: ジュ
号
5 strokes
Radical: mouth, opening 口
Parts: 一 勹 口
Variants: 號
псевдоним, номер, предмет, должность, псевдоним, имя, вызов
Kun: さけ.ぶ、 よびな
On: ゴウ"""
        native_kun_on_211_240 = """走
7 strokes
Radical: run 走 (赱)
Parts: 土 走
Variants: 赱
бежать
Kun: はし.る
On: ソウ
止
4 strokes
Radical: stop 止
Parts: 止
останавливаться, остановка
Kun: と.まる、 -ど.まり、 と.める、 -と.める、 -ど.め、 とど.める、 とど.め、 とど.まる、 や.める、 や.む、 -や.む、 よ.す、 -さ.す、 -さ.し
On: シ
活
9 strokes
Radical: water 水 (氵, 氺)
Parts: ノ 十 口 汁 舌
живой, жить
Kun: い.きる、 い.かす、 い.ける
On: カツ
店
8 strokes
Radical: house on cliff 广
Parts: 卜 口 广
магазин
Kun: みせ、 たな
On: テン
買
12 strokes
Radical: shell 貝
Parts: ハ 目 買 貝
покупать
Kun: か.う
On: バイ
売
7 strokes
Radical: scholar, bachelor 士
Parts: 儿 冖 士
Variants: 賣
продавать
Kun: う.る、 う.れる
On: バイ
午
4 strokes
Radical: ten, complete 十
Parts: ノ 十 干 乞
полдень, лошадь (знак гороскопа)
Kun: うま
On: ゴ
汽
7 strokes
Radical: water 水 (氵, 氺)
Parts: 汁 气 乞
пар
On: キ
弓
3 strokes
Radical: bow 弓
Parts: 弓
лук, смычок (стрельба из лука, скрипка)
Kun: ゆみ
On: キュウ
回
6 strokes
Radical: enclosure 囗
Parts: 口 囗
Variants: 囘
время, раунд, игра, вращение, счетчик вхождений
Kun: まわ.る、 -まわ.る、 -まわ.り、 まわ.す、 -まわ.す、 まわ.し-、 -まわ.し、 もとお.る、 か.える
On: カイ、 エ
会
6 strokes
Radical: man, human 人 (亻)
Parts: 二 个 厶
Variants: 會
встреча, знакомиться, вечеринка, ассоциация, собеседование, присоединяться
Kun: あ.う、 あ.わせる、 あつ.まる
On: カイ、 エ
組
11 strokes
Radical: silk 糸 (糹)
Parts: 一 小 幺 目 糸
объединение, заплетать, заплетать косичку, конструировать, собирать, объединять, сотрудничать, схватываться
Kun: く.む、 くみ、 -ぐみ
On: ソ
船
11 strokes
Radical: boat 舟
Parts: ハ 口 舟
Variants: 舩
корабль, лодка
Kun: ふね、 ふな-
On: セン
明
8 strokes
Radical: sun, day 日
Parts: 日 月
Variants: 朙
яркий, светлый
Kun: あ.かり、 あか.るい、 あか.るむ、 あか.らむ、 あき.らか、 あ.ける、 -あ.け、 あ.く、 あ.くる、 あ.かす
On: メイ、 ミョウ、 ミン
社
7 strokes
Radical: sign 示 (礻)
Parts: 土 礼
компания, фирма, офис, ассоциация, святилище
Kun: やしろ
On: シャ
切
4 strokes
Radical: knife, sword 刀 (刂)
Parts: 刀 匕
резать, отсекать, быть острым
Kun: き.る、 -き.る、 き.り、 -き.り、 -ぎ.り、 き.れる、 -き.れる、 き.れ、 -き.れ、 -ぎ.れ
On: セツ、 サイ
電
13 strokes
Radical: rain 雨
Parts: 乙 田 雨
электричество, вспышка
On: デン
毎
6 strokes
Radical: mother, do not 毋 (母, ⺟)
Parts: 毋 母 乞
каждый
Kun: ごと、 -ごと.に
On: マイ
合
6 strokes
Radical: mouth, opening 口
Parts: 一 个 口
подгонка, костюм, соединяться, подходить
Kun: あ.う、 -あ.う、 あ.い、 あい-、 -あ.い、 -あい、 あ.わす、 あ.わせる、 -あ.わせる
On: ゴウ、 ガッ、 カッ
当
6 strokes
Radical: pig snout 彐 (彑)
Parts: 尚 ヨ
Variants: 當
попадать, данный, ударить, удаваться
Kun: あ.たる、 あ.たり、 あ.てる、 あ.て、 まさ.に、 まさ.にべし
On: トウ
台
5 strokes
Radical: mouth, opening 口
Parts: 厶 口
Variants: 臺 坮
тумба, подставка, прилавок для станков и транспортных средств
Kun: うてな、 われ、 つかさ
On: ダイ、 タイ
楽
13 strokes
Radical: tree 木
Parts: 冫 木 白
Variants: 樂
музыка, комфорт, непринужденность
Kun: たの.しい、 たの.しむ、 この.む
On: ガク、 ラク、 ゴウ
公
4 strokes
Radical: eight 八
Parts: ハ 厶
общественность, принц, чиновник, правительство
Kun: おおやけ
On: コウ、 ク
引
4 strokes
Radical: bow 弓
Parts: ｜ 弓
тянуть, перетягивать, дергать рывком, признавать, устанавливать, цитировать, ссылаться на
Kun: ひ.く、 ひ.ける
On: イン
科
9 strokes
Radical: grain 禾
Parts: 斗 禾
отрасль, кафедра, курс, секция
On: カ
歌
14 strokes
Radical: lack, yawn 欠
Parts: 一 亅 口 欠
песня, петь
Kun: うた、 うた.う
On: カ
刀
2 strokes
Radical: knife, sword 刀 (刂)
Parts: 刀
Variants: 釖 刂
меч, сабля, нож
Kun: かたな、 そり
On: トウ
番
12 strokes
Radical: field 田
Parts: 田 米 釆
очередь, номер в серии
Kun: つが.い
On: バン
用
5 strokes
Radical: use 用 (甩)
Parts: 用
использовать, бизнес, услуга, нанимать
Kun: もち.いる
On: ヨウ
何
7 strokes
Radical: man, human 人 (亻)
Parts: 一 亅 化 口
что
Kun: なに、 なん、 なに-、 なん-
On: カ"""
        native_kun_on_181_210 = """図
7 strokes
Radical: enclosure 囗
Parts: 囗 斗
Variants: 圖
карта, чертёж, план
Kun: え、 はか.る
On: ズ、 ト
工
3 strokes
Radical: work 工
Parts: 工
ремесло, строительство, техника
On: コウ、 ク、 グ
教
11 strokes
Radical: rap 攴 (攵)
Parts: 子 老 乞 攵
учить
Kun: おし.える、 おそ.わる
On: キョウ
晴
12 strokes
Radical: sun, day 日
Parts: 二 亠 土 日 月 青
Variants: 暒
прояснять, ясная погода
Kun: は.れる、 は.れ、 は.れ-、 -ば.れ、 は.らす
On: セイ
思
9 strokes
Radical: heart 心 (忄, ⺗)
Parts: 心 田
Variants: 恖
думать
Kun: おも.う、 おもえら.く、 おぼ.す
On: シ
考
6 strokes
Radical: old 老 (耂)
Parts: 勹 老
размышлять, мысль, идея
Kun: かんが.える、 かんが.え
On: コウ
知
8 strokes
Radical: arrow 矢
Parts: 口 矢 乞
знание, мудрость
Kun: し.る、 し.らせる
On: チ
才
3 strokes
Radical: hand 手 (扌龵)
Parts: 一 ノ 亅
талант, дарование
On: サイ
理
11 strokes
Radical: jade (king) 玉 (王)
Parts: 王 里
принцип, довод, аргумент
Kun: ことわり
On: リ
算
14 strokes
Radical: bamboo 竹 (⺮)
Parts: 廾 目 竹 乞
вычислять, считать
Kun: そろ
On: サン
作
7 strokes
Radical: man, human 人 (亻)
Parts: 一 ｜ ノ 化 乞
делать, создавать
Kun: つく.る、 つく.り、 -づく.り
On: サク、 サ
元
4 strokes
Radical: legs 儿
Parts: 二 儿 元
начало, основание
Kun: もと
On: ゲン、 ガン
食
9 strokes
Radical: eat, food 食 (飠)
Parts: 食
еда, кушать
Kun: く.う、 く.らう、 た.べる、 は.む
On: ショク、 ジキ
肉
6 strokes
Radical: meat 肉 (⺼)
Parts: 人 冂 肉
мясо
Kun: しし
On: ニク
馬
10 strokes
Radical: horse 馬
Parts: 杰 馬
лошадь
Kun: うま、 うま-、 ま
On: バ
牛
4 strokes
Radical: cow 牛 (牜)
Parts: 牛
корова
Kun: うし
On: ギュウ
魚
11 strokes
Radical: fish 魚
Parts: 杰 田 魚
рыба
Kun: うお、 さかな、 -ざかな
On: ギョ
鳥
11 strokes
Radical: bird 鳥
Parts: 杰 鳥
птица
Kun: とり
On: チョウ
羽
6 strokes
Radical: feather 羽
Parts: 冫 羽
перо
Kun: は、 わ、 はね
On: ウ
鳴
14 strokes
Radical: bird 鳥
Parts: 口 杰 鳥
чирикать, плакать,
Kun: な.く、 な.る、 な.らす
On: メイ
麦
7 strokes
Radical: wheat 麥
Parts: 二 亠 土 夂 麦
Variants: 麥
хлебные злаки
Kun: むぎ
On: バク
米
6 strokes
Radical: rice 米
Parts: 米
рис
Kun: こめ、 よね
On: ベイ、 マイ、 メエトル
茶
9 strokes
Radical: grass 艸 (艹)
Parts: 个 艾 木
чай
On: チャ、 サ
色
6 strokes
Radical: colour, prettiness 色
Parts: 勹 巴 色
цвет
Kun: いろ
On: ショク、 シキ
黄
11 strokes
Radical: yellow 黃
Parts: ハ 田 黄
жёлтый
Kun: き、 こ-
On: コウ、 オウ
黒
11 strokes
Radical: black 黑
Parts: 杰 里 黒
чёрный
Kun: くろ、 くろ.ずむ、 くろ.い
On: コク
来
7 strokes
Radical: tree 木
Parts: ｜ 二 亠 木 米
Variants: 來
приходить, прибывать
Kun: く.る、 きた.る、 きた.す、 き.たす、 き.たる、 き、 こ
On: ライ、 タイ
行
6 strokes
Radical: go, do 行
Parts: 彳 行
идти, ходить, совершать
Kun: い.く、 ゆ.く、 -ゆ.き、 -ゆき、 -い.き、 -いき、 おこな.う、 おこ.なう
On: コウ、 ギョウ、 アン
帰
10 strokes
Radical: turban, scarf 巾
Parts: 冖 刈 巾 ヨ
Variants: 歸 皈
возвращаться
Kun: かえ.る、 かえ.す、 おく.る、 とつ.ぐ
On: キ
歩
8 strokes
Radical: stop 止
Parts: ノ 小 止
ходить, идти
Kun: ある.く、 あゆ.む
On: ホ、 ブ、 フ"""
        native_kun_on_151_180 = """原
10 strokes
Radical: cliff 厂
Parts: 厂 小 白
Variants: 厡
луг, поле, равнина
Kun: はら
On: ゲン
里
7 strokes
Radical: village, mile 里
Parts: 里
деревня, родина
Kun: さと
On: リ
市
5 strokes
Radical: turban, scarf 巾
Parts: 亠 巾
город, рынок
Kun: いち
On: シ
京
8 strokes
Radical: lid 亠
Parts: 亠 口 小
Variants: 亰
столица
Kun: みやこ
On: キョウ、 ケイ、 キン
風
9 strokes
Radical: wind 風
Parts: ノ 几 虫 風
Variants: 凮 飌
ветер, воздух
Kun: かぜ、 かざ-
On: フウ、 フ
雪
11 strokes
Radical: rain 雨
Parts: ヨ 雨
снег
Kun: ゆき
On: セツ
雲
12 strokes
Radical: rain 雨
Parts: 一 二 厶 雨
облако, туча
Kun: くも、 -ぐも
On: ウン
池
6 strokes
Radical: water 水 (氵, 氺)
Parts: 汁 也
пруд, бассейн, водохранилище
Kun: いけ
On: チ
海
9 strokes
Radical: water 水 (氵, 氺)
Parts: 汁 毋 母 乞
море, океан
Kun: うみ
On: カイ
岩
8 strokes
Radical: mountain 山
Parts: 口 山 石
валун, скала, утёс
Kun: いわ
On: ガン
星
9 strokes
Radical: sun, day 日
Parts: 日 生
Variants: 皨
звезда
Kun: ほし、 -ぼし
On: セイ、 ショウ
室
9 strokes
Radical: roof 宀
Parts: 厶 土 宀 至
комната, теплица, погреб
Kun: むろ
On: シツ
戸
4 strokes
Radical: door, house 戶 (户, 戸)
Parts: 一 尸 戸
дверь, ставня
Kun: と
On: コ
家
10 strokes
Radical: roof 宀
Parts: 宀 豕
дом, приют, семья
Kun: いえ、 や、 うち
On: カ、 ケ
寺
6 strokes
Radical: thumb, inch 寸
Parts: 土 寸
буддийский храм
Kun: てら
On: ジ
通
10 strokes (also 9)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: マ 込 用
движение, проход, поездка
Kun: とお.る、 とお.り、 -とお.り、 -どお.り、 とお.す、 とお.し、 -どお.し、 かよ.う
On: ツウ、 ツ
門
8 strokes
Radical: gate 門
Parts: 門
ворота
Kun: かど、 と
On: モン
道
12 strokes (also 11)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 并 込 自 首
Variants: 噵 衜 衟
дорога, путь, курс
Kun: みち、 いう
On: ドウ、 トウ
話
13 strokes
Radical: speech 言 (訁)
Parts: 口 舌 言
сказка, беседа, разговор
Kun: はな.す、 はなし
On: ワ
言
7 strokes
Radical: speech 言 (訁)
Parts: 言
говорить, сказать, слово
Kun: い.う、 こと
On: ゲン、 ゴン
答
12 strokes
Radical: bamboo 竹 (⺮)
Parts: 一 个 口 竹 乞
решение, ответ
Kun: こた.える、 こた.え
On: トウ
声
7 strokes
Radical: scholar, bachelor 士
Parts: 士 尸
Variants: 聲
голос
Kun: こえ、 こわ-
On: セイ、 ショウ
聞
14 strokes
Radical: ear 耳
Parts: 耳 門
Variants:
слышать, спрашивать
Kun: き.く、 き.こえる
On: ブン、 モン
語
14 strokes
Radical: speech 言 (訁)
Parts: 口 五 言
слово, речь, язык
Kun: かた.る、 かた.らう
On: ゴ
読
14 strokes
Radical: speech 言 (訁)
Parts: 儿 冖 士 言
Variants: 讀
читать
Kun: よ.む、 -よ.み
On: ドク、 トク、 トウ
書
10 strokes
Radical: say 曰
Parts: 日 聿
писать
Kun: か.く、 -が.き、 -がき
On: ショ
記
10 strokes
Radical: speech 言 (訁)
Parts: 已 言
отчет, записывать
Kun: しる.す
On: キ
紙
10 strokes
Radical: silk 糸 (糹)
Parts: 小 幺 氏 糸
Variants: 帋
бумага
Kun: かみ
On: シ
画
8 strokes
Radical: field 田
Parts: 一 凵 田
Variants: 畫
картина, план
Kun: えが.く、 かく.する、 かぎ.る、 はかりごと、 はか.る
On: ガ、 カク、 エ、 カイ
絵
12 strokes
Radical: silk 糸 (糹)
Parts: 二 个 厶 小 幺 糸
Variants: 繪
картина, рисунок, эскиз
On: カイ、 エ"""
        native_kun_on4 = """朝
12 strokes
Radical: moon, month 月
Parts: 十 日 月
утро, эпоха, период
Kun: あさ
On: チョウ
昼
9 strokes
Radical: sun, day 日
Parts: 一 丶 尸 日
Variants: 晝
дневное время, полдень
Kun: ひる
On: チュウ
夜
8 strokes
Radical: evening, sunset 夕
Parts: 亠 化 夕
ночь, вечер
Kun: よ、 よる
On: ヤ
分
4 strokes
Radical: knife, sword 刀 (刂)
Parts: ハ 刀
часть, минута, сегмент, доля, понимать, шанс
Kun: わ.ける、 わ.け、 わ.かれる、 わ.かる、 わ.かつ
On: ブン、 フン、 ブ
週
11 strokes (also 10)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 冂 込 口 土
неделя
On: シュウ
春
9 strokes
Radical: sun, day 日
Parts: 一 二 人 大 日
Variants: 旾
весна
Kun: はる
On: シュン
夏
10 strokes
Radical: go slowly 夊
Parts: 一 夂 目 自
Variants: 夓
лето
Kun: なつ
On: カ、 ガ、 ゲ
秋
9 strokes
Radical: grain 禾
Parts: 火 禾
Variants: 穐 龝
осень
Kun: あき、 とき
On: シュウ
冬
5 strokes
Radical: ice 冫
Parts: 丶 夂 攵
зима
Kun: ふゆ
On: トウ
今
4 strokes
Radical: man, human 人 (亻)
Parts: 一 个
сейчас
Kun: いま
On: コン、 キン
新
13 strokes
Radical: axe 斤
Parts: 亠 并 斤 木 立 辛
новый
Kun: あたら.しい、 あら.た、 あら-、 にい-
On: シン
古
5 strokes
Radical: mouth, opening 口
Parts: 十 口
старый
Kun: ふる.い、 ふる-、 -ふる.す
On: コ
間
12 strokes
Radical: gate 門
Parts: 日 門
Variants:
интервал, пробел
Kun: あいだ、 ま、 あい
On: カン、 ケン
方
4 strokes
Radical: square 方
Parts: 方
направление, альтернатива
Kun: かた、 -かた、 -がた
On: ホウ
北
5 strokes
Radical: spoon 匕
Parts: 匕 爿
север
Kun: きた
On: ホク
南
9 strokes
Radical: ten, complete 十
Parts: 并 冂 十 干
юг
Kun: みなみ
On: ナン、 ナ
東
8 strokes
Radical: tree 木
Parts: 一 ｜ 日 木 田
восток
Kun: ひがし
On: トウ
西
6 strokes
Radical: west 西 (襾, 覀)
Parts: 西
Variants:
запад
Kun: にし
On: セイ、 サイ、 ス
遠
13 strokes (also 12)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 込 口 土 衣
далёкий, отдалённый
Kun: とお.い
On: エン、 オン
近
7 strokes (also 6)
Radical: walk 辵 (辶, ⻌, ⻍)
Parts: 込 斤
близкий, ранний, равнозначный
Kun: ちか.い
On: キン、 コン
前
9 strokes
Radical: knife, sword 刀 (刂)
Parts: 一 并 刈 月
впереди
Kun: まえ、 -まえ
On: ゼン
後
9 strokes
Radical: step 彳
Parts: 夂 幺 彳
позади
Kun: のち、 うし.ろ、 うしろ、 あと、 おく.れる
On: ゴ、 コウ
内
4 strokes
Radical: open country 冂
Parts: 人 冂
внутри, между, среди
Kun: うち
On: ナイ、 ダイ
外
5 strokes
Radical: evening, sunset 夕
Parts: 卜 夕
снаружи
Kun: そと、 ほか、 はず.す、 はず.れる、 と-
On: ガイ、 ゲ
場
12 strokes
Radical: earth 土
Parts: 一 土 日 勿
Variants: 塲
местоположение, место
Kun: ば
On: ジョウ、 チョウ
地
6 strokes
Radical: earth 土
Parts: 土 也
земля, почва
On: チ、 ジ
国
8 strokes
Radical: enclosure 囗
Parts: 丶 囗 王
Variants: 國 圀
страна
Kun: くに
On: コク
園
13 strokes
Radical: enclosure 囗
Parts: 口 囗 土 衣
Variants: 薗
парк, сад, двор, ферма
Kun: その
On: エン
谷
7 strokes
Radical: valley 谷
Parts: 个 ハ 口 谷
долина
Kun: たに、 きわ.まる
On: コク
野
11 strokes
Radical: village, mile 里
Parts: 亅 矛 里
Variants: 埜 壄
равнины, поля
Kun: の、 の-
On: ヤ、 ショ"""
        native_kun_on3 = """弱
10 strokes
Radical: bow 弓
Parts: 冫 弓
слабый, хилый
Kun: よわ.い、 よわ.る、 よわ.まる、 よわ.める
On: ジャク
強
11 strokes
Radical: bow 弓
Parts: 厶 弓 虫
сильный, мощный
Kun: つよ.い、 つよ.まる、 つよ.める、 し.いる、 こわ.い
On: キョウ、 ゴウ
高
10 strokes
Radical: tall 高 (髙)
Parts: 亠 冂 口 高
высокий, дорогой
Kun: たか.い、 たか、 -だか、 たか.まる、 たか.める
On: コウ
同
6 strokes
Radical: mouth, opening 口
Parts: 一 冂 口
равный, одинаковый, такой же, соглашаться
Kun: おな.じ
On: ドウ
親
16 strokes
Radical: see 見
Parts: 亠 并 木 立 見 辛
родитель, близость, родственник
Kun: おや、 おや-、 した.しい、 した.しむ
On: シン
母
5 strokes
Radical: mother, do not 毋 (母, ⺟)
Parts: 毋 母
мать
Kun: はは、 も
On: ボ
父
4 strokes
Radical: father 父
Parts: 父
отец
Kun: ちち
On: フ
姉
8 strokes
Radical: woman, female 女
Parts: 亠 女 巾
Variants: 姊
старшая сестра
Kun: あね、 はは
On: シ
兄
5 strokes
Radical: legs 儿
Parts: 儿 口
старший брат
Kun: あに
On: ケイ、 キョウ
弟
7 strokes
Radical: bow 弓
Parts: ｜ ノ 并 弓
младший брат
Kun: おとうと
On: テイ、 ダイ、 デ
妹
8 strokes
Radical: woman, female 女
Parts: ｜ 二 亠 ハ 女 木
младшая сестра
Kun: いもうと
On: マイ
自
6 strokes
Radical: self 自
Parts: 目 自
сам, лично, самостоятельно
Kun: みずか.ら、 おの.ずから、 おの.ずと
On: ジ、 シ
友
4 strokes
Radical: right hand 又
Parts: 一 ノ 又
друг
Kun: とも
On: ユウ
体
7 strokes
Radical: man, human 人 (亻)
Parts: 一 化 木
Variants: 躰 軆 體 骵
тело, вещество, объект
Kun: からだ、 かたち
On: タイ、 テイ
毛
4 strokes
Radical: fur, hair 毛
Parts: 毛
мех, шерсть, волос, перо
Kun: け
On: モウ
頭
16 strokes
Radical: leaf 頁
Parts: ハ 并 口 目 豆 貝 頁
голова, глава
Kun: あたま、 かしら、 -がしら、 かぶり
On: トウ、 ズ、 ト
顔
18 strokes
Radical: leaf 頁
Parts: 亠 ハ 厂 彡 目 立 貝 頁
Variants: 顏
лицо, выражение
Kun: かお
On: ガン
首
9 strokes
Radical: head 首
Parts: 并 目 自 首
шея
Kun: くび
On: シュ
心
4 strokes
Radical: heart 心 (忄, ⺗)
Parts: 心
Variants: 忄
сердце, ум, душа
Kun: こころ、 -ごころ
On: シン
時
10 strokes
Radical: sun, day 日
Parts: 土 寸 日
Variants: 旹
время, час
Kun: とき、 -どき
On: ジ
曜
18 strokes
Radical: sun, day 日
Parts: ヨ 日 隹
день недели
On: ヨウ"""
        native_kun_on2 = """空
8 strokes
Radical: cave 穴
Parts: 儿 宀 工 穴
пустота, небо, вакуум, свободное пространство
Kun: そら、 あ.く、 あ.き、 あ.ける、 から、 す.く、 す.かす、 むな.しい
On: クウ
糸
6 strokes
Radical: silk 糸 (糹)
Parts: 小 幺 糸
Variants: 絲
нить, леска
Kun: いと
On: シ
数
13 strokes
Radical: rap 攴 (攵)
Parts: 夂 女 米 乞 攵
Variants: 數
число, цифра, количество, закон
Kun: かず、 かぞ.える、 しばしば、 せ.める、 わずらわ.しい
On: スウ、 ス、 サク、 ソク、 シュ
多
6 strokes
Radical: evening, sunset 夕
Parts: 夕
Variants: 夛
много, часто
Kun: おお.い、 まさ.に、 まさ.る
On: タ
少
4 strokes
Radical: small, insignificant 小
Parts: ノ 小
немного, мало
Kun: すく.ない、 すこ.し
On: ショウ
万
3 strokes
Radical: one 一
Parts: 一 ｜ ノ
Variants: 萬
десять тысяч, 10000
Kun: よろず
On: マン、 バン
半
5 strokes
Radical: ten, complete 十
Parts: ｜ 二 并 十
половина, средний
Kun: なか.ば
On: ハン
形
7 strokes
Radical: bristle, beard 彡
Parts: 一 ノ 二 廾 彡
форма, вид, стиль, облик, образ
Kun: かた、 -がた、 かたち、 なり
On: ケイ、 ギョウ
太
4 strokes
Radical: big, very 大
Parts: 丶 大
полнеть, толстый
Kun: ふと.い、 ふと.る
On: タイ、 タ
細
11 strokes
Radical: silk 糸 (糹)
Parts: 小 幺 田 糸
утонченный, похудеть, сужение, стройный, подробный, точный
Kun: ほそ.い、 ほそ.る、 こま.か、 こま.かい
On: サイ
広
5 strokes
Radical: house on cliff 广
Parts: 厶 广
Variants: 廣
широкий, обширный, просторный
Kun: ひろ.い、 ひろ.まる、 ひろ.める、 ひろ.がる、 ひろ.げる
On: コウ
長
8 strokes
Radical: long, grow 長 (镸)
Parts: 長
Variants: 兏 镸
длинный, лидер, превосходящий, старший
Kun: なが.い、 おさ
On: チョウ
点
9 strokes
Radical: fire 火 (灬)
Parts: 卜 口 杰
Variants: 點
пятно, точка, отметка, частичка
Kun: つ.ける、 つ.く、 た.てる、 さ.す、 とぼ.す、 とも.す、 ぼち
On: テン
丸
3 strokes
Radical: dot 丶
Parts: 丶 九
круглый, таблетки, свернуть
Kun: まる、 まる.める、 まる.い
On: ガン
交
6 strokes
Radical: lid 亠
Parts: 亠 父
смешивать, сочетать, объединение, пересекать
Kun: まじ.わる、 まじ.える、 ま.じる、 まじ.る、 ま.ざる、 ま.ぜる、 -か.う、 か.わす、 かわ.す、 こもごも
On: コウ
光
6 strokes
Radical: legs 儿
Parts: 一 儿 尚
Variants: 灮 炗
луч, свет, сверкать
Kun: ひか.る、 ひかり
On: コウ
角
7 strokes
Radical: horn 角
Parts: ｜ 勹 月 角
угол, площадь
Kun: かど、 つの
On: カク
計
9 strokes
Radical: speech 言 (訁)
Parts: 十 言
спланировать, измерять, замышлять
Kun: はか.る、 はか.らう
On: ケイ
直
8 strokes
Radical: eye 目
Parts: 一 ｜ 十 目
прямой, откровенность, честный, исправить, чинить
Kun: ただ.ちに、 なお.す、 -なお.す、 なお.る、 なお.き、 す.ぐ
On: チョク、 ジキ、 ジカ
線
15 strokes
Radical: silk 糸 (糹)
Parts: 小 幺 水 白 糸
Variants: 綫
линия, дорожка
Kun: すじ
On: セン
矢
5 strokes
Radical: arrow 矢
Parts: 一 ノ 大 矢 乞
дротик, стрела
Kun: や
On: シ"""
        native_kun_on = """校
10 strokes
Radical: tree 木
Parts: 亠 木 父
экзамен, школа, доказательство, исправление
On: コウ、 キョウ
本
5 strokes
Radical: tree 木
Parts: 一 木
Variants: 夲
книга, главный, источник, истинный
Kun: もと
On: ホン
文
4 strokes
Radical: script, literature 文
Parts: 文
предложение, литература, стиль, искусство
Kun: ふみ、 あや
On: ブン、 モン
字
6 strokes
Radical: child, seed 子
Parts: 子 宀
символ, буква, иероглиф
Kun: あざ、 あざな、 -な
On: ジ
名
6 strokes
Radical: mouth, opening 口
Parts: 口 夕
имя, репутация, уважаемый
Kun: な、 -な
On: メイ、 ミョウ
学
8 strokes
Radical: child, seed 子
Parts: 冖 子 尚
Variants: 學 斈 斅
изучать, учить, наука
Kun: まな.ぶ
On: ガク
先
6 strokes
Radical: legs 儿
Parts: ノ 儿 土
до, впереди, предыдущий, старшинство
Kun: さき、 ま.ず
On: セン
立
5 strokes
Radical: stand, erect 立
Parts: 立
вставать, подниматься, основать, возводить
Kun: た.つ、 -た.つ、 た.ち-、 た.てる、 -た.てる、 た.て-、 たて-、 -た.て、 -だ.て、 -だ.てる
On: リツ、 リュウ、 リットル
早
6 strokes
Radical: sun, day 日
Parts: 十 日
рано, быстро
Kun: はや.い、 はや、 はや-、 はや.まる、 はや.める、 さ-
On: ソウ、 サッ
休
6 strokes
Radical: man, human 人 (亻)
Parts: 化 木
отдых, выходной, спать
Kun: やす.む、 やす.まる、 やす.める
On: キュウ
町
7 strokes
Radical: field 田
Parts: 一 亅 田
Variants: 甼
небольшой город, квартал, улица
Kun: まち
On: チョウ
村
7 strokes
Radical: tree 木
Parts: 寸 木
деревня, село
Kun: むら
On: ソン
王
4 strokes
Radical: jade (king) 玉 (王)
Parts: 王
король, магнат, царь, правитель
On: オウ、 -ノウ
年
6 strokes
Radical: pestle 干
Parts: 一 ノ 干 乞
Variants: 秊
год, срок
Kun: とし
On: ネン
車
7 strokes
Radical: cart, car 車
Parts: 車
машина, повозка, фургон, вагон, колесо
Kun: くるま
On: シャ
入
2 strokes
Radical: enter 入
Parts: 入
вход, вставлять
Kun: い.る、 -い.る、 -い.り、 い.れる、 -い.れ、 はい.る
On: ニュウ、 ジュ
出
5 strokes
Radical: container, open mouth 凵
Parts: ｜ 山 凵
выход, покидать, выводить из себя, выпирать
Kun: で.る、 -で、 だ.す、 -だ.す、 い.でる、 い.だす
On: シュツ、 スイ
玉
5 strokes
Radical: jade (king) 玉 (王)
Parts: 丶 王
драгоценность, шарик, бусинка
Kun: たま、 たま-、 -だま
On: ギョク"""
        geo1 = """Нигерия; Федеративная Республика Нигерия
государство в Западной Африке.
Nigeria; Federal Republic of Nigeria
Абуджа; Abuja
английский; English
NGN, найра; Nigerian naira
Тунис; Тунисская Республика
государство на крайнем севере Африки.
Tunisia; Republic of Tunisia
Тунис; Tunis
арабский; Arabic
TND, Тунисский динар; Tunisian dinar
Бангладеш; Народная Республика Бангладеш
государство в Южной Азии.
Bangladesh; People's Republic of Bangladesh
Дакка; Dhaka
бенгальский; Bengali
BDT, Бангладешская така; Bangladeshi taka
Таджикистан; Республика Таджикистан
государство в Центральной Азии.
Tajikistan; Republic of Tajikistan
Душанбе; Dushanbe
Таджикский; Tajik
TJS, Сомони; Tajikistani somoni
Непал; Федеративная Демократическая Республика Непал
государство в Гималаях в Южной Азии.
Nepal; Federal Democratic Republic of Nepal
Катманду; Kathmandu
Непальский; Nepali
NPR, Непальская рупия; Nepalese rupee
Греция; Греческая Республика
государство в Южной Европе.
Greece; Hellenic Republic
Афины; Athens
Греческий; Greek
EUR, Евро; Euro
Никарагуа; Республика Никарагуа
государство в Центральной Америке.
Nicaragua; Republic of Nicaragua
Манагуа; Managua
Испанский; Spanish
NIO, Никарагуанская кордоба; Nicaraguan córdoba
Эритрея; Государство Эритрея
государство в Восточной Африке.
Eritrea; State of Eritrea
Асмэра; Asmara
Арабский, Английский; Arabic, English
ERN, Эритрейская накфа; Eritrean nakfa
Корейская Народно-Демократическая Республика; КНДР; Северная Корея
государство в Восточной Азии.
Democratic People's Republic of Korea; DPRK; North Korea
Пхеньян; Pyongyang
Корейский; Korean
KPW, Северокорейская вона; North Korean won
Малави; Республика Малави
государство в регионе Южная Африка.
Malawi; Republic of Malawi
Лилонгве; Lilongwe
Английский, Чива (Ньянджа); English, Chewa (Nyanja)
MWK, Малавийская квача; Malawian kwacha
Бенин; Республика Бенин
государство в Западной Африке.
Benin; Republic of Benin
Порто-Ново; Porto-Novo
Французский; French
XOF, Западноафриканский франк КФА; West African CFA franc
Гондурас; Республика Гондурас
государство в Центральной Америке.
Honduras; Republic of Honduras
Тегусигальпа; Tegucigalpa
Испанский; Spanish
HNL, Гондурасская лемпира; Honduran lempira
Либерия; Республика Либерия
государство в Западной Африке.
Liberia; Republic of Liberia
Монровия; Monrovia
Английский; English
LRD, Либерийский доллар; Liberian dollar
Болгария; Республика Болгария
государство в Юго-Восточной Европе.
Bulgaria; Republic of Bulgaria
София; Sofia
Болгарский; Bulgarian
BGN, Болгарский лев; Bulgarian lev
Куба; Республика Куба
островное государство в Латинской Америке, в Карибском бассейне.
Cuba; Republic of Cuba
Гавана; Havana
Испанский; Spanish
CUP, Кубинское песо; Cuban peso
Гватемала; Республика Гватемала
государство в Центральной Америке.
Guatemala; Republic of Guatemala
Гватемала; Guatemala City
Испанский; Spanish
GTQ, Гватемальский кетсаль; Guatemalan quetzal
Исландия
островное государство, расположенное на западе Северной Европы.
Iceland
Рейкьявик; Reykjavík
Исландский; Icelandic
ISK, Исландская крона; Icelandic króna
Республика Корея; Южная Корея
государство в Восточной Азии.
Republic of Korea; South Korea
Сеул; Seoul
Корейский; Korean
KRW, Южнокорейская вона; South Korean won
Венгрия
государство в Центральной Европе.
Hungary
Будапешт; Budapest
Венгерский; Hungarian
HUF, Форинт; Hungarian forint
Португалия; Португальская Республика
государство в Южной Европе.
Portugal; Portuguese Republic
Лиссабон; Lisbon
Португальский; Portuguese
EUR, Евро; Euro
Иордания; Иорданское Хашимитское Королевство
государство на Ближнем Востоке.
Jordan; Hashemite Kingdom of Jordan
Амман; Amman
Арабский; Arabic
JOD, Иорданский динар; Jordanian dinar
Сербия; Республика Сербия
государство в юго-восточной Европе.
Serbia; Republic of Serbia
Белград; Belgrade
Сербский; Serbian
RSD, Сербский динар; Serbian dinar
Азербайджан; Азербайджанская Республика
государство в восточной части Закавказья на побережье Каспийского моря.
Azerbaijan; Republic of Azerbaijan
Баку; Baku
Азербайджанский; Azerbaijani
AZN, Азербайджанский манат; Azerbaijani manat
Австрия; Австрийская Республика
государство в Центральной Европе.
Austria; Republic of Austria
Вена; Vienna
Австрийский немецкий; Austrian German
EUR, Евро; Euro
Объединённые Арабские Эмираты; ОАЭ
государство на Ближнем Востоке.
United Arab Emirates; UAE
Абу-Даби; Abu Dhabi
Арабский, Английский; Arabic, English
AED, Дирхам ОАЭ; United Arab Emirates dirham
Чехия; Чешская Республика
государство в Центральной Европе.
Czechia; Czech Republic
Прага; Prague
Чешский; Czech
CZK, Чешская крона; Czech koruna
Панама; Республика Панама
государство в Центральной Америке.
Panama; Republic of Panama
Панама; Panama City
Испанский; Spanish
PAB, USD, Панамский бальбоа, Доллар США; Panamanian balboa, United States dollar
Сьерра-Леоне; Республика Сьерра-Леоне
государство в Западной Африке.
Sierra Leone; Republic of Sierra Leone
Фритаун; Freetown
Крио, Английский; Krio, English
SLE, Леоне; Sierra Leonean leone
Ирландия; Республика Ирландия
государство в Северной Европе.
Ireland; Republic of Ireland
Дублин; Dublin
Ирландский, Английский; Irish, English
EUR, Евро; Euro
Грузия
государство, расположенное в западной части Закавказья.
Georgia
Тбилиси; Tbilisi
Грузинский; Georgian
GEL, Грузинский лари; Georgian lari
Шри-Ланка; Демократическая Социалистическая Республика Шри-Ланка
островное государство в Южной Азии.
Sri Lanka; Democratic Socialist Republic of Sri Lanka
Шри-Джаяварденепура-Котте; Sri Jayawardenepura Kotte
Тамильский, Сингальский; Tamil, Sinhala
LKR, Шри-ланкийская рупия; Sri Lankan rupee
Литва; Литовская Республика
государство, расположенное в Северной Европе.
Lithuania; Republic of Lithuania
Вильнюс; Vilnius
Литовский; Lithuanian
EUR, Евро; Euro
Латвия; Латвийская Республика
государство в Северной Европе.
Latvia; Republic of Latvia
Рига; Riga
Латышский; Latvian
EUR, Евро; Euro
Того; Тоголезская Республика
государство в Западной Африке.
Togo; Togolese Republic
Ломе; Lomé
Французский; French
XOF, Западноафриканский франк КФА; West African CFA franc
Хорватия; Республика Хорватия
государство на юге Центральной Европы.
Croatia; Republic of Croatia
Загреб; Zagreb
Хорватский; Croatian
EUR, Евро; Euro"""
        geo2 = """Босния и Герцеговина
государство в Юго-Восточной Европе, в западной части Балканского полуострова.
Bosnia and Herzegovina
Сараево; Sarajevo
боснийский, сербский, хорватский; Bosnian, Serbian, Croatian
BAM, Конвертируемая марка; Bosnia and Herzegovina convertible mark
Коста-Рика; Республика Коста-Рика
государство в Центральной Америке.
Costa Rica; Republic of Costa Rica
Сан-Хосе; San José
Испанский; Spanish
CRC, Коста-риканский колон; Costa Rican colón
Словакия; Словацкая Республика
государство в Центральной Европе.
Slovakia; Slovak Republic
Братислава; Bratislava
Словацкий; Slovak
EUR, Евро; Euro
Доминиканская Республика
государство в восточной части острова Гаити (Карибское море) и на прибрежных островах.
Dominican Republic
Санто-Доминго; Santo Domingo
Испанский; Spanish
DOP, Доминиканское песо; Dominican peso
Эстония; Эстонская Республика
государство, расположенное в Северной Европе на восточном побережье Балтийского моря.
Estonia; Republic of Estonia
Таллин; Tallinn
Эстонский; Estonian
EUR, Евро; Euro
Дания; Королевство Дания
государство в Северной Европе.
Denmark; Kingdom of Denmark
Копенгаген; Copenhagen
Датский; Danish
DKK, Датская крона; Danish krone
Нидерланды, Голландия; Королевство Нидерландов
государство, состоящее из основной территории в Западной Европе и островов в Карибском море.
Netherlands, Holland; Kingdom of the Netherlands
Амстердам; Amsterdam
Нидерландский (голландский); Dutch
EUR, Евро; Euro
Швейцария; Швейцарская Конфедерация
государство в Западной Европе.
Switzerland; Swiss Confederation
Берн; Bern
Немецкий, Итальянский, Французский; German, Italian, French
CHF, Швейцарский франк; Swiss franc
Бутан; Королевство Бутан
государство в Южной Азии.
Bhutan; Kingdom of Bhutan
Тхимпху; Thimphu
Дзонг-кэ; Dzongkha
BTN, Нгултрум; Bhutanese ngultrum
Гвинея-Бисау; Республика Гвинея-Бисау
государство в Западной Африке.
Guinea-Bissau; Republic of Guinea-Bissau
Бисау; Bissau
Португальский; Portuguese
XOF, Западноафриканский франк КФА; West African CFA franc
Молдавия; Республика Молдова
государство в Юго-Восточной Европе.
Moldova; Republic of Moldova
Кишинёв; Kishinev
Румынский; Romanian
MDL, Молдавский лей; Moldovan leu
Бельгия; Королевство Бельгия
государство, находящееся на северо-западе Европы.
Belgium; Kingdom of Belgium
Брюссель; City of Brussels
Нидерландский (голландский), Немецкий, Французский; Dutch, German, French
EUR, Евро; Euro
Лесото; Королевство Лесото
государство-анклав в Южной Африке.
Lesotho; Kingdom of Lesotho
Масеру; Maseru
Сесото, английский; Sotho, English
ZAR, LSL, Южноафриканский рэнд, Лоти Лесото; South African rand, Lesotho loti
Армения; Республика Армения
государство в Закавказье, расположено на севере Передней Азии.
Armenia; Republic of Armenia
Ереван; Yerevan
Армянский; Armenian
AMD, Армянский драм; Armenian dram
Албания; Республика Албания
государство в западной части Балканского полуострова.
Albania; Republic of Albania
Тирана; Tirana
Албанский; Albanian
ALL, Албанский лек; Albanian lek
Соломоновы Острова
государство в юго-западной части Тихого океана.
Solomon Islands
Хониара; Honiara
Английский; English
SBD, Доллар Соломоновых Островов; Solomon Islands dollar
Экваториальная Гвинея; Республика Экваториальная Гвинея
государство в Центральной Африке.
Equatorial Guinea; Republic of Equatorial Guinea
Малабо; Malabo
Испанский, Португальский, Французский; Spanish, Portuguese, French
XAF, Центральноафриканский франк КФА; Central African CFA franc
Бурунди; Республика Бурунди
государство в Восточной Африке.
Burundi; Republic of Burundi
Гитега; Gitega
Рунди, Французский, Английский; Kirundi, French, English
BIF, Бурундийский франк; Burundian franc
Гаити; Республика Гаити
государство в западной части одноимённого острова и на ряде прибрежных островов.
Haiti; Republic of Haiti
Порт-о-Пренс; Port-au-Prince
Гаитянский креольский, Французский; Haitian Creole, French
HTG, Гаитянский гурд; Haitian gourde
Руанда; Республика Руанда
государство в Восточной Африке.
Rwanda; Republic of Rwanda
Кигали; Kigali
Руанда, Английский, Французский, Суахили; Kinyarwanda, English, French, Swahili
RWF, Франк Руанды; Rwandan franc
Северная Македония; Республика Северная Македония
государство на юго-востоке Европы, на Балканском полуострове.
North Macedonia; Republic of North Macedonia
Скопье; Skopje
Македонский, Албанский; Macedonian, Albanian
MKD, Македонский денар; Macedonian denar
Джибути; Республика Джибути
государство в Восточной Африке.
Djibouti; Republic of Djibouti
Джибути; Djibouti City
арабский, Французский; Arabic, French
DJF, Франк Джибути; Djiboutian franc
Белиз
государство в Центральной Америке.
Belize
Бельмопан; Belmopan
Английский; English
BZD, Белизский доллар; Belize dollar
Израиль; Государство Израиль
государство на Ближнем Востоке.
Israel; State of Israel
Иерусалим; Jerusalem
Иврит; Hebrew
ILS, Новый израильский шекель; Israeli new shekel
Сальвадор; Республика Эль-Сальвадор
государство в Центральной Америке.
El Salvador; Republic of El Salvador
Сан-Сальвадор; San Salvador
Испанский; Spanish
USD, BTC, Доллар США, Биткойн; United States dollar, Bitcoin
Словения; Республика Словения
государство в Южной Европе.
Slovenia; Republic of Slovenia
Любляна; Ljubljana
Словенский; Slovenian
EUR, Евро; Euro
Фиджи; Республика Фиджи
государство в Океании на востоке Меланезии.
Fiji; Republic of Fiji
Сува; Suva
Английский, Хиндустани; English, Hindustani
FJD, Доллар Фиджи; Fijian dollar
Кувейт; Государство Кувейт
государство в юго-западной Азии.
Kuwait; State of Kuwait
Эль-Кувейт; Kuwait City
арабский; Arabic
KWD, Кувейтский динар; Kuwaiti dinar
Эсватини; Королевство Эсватини
государство в Южной Африке.
Eswatini; Kingdom of Eswatini
Мбабане; Mbabane
Английский; English
SZL, Лилангени; Swazi lilangeni
Восточный Тимор; Демократическая Республика Тимор-Лешти
государство в Юго-Восточной Азии, занимающее восточную часть острова Тимор.
East Timor; Democratic Republic of Timor-Leste
Дили; Dili
Тетум, Португальский; Tetum, Portuguese
USD, Доллар США, Восточно-тиморское сентаво; United States dollar, East Timor centavo coins"""

        # TitleBlock.resplit_to_JP_read_kanji(native_kun_on)
        # TitleBlock.resplit_to_RU_read_kanji(native_kun_on)
        TitleBlock.resplit_to_post_kanji(native_kun_on_271_300)
        TitleBlock.resplit_to_menu_kanji(native_kun_on_271_300)
        # TitleBlock.resplit_to_post_examples(native_examples)
        # TitleBlock.resplit_to_post_geo(geo2)
        # TitleBlock.resplit_to_z_name_geo(geo2)
