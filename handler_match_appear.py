

from template import *
from status import *

def handle_match_qifu_exit(interval):
    if match_qifu_exit(interval):
        print("祈福退出匹配成功")
        return True
    else:
        print("祈福退出匹配成功")
        return False
def handle_match_organization_exit(interval):
    if match_organization_exit(interval):
        print("组织退出匹配成功")
        return True
    else:
        print("祈福退出匹配成功")
        return False
def handle_match_menu(interval):
    if match_menu(interval):
        print("主菜单匹配成功")
        return True
    else:
        print("主菜单匹配成功")
        return False

# 设备连接
def handle_match_organization(interval):
    if match_organization(interval):
        print("组织按钮匹配成功")

        return True  # 继续执行下一个状态
    else:
        print("组织按钮匹配失败")
        return False  # 不再执行后续步骤
def handle_match_alreay_qifu_button(interval):
    if match_qifu_alreay(interval):
        print("重复祈福匹配成功")

        return True  # 继续执行下一个状态
    else:
        print("重复祈福匹配失败")
        return False  # 不再执行后续步骤

def handle_match_qifu_END_button(interval):
    if match_qifu_end(interval):
        print("祈福完成匹配成功")

        return True  # 继续执行下一个状态
    else:
        print("祈福完成匹配失败")
        return False  # 不再执行后续步骤

def handle_match_wanfa_button(interval):
    if match_wanfa_button(interval):
        print("玩法按钮匹配成功")
        #match_goto_button(interval)
        time.sleep(interval)
        device.click(410,763)
        return True  # 继续执行下一个状态
    else:
        print("玩法按钮匹配失败")
        return False  # 不再执行后续步骤

def handle_match_fengrao(interval):
    if match_fengrao_menu(interval):
        global  fengrao_menu
        fengrao_menu=1
        return 1
    else: return 0
def handle_match_fengrao_tiaozhan(interval=2):
    if match_fengrao_tiaozhan(interval):
        global fengrao_tiaozhan
        global fengrao_menu
        fengrao_menu=1
        fengrao_tiaozhan=1
        return 1
    else: return 0
def handle_match_fengrao_fightting(interval=2):
    if match_yaosai_fighting(interval):
        global fengrao_fighting
        fengrao_tiaozhan=1
        match_fighting(object=['./datasets/fengrao_enemy_1.png', './datasets/fengrao_enemy_2.png'],mode='fengrao')
        return 1
    else: return 0

def handle_match_goto_button(interval):
    if match_goto_button(interval):
        print("前往按钮匹配成功")

        return True  # 继续执行下一个状态
    else:
        print("前往按钮匹配失败")
        return False  # 不再执行后续步骤


def handle_match_qifu_button(interval):
    if match_qifu_button(interval):
        print("祈福按钮匹配成功")
        # 祈福按钮匹配成功后的操作
        return True  # 结束，匹配到祈福按钮
    else:
        print("祈福按钮匹配失败")
        return False  # 结束，因为是最后一步
def handle_match_xiaoduituxi(interval):
    if match_xiaoduituxi_button(interval):
        print("小队突袭匹配成功")
        global xiaoduituxi_menu
        xiaoduituxi_menu=1
        time.sleep(interval)
        if handle_match_xiaodui_complete_or_NOT_button(interval):
            return False
        # 祈福按钮匹配成功后的操作
        return True  # 结束，匹配到祈福按钮
    else:
        print("小队突袭匹配失败")
        return True

def handle_match_start_button(interval=2):
    if match_start_button(interval):
        print("开始匹配成功")
        # 祈福按钮匹配成功后的操作
        return True  # 结束，匹配到祈福按钮
    else:
        print("开始匹配失败")
        return False  # 结束，因为是最后一步
def handle_match_zhuzhan_button(interval=2):
    if match_zhuzhan_button(interval):
        print("助战匹配成功")
        global xiaoduituxi_zhuzhan
        xiaoduituxi_zhuzhan=1
        time.sleep(interval)
        if handle_match_xiaodui_complete_or_NOT_button(interval):
            return False

        return True
    else:
        print("助战匹配失败")
        return True
def handle_match_xiaodui_end_button(interval):
    if match_xiaodui_end_button(interval):
        print("小队战斗结束匹配成功")
        global xiaoduituxi_zhuzhan
        global xiaoduituxi_yaoqing
        xiaoduituxi_yaoqing=0
        xiaoduituxi_zhuzhan=0
        # 祈福按钮匹配成功后的操作
        return True  # 结束，匹配到祈福按钮
    else:
        print("小队战斗结束匹配失败")
        return False  # 结束，因为是最后一步
def handle_match_yaoqing_button(interval):
    if match_yaoqing_button(interval):
        print("助战匹配成功")
        if handle_match_xiaodui_complete_or_NOT_button(interval):
            return False
        if match_ready_FIGHT(interval):

            match_start_button(interval)
            global xiaoduituxi_yaoqing
            xiaoduituxi_yaoqing=1
            time.sleep(interval)
        return True
    else:
        print("助战匹配失败")
        return True
def handle_match_xiaodui_complete_or_NOT_button(interval):
    if match_xiaodui_complete_or_NOT_button(interval):
        setzero()
        print("小队已完成匹配成功")
        return True
    else:
        print("小队已完成匹配失败")
        return False
def handle_match_zhuzhan_exit(interval):
    if match_zhuzhan_exit(interval):
        print("助战退出匹配成功")
        return True
    else:
        print("助战退出匹配失败")
        return False
def handle_match_yaosai_menu(interval):
    if match_yaosai_menu(interval):
        print("要塞界面匹配成功")
        return True
    else:
        print("要塞界面匹配失败")
        return False

def handle_match_yaosai_fighting(interval):
    if match_yaosai_fighting(interval):
        print('战斗状态匹配成功')
        return True
    else:
        print('战斗状态匹配失败')
        return False
def handle_match_yaosai_fighting_end(interval):
    if match_yaosai_fighting_end(interval):
        print('战斗结束匹配成功')
        return True
    else:
        print('战斗结束匹配失败')
        return False
def handle_match_yaosai_end(interval):
    if match_yaosai_end(interval):
        print('要塞收益全部获得匹配成功')
        return True
    else:
        print('要塞收益全部获得匹配失败')
        return False
