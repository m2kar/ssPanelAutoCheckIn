# -*- coding: utf-8 -*-
"""

"""
#   @File:  CheckIn
#   @Time:  2018/5/4 23:32
#   @Author: iMakar
#   @EMail: iMakar@qq.com
import requests
import argparse
import time
import logging

from tkinter import Tk

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("ssr_checkin_log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# website="https://nicessrr.com"


def _do_checkin(se: requests.Session, email, passwd, site):
    se.headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139',
        'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8'
    }
    login = se.post(r'{}/auth/login'.format(site),
                    data={'email': email, 'passwd': passwd, 'code': ''})
    logger.info(str(login.json()))
    time.sleep(2)
    checkin = se.post(r'{}/user/checkin'.format(site))
    logger.info(str(checkin.json()))
    logger.info("Finish----------------")
    return checkin.json()


def checkin(email, passwd, site):
    se = requests.Session()
    return _do_checkin(se, email, passwd, site)


def checkin_with_proxy(email, passwd, site, proxy):
    se = requests.Session()
    se.proxies["http"] = proxy
    se.proxies["https"] = proxy
    return _do_checkin(se, email, passwd, site)


if __name__ == '__main__':
    logger.info("----------------")
    logger.info("Start print log")
    parse = argparse.ArgumentParser()
    parse.description = "Auto checkin for SS Panel sites"
    parse.add_argument('-e', '--email', dest="email",
                       required=True, type=str, help="User email")
    parse.add_argument('-p', '--password', dest='passwd',
                       required=True, type=str, help="User password")
    parse.add_argument("-s", "--site", dest="site", required=False, type=str,
                       default="https://v2.freeok.xyz/", help="Website url like https://v2.freeok.xyz/")
    parse.add_argument('--proxy', dest='proxy', required=False,
                       type=str, help="Http proxy server address")
    args = parse.parse_args()
    email = args.email
    passwd = args.passwd
    site = args.site
    print("email: {}\npasswd:{}\nsite:{}\n".format(email, "*", site))
    if not args.proxy:
        print(checkin(email, passwd, site))
    if args.proxy:
        print(checkin_with_proxy(email, passwd, site, args.proxy))
