import cv2
import uiautomator2 as u2

def get_serial():
    return '127.0.0.1:16448'
def adb_connect(device):
    d=u2.connect(device)
    return d
def checkconnect(device):
    try:
        info=device.info
        print(info)
        print("设备连接成功")
        return 1
    except Exception as e:
        print("设备未连接或终端")
        return 0
if __name__ == '__main__':
    adb_connect(get_serial())













