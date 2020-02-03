

class CoffeeMachine:
    def __init__(self):
        self.milk = 1000
        self.coffee = 1000
        self.sugar = 1000

    def make_coffee(self, milk, coffee, sugar):
        if  self.milk < milk:
            res_m = self.__subtract_milk(milk)
            print( 'Пополни молоко на ' + str(res_m))
        elif self.coffee < coffee:
            res_c = self.__subtract_coffee(coffee)
            print('Пополни кофе на ' + str(res_c))
        elif self.sugar < sugar:
            res_s = self.__subtract_sugar(sugar)
            print('Пополни сахар на ' + str(res_s))
        else:
            res_m = self.__subtract_milk(milk)
            self.milk = res_m
            res_c = self.__subtract_coffee(coffee)
            self.coffee = res_c
            res_s = self.__subtract_sugar(sugar)
            self.sugar = res_s
            print('Процесс приготовлени кофе завершен.')
    def __subtract_milk(self, milk):
        res_m = self.milk - milk
        return res_m

    def __subtract_coffee(self, coffee):
        res_c = self.coffee - coffee
        return res_c

    def __subtract_sugar(self, sugar):
        res_s = self.sugar - sugar
        return res_s


if __name__ == "__main__":    
    obj = CoffeeMachine()
    obj.make_coffee(1000, 1000, 1000)