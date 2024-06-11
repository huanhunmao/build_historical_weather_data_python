import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 配置 Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式，不打开实际的浏览器窗口
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")


def check_udemy_discounts():
    url = "https://www.udemy.com/zh-cn/courses/development/"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    time.sleep(5)  # 等待页面加载完成

    courses = driver.find_elements(By.CLASS_NAME,
                                   'course-card--main-content--3xEIw')
    discounted_courses = []

    for course in courses:
        title = course.find_element(By.CLASS_NAME,
                                    'course-card--course-title--2f7tE').text
        price = course.find_element(By.CLASS_NAME,
                                    'price-text--price-part--Tu6MH').text
        original_price_tag = course.find_elements(By.CLASS_NAME,
                                                  'price-text--original-price--2e-F5')

        if original_price_tag:
            original_price = original_price_tag[0].text
            link = course.find_element(By.TAG_NAME, 'a').get_attribute('href')
            discounted_courses.append({
                'title': title,
                'price': price,
                'original_price': original_price,
                'link': link
            })

    driver.quit()
    return discounted_courses


def send_email(discounted_courses):
    from_email = "markfu1996@gmail.com"
    from_password = "kotl opnk liwt mjsx"
    to_email = "markfu1996@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Udemy开发课程优惠通知"

    body = "以下是目前有优惠的Udemy开发课程：\n\n"
    for course in discounted_courses:
        body += f"课程名称：{course['title']}\n"
        body += f"原价：{course['original_price']}\n"
        body += f"现价：{course['price']}\n"
        body += f"链接：{course['link']}\n\n"

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败：{e}")


def main():
    while True:
        discounted_courses = check_udemy_discounts()
        if discounted_courses:
            send_email(discounted_courses)
        time.sleep(86400)  # 每天检查一次


if __name__ == "__main__":
    main()
