#!/user/bin/env python    
#-*- coding:utf-8 -*-
'''
此脚本通过adb命令进行模拟鼠标点击游戏，来完成自动化的作弊脚本。
虽然是模拟鼠标点击，但还存在被游戏服务器根据点击的同一个位置和频率来确定是通过作弊来实现的，因此增加一个随机数，来避免风险
全自动化刷40级狗粮本，使用条件，登录游戏
选择狗粮本，然后
请自己选择40级种火本并且完成助战选择。
by:忧郁
'''

print("注意:运行此脚本后可缩放夜神模拟器.等待脚本运行完毕即可")
import os
import time
import random

def fgo_login(x,y):#FGO登录
    return os.system("adb shell input tap {} {}".format(x,y))#模拟点击屏幕

#开始的随机
start_x,start_y = random.randint(1140,1240),random.randint(644,690)
#1，2，3为从左边数第一个从者的3个技能
one_x,one_y = random.randint(40,90),random.randint(559,595)
two_x,two_y = random.randint(140,180),random.randint(559,595)
three_x,three_y = random.randint(230,270),random.randint(559,595)
#4，5，6为从左边数第二个从者的3个技能
four_x,four_y = random.randint(365,405),random.randint(559,595)
five_x,five_y = random.randint(456,506),random.randint(559,595)
six_x,six_y = random.randint(548,590),random.randint(559,595)
#7，8，9为从左边数第三个从者的3个技能
seven_x,seven_y = random.randint(680,725),random.randint(559,595)
eight_x,eight_y = random.randint(773,820),random.randint(559,595)
nine_x,nine_y = random.randint(870,910),random.randint(559,595)
#R1,R2,R3代表的是从左到右的3个从者的宝具
R1_x,R1_y = random.randint(360,460),random.randint(130,280)
R2_x,R2_y = random.randint(590,690),random.randint(130,280)
R3_x,R3_y = random.randint(820,920),random.randint(130,280)
#Attack代表选择，准备开始选择宝具、指令卡
Attack_x,Attack_y = random.randint(1090,1180),random.randint(560,650)
#card1-5代表每回合的指令卡牌位置，从左到右是1-5
card1_x,card1_y = random.randint(68,188),random.randint(430,580)
card2_x,card2_y = random.randint(320,440),random.randint(430,580)
card3_x,card3_y = random.randint(580,700),random.randint(430,580)
card4_x,card4_y = random.randint(830,960),random.randint(430,580)
card5_x,card5_y = random.randint(1090,1220),random.randint(430,580)
#skill_roles1-3是技能选择释放角色的位置
skill_roles1_x,skill_roles1_y = random.randint(290,390),random.randint(448,530)
skill_roles2_x,skill_roles2_y = random.randint(550,670),random.randint(448,530)
skill_roles3_x,skill_roles3_y = random.randint(858,990),random.randint(448,530)
#exit是退出副本后的下一步
exit_x,exit_y = random.randint(990,1220),random.randint(650,690)

if __name__=='__main__':
    fgo_login(start_x, start_y)
    print("开始战斗，31秒加载战斗")
    time.sleep(31)

    fgo_login(three_x, three_y)
    print("技能释放：阿拉什-箭矢制作")
    time.sleep(2)
    fgo_login(four_x, four_y)
    print("技能释放：班杨-愉悦的同伴们")
    time.sleep(2)

    fgo_login(Attack_x, Attack_y)
    time.sleep(2)
    fgo_login(R1_x, R1_y)
    print("选择宝具卡-流行一条")
    time.sleep(1)
    print("选择指令卡一")
    fgo_login(card4_x, card4_y)
    time.sleep(1)
    print("选择指令二")
    fgo_login(card2_x, card2_y)
    print("宝具释放：流行一条，等待35秒进入第2回合")

    time.sleep(35)  # 第一回合结束，停止15秒看宝具

    fgo_login(one_x, one_y)
    print("技能释放：梅林-梦幻的领导力")
    time.sleep(2)

    fgo_login(Attack_x, Attack_y)
    time.sleep(2)
    print("选择宝具卡-令人惊叹的伟业")
    fgo_login(R2_x, R2_y)
    time.sleep(1)
    print("选择指令卡一")
    fgo_login(card1_x, card1_y)
    time.sleep(1)
    print("选择指令二")
    fgo_login(card2_x, card2_y)
    print("宝具释放：令人惊叹的伟业，等待32秒进入第3回合")
    time.sleep(32)  # 第二回合结束，停止15秒看宝具

    fgo_login(three_x, three_y)
    time.sleep(2)
    fgo_login(skill_roles3_x, skill_roles3_y)
    print("技能释放：梅林-英雄塑造")
    time.sleep(2)
    fgo_login(six_x, six_y)
    print("技能释放：班杨-爆米花的暴风雪")
    time.sleep(2)

    fgo_login(Attack_x, Attack_y)
    time.sleep(2)
    print("选择宝具卡-绚烂魔界日轮城")

    fgo_login(R3_x, R3_y)
    time.sleep(1)
    print("选择指令卡一")
    fgo_login(card5_x, card5_y)
    time.sleep(1)
    print("选择指令二")
    fgo_login(card1_x, card1_y)
    print("宝具释放：绚烂魔界日轮城，等待35秒确认奖励")

    time.sleep(35)  # 第二回合结束，停止15秒看宝具

    print("奖励获取：羁绊")
    fgo_login(R1_x, R1_y)#这个位置哪里都行
    time.sleep(5)
    print("奖励获取：经验")
    fgo_login(R2_x, R2_y)#这个位置哪里都行
    time.sleep(3)
    print("奖励获取：副本掉落，下一步")
    fgo_login(exit_x, exit_y)
    time.sleep(3)
    print("40级种火副本完成")
