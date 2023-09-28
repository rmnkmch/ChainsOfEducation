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
        num = 62
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
        num = 151
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
BDT, Бангладешская така; Bangladeshi taka"""

        # TitleBlock.resplit_to_JP_read_kanji(native_kun_on)
        # TitleBlock.resplit_to_RU_read_kanji(native_kun_on)
        # TitleBlock.resplit_to_post_kanji(native_kun_on_151_180)
        # TitleBlock.resplit_to_menu_kanji(native_kun_on_151_180)
        # TitleBlock.resplit_to_post_examples(native_examples)
        TitleBlock.resplit_to_post_geo(geo)
        TitleBlock.resplit_to_z_name_geo(geo)
