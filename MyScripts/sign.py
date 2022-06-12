import pytz
import requests
import datetime
from urllib import parse


class SignPlan:
    def __init__(self, date: datetime.date, in_time: datetime.time, out_time: datetime.time, state):
        self.date = date
        self.in_time = in_time
        self.out_time = out_time
        self.state = state

    def do_sign(self):
        """
        return:
        1 : 签入成功
        2 : 签出成功
        3 : 已结束
        """
        curr_date = datetime.date.today()
        curr_time = datetime.datetime.now()
        if self.date == curr_date:
            match self.state:
                case 0:
                    if self.in_time <= curr_time:
                        if self._sign_in() == 200:
                            return 1
                case 1:
                    if self.out_time <= curr_time:
                        print("执行签出")
                        if self._sign_out() == 200:
                            return 2
                case 2:
                    return 3
                case _:
                    return 3
                    # raise "NO CASE, check your state of params"

    def _sign_in(self):
        """
        签入
        :return:
        code
        """
        url = "http://wechat-pro.bill-jc.com/wechatCloud/attendanceController/signSava?wxuId=B-80732&isgonggancheck=0&iswangluocheck=0"
        headers = {
            "Host": "wechat-pro.bill-jc.com",
            "Connection": "keep-alive",
            "Content-Length": "600",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045811 Mobile Safari/537.36 MMWEBID/2782 MicroMessenger/8.0.15.2020(0x28000F31) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://wechat-pro.bill-jc.com",
            "Referer": "http://wechat-pro.bill-jc.com/wechatCloud/attendanceController/goSignView?workId=Xv0GSGRKhxy%2BOz%2FLIRCeLEDx2wYdYGpKibfGJWq5F%2BM%3D&wxuid=Xv0GSGRKhxy%2BOz%2FLIRCeLEDx2wYdYGpKibfGJWq5F%2BM%3D",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        in_data = 'gongganRemarks=&workId=B-80732&departmentName=ISBG-BU3-DU1&signDate=' \
                  + parse.quote(self.date.strftime('%Y-%m-%d')) \
                  + '&signAddress=aQU9ucLsyxhPP%252B1HeM25e1MgwEuKvJbXWTLqLHPsaDVoW7CAkOur8drqla%252BIma9o' \
                    'Ol9A9nrEd1Qx%250ANungHgDTNmEVX%252B3KVX8KtMXLHGSxdHhhHtptMjdE%252B7dtUDa0UU8%252F&signTime=' \
                  + parse.quote(self.in_time.strftime('%Y-%m-%d %H:%M:%S')) \
                  + '&signlnglat=113.94032569897%2C22.54645007723&employeeName=%E6%9B%BE%E8%82%B2%E8%BE%89&' \
                    'flag=&precise=450&juli=87.23&addressId=566&workAddress=%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%8D%9' \
                    '7%E5%B1%B1%E5%8C%BA%E7%A7%91%E7%A0%94%E8%B7%AF%E6%9D%BE%E6%97%A5%E9%BC%8E%E7%9B%9B%' \
                    'E5%A4%A7%E5%8E%A6&isSite=onsite&teste=09%3A30&wxVersion=8.0152020028000f3d)'
        print("执行签入")
        in_response = requests.post(url, headers=headers, data=in_data)
        return in_response.status_code
        return 200

    def _sign_out(self):
        """
        签出
        :return:
        rescode
        """
        url = "http://wechat-pro.bill-jc.com/wechatCloud/attendanceController/signOutSava?ischeck=no&wxuId=B-80732&isgonggancheck=0&iswangluocheck=0"
        headers = {
            "Host": "wechat-pro.bill-jc.com",
            "Connection": "keep-alive",
            "Content-Length": "597",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045811 Mobile Safari/537.36 MMWEBID/2782 MicroMessenger/8.0.15.2020(0x28000F31) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://wechat-pro.bill-jc.com",
            "Referer": "http://wechat-pro.bill-jc.com/wechatCloud/attendanceController/goSignOutView?workId=auUw3rMQR%2Fn7JmKPKyC0Czy2r4wZpS4wtpGAvkTPwBQ%3D&wxuid=auUw3rMQR%2Fn7JmKPKyC0Czy2r4wZpS4wtpGAvkTPwBQ%3D",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        out_data = "gongganRemarks=&workId=B-80732&departmentName=ISBG-BU3-DU1&signOutDate=" \
                   + parse.quote(self.date.strftime('%Y-%m-%d')) \
                   + "&signOutAddress=aQU9ucLsyxhPP%252B1HeM25e1MgwEuKvJbXWTLqLHPsaDVoW7CAkOur8drql" \
                     "a%252BIma9oOl9A9nrEd1Qx%250ANungHgDTNsrhhzmw9mDUMrvmM6mW7dthHtptMjdE%252B7dtUDa0UU8%252F&signOutTime=" \
                   + parse.quote(self.out_time.strftime('%Y-%m-%d %H:%M:%S')) \
                   + "&signOutlnglat=113.94030574168%2C22.546208194393&employeeName=%E6%9B%BE%E8%82%B2%E8%BE%89&attId=6945466" \
                     "&hours=&addressId=566&workAddress=%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%8D%97%E5%B1%B1%E5%8C%BA" \
                     "%E7%A7%91%E7%A0%94%E8%B7%AF%E6%9D%BE%E6%97%A5%E9%BC%8E%E7%9B%9B%E5%A4%A7%E5%8E%A6&isSite=o" \
                     "nsite&precise=450&juli=89.83&xiabTime=" \
                   + parse.quote(str(self.out_time.strftime('%H:%M')))
        print("执行签出")
        out_response = requests.post(url, headers=headers, data=out_data)
        return out_response.status_code
        return 200


if __name__ == "__main__":
    sign_date = SignPlan(datetime.date.today(), datetime.datetime.now(), datetime.datetime.now(), 1)
    print(sign_date.do_sign())