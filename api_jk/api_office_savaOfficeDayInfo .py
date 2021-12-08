from api_jk.api_decrypt import *
import requests
import random
from common.ParseConfig import do_conf
from common.Random_time import *


#  机关食堂当天餐厨垃圾录入接口

class office_savaOfficeDayInfo(object):
    def data():
        # 请求参数
        data = {
            "uid": str(random.randint(1,100000)),
            "officeCode": "330106000000" + str(random.randint(100000, 999999)),
            "eatNum": random.randint(1, 100000),
            "fullDate": Random_time.get_random_time(),
            "foodWeight": random.randint(1,100000),
        }
        return data

    def api(data):
        url = do_conf('URL_api', 'Host_Url') + '/api/v1/office/savaOfficeDayInfo'
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
    data = office_savaOfficeDayInfo.data()
    test = decrypt.decrypt_api(data=data)
    test = office_savaOfficeDayInfo.api(test)
