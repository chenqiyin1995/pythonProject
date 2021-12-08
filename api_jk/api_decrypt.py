# from common.SendRequests import request
from api_jk.api_neighbourhoodInfo import *
from common.HandleJson import *

# 接口进行加密

class DecryptApi(object):
    def decrypt_api(self, data):
        data = 'appKey=' + do_conf('APPKEY', 'appKey') + '&' + 'body=' + HandleJson.python_to_json(
            data) + '&' + 'token=' + do_conf('APPKEY', 'token')
        url = do_conf('URL_decrypt', 'Host_Url') + do_conf('Decrypt_api', 'Path')
        print('加密请求地址：',url)
        print('加密前的数据：', data)
        headers = {
            'Referer': do_conf('URL_decrypt', 'Host_Url') + '/doc.html',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': do_conf('URL_decrypt', 'Host_Url'),
        }

        response = requests.post(url=url, data=data, headers=headers).json()
        data_test = response.get('data')
        data_test = HandleJson.python_to_json(data_test)
        print('加密后的数据：',data_test)
        return data_test

decrypt = DecryptApi()

if __name__ == '__main__':
    data = NeighbourhoodInfo.data()
    test = decrypt.decrypt_api(data=data)
