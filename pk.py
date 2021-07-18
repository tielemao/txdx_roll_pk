from role import Role
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

    def round(self, role):
        """
        单回合的pk结算
        :param role: 传入一个角色（有高低波段属性）
        :return:
        """
        pass


    def solo(self, left, right, count):
        """
        1 vs 1 pk
        :param left: 左边主动攻击方
        :param right: 右边被动迎击方
        :return: pk经过
        """
        round_count = 0
        count = count - 1
        while round_count <= count:
            round_count += 1
            print("第 %s 回合， %s 使用 %s 武学， %s 使用 %s 武学" % (round_count, left.name, left.skills, right.name, right.skills))
            #print(left.__dict__)
            #print(right.__dict__)
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
                    print("第 %s 回合, %s命中为%s, %s成功闪避." % (round_count, left.name, left_hit, right.name))
                    continue
                roll_value = left_value - right_value
                # 如果暴击率大于等于随机的百分比则触发暴击
                crit_result = random.randint(1, 100)
                if left.crit_rate >= crit_result:
                    damage = math.ceil(roll_value * left.str * (1+left.crit))
                    right.hp -= damage
                    print("第 %s 回合，%s 投出了 %s，%s 投出了 %s，%s 触发了暴击， 对 %s 造成了 %s倍 共%s伤害， %s 余 %s HP." % (
                        round_count, left.name, left_value, right.name, right_value, left.name, right.name, 1+left.crit, damage,
                        right.name, right.hp))
                if left.crit_rate < crit_result:
                    damage = math.ceil(roll_value * left.str)
                    right.hp -= damage
                    print("第 %s 回合，%s 投出了 %s，%s 投出了 %s，%s 对 %s 造成了 %s 伤害，%s 余 %s HP." % (
                        round_count, left.name, left_value, right.name, right_value, left.name, right.name, damage, right.name, right.hp))
                if right.hp <= 0:
                    print("%s hp 归零，%s 获胜， 余 %s HP" % (right.name, left.name, left.hp))
                    break
            # 当被动方投骰波段高于主动方
            if left_value < right_value:
                if right_hit <= right.dex:
                    print("第 %s 回合, %s命中为%s, %s成功闪避." % (round_count, right.name, right_hit, left.name))
                    continue
                roll_value = right_value - left_value
                # 如果暴击率大于等于随机的百分比则触发暴击
                crit_right_result = random.randint(1, 100)
                if right.crit_rate >= crit_right_result:
                    damage = math.ceil(roll_value * right.str * (1+right.crit))
                    left.hp -= damage
                    print("第 %s 回合，%s 投出了 %s，%s 投出了 %s，%s 触发了暴击， 对 %s 造成了 %s倍 共%s伤害， %s 余 %s HP." % (
                        round_count, right.name, right_value, left.name, left_value, right.name, left.name, 1+right.crit, damage,
                        left.name, left.hp))
                if right.crit_rate < crit_right_result:
                    damage = math.ceil(roll_value * right.str)
                    left.hp -= damage
                    print("第 %s 回合，%s 投出了 %s，%s 投出了 %s，%s 对 %s 造成了 %s 伤害，%s 余 %s HP." % (
                        round_count, right.name, right_value, left.name, left_value, right.name, left.name, damage, left.name, left.hp))
                if left.hp <= 0:
                    print("%s hp 归零，%s 获胜， 余 %s HP" % (left.name, right.name, right.hp))
                    break
            if left_value == right_value:
                roll_value = left_value
                print("第 %s 回合，双方都投出了%s,打成平手" % (round_count, roll_value))
                continue

def main():
    play1 = ["白夜行",60,120,7,2,5,30,30,0.5]
    play2 = ["邪灵114",80,100,6,1,5,10,40,0.3]
    role1 = Role(name=play1[0], hp=int(play1[1]), mp=int(play1[2]), str=int(play1[3]), low_roll=int(play1[4]),
                 high_roll=int(play1[5]), dex=int(play1[6]), crit_rate=(play1[7]), crit=(play1[8]))
    role2 = Role(name=play2[0], hp=int(play2[1]), mp=int(play2[2]), str=int(play2[3]), low_roll=int(play2[4]),
                 high_roll=int(play2[5]), dex=int(play2[6]), crit_rate=(play2[7]), crit=(play2[8]))
    human1 = role1 + skill.arhat_fist() + skill.yijinjing()
    human2 = role2 + skill.wulang8guagun() + skill.jiuyinzhenjing()
    pk1 = Pk()
    pk1.solo(human1,human2,1)
    human1 = role1 - skill.arhat_fist() + skill.wulang8guagun()
    human2 = role2 - skill.wulang8guagun() + skill.arhat_fist()
    pk1.solo(human1,human2,1)

if __name__ == "__main__":
    main()