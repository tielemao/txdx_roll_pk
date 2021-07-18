class Role:
    """
    角色基本类，相当于裸装，真实面板，用于给人物，装备，武学等进行继承
    以下默认的面板属性初始皆为0
    """

    def __init__(self, name, hp, mp, str, low_roll, high_roll, defense=0, dex=0, crit_rate=0, crit=0,):
        """
        角色裸装的属性
        :param name: 名字
        :param hp: 血量
        :param mp: 真气
        :param str: 功力
        :param defense: 护甲
        :param low_roll: 最低波段
        :param high_roll: 最高波段
        :param dex: 闪避率
        :param crit_rate: 暴击率（触发百分比）
        :param crit: 暴击系数
        """
        self.name = name
        self.hp = hp
        self.mp = mp
        self.str = str
        self.defense = defense
        self.low_roll = low_roll
        self.high_roll = high_roll
        self.dex = dex
        self.crit_rate = crit_rate
        self.crit = crit

        self.panel_hp = hp
        self.panel_mp = mp
        self.panel_str = str
        self.panel_defense = defense
        self.panel_low_roll = low_roll
        self.panel_high_roll = high_roll
        self.panel_dex = dex
        self.panel_crit_rate = crit_rate
        self.panel_crit = crit
        self.skills = set()

    def __add__(self, other):
        """
        为对象实现相加的方法，统计最终面板属性
        """
        self.panel_hp += other.hp
        self.panel_mp += other.mp
        self.panel_str += other.str
        self.panel_defense += other.defense
        self.panel_low_roll += other.low_roll
        self.panel_high_roll += other.high_roll
        self.panel_dex += other.dex
        self.panel_crit_rate += other.crit_rate
        self.panel_crit += other.crit
        self.skills.add(other.name)
        return self

    def __sub__(self, other):
        """
        为对象实现相减的方法，例子是卸装备，换武学
        :param other:
        :return:
        """
        self.panel_hp -= other.hp
        self.panel_mp -= other.mp
        self.panel_str -= other.str
        self.panel_defense -= other.defense
        self.panel_low_roll -= other.low_roll
        self.panel_high_roll -= other.high_roll
        self.panel_dex -= other.dex
        self.panel_crit_rate -= other.crit_rate
        self.panel_crit -= other.crit
        self.skills.remove(other.name)
        return self

def main():
    pass

if __name__ == "__main__":
    main()
