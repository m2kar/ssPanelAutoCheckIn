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
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def checkin(email,passwd):
    se=requests.Session()
    se.headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139',
        'Content-Type':r'application/x-www-form-urlencoded; charset=UTF-8'
    }
    login=se.post(r'http://my.ssrcube.com/auth/login',data={'email':email,'passwd':passwd,'code':''})
    logger.info(str(login.json()))
    time.sleep(2)
    checkin=se.post(r'http://my.ssrcube.com/user/checkin')
    logger.info(str(checkin.json()))
    logger.info("Finish----------------")

if __name__ == '__main__':
    logger.info("----------------")
    logger.info("Start print log")
    parse=argparse.ArgumentParser()
    parse.add_argument('-m','--email',dest="email",required=True,type=str)
    parse.add_argument('-p','--password',dest='passwd',required=True,type=str)
    args=parse.parse_args()
    email=args.email
    passwd=args.passwd
    print("email: {}\npasswd:{}\n".format(email,passwd))
    checkin(email,passwd)
    # Tk().mainloop()
    exit()



