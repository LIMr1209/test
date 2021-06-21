# import xlrd
#
# xlsx_file = xlrd.open_workbook('20210415 企业设计招聘爬取数据_杭州苏州宁波丽水 筛选后 .xlsx')
# table = xlsx_file.sheets()[0]
# company_names = table.col_values(4)[2:]
# nrows = table.nrows
# new_csv_data = [['序号','爬取城市','爬取关键词','公司名称','联系人','手机号','职位名称','工作经验要求','学历','薪资','发布时间','原文链接']]
# for i in range(2,nrows):
#     data = table.row_values(i)
#     data.pop(0)
#     data.insert(4,'test_name')
#     data.insert(5,'test_phone')
#     new_csv_data.append(data)
#     print(new_csv_data)

# import numpy as np
# from matplotlib import pyplot as plt
# plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
#
# # myfont = font_manager.FontProperties(fname="/usr/share/fonts/truetype/arphic/ukai.ttc")
# a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
# data = [{'name': '9月14日','value': [15746, 312, 4497, 319]},{'name': '9月15日','value': [15746, 312, 4497, 319]},{'name': '9月16日','value': [15746, 312, 4497, 319]}]
# bar_width = 0.1
# temp_x = list(range(len(a)))
# ticks = None
# h = np.arange(len(a))
# for i, j in enumerate(data):
#     if i == 1:
#         ticks = temp_x
#     bar = plt.bar(temp_x, j['value'], width=bar_width, label=j['name'])
#     for x, y in zip(temp_x, j['value']):
#         plt.text(x,y+1,'%.0f'%y,ha='center',va='bottom',fontsize=7)
#     temp_x = list(i + bar_width for i in temp_x)
#
#
# plt.legend(['9月14日','9月15号','9月16号'])
# # 设置x轴刻度
# plt.xlabel('brand')
# plt.ylabel('sale_count')
# plt.xticks(ticks, a)
# plt.savefig("./mutiy.png")
# plt.show()
