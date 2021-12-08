
import json
import requests

from common.RecordLog import log


class HttpRequests(object):
    def __init__(self):
        self.session = requests.Session()
        log.info('建立请求...')

    def send_request(self, method, url, data=None, **kwargs):
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

    def __call__(self, method, url, params_type='form', data=None, **kwargs):
        return self.send_request(method, url,
                                 params_type=params_type,
                                 data=data,
                                 **kwargs)

    def close_session(self):
        self.session.close()
        try:
            log.info('关闭请求...')
            del self.session.cookies['JSESSIONID']
        except Exception:
            pass


request = HttpRequests()


if __name__ == '__main__':
    pass
