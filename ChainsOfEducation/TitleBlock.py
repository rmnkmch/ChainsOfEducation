import manim


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
    """Block with title"""

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
        num = 63
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
        num = 61
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
    def Jpn_Geo():
        """
        #menu
        #English
        #Quote"""
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
On: ギョク
空
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
On: シ"""
        geo = """Нигерия; Федеративная Республика Нигерия
государство в Западной Африке.
Nigeria; Federal Republic of Nigeria
Абуджа; Abuja
английский; English
NGN, найра; Nigerian naira"""

        #TitleBlock.resplit_to_JP_read_kanji(native_kun_on)
        #TitleBlock.resplit_to_RU_read_kanji(native_kun_on)
        #TitleBlock.resplit_to_post_kanji(native_kun_on)
        #TitleBlock.resplit_to_menu_kanji(native_kun_on)
        TitleBlock.resplit_to_post_examples(native_examples)
        TitleBlock.resplit_to_post_geo(geo)
        #TitleBlock.resplit_to_z_name_geo(geo)
