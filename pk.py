from player import Player
from prettytable import PrettyTable
import prettytable
import skill
import random
import math

class Pk():
    """
    PK
    :return:
    """
    def __init__(self):
        pass

    def roll(self, role):
        """
        投骰
        :param role: 传入一个角色（有高低波段属性）
        :return: 最终骰值
        """
        lowest = role.panel_low_roll
        highest = role.panel_high_roll
        result = random.randint(lowest, highest)
        return result

    def echotable(self, left, right):
        """
        使用表格展示对战回合信息
        :param att_list: 传入一个属性字典
        :return:
        """
        table = PrettyTable(["属性", "攻击方"], align="c",padding_width=2)
        convert = {"name": "角色名字",
                   "hp": "真实生命",
                   "mp": "裸装真气",
                   "str": "裸装功力",
                   "defense": "裸装护甲",
                   "low_roll": "裸低波段",
                   "high_roll": "裸高波段",
                   "dex": "裸装敏捷",
                   "crit": "暴击系数",
                   "crit_rate": "暴击概率",
                   "panel_hp": "面板生命",
                   "panel_mp": "面板真气",
                   "panel_str": "面板功力",
                   "panel_defense": "面板护甲",
                   "panel_low_roll": "面低波段",
                   "panel_high_roll": "面高波段",
                   "panel_dex": "面板敏捷",
                   "panel_crit": "面板暴击",
                   "panel_crit_rate": "面暴击率",
                   "skills": "装备武学",
                   }
        for key, value in left.items():
            if key in convert.keys():
                table.add_row([convert[key], value])
        value2 = list(right.values())
        table.add_column("迎击方", value2)
        return table

    def solo(self, left, right, count_round=1):
        """
        1 v 1 pk 单回合
        :param left: 左边主动攻击方
        :param right: 右边被动迎击方
        :param count_round: 总回合数记录
        :return: pk经过
        """
        # 双方hp大于0才能展开pk
        if left.hp > 0 and right.hp > 0:
            # 主动攻击方的投骰
            left_value = self.roll(left)
            # 被攻击方的投骰
            right_value = self.roll(right)
            # 计算命中hit
            left_hit = random.randint(1, 100)
            right_hit = random.randint(1, 100)
            # 当主动攻击方的波段投骰高于被动方
            if left_value > right_value:
                if left_hit <= right.panel_dex:
                    print("第 %s 回合, %s命中为%s, %s成功闪避." % (count_round, left.name, left_hit, right.name))
                    return True
                roll_value = left_value - right_value
                crit_result = random.randint(1, 100)
                # 如果暴击率大于等于随机的百分比则触发暴击
                if left.crit_rate >= crit_result:
                    damage = math.ceil(roll_value * left.str * (1+left.crit))
                    right.hp -= damage
                    print("第 %s 回合，%s 投出了 %s，%s 投出了 %s，%s 触发了暴击， 对 %s 造成了 %s倍 共%s伤害， %s 余 %s HP." % (
                        count_round, left.name, left_value, right.name, right_value, left.name, right.name, 1+left.crit, damage,
                        right.name, right.hp))
                    print(self.echotable(left.__dict__, right.__dict__))
                # 没有触发暴击则按平常伤害算
                if left.crit_rate < crit_result:
                    damage = math.ceil(roll_value * left.str)
                    right.hp -= damage
                    print("第 %s 回合，%s 投出了 %s，%s 投出了 %s，%s 对 %s 造成了 %s 伤害，%s 余 %s HP." % (
                        count_round, left.name, left_value, right.name, right_value, left.name, right.name, damage, right.name, right.hp))
                    print(self.echotable(left.__dict__, right.__dict__))
                if right.hp <= 0:
                    print("%s hp 归零，%s 获胜， 余 %s HP" % (right.name, left.name, left.hp))
                    return False
                return True
            # 当被动方投骰波段高于主动方
            if left_value < right_value:
                if right_hit <= right.dex:
                    print("第 %s 回合, %s命中为%s, %s成功闪避." % (count_round, right.name, right_hit, left.name))
                    return True
                roll_value = right_value - left_value
                # 如果暴击率大于等于随机的百分比则触发暴击
                crit_right_result = random.randint(1, 100)
                if right.crit_rate >= crit_right_result:
                    damage = math.ceil(roll_value * right.str * (1+right.crit))
                    left.hp -= damage
                    print("第 %s 回合，%s 投出了 %s，%s 投出了 %s，%s 触发了暴击， 对 %s 造成了 %s倍 共%s伤害， %s 余 %s HP." % (
                        count_round, right.name, right_value, left.name, left_value, right.name, left.name, 1+right.crit, damage,
                        left.name, left.hp))
                    print(self.echotable(left.__dict__, right.__dict__))
                if right.crit_rate < crit_right_result:
                    damage = math.ceil(roll_value * right.str)
                    left.hp -= damage
                    print("第 %s 回合，%s 投出了 %s，%s 投出了 %s，%s 对 %s 造成了 %s 伤害，%s 余 %s HP." % (
                        count_round, right.name, right_value, left.name, left_value, right.name, left.name, damage, left.name, left.hp))
                    print(self.echotable(left.__dict__, right.__dict__))
                if left.hp <= 0:
                    print("%s hp 归零，%s 获胜， 余 %s HP" % (left.name, right.name, right.hp))
                    return False
                return True
            if left_value == right_value:
                roll_value = left_value
                print("第 %s 回合，双方都投出了%s,打成平手" % (count_round, roll_value))
                return True
        else:
            return False

    def auto(self, left, left_skill, right, right_skill, count_round):
        """
        自动战斗n回合
        """
        for i in range(1, count_round):
            left.mount_skill(left_skill)
            right.mount_skill(right_skill)
            if self.solo(left, right, i):
                left.unmount_skill(left_skill)
                right.unmount_skill(right_skill)
            else:
                break

def main():
    play1 = ["白夜行",60,20,7,2,5,30,30,0.5]
    play2 = ["邪灵114",80,30,6,1,4,10,40,0.3]
    role1 = Player(name=play1[0], hp=int(play1[1]), mp=int(play1[2]), str=int(play1[3]), low_roll=int(play1[4]),
                 high_roll=int(play1[5]), dex=int(play1[6]), crit_rate=(play1[7]), crit=(play1[8]))
    role2 = Player(name=play2[0], hp=int(play2[1]), mp=int(play2[2]), str=int(play2[3]), low_roll=int(play2[4]),
                 high_roll=int(play2[5]), dex=int(play2[6]), crit_rate=(play2[7]), crit=(play2[8]))
    pk1 = Pk()
    pk1.auto(role1, skill.arhat_fist(), role2, skill.wulang8guagun(),8)


if __name__ == "__main__":
    main()