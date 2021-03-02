import json
import time

import requests

from web.SendMailDemo import sendMail


def search_my_ak():
    url = "https://myikangapi.health.ikang.com/myikang/booking/org/list"
    header = {
        "Host": "myikangapi.health.ikang.com",
        "Connection": "keep-alive",
        "Content-Length": "215",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://my.ikang.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://my.ikang.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "Hm_lvt_06cf025722cd0ca838fc7496abcc510d=1603864009,1603878692,1603933090; MY_IKANG_SESSION=57927a39-b2f4-440d-874e-c8b162deb91c; route=a392a2388926068f0972ac3e4b7a73d1; access_token=797fc45a6ad1bbe5a134c27a343f94a9; Hm_lpvt_06cf025722cd0ca838fc7496abcc510d=1603933143; TINGYUN_DATA=%7B%22id%22%3A%220CCx_3ChWr0%23svB-GMpYmCk%22%2C%22n%22%3A%22WebAction%2FSpringController%252Fcommon%252Fcity%252Flist%2Fip%22%2C%22a%22%3A93%2C%22q%22%3A0%2C%22tid%22%3A%22%22%7D"
    }
    body = """
    {"cardNumber":"0010900151350172","comboCode":"NONEM2616432","cityCode":"0010","comboId":"2616432","comboType":"1","dayNum":"","latitude":"39.9","longitude":"116.4","sortCardNumber":"0010900151350172","startDate":""}
    """
    rsp = requests.post(url=url, headers=header, data=body)
    print("响应结果" + rsp.text)
    rsp_json = json.loads(rsp.text)
    rsp_code = rsp_json.get("code")
    if rsp_code == 1:
        res_list = rsp_json.get("results")[0].get("list")
        for day in res_list:
            if day.get("date") == "2020-10-31":
                hos_list = day.get("list")
                print("日期：" + day.get("date"))
                # print(hosList)
                print("名称                    状态 最大 已约 百分比")
                for hospital in hos_list:
                    org_code = hospital.get("orgCode")
                    if org_code == "099" or org_code == "753":
                        print("%-15s" % hospital.get("orgName"), end='\t')
                        print(str(hospital.get("level")), end='\t')
                        print(str(hospital.get("maxNum")), end='\t')
                        print(str(hospital.get("useNum")), end='\t')
                        print(hospital.get("percent"))
                        if hospital.get("percent") != "100%":
                            sendMail()
                break
        print("----------------------------------------")


if __name__ == "__main__":
    total = 0
    while True:
        total += 1
        print("《《《《《《《《《开始执行第%s次查询》》》》》》》》》》》" % total)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        search_my_ak()
        print("《《《《《《《《《第%s次查询执行结束》》》》》》》》》》》" % total)
        count = 60 * 3
        for i in range(count):
            print('\r' + "将在" + str(count - i) + "秒后刷新", end='', flush=True)
            time.sleep(1)
