import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 配置
api_key = 'xxx'  # 替换为你的open weather API 密钥
city_name = 'Guangzhou'

# 获取天气数据
def get_weather_data(api_key, city_name):
    url = f"https://api.openweathermap.org/data/2.5/forecast" \
          f"?q={city_name}&exclude=current,minutely,hourly&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve weather data.")

# 处理天气数据
def format_weather_data(data):
    formatted_data = ""
    for day in data['list'][:18]:  # 只获取未来3天每3小时的数据
        date = day['dt_txt']
        weather_description = day['weather'][0]['description']
        if weather_description == 'overcast clouds':
            weather_description = '阴天☁️'
        elif weather_description == 'light rain':
            weather_description = '小雨🌧️'
        elif weather_description == 'moderate rain':
            weather_description = '中雨🌧️🌧️'
        elif weather_description == 'heavy intensity rain':
            weather_description = '大雨🌧️🌧️🌧️'
        temperature_min = day['main']['temp_min'] - 273.15  # 转换为摄氏度
        temperature_max = day['main']['temp_max'] - 273.15  # 转换为摄氏度
        rain_info = "未下雨"  # 默认情况下没有雨
        if 'rain' in day:
            rain_info = f"<span style='color: red;'>下雨量: {day['rain']['3h']} mm</span>"  # 如果有雨则标红
        formatted_data += f"{date}: {weather_description}, 最低气温: {temperature_min:.2f}°C, 最高气温: {temperature_max:.2f}°C, {rain_info}<br>"
        return formatted_data
# 发送邮件
def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_pass):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("邮件已发送！")
    except Exception as e:
        print(f"Error sending email: {e}")

# 配置邮件发送参数
to_email = 'markfu1996@gmail.com'
from_email = 'markfu1996@gmail.com'  # 发件人邮件地址
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'markfu1996@gmail.com'  # 发件人邮箱用户名
smtp_pass = 'kotl opnk liwt mjsx'  # 发件人邮箱密码或应用专用密码

# 主函数
if __name__ == "__main__":
    weather_data = get_weather_data(api_key, city_name)
    print('weather_data', weather_data)
    if weather_data:
        weather_info = format_weather_data(weather_data)
        subject = "未来3天的天气预报"
        send_email(subject, weather_info, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_pass)
        print("邮件已发送！")
    else:
        print("无法获取天气数据，邮件未发送。")
