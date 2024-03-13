import manim


class Welldungeon(manim.RoundedRectangle):
    """Welldungeon"""

    @staticmethod
    def get_best_offers(number_offers: int = 5):
        def remove_most_expensive(lst: list):
            ret = []
            ppo_most_expensive = 0.1
            lot_most_expensive = "000000"
            for data in lst:
                if data[0] > ppo_most_expensive:
                    ppo_most_expensive = data[0]
                    lot_most_expensive = data[3]
            for data in lst:
                if data[3] != lot_most_expensive:
                    ret.append(data)
            return ret
        
        def show_best_offers(lst: list):
            for offer in lst:
                pr = offer[1] + " штук за " + offer[2] + "🌕, "
                pr += str(offer[0]) + "🌕 за одну: "
                pr += "Купить лот " + offer[3]
                print(pr)

        lines = []
        with open(r"media\images\ChainsOfEducation\wldg.txt") as f:
            lines = f.readlines()
        bests = []
        for line in lines:
            data_1 = line.split("*")
            count = data_1[0]
            data_2 = data_1[1].split(" - ")
            data_3 = data_2[1].split(" ")
            price = data_3[0]
            price_per_one = round(int(price) / int(count), 2)
            lot = data_3[2][1:7:1]
            if len(bests) < number_offers:
                bests.append([price_per_one, count, price, lot])
            else:
                bests.append([price_per_one, count, price, lot])
                bests = remove_most_expensive(bests)
        show_best_offers(bests)

    @staticmethod
    def do(scene: manim.Scene):
        Welldungeon.get_best_offers()