import cv2
from connect import adb_connect, checkconnect, get_serial
from template import *

INTERVAL = 0.5





def run_state_flow():
    # 遍历状态列表并执行匹配
    while 1:
        if handle_match_organization(interval=2):
            continue
        if handle_match_wanfa_button(interval=2):
            continue
        if handle_match_goto_button(interval=2):
            continue
        if handle_match_qifu_button(interval=2):
            continue
        if handle_match_qifu_END_button(interval=2):
            break
        if handle_match_alreay_qifu_button(interval=2):
            break



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
        print("祈福按钮匹配成功")  #todo 在祈福界面会误识别goto成功
        # 祈福按钮匹配成功后的操作
        return True  # 结束，匹配到祈福按钮
    else:
        print("祈福按钮匹配失败")
        return False  # 结束，因为是最后一步


def run():
    while True:
        d = adb_connect(get_serial())
        status = checkconnect(d)
        if status:
            print('connect success')
            break
        else:
            continue

    while True:
        match()


if __name__ == '__main__':
    run_state_flow()
