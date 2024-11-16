import threading
from status import *
import cv2
import numpy as np
from pygments.lexers import q
import time
from connect import get_serial, adb_connect
serial = get_serial()
device = adb_connect(serial)


# 模板匹配
def template_match(template_path=None, templates=None, threshold=0.8):
    loc_copy = None
    perhaps_x_copy = None
    perhaps_y_copy = None
    if templates is None:
        templates = [template_path]
    for t in templates:
        print(threshold)
        screen_shot()
        screenshot = cv2.imread('./datasets/screenshot.png')
        template = cv2.imread(t, 0)
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
        w, h = template.shape[::-1]  # 模板的宽度和高度
        loc = np.where(result >= threshold)
        print(w, h)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(max_val)
        top_left = max_loc
        perhaps_x = top_left[0] + w / 2
        perhaps_y = top_left[1] + h / 2
        print(perhaps_x, perhaps_y)
        loc_copy = loc
        perhaps_x_copy = perhaps_x
        perhaps_y_copy = perhaps_y
        if max_val >= threshold:
            print("模板匹配成功")

            return 1, perhaps_x, perhaps_y, loc
        else:
            continue
    print("模板匹配失败")
    return 0, perhaps_x_copy, perhaps_y_copy, loc_copy


def match():
    screen_shot()
    yaosai = cv2.imread('./datasets/replace.png')
    wait = cv2.imread('./datasets/pipei.png')
    fight = cv2.imread('./datasets/attack.png')
    zuzhi = cv2.imread('datasets/wanfa.png')
    if template_match(yaosai):
        match_yaosai()
    elif template_match(wait):
        match_wait()
    elif template_match(fight):
        match_fighting()


def screen_shot():
    device.screenshot("./datasets/screenshot.png")


# 要塞界面
def match_yaosai():
    center_x, center_y = 271, 692
    device.drag(center_x, center_y, center_x + 300, center_y, duration=2.0)


# 匹配状态
def match_wait():
    ''''
    '''


# 战斗界面


# 组织主界面
def match_zuzhi():
    x = 155
    y = 555
    device.click(x, y)


def match_organization(interval):
    result = template_match(template_path='./datasets/zuzhi_enter.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_wanfa_button(interval):
    result = template_match(template_path='./datasets/wanfa.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_goto_button(interval):
    result = template_match(template_path='./datasets/qifu.png')
    if result == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y + 244)

    return 1


def match_fengrao_menu(interval):
    result = template_match(template_path='./datasets/fengrao.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_fengrao_tiaozhan(interval):
    result = template_match(template_path='./datasets/fengrao_tiaozhan.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_qifu_button(interval):
    result = template_match(template_path='./datasets/qifu_button.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_qifu_end(interval):
    result = template_match(template_path='./datasets/qifu_end.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)
    time.sleep(interval)
    return 1


def match_qifu_alreay(interval):
    result = template_match(template_path='./datasets/qifu_already.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y + 155)
    time.sleep(interval)
    return 1


def match_qifu_exit(interval):
    result = template_match(template_path='./datasets/qifu_exit.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_organization_exit(interval):
    result = template_match(template_path='./datasets/organization_exit.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_menu(interval):
    result = template_match(template_path='./datasets/menu.png')
    if result[0] == 0:
        return 0
    # x=result[1]
    # y=result[2]
    # device.click(x,y)

    return 1


def match_xiaoduituxi_button(interval):
    result = template_match(template_path='./datasets/xiaoduituxi.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_start_button(interval):
    result = template_match(template_path='./datasets/chuzhan.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_zhuzhan_button(interval):
    result = template_match(template_path='./datasets/zuzhizhuzhan.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_ready_FIGHT(interval):
    result = template_match(template_path='./datasets/ready_fight.png')
    if result[0] == 0:
        return 0
    return 1


def match_yaoqing_button(interval):
    result = template_match(template_path='./datasets/yaoqingzhuzhan.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_xiaodui_end_button(interval):
    result = template_match(template_path='./datasets/xiaodui_end.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y)

    return 1


def match_xiaodui_complete_or_NOT_button(interval):
    result = template_match(template_path='./datasets/xiaoduicomplete.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    # device.click(x,y)

    return 1


def match_zhuzhan_exit(interval):
    result = template_match(template_path='./datasets/zhuzhan_exit.png')
    if result[0] == 0:
        return 0
    x = result[1]
    y = result[2]
    device.click(x, y + 172)
    time.sleep(interval)
    return 1


def move_joystick(direction, center_x=271, center_y=693, move_distance=100):
    if direction == 'left':
        device.drag(center_x, center_y, center_x - move_distance, center_y, duration=2)
    elif direction == 'right':
        device.drag(center_x, center_y, center_x + move_distance, center_y, duration=2)
    elif direction == 'up':
        device.drag(center_x, center_y, center_x, center_y - move_distance, duration=2)
    elif direction == 'down':
        device.drag(center_x, center_y, center_x, center_y + move_distance, duration=2)


def match_self(t):
    template = ['./datasets/self.png', './datasets/self_1.png']
    result = template_match(templates=template, threshold=t)
    return result


def match_enemy(t,object):
    template = object
    loc = template_match(templates=template, threshold=t)
    return loc


def click(device, x, y):
    while fighting_running:
        device.click(x, y)


def long_press(device, x, y, duration=1000):
        device.touch.down(x, y)




def match_fighting(interval=30, object=None,mode=None):
    screen_shot()
    thread=0.5
    if object is None:
        object = ['./datasets/enemy_1.png', './datasets/enemy.png', './datasets/enemy2.png',]
    if mode == 'fengrao':
        object=['./datasets/fengrao_enemy_1.png', './datasets/fengrao_enemy_2.png']
        thread=0.3
    start_time = time.time()
    # device.touch.down(1428, 746)
    # device.touch.down(1250, 800)
    # device.touch.down(, 746)
    long_press_thread = threading.Thread(target=click, args=(device, 1424, 751))
    long_press_thread.start()

    # device.touch.down(1424, 751)
    center_x = 271  # 实际轮盘中心x坐标
    center_y = 693  # 实际轮盘中心y坐标
    try:
        while True:
        # 检测敌人

            enemy_location = match_enemy(t=thread,object=object)
            self_location = match_self(t=thread)

            if enemy_location[0] == 1:  # 如果检测到敌人
                enemy_x = enemy_location[1]
                self_x = self_location[1]
                if enemy_x < self_x:
                # 敌人在左侧，向左移动并释放技能
                    move_left = threading.Thread(target=move_joystick, args=('left',))
                    move_left.start()
                    #move_joystick('left')
                    click_1 = threading.Thread(target=click, args=(device, 1252, 806))
                    click_2 = threading.Thread(target=click, args=(device, 1274, 628))
                    click_1.start()
                    click_2.start()
            # device.click(1252, 806)
            # device.click(1274, 628)
            # 释放技能
                else:
                # 敌人在右侧，向右移动并释放技能
                    move_right = threading.Thread(target=move_joystick, args=('right',))
                    #move_joystick('right')  # 向右移动
                    move_right.start()
                    click_1 = threading.Thread(target=click, args=(device, 1252, 806))
                    click_2 = threading.Thread(target=click, args=(device, 1274, 628))
                    click_1.start()
                    click_2.start()
                # device.click(1252, 806)
                # device.click(1274, 628)  # 释放技能
            if time.time() - start_time > interval:
                print('超过战斗时间限制')
                device.touch.up(1424, 751)
                global fighting_running
                fighting_running = 0
                break

#TODO 战斗功能基本完善，但丰饶之间等副本里小怪脚底无红圈导致无法识别


    finally:
        fighting_running=0




def match_yaosai_waiting(interval):
    result=template_match(template_path='./datasets/pipei.png')
    if result[0] == 0:
        print('要塞等待匹配失败')
        return 0
    print('要塞等待匹配成功')
    return 1
def match_yaosai_menu(interval):
    result=template_match(template_path='./datasets/replace.png')
    if result[0] == 0:
        return 0
    move_joystick('right')
    if match_yaosai_waiting(interval=1):
        global yaosai_pipei
        yaosai_pipei=1
        return 1
    return 1
def match_yaosai_fighting(interval):
    screen_shot()
    result=template_match(template_path='./datasets/attack.png',threshold=0.5)
    if result[0] == 0:
        return 0
    global yaosai_fighting
    yaosai_fighting=1
    match_fighting(interval)
    return 1
def match_yaosai_fighting_end(interval):
    result=template_match(template_path='./datasets/fighting_end.png')
    if result[0] == 0:
        return 0
    global  yaosai_pipei
    yaosai_pipei=0
    global  yaosai_fighting
    yaosai_fighting=0
    click(500,500)
    return 1
def match_yaosai_end(interval):
    result=template_match(template_path='./datasets/yaosai_end.png')
    if result[0]==0:
        return 0
    return 1
if __name__ == '__main__':
    match_fighting(mode='fengrao')





