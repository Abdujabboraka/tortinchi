class Soda:
    def __init__(self, meva: str):
        self.meva = meva

    def show_my_drink(self, nomi="oddiy gazli suv"):
        if nomi == "oddiy gazli suv":
            return nomi
        else:
            return f" {nomi}li {self.meva} "


pepsi = Soda("Coca_Cola")
print(pepsi.show_my_drink())
