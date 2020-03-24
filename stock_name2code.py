import baostock as bs
import pandas as pd
import time

lg = bs.login()
print("login respond error_code:", lg.error_code)
print("login respond error msg:", lg.error_msg)

tic = time.time()
# rs = bs.query_stock_industry(code="sh.600001")
indus = ["房地产", "银行", "电子", "互联网"]
fang_list = list()
yinhang_list = list()
dianzi_list = list()
hulianwang_list = list()
for basic in ['sh', 'sz']:
    for seq in range(4000):
        rs = bs.query_stock_industry(code=basic + ".00" + '%04d'%seq)
        if rs.error_code != '0':
            print("query code:", rs.error_code)
        if rs.error_msg != 'success':
            print("query msg:", rs.error_msg)

        while (rs.error_code == '0') & rs.next():
            tmp_list = rs.get_row_data()
            print(tmp_list)
            if tmp_list[3] == "房地产":
                fang_list.append(tmp_list)
            elif tmp_list[3] == indus[1]:
                yinhang_list.append(tmp_list)
            elif tmp_list[3] == indus[2]:
                dianzi_list.append(tmp_list)
            elif tmp_list == indus[3]:
                hulianwang_list.append(tmp_list)

print(fang_list)
fang_ind = pd.DataFrame(fang_list, columns=['data', 'code', 'name', 'indus', 'shenwan'])
yinhang_ind = pd.DataFrame(yinhang_list, columns=['data', 'code', 'name', 'indus', 'shenwan'])
dianzi_ind = pd.DataFrame(dianzi_list, columns=['data', 'code', 'name', 'indus', 'shenwan'])
hulianwang_ind = pd.DataFrame(hulianwang_list, columns=['data', 'code', 'name', 'indus', 'shenwan'])

print('elapse time: ', time.time() - tic)
fang_ind.to_csv("fang.csv", index=False, encoding='gbk')
yinhang_ind.to_csv("yinhang.csv", index=False, encoding='gbk')
dianzi_ind.to_csv("dianzi.csv", index=False, encoding='gbk')
hulianwang_ind.to_csv("hulianwang.csv", index=False, encoding='gbk')