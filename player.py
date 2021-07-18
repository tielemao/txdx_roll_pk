from role import Role

class Player(Role):

    def mount_skill(self, skill):
        """
        装载武学招式
        """
        if self.panel_mp >= skill.use_mp:
            return self + skill
        else:
            print(" %s 真气不满足装载武学，使用普攻" % (self.name))
            return self

    def unmount_skill(self, skill):
        """
        卸载武学招式，切换招式
        """
        if skill.getname() in self.skills:
            return self - skill
        else:
            #print("该武学未装载")
            return self

def main():
    pass

if __name__ == "__main__":
    main()