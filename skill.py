# 武学类
from role import Role

class Skill(Role):
    """
    武学类
    """
    use_mp = 0
    def usemp(self, use_mp=0):
        """
        耗蓝
        """
        self.use_mp = use_mp
        return self.use_mp

    def vampire(self, right, blood=0):
        """
        吸血机制，暂留实现
        :param right:
        :param blood:
        :return:
        """
        self.hp += blood
        right.hp -= blood
        return

    def getname(self):
        """
        获取武学名称
        :return:
        """
        return self.name

def arhat_fist():
    """
    罗汉拳
    :return:
    """
    arhat_fist = Skill("罗汉拳", hp=0, mp=0, str=1, low_roll=0, high_roll=1)
    arhat_fist.use_mp = 5
    return arhat_fist

def yijinjing():
    """
    易筋经
    :return:
    """
    yijinjing = Skill("易筋经", hp=0, mp=100, str=2, low_roll=1, high_roll=3)
    return yijinjing

def wulang8guagun():
    """
    五郎八卦棍
    :return:
    """
    wulang8guagun = Skill("五郎八卦棍", hp=0, mp=0, str=1, low_roll=0, high_roll=2)
    wulang8guagun.use_mp = 10
    return wulang8guagun

def jiuyinzhenjing():
    """
    九阴真经
    :return:
    """
    jiuyinzhenjing = Skill("九阴真经", hp=0, mp=120, str=2, low_roll=2, high_roll=2)
    return jiuyinzhenjing

def main():
    pass

if __name__ == "__main__":
    main()