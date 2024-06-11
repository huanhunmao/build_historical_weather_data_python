import time
from datetime import datetime
import os


def schedule_reminder(reminder_time, message):
    # 计算到提醒时间的秒数
    now = datetime.now()
    delay = (reminder_time - now).total_seconds()

    if delay < 0:
        print("提醒时间已经过去了，请输入一个未来的时间")
        return

    # 等待到提醒时间
    time.sleep(delay)

    # 使用 terminal-notifier 显示提醒
    notification_cmd = f'''
    terminal-notifier -message "{message}" -title "提醒事项" -timeout 60
    '''
    os.system(notification_cmd)

    # 1分钟后关闭提醒
    time.sleep(60)
    os.system('killall TerminalNotifier')


# 设置提醒时间和提醒内容
reminder_time_str = "2024-06-07 16:53:20"
reminder_time = datetime.strptime(reminder_time_str, "%Y-%m-%d %H:%M:%S")
message = "去吃饭去吃饭去吃饭！"

# 调用函数
schedule_reminder(reminder_time, message)
