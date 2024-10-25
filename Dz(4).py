class Brawl_Stars_Characters_maps:
    def __init__(self, name, prizes):
        self.name = name
        self.age = prizes
        self.wild_bazz = "Броулбол"
        self.wild_volt = "Нокаут"


class characters(Brawl_Stars_Characters_maps):
    def __init__(self, name, prizes, species):
        super().__init__(name, prizes)
        self.species = species



    def info(self):
        print(f"Имя: {self.name}, Кубки: {self.age}, Вид бойца: {self.species}")

    def wild_info(self):
        if self.species == "убийца":
            print(f"Режим игры: {self.wild_bazz}")
        elif self.species == "урон":
            print(f"Режим игры: {self.wild_volt}")

# Создаем экземпляр класса
volt = characters("Вольт", 899, "урон")
bazz = characters("Базз", 650 ,"убийца")

# Вызываем методы
volt.info()
volt.wild_info()
bazz.info()
bazz.wild_info()