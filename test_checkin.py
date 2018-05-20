# -*- coding: utf-8 -*- 
"""

"""
#   @File:  test_checkin
#   @Time:  2018/5/5 9:05
#   @Author:
#   @EMail:
from unittest import TestCase


class TestCheckin(TestCase):
    def test_checkin(self):
        from CheckIn import checkin
        checkin(r"email",r"passwd")

