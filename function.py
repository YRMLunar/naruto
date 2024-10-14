import cv2
from connect import adb_connect, checkconnect, get_serial
from template import *

INTERVAL = 0.5
from handler_match_appear import *


# 祈福
def qifu():
    # 遍历状态列表并执行匹配
    while 1:
        handle_match_organization(interval=2)
        handle_match_wanfa_button(interval=2)
        handle_match_qifu_button(interval=2)

        if handle_match_qifu_END_button(interval=2):
            break
        if handle_match_alreay_qifu_button(interval=2):
            break
    while 1:
        if handle_match_qifu_exit(interval=2):
            continue
        if handle_match_organization_exit(interval=2):
            continue
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
    qifu()