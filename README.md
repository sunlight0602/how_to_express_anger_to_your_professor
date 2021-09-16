# how_to_express_anger_to_your_professor

指導教授不讀信，你累了嗎？\
多寄幾封，他會讀了吧！\
這裡有個小程式，讓你輕鬆表達你的不滿：

![](https://i.imgur.com/Ed9HSCu.png)

## 如何使用：

1. Clone and enter this repository
2. Change the information in config.json
```json=
{
    "sender_address": "[YOUR_EMAIL]",
    "sender_password": "[YOUR_EMAIL_PASSWORD]",
    "receiver_address": "[YOUR_PROFESSOR_EMAIL]",
    "titles": "老師幫我改論文！😤😠😡",
    "content": "來自憤怒的研究生"
}
```
:warning:
```[YOUR_EMAIL_PASSWORD]``` 並不是信箱的密碼，是 Gmail 應用程式密碼。

如何取得 Gmail 應用程式密碼：[圖文教學](https://www.learncodewithmike.com/2020/02/python-email.html)

1. 進入寄件者的Google帳戶。
1. 點擊左邊欄的安全性頁籤，接著設定兩步驟驗證。
1. 兩步驟設定完成後，會看到下方多了應用程式密碼。
1. 在選取應用程式的地方選擇其他。
1. 接著輸入應用程式的名稱，點擊產生。
1. 最後即可取得應用程式的密碼。


3. Run the code in your terminal:
```json=
$ python main.py
```

## Reference
[Learn Code With Mike - [Python實戰應用]Python寄送Gmail電子郵件實作教學](https://www.learncodewithmike.com/2020/02/python-email.html)
