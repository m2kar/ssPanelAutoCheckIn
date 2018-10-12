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
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("ssr_checkin_log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

website="https://nicessrr.com"

def _do_checkin(se:requests.Session,email,passwd):
    se.headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139',
        'Content-Type':r'application/x-www-form-urlencoded; charset=UTF-8'
    }
    login=se.post(r'{}/auth/login'.format(website),data={'email':email,'passwd':passwd,'code':''})
    logger.info(str(login.json()))
    time.sleep(2)
    checkin=se.post(r'{}/user/checkin'.format(website))
    logger.info(str(checkin.json()))
    logger.info("Finish----------------")

def checkin(email,passwd):
    se=requests.Session()
    _do_checkin(se,email,passwd)

def checkin_with_proxy(email, passwd, proxy):
    se=requests.Session()
    se.proxies["http"]=proxy
    _do_checkin(se,email,passwd)

if __name__ == '__main__':
    logger.info("----------------")
    logger.info("Start print log")
    parse=argparse.ArgumentParser()
    parse.add_argument('-m','--email',dest="email",required=True,type=str)
    parse.add_argument('-p','--password',dest='passwd',required=True,type=str)
    parse.add_argument('--proxy',dest='proxy',required=False,type=str)
    args=parse.parse_args()
    email=args.email
    passwd=args.passwd
    print("email: {}\npasswd:{}\n".format(email,passwd))
    if not args.proxy:
        checkin(email,passwd)
    if args.proxy:
        checkin_with_proxy(email,passwd,args.proxy)
    # Tk().mainloop()
    exit()



