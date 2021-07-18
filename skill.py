# 武学类
from role import Role

class Skill(Role):
    """
    武学类
    """
    def level(self, lv):
        self.lv = lv

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
    arhat_fist = Skill("罗汉拳", 10, 10, 1, 1, 1, 0, 0)
    return arhat_fist

def yijinjing():
    """
    易筋经
    :return:
    """
    yijinjing = Skill("易筋经", 30, 120, 2, 3, 3, 10, 20)
    return yijinjing

def wulang8guagun():
    """
    五郎八卦棍
    :return:
    """
    wulang8guagun = Skill("五郎八卦棍", 5, 50, 1, 2, 2, 10, 10)
    return wulang8guagun

def jiuyinzhenjing():
    """
    九阴真经
    :return:
    """
    jiuyinzhenjing = Skill("九阴真经", 20, 150, 2, 1, 4, 20, 10)
    return jiuyinzhenjing

def main():
    pass

if __name__ == "__main__":
    main()