import cv2
from pygments.lexers import q
import  time
from connect import get_serial, adb_connect

serial = get_serial()
device = adb_connect(serial)

#模板匹配
def template_match(template):
    screen_shot()
    screenshot = cv2.imread('./datasets/screenshot.png')
    template=cv2.imread(template,0)
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    w,h = template.shape[::-1]  # 模板的宽度和高度
    threshold = 0.8
    print(w,h)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)
    top_left = max_loc
    perhaps_x =top_left[0]+w/2
    perhaps_y =top_left[1]+h/2
    print(perhaps_x,perhaps_y)
    if max_val >= threshold:
        print("匹配成功")

        return 1,perhaps_x,perhaps_y
    else:
        print("匹配失败，状态不存在")
        return 0,perhaps_x,perhaps_y


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

#要塞界面
def match_yaosai():
    center_x, center_y = 271, 692
    device.drag(center_x, center_y, center_x + 300, center_y, duration=2.0)

#匹配状态
def match_wait():
  ''''
  '''
#战斗界面
def match_fighting():
    '''


    '''
#组织主界面
def match_zuzhi():
  x=155
  y=555
  device.click(x,y)

def match_organization(interval):
    result=template_match('./datasets/zuzhi_enter.png')
    if result[0]==0:
        return 0
    x=result[1]
    y=result[2]
    device.click(x,y)
    time.sleep(interval)
    return 1

def match_wanfa_button(interval):
    result=template_match('./datasets/wanfa.png')
    if result[0]==0:
        return 0
    x=result[1]
    y=result[2]
    device.click(x,y)
    time.sleep(interval)
    return 1


def match_goto_button(interval):
    result=template_match('./datasets/qifu.png')
    if result==0:
        return 0
    x=result[1]
    y=result[2]
    device.click(x,y+244)
    time.sleep(interval)
    return 1

def match_qifu_button(interval):
    result=template_match('./datasets/qifu_button.png')
    if result[0]==0:
        return 0
    x=result[1]
    y=result[2]
    device.click(x,y)
    time.sleep(interval)
    return 1
def match_qifu_end(interval):
    result=template_match('./datasets/qifu_end.png')
    if result[0]==0:
        return 0
    x=result[1]
    y=result[2]
    device.click(x,y)
    time.sleep(interval)
    return 1
def match_qifu_alreay(interval):
    result=template_match('./datasets/qifu_already.png')
    if result[0]==0:
        return 0
    x=result[1]
    y=result[2]
    device.click(x,y+155)
    time.sleep(interval)
    return 1
def match_qifu_exit(interval):
    result=template_match('./datasets/qifu_exit.png')
    if result[0]==0:
        return 0
    x=result[1]
    y=result[2]
    device.click(x,y)
    time.sleep(interval)
    return 1
def match_organization_exit(interval):
    result=template_match('./datasets/organization_exit.png')
    if result[0]==0:
        return 0
    x=result[1]
    y=result[2]
    device.click(x,y)
    time.sleep(interval)
    return 1
def match_menu(interval):
    result=template_match('./datasets/menu.png')
    if result[0]==0:
        return 0
    # x=result[1]
    # y=result[2]
    # device.click(x,y)
    time.sleep(interval)
    return 1
def match_xiaoduituxi_button(interval):
    result=template_match('./datasets/organization_exit.png')#todo 图片更改
    if result[0]==0:
        return 0
    x=result[1]
    y=result[2]
    device.click(x,y)
    time.sleep(interval)
    return 1
def match_start_button(interval):
    result=template_match('./datasets/organization_exit.png')#todo 图片更改
    if result[0]==0:
        return 0
    x=result[1]
    y=result[2]
    device.click(x,y)
    time.sleep(interval)
    return 1

if __name__ == '__main__':
    match_organization()
    match_wanfa_button()
    match_goto_button()