import baostock as bs
import pandas as pd
import time

lg = bs.login()
print("login respond error_code:", lg.error_code)
print("login respond error msg:", lg.error_msg)

tic = time.time()
# rs = bs.query_stock_industry(code="sh.600001")


def fetch_stock_industry():
    indus = ["房地产", "银行", "电子", "互联网"]

    total_data_dict = dict()
    for item in indus:
        total_data_dict[item] = list()
    for basic in ['sz', 'sh']:
        code_head = ''
        if basic == 'sz':
            code_head = 'sz.00'
        elif basic == 'sh':
            code_head = 'sh.60'
        for seq in range(4000):
            rs = bs.query_stock_industry(code=code_head + '%04d' % seq)
            if rs.error_code != '0':
                print("query code:", rs.error_code)
            if rs.error_msg != 'success':
                print("query msg:", rs.error_msg)

            while (rs.error_code == '0') & rs.next():
                tmp_list = rs.get_row_data()
                # print(tmp_list)
                for i, item in enumerate(indus):
                    if tmp_list[3] == item:
                        total_data_dict[item].append(tmp_list)

    print(total_data_dict)
    for key in total_data_dict:
        tmp_pd = pd.DataFrame(total_data_dict[key], columns=['data', 'code', 'name', 'indus', 'shenwan'])
        tmp_pd.to_csv('data/' + key + '.csv', encoding='gbk')

    print('elapse time: ', time.time() - tic)


if __name__ == '__main__':
    fetch_stock_industry()

