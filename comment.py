# coding='utf-8'
import requests
import time
import xlwt

import pandas as pd
import re

if __name__ == '__main__':
    webdata = pd.read_excel('web.xls')
    newTable = "com.xls"  # 创建文件
    wb = xlwt.Workbook("encoding='utf-8")
    ws = wb.add_sheet('sheet1')  # 创建表
    headDate = ['skuId', 'goodCountStr', 'goodRate', 'generalCountStr', 'generalRate', 'poorCountStr',
                'poorRate']  # 定义标题
    for i in range(0, 7):  # for循环遍历写入
        ws.write(0, i, headDate[i], xlwt.easyxf('font: bold on'))
    index = 1  # 行数
    N = webdata.shape[0]
    for i in range(N):
        item = webdata['web'][i]
        ID = re.findall(r'\d+', item)
        print(ID)
        url = 'https://club.jd.com/comment/productPageComments.action?&productId=' + str(ID[0]) + '&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'

        # url = 'https://club.jd.com/comment/productPageComments.action?&productId=12109713&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36"
        }
        time.sleep(2)
        test = requests.get(url=url, headers=headers)
        # data = json.loads(test)#loads?
        data = test.json()
        cdata = []
        items = data['productCommentSummary']
        print(items)
        cdata.append(items['skuId'])
        cdata.append(items['goodCountStr'])
        cdata.append(items['goodRate'])
        cdata.append(items['generalCountStr'])
        cdata.append(items['generalRate'])
        cdata.append(items['poorCountStr'])
        cdata.append(items['poorRate'])
        for i in range(0, 7):
            ws.write(index, i, cdata[i])
        print(ws)
        index=index+1
    wb.save(newTable)