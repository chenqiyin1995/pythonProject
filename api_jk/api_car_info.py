from api_jk.api_decrypt import *
import requests
import random
from common.ParseConfig import do_conf
from common.Random_time import *


# 运输车辆基础信息数据接口

class car_info(object):
    def data():
        # 请求参数
        data = {
            "uid": str(random.randint(1,100000)),
            "orgCode": "330106000000",
            "code": "浙A" + str(random.randint(10000, 99999)),
            "photo": "-",
            "fuelType": random.randint(1,5),
            "trashType": "0" + str(random.randint(1, 4)) + '00',
            "operationUnit": "operationUnit" + str(random.randint(1, 100000)),
            "operationDate": Random_time.get_random_time(),
            "isBindGps": random.randint(0,1),
            "gpsNo": "gpsNo" + str(random.randint(1, 100000)),
            "videoMonitor": (random.randint(0, 1)),
            "loads": (random.randint(1, 1000)),
            "buyDate": Random_time.get_random_time(),
            "belongUnit": "belongUnit" + str(random.randint(1, 100000)),
            "operation": "I"
        }
        return data

    def api(data):
        url = do_conf('URL_api', 'Host_Url') + '/api/v1/car/info'
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
    data = car_info.data()
    test = decrypt.decrypt_api(data=data)
    test = car_info.api(test)
