from finaly.police import Police
from finaly.timo import Timo


class HeroFactory:
    def create_hero(self,name):
        if name == 'Timo':
            return Timo()
        elif name == 'Police':
            return Police()
        else:
            raise Exception("此英雄不在英雄工厂内")

hero_factory = HeroFactory()
timo = hero_factory.create_hero("Timo")
police = hero_factory.create_hero("Police")

timo.fight(police.hp, police.power)
timo.speak_lines()
police.speak_lines()
