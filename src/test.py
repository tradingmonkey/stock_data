#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import colorama

from sz.stock_data.stock_data import StockData
from sz.stock_data.toolbox.data_provider import bao_login, bao_logout

colorama.init(autoreset = True)

logging.basicConfig(
    level = logging.DEBUG,
    format = "[%(asctime)-15s] [%(filename)s:%(lineno)d] [%(threadName)s] [%(levelname)s] %(message)s"
)


def test():
    StockData().zz500.update()
    StockData().hs300.update()

    logging.info(colorama.Fore.GREEN + '更新完毕')


if __name__ == '__main__':
    bao_login()
    StockData().setup(data_dir = '/Volumes/USBDATA/stock_data')
    test()
    bao_logout()