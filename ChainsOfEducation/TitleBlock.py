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
        num = 90
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
        num = 181
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
        kanji = "図 工 教 晴 思 考 知 才 理 算 作 元 食\
        肉 馬 牛 魚 鳥 羽 鳴 麦 米 茶 色 黄 黒 来 行 帰 歩"
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
        native_kun_on_781_810 = """"""
        native_kun_on_751_780 = """"""
        native_kun_on_721_750 = """"""
        native_kun_on_691_720 = """"""
        native_kun_on_661_690 = """"""
        native_kun_on_631_660 = """"""
        native_kun_on_601_630 = """"""
        native_kun_on_571_600 = """"""
        native_kun_on_541_570 = """"""
        native_kun_on_511_540 = """"""
        native_kun_on_481_510 = """"""
        native_kun_on_451_480 = """"""
        native_kun_on_421_450 = """"""
        native_kun_on_391_420 = """"""
        native_kun_on_361_390 = """"""
        native_kun_on_331_360 = """"""
        native_kun_on_301_330 = """"""
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
        geo = """Нигерия; Федеративная Республика Нигерия
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

        # TitleBlock.resplit_to_JP_read_kanji(native_kun_on)
        # TitleBlock.resplit_to_RU_read_kanji(native_kun_on)
        TitleBlock.resplit_to_post_kanji(native_kun_on_211_240)
        TitleBlock.resplit_to_menu_kanji(native_kun_on_211_240)
        # TitleBlock.resplit_to_post_examples(native_examples)
        # TitleBlock.resplit_to_post_geo(geo)
        # TitleBlock.resplit_to_z_name_geo(geo)
