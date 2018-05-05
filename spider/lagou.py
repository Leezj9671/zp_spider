import json
import time

import requests
import pymysql.cursors

from config import SQL_ADDR, SQL_DATABASE, SQL_PWD, SQL_TABLE, SQL_USER, PROXY_API_URL

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "DNT": "1",
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_",  
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": None,
    "X-Requested-With": "XMLHttpRequest" # 请求方式XHR
}

def save_json_to_mysql(jsondata):
    connection = pymysql.connect(host=SQL_ADDR,
                             user=SQL_USER,
                             password=SQL_PWD,
                             db=SQL_DATABASE,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO employ_info(city, companyFullName, companyShortName, companySize, createTime, district, education, financeStage, positionAdvantage, positionName, positionURL, salary, workYear, crawl_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())"
            cursor.execute(sql, [jsondata["city"], jsondata["companyFullName"], jsondata["companyShortName"], jsondata["companySize"], jsondata["createTime"], jsondata["district"], jsondata["education"], jsondata["financeStage"], jsondata["positionAdvantage"], jsondata["positionName"], 'https://www.lagou.com/jobs/{}.html'.format(jsondata["positionId"]), jsondata["salary"], jsondata["workYear"],])
        connection.commit()
    finally:
        connection.close()

def getproxy():
    return { "http": requests.get(PROXY_API_URL).text }

ajax_url = 'https://www.lagou.com/jobs/positionAjax.json' 

post_param = {"first": "false", "pn": "1", "kd": ""} 

for pn in range(1, 25):
    post_param['pn'] = str(pn)
    r = requests.post(ajax_url, headers=headers, data=post_param, proxies=getproxy())
    time.sleep(2)
    result = json.loads(r.text)
    for item in result["content"]["positionResult"]["result"]:
        save_json_to_mysql(item)