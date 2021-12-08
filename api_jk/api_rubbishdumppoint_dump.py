from api_jk.api_decrypt import *
import requests
import random
from common.ParseConfig import do_conf
from common.Random_time import *


# 居民垃圾投放信息数据接口（选填）

class Dump(object):
    def data():
        # 请求参数
        data = {
            "uid": str(random.randint(1,100000)),
            "residentCode": "330106000000" + str(random.randint(100000, 999999)),
            "dumpCode": "330106000000" + str(random.randint(100000, 999999)),
            "trashType": "0"+str(random.randint(1,4))+'00',
            "trashCapacity":  str(random.randint(1, 100000)),
            "dumpDate": Random_time.get_random_time(),
            "operation": "I"
        }
        return data

    def api(data):
        url = do_conf('URL_api', 'Host_Url') + '/api/v1/rubbishdumppoint/dump'
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
    data = Dump.data()
    test = decrypt.decrypt_api(data=data)
    test = Dump.api(test)
