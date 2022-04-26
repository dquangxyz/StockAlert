import requests
from send_email import send_email

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def movement():
    global go_up
    if go_up == True:
        return "is going up"
    elif go_up == False:
        return "is going down"


Favourite = {
    "TSLA": "Tesla",
    "TWTR": "Twitter",
    "FB": "Facebook"
}

for key in Favourite:
    STOCK_SYMBOL = key
    COMPANY_NAME = Favourite[STOCK_SYMBOL]

    api_key_stock = "BD05GH6DQ1NY8FP0"
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_SYMBOL,
        "apikey": api_key_stock
    }

    api_key_news = "074deb8e504f40409d9fe584df576d4c"
    news_parameters = {
        "apikey": api_key_news,
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "language": "en"
    }


    # STOCK PRICE MOVEMENT
    response1 = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
    response1.raise_for_status()
    data1 = response1.json()["Time Series (Daily)"]

    data_list = [value for (key, value) in data1.items()]
    x1 = float(data_list[0]["4. close"])
    x2 = float(data_list[1]["4. close"])
    go_up = True
    if x1 > x2:
        go_up = True
    elif x1 < x2:
        go_up = False

    delta = round(abs(x1-x2)/x2*100, 2)
    if delta >= 0.1:
        # GET NEWS
        response2 = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
        response2.raise_for_status()
        data2 = response2.json()["articles"]
        top1_news_title = data2[0]["title"]
        top1_news_url = data2[0]["url"]
        top2_news_title = data2[1]["title"]
        top2_news_url = data2[1]["url"]

        sending_email = "arsdangquangpro@gmail.com"
        login_password = "" #put password here
        receiving_email = "dq2209@gmail.com"
        body_text = f"Hey Andy,\n" \
                    f"{STOCK_SYMBOL} {movement()} {delta}%\n" \
                    f"Check the news:\n\n" \
                    f"Headline: {top1_news_title}\nUrl: {top1_news_url}\n\n" \
                    f"Headline: {top2_news_title}\nUrl: {top2_news_url}\n\n"
        print(body_text)
        send_email(sending_email, login_password, receiving_email, message=body_text)


