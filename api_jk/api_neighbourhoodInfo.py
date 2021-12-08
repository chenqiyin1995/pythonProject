from api_jk.api_decrypt import *
import requests
import random
from common.ParseConfig import do_conf


# 小区信息数据接口

class NeighbourhoodInfo(object):
    def data():
        # 请求参数
        data = {
            "uid": str(random.randint(1, 100000)),
            "unitCode": "330106000000" + str(random.randint(100000, 999999)),
            "unitName": "unitName" + str(random.randint(1, 100000)),
            "unitAddr": "unitAddr" + str(random.randint(1, 100000)),
            "lon": "120.154856",
            "lat": "30.236734",
            "isHigh": (random.randint(0, 1)),
            "communityName": "communityName" + str(random.randint(1, 100000)),
            "orgCode": "330106000000",
            "officer": "officer" + str(random.randint(1, 100000)),
            "officerMobile": "166" + str(random.randint(10000000, 99999999)),
            "tenementName": "tenementName" + str(random.randint(1, 100000)),
            "operation": "I",
        }
        return data

    def api(data):
        url = do_conf('URL_api', 'Host_Url') + '/api/v1/rubbishunit/neighbourhoodInfo'
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
    data = NeighbourhoodInfo.data()
    test = decrypt.decrypt_api(data=data)
    test = NeighbourhoodInfo.api(test)
