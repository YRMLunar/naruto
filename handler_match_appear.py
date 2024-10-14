from template import *


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
        match_goto_button(interval)
        return True  # 继续执行下一个状态
    else:
        print("玩法按钮匹配失败")
        return False  # 不再执行后续步骤


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
