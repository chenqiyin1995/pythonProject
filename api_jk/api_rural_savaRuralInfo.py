from api_jk.api_decrypt import *
import requests
import random
from common.ParseConfig import do_conf
from common.Random_time import *


# 农村易腐垃圾站点录入接口

class rural_savaRuralInfo(object):
    def data():
        # 请求参数
        data = {
            "uid": str(random.randint(1,100000)),
            "name": "name"+str(random.randint(1,100000)),
            "process": random.randint(1, 100),
            "model": "model" + str(random.randint(1, 100000)),
            "orgCode": "330106000000",
            "manager": "manager" + str(random.randint(100000, 999999)),
            "lon":  "120.154856",
            "lat": "30.236734",
            "cardNumber": random.randint(1, 100),
            "address": "address" + str(random.randint(100000, 999999)),
            "status": str(random.randint(1,2)),
            "code": "330106000000" + str(random.randint(100000, 999999))
        }
        return data

    def api(data):
        url = do_conf('URL_api', 'Host_Url') + '/api/v1/rural/savaRuralInfo'
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
    data = rural_savaRuralInfo.data()
    test = decrypt.decrypt_api(data=data)
    test = rural_savaRuralInfo.api(test)
