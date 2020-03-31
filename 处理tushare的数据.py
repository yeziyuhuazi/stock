# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:08:18 2020

@author: youzi
"""

import tushare as ts
stock_company=ts.get_stock_basics()

tmp_list=['黑芝麻','华海药业','山西证券','阳普医疗','保变电气','惠程科技','浙数文化','金洲管道']

stock_company[stock_company['name']=='惠程科技'].T


df = ts.get_realtime_quotes('600521') #Single stock symbol
df[['code','name','price','bid','ask','volume','amount','time']]

ts.get_realtime_quotes(['600521','000980','000981']).T
#from a Series
ts.get_realtime_quotes(df['code'].tail(10))  #一次获取10个股票的实时分笔数据

#0：name，股票名字
#1：open，今日开盘价
#2：pre_close，昨日收盘价
#3：price，当前价格
#4：high，今日最高价
#5：low，今日最低价
#6：bid，竞买价，即“买一”报价
#7：ask，竞卖价，即“卖一”报价
#8：volume，成交量 maybe you need do volume/100
#9：amount，成交金额（元 CNY）
#10：b1_v，委买一（笔数 bid volume）
#11：b1_p，委买一（价格 bid price）
#12：b2_v，“买二”
#13：b2_p，“买二”
#14：b3_v，“买三”
#15：b3_p，“买三”
#16：b4_v，“买四”
#17：b4_p，“买四”
#18：b5_v，“买五”
#19：b5_p，“买五”
#20：a1_v，委卖一（笔数 ask volume）
#21：a1_p，委卖一（价格 ask price）
#...
#30：date，日期；
#31：time，时间；

##获取多天的历史数据，近两年20170101至今
##加上多天的资金流量比例。
##当前所有股票
all_stock=ts.get_today_all()
all_stock_code=list(all_stock['code'])
all_stock_name=list(all_stock['name'])
hh_date=ts.get_hist_data('600521') 
hckj=ts.get_hist_data('002168')
hckj=hckj.reset_index()
all_stock_hist_data=pd.DataFrame()
all_stock_hist_data=all_stock_hist_data.reset_index()
import pandas as pd
import numpy as np
#获取历史的stock数据
all_stock_hist_data=pd.DataFrame()
for i in all_stock_code:
    tmp_data=ts.get_hist_data(i)
    
    try:
        tmp_data=tmp_data.reset_index()
        tmp_data['code']=i
    except Exception as e:
        print(e)
        tmp_data=pd.DataFrame()
        tmp_data['code']=i
#    tmp_data['name']=all_stock_name[i]
    all_stock_hist_data=all_stock_hist_data.append(tmp_data)

#把股票的名称匹配回去
stock_name=all_stock[['code','name']]
stock_detail=all_stock_hist_data.merge(stock_name,on='code',how='left')
stock_detail.to_csv('stock_detail.csv')

###添加一下资金量的比例，净大单，大单，这个需要参考家里的代码