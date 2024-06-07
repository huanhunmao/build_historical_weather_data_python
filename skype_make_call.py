from skpy import Skype
import datetime
import time

# 创建 Skype 实例
skype = Skype("1311926640@qq.com", "xxx")

def send_reminder():
    # 拨打电话提醒
    skype.call("电话号码")

def schedule_daily_reminder(hour, minute):
    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == minute:
            send_reminder()
            time.sleep(60)  # 避免重复发送提醒
        else:
            time.sleep(30)  # 检查提醒时间间隔
# 设置每天的提醒时间，例如每天早上7点
schedule_daily_reminder(7, 0)
