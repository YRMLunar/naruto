import cv2
from connect import adb_connect, checkconnect, get_serial
from template import *
from handler_match_appear import *
def fengrao():
   while 1:
       if fengrao_menu==0:
           handle_match_fengrao(interval=2)
       if fengrao_tiaozhan==0:
           handle_match_fengrao_tiaozhan(interval=2)
#todo 丰饶之间战斗模式和结束识别 待完成

fengrao_tiaozhan=0
fengrao_menu=0



def xiaodui():




    while 1:
        if xiaoduituxi_menu==0:
            if not handle_match_xiaoduituxi(interval=1):
                break

        if handle_match_xiaodui_complete_or_NOT_button(interval=1):
            break
        if xiaoduituxi_zhuzhan==0:
            if not handle_match_zhuzhan_button(interval=1):
                break
        if xiaoduituxi_yaoqing==0:
            if not handle_match_yaoqing_button(interval=1):
                break

        if handle_match_xiaodui_end_button(interval=1):
            continue

# todo 小队突袭

    while 1:
        handle_match_zhuzhan_exit(interval=1)
        handle_match_qifu_exit(interval=1)
        if match_menu(interval=1):
            break














# 祈福
def qifu():
    # 遍历状态列表并执行匹配
    while 1:
        handle_match_organization(interval=1)
        handle_match_wanfa_button(interval=1)
        handle_match_qifu_button(interval=1)

        if handle_match_qifu_END_button(interval=1):
            break
        if handle_match_alreay_qifu_button(interval=1):
            break
    while 1:
        handle_match_qifu_exit(interval=2)
        handle_match_organization_exit(interval=2)
        if handle_match_menu(interval=2):
            break




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
    device.drag(270,691,110,691,0.1)