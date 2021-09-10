import smtplib
import time
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


with open('config.json', 'r') as f:
    config = json.load(f)

print(config)

for i in range(len(config['titles'])):
    
    content = MIMEMultipart()  #建立MIMEMultipart物件

    content["from"] = config['sender_address']  #寄件者
    content["to"] = config['receiver_address'] #收件者
    
    content["subject"] = config['titles'][len(config['titles'])-1-i] #郵件標題
    content.attach(MIMEText(config['content']))  #郵件內容
    
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(config['sender_address'], config['sender_password'])  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            
            print("Complete! Title: " + config['titles'][len(config['titles'])-1-i])
            
            time.sleep(3)
        except Exception as e:
            print("Error message: ", e)
