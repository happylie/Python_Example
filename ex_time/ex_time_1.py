#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


def day_of_the_week(lang='en'):
    """
    Check Day Of The Week
    0:Mon(월), 1:Tue(화), 2:Wed(수), 3:Thu(목), 4:Fri(금), 5:Sat(토), 6:Sun(일)
    :param lang: Return Lang(Default:En)
    :return:
    """
    tm = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    if lang == 'ko':
        tm = ['월', '화', '수', '목', '금', '토', '일']
    n = time.localtime().tm_wday
    return tm[n]


if __name__ == '__main__':
    print day_of_the_week()
    print day_of_the_week('ko')


