import json
import time

import requests
import pymysql.cursors

from config import SQL_ADDR, SQL_PORT, SQL_DATABASE, SQL_PWD, JOB_SQL_TABLE, SQL_USER, PROXY_API_URL, COMPANY_SQL_TABLE
from headers import get_lagou_header

def save_json_to_mysql(jsondata):
    """
    保存json/dict数据到数据库中
    """
    connection = pymysql.connect(host=SQL_ADDR,
                             port=SQL_PORT,
                             user=SQL_USER,
                             password=SQL_PWD,
                             db=SQL_DATABASE,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        # with connection.cursor() as cursor:        
        #     company_sql = "INSERT INTO {}(companyFullName, companyUrl, companyShortName, companySize, financeStage) VALUES (%s, %s, %s, %s, %s)".format(COMPANY_SQL_TABLE)
        #     cursor.execute(company_sql, [jsondata["companyFullName"], 'https://www.lagou.com/gongsi/{}}.html'.format(jsondata["companyId"]), jsondata["companyShortName"], jsondata["companySize"], jsondata["financeStage"]])
        # connection.commit()
        # with connection.cursor() as cursor:
        #     job_sql = "INSERT INTO {}(city, createTime, district, education, positionAdvantage, positionName, positionID, positionURL, salary, workYear, crawl_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())".format(JOB_SQL_TABLE)
        #     cursor.execute(job_sql, [jsondata["city"], jsondata["createTime"], jsondata["district"], jsondata["education"], jsondata["positionAdvantage"].replace('&nbsp;', ''), jsondata["positionName"], jsondata["positionId"], 'https://www.lagou.com/jobs/{}.html'.format(jsondata["positionId"]), jsondata["salary"], jsondata["workYear"],])
        # connection.commit()
        with connection.cursor() as cursor:
            sql = "INSERT INTO {}(city, companyFullName, companyID,companyShortName, companySize, createTime, district, education, financeStage, positionAdvantage, positionName, positionID, positionURL, salary, workYear, crawl_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())".format(JOB_SQL_TABLE)
            cursor.execute(sql, [jsondata["city"], jsondata["companyFullName"], jsondata["companyId"], jsondata["companyShortName"], jsondata["companySize"], jsondata["createTime"], jsondata["district"], jsondata["education"], jsondata["financeStage"], jsondata["positionAdvantage"].replace('&nbsp;', ''), jsondata["positionName"], jsondata["positionId"], 'https://www.lagou.com/jobs/{}.html'.format(jsondata["positionId"]), jsondata["salary"], jsondata["workYear"],])
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def getproxy():
    proxy = requests.get(PROXY_API_URL).text
    return { "http": proxy, "https": proxy}

def main():
    # 请求URL
    ajax_url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false&isSchoolJob=1'
    # 抓取应届毕业生的招聘信息
    post_param = {"first": "false", "pn": "1", "kd": ""}
    for pn in range(1, 50):
        post_param['pn'] = str(pn)
        is_success = False
        try_times = 10
        result = ''
        while not is_success:
            print(pn)
            try:
                r = requests.post(ajax_url, headers=get_lagou_header(), data=post_param)
                result = json.loads(r.text)
                is_success = result['success']
                for item in result["content"]["positionResult"]["result"]:
                    save_json_to_mysql(item)
            except:
                time.sleep(1)
                continue
        time.sleep(5)

if __name__ == '__main__':
    main()
