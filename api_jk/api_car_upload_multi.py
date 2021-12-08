from api_jk.api_decrypt import *
import requests
import random
from common.ParseConfig import do_conf
from common.Random_time import *


# 运输车辆运行数据接口

class car_upload_multi(object):
    def data():
        # 请求参数
        data = {
            "uid": str(random.randint(1,100000)),
            "code": "浙A" + str(random.randint(10000, 99999)),
            "gpsNo": "gpsNo" + str(random.randint(1, 100000)),
            "locateTime": Random_time.get_random_time(),
            "locateType": random.randint(1, 3),
            "lon": "120.154856",
            "lat": "30.236734",
            "speed": random.randint(1, 200),
            "direction": random.randint(1, 200),
            "operation": "I"
        }
        return data

    def api(data):
        url = do_conf('URL_api', 'Host_Url') + '/api/v1/car/upload/multi'
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
    data = car_upload_multi.data()
    test = decrypt.decrypt_api(data=data)
    test = car_upload_multi.api(test)
