class Goods:
    pass


class DataManipulator:
    def save_data(self, goods: Goods):
        # Сохранение данных в БД
        pass

    def load_data(self, goods: Goods):
        # извлечение данных из БД
        pass


class MoneyMaker:
    def buy(self, goods: Goods):
        # покупаем товары
        pass

    def sell(self, goods: Goods):
        # продаем товары
        pass


class AnalysisMaker():
    def make_analysis(self, *args):
        # считаем какую-то аналитику
        pass
