import random
import string

USER_AGENTS = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.31',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
]


def get_lagou_header():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "DNT": "1",
        "Host": "www.lagou.com",
        'Referer': 'https://www.lagou.com/jobs/list_?px=new&gx=&isSchoolJob=1',
        "Origin": "https://www.lagou.com",
        'Cookie': 'JSESSIONID={}'.format('ABAAABAAAGFABEF' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))),
        "X-Anit-Forge-Code": "0",
        "X-Anit-Forge-Token": None,
        "X-Requested-With": "XMLHttpRequest" # 请求方式XHR
    }
