#!/usr/local/bin/python3
# -*- coding:UTF-8 -*-
"""
@FileName           :main.py
@Copyright          :Copyright ©2014-2021 创业翼
@Author             :GourdBoy
@Date               :2023/11/15
"""
import pytest

# import schedule
# import datetime
# import time
# import os
# import sys


# def job():
#     print("执行时间：{0}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#     pytest.main()


if __name__ == '__main__':
    pytest.main()

    # path = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
    # if path not in sys.path:
    #     sys.path.append(path)
    # # schedule.every(5).to(10).days.do(job)
    # # schedule.every().monday.do(job)
    # # schedule.every().wednesday.at("13:15").do(job)
    # # schedule.every(10).minutes.do(job)
    # # schedule.every().hour.do(job)
    # schedule.every().day.at("16:17").do(job)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
