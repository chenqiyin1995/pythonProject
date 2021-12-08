from api_jk.api_decrypt import *
import requests
import random
from common.ParseConfig import do_conf
from common.Random_time import *


# 设备视频监控上报接口

class process_videomonitor(object):
    def data():
        # 请求参数
        data = {
            "uid": str(random.randint(1,100000)),
            "videoCode": "330106000000" + str(random.randint(100000, 999999)),
            "processCode": "stationName"+str(random.randint(1,100000)),
            "type": "1",
            "name": "name" + str(random.randint(1, 100000)),
            "protocolType": "0"+str(random.randint(1,4)),
            "url": "https://www.baidu.com/index.php?tn=monline_3_dg",
            "address": "address" + str(random.randint(1, 100000)),
            "lon": "120.154856",
            "lat": "30.236734",
            "orgCode": "330106000000",
            "uploadTime": Random_time.get_random_time(),
            "operation": "I"
        }
        return data

    def api(data):
        url = do_conf('URL_api', 'Host_Url') + '/api/v1/process/videomonitor'
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
    data = process_videomonitor.data()
    test = decrypt.decrypt_api(data=data)
    test = process_videomonitor.api(test)
