import schedule
import time
import os

def show_notification(message):
    # 使用 terminal-notifier 显示提醒
    notification_cmd = f'''
    terminal-notifier -message "{message}" -title "提醒事项" -timeout 60
    '''
    os.system(notification_cmd)

def morning_reminder():
    show_notification("去吃午饭")

def afternoon_reminder():
    show_notification("去吃晚饭")

def evening_reminder():
    show_notification("回家回家回家")

# 定义工作日的提醒时间
schedule.every().monday.at("11:45").do(morning_reminder)
schedule.every().monday.at("18:44").do(afternoon_reminder)
schedule.every().monday.at("21:00").do(evening_reminder)

schedule.every().tuesday.at("11:45").do(morning_reminder)
schedule.every().tuesday.at("18:44").do(afternoon_reminder)
schedule.every().tuesday.at("21:00").do(evening_reminder)

schedule.every().wednesday.at("11:45").do(morning_reminder)
schedule.every().wednesday.at("18:44").do(afternoon_reminder)
schedule.every().wednesday.at("21:00").do(evening_reminder)

schedule.every().thursday.at("11:45").do(morning_reminder)
schedule.every().thursday.at("18:44").do(afternoon_reminder)
schedule.every().thursday.at("21:00").do(evening_reminder)

schedule.every().friday.at("11:45").do(morning_reminder)
schedule.every().friday.at("18:44").do(afternoon_reminder)
schedule.every().friday.at("21:00").do(evening_reminder)

# 运行调度器
while True:
    schedule.run_pending()
    time.sleep(1)
