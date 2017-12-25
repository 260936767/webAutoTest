#coding:utf-8
from selenium import webdriver
import time

'''
<table id = 'testID'>
    <thead></thead>
    
    <tbody>
        <tr>
            <th>姓名</th>
            <th>年龄</th>    
        </tr>
        <tr>
            <td>张三</td>
            <td>28</td>    
        </tr>
    </tbody>
    
    <tfoot></tfoot>
</table>

张三：xpath: ..//*[@id = 'testID']/tbody/tr[2]/td[1] 

'''