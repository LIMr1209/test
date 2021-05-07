import xlrd

xlsx_file = xlrd.open_workbook('20210415 企业设计招聘爬取数据_杭州苏州宁波丽水 筛选后 .xlsx')
table = xlsx_file.sheets()[0]
company_names = table.col_values(4)[2:]
nrows = table.nrows
new_csv_data = [['序号','爬取城市','爬取关键词','公司名称','联系人','手机号','职位名称','工作经验要求','学历','薪资','发布时间','原文链接']]
for i in range(2,nrows):
    data = table.row_values(i)
    data.pop(0)
    data.insert(4,'test_name')
    data.insert(5,'test_phone')
    new_csv_data.append(data)
    print(new_csv_data)