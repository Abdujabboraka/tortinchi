from  Topshiriq_2 import Converter
class Calculate(Converter):
    @staticmethod
    def summa(x: object, y: object) -> object:
        return x + y

    @staticmethod
    def difference(x: object, y: object) -> object:
        return x - y

    @staticmethod
    def multiple(x: object, y: object) -> object:
        return x * y

    @staticmethod
    def division(x: object, y: object) -> object:
        return x / y


a = Calculate()
print(a.multiple(x=45, y=45))
print(a.km_ot_metr(45))
