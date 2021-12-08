from api_jk.api_decrypt import *
import requests
import random
from common.ParseConfig import do_conf
from common.Random_time import *


# 处置设施基本信息接口

class process_enter(object):
    def data():
        # 请求参数
        data = {
            "uid": str(random.randint(1,100000)),
            "processCode": "330106000000" + str(random.randint(100000, 999999)),
            "processType": "1",
            "inTime": Random_time.get_random_time(),
            "sendFactory": "sendFactory" + str(random.randint(100000, 999999)),
            "tracUnit": "tracUnit" + str(random.randint(100000, 999999)),
            "carNo": "浙A" + str(random.randint(10000, 99999)),
            "totalWeight": (random.randint(1, 1000)),
            "actualWeight": (random.randint(1, 1000)),
            "weight": (random.randint(1, 1000)),
            "type": "0" + str(random.randint(1, 9)),
            "operation": "I"
        }
        return data

    def api(data):
        url = do_conf('URL_api', 'Host_Url') + '/api/v1/process/enter'
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
    data = process_enter.data()
    test = decrypt.decrypt_api(data=data)
    test = process_enter.api(test)
