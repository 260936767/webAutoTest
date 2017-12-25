#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 11:09
# @Author  : yc
# @Site    : 
# @File    : ExcelUtil.py
# @Software: PyCharm

import xlrd

class ExcelUtil():
    def __init__(self,filePath,sheetName):
        # 数据集
        self.data = xlrd.open_workbook(filePath)
        # self.table = self.data.sheet_by_index()
        # table
        self.table = self.data.sheet_by_name(sheetName)
        # 第一行值作为key
        self.keys = self.table.row_values(0)

        self.rowNum = self.table.nrows  # 总行数
        self.colNum = self.table.ncols  # 总列数

    def dict_data(self):
        if self.rowNum<=1:
            print(u'总行数小于1')
        else:
            r = []
            j = 1
            # 读取每一行
            for i in range(self.rowNum-1):
                s = {}
                values = self.table.row_values(j)
                j += 1
                # 读取每一列
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
            return r


if __name__ == '__main__':
    filePath = 'E:/test.xlsx'
    sheetName = 'Sheet1'
    data = ExcelUtil(filePath,sheetName)
    print(data.dict_data())
