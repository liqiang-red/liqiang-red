class HERO:
    hp = 0
    power = 0
    name = ''
    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        final_enemy_hp = enemy_hp - self.power
        if final_hp > final_enemy_hp:
            print(f"{self.name}赢了")
        elif final_hp < final_enemy_hp:
            print("敌方输了")
        else:
            print("打成平局")

    def speak_lines(self):
        if self.name == 'Timo':
            print("提莫队长正在待命")
        elif self.name == 'Police':
            print("见识一下法律的子弹")
        else:
            print("暂时没有此英雄")