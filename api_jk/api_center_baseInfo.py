from api_jk.api_decrypt import *
import requests
import random
from common.ParseConfig import do_conf
from common.Random_time import *


# 中转站信息数据接口

class center_baseInfo(object):
    def data():
        # 请求参数
        data = {
            "uid": str(random.randint(1,100000)),
            "centerCode": "330106000000" + str(random.randint(100000, 999999)),
            "centerName": "stationName"+str(random.randint(1,100000)),
            "operationUnit": "operationUnit" + str(random.randint(1, 100000)),
            "operationDate": Random_time.get_random_time(),
            "orgCode": "330106000000",
            "photo": "-",
            "address": "address" + str(random.randint(1, 100000)),
            "lon": "120.154856",
            "lat": "30.236734",
            "dailyDesignValue": (random.randint(1, 1000)),
            "designWeight": (random.randint(1, 1000)),
            "nature": (random.randint(1, 3)),
            "officer": "officer" + str(random.randint(1, 100000)),
            "officerMobile": "166" + str(random.randint(10000000, 99999999)),
            "state": (random.randint(1, 4)),
            "videoMonitor": (random.randint(0, 1)),
            "operation": "I"
        }
        return data

    def api(data):
        url = do_conf('URL_api', 'Host_Url') + '/api/v1/center/baseInfo'
        method = 'POST'
        headers = {
            'Referer': do_conf('URL_api', 'Host_Url') + '/doc.html',
            'Content-Type': 'application/json',
            'Origin': do_conf('URL_api', 'Host_Url'),
        }
        if method == 'GET':
            response = requests.request(method=method, url=url, headers=headers, params=data)
            # response = self.session.request(method=method, url=url, params=data, **kwargs)
        elif method == 'POST':
            print("开始发送{}请求，URL为：{}，请求数据为:{}".format(method, url, data))
            response = requests.request(method=method, url=url, headers=headers, data=data)
            # response = self.session.request(method=method, url=url, data=data, **kwargs)
        else:
            print("请求方法错误：request method '{}' error !".format(method))
        print('接口请求结果：', response.text)
        return response.text


if __name__ == '__main__':
    data = center_baseInfo.data()
    test = decrypt.decrypt_api(data=data)
    test = center_baseInfo.api(test)
