# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description: 
"""

import addressparser

if __name__ == '__main__':
    location_str = ["徐汇区虹漕路461号58号楼5楼",
                    "泉州市洛江区万安塘西工业区",
                    "朝阳区北苑华贸城",
                    "襄阳市建锦路丽江泊林小区11栋4单元1楼2号",
                    "上海浦东新区城区昌邑路1669弄7号602（苗圃路口）",
                    "湖北天门市渔薪镇湖北省天门市三渔薪镇王湾村六组",
                    "收货人:xxx, 地址:湖北恩施州建始县业州镇湖北省建始县桂苑小区二单元111-2, 电话:13593643115",
                    "收货人:木鱼, 地址:浙江嘉兴市浙江嘉兴市浙江嘉兴市海宁市许村镇浙江省海宁市许村镇茗山村徐家石桥1号, 电话:13593643115",
                    ]
    df = addressparser.transform(["襄阳市建锦路丽江泊林小区11栋4单元1楼2号",
                                  "浙江嘉兴市浙江嘉兴市浙江嘉兴市海宁市许村镇浙江省海宁市许村镇茗山村徐家石桥1号",
                                  "大红门 / 北京市-丰台区"], cut=False)
    # print(type(df))
    # print(df)
    # df = addressparser.transform(location_str, cut=False)
    # # print(df)
    #
    for map_key in zip(df["省"], df["市"], df["区"], df["地址"]):
        print(list(map_key))
