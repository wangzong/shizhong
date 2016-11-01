#!C:\Program Files\Python35\python.exe
import requests
from bs4 import BeautifulSoup
import re
import chardet


def trim(string):
    string = string.strip()
    string = re.sub('\s+', '', string)
    # string = string.replace(' ','')
    return (string)


# url = "http://past.nths.cn:8080/xiaoyou/xiaoyou/01/1991.htm"

out_file = r"test.txt"
writer = open(out_file, 'w', encoding='utf-8')

for i in range(1980, 2016, 1):
    url = 'http://past.nths.cn:8080/xiaoyou/xiaoyou/01/' + str(i) + ".htm"
    try:
        print(url)
        response = requests.get(url)
        page = response.content
        charset = chardet.detect(page)
        chartype = charset['encoding']

        if chartype.find("UTF") >= 0:
            unicode_page = page
        else:
            unicode_page = page.decode('gbk')

        soup = BeautifulSoup(unicode_page, "lxml")

        # fonts = soup.find_all(re.compile("font"))  # use tag:font to get the names
        fonts = soup.find_all(name="font",attrs={"size":"2"})  # use tag:font with size=2 to get the names

        for font in fonts:
            name = ""
            for content in font.contents:
                name = name + trim(content.string)
            # print(name)
            if name is not None:
                # print(font.string)
                # print(font.color)
                if font.get('color') is not None:
                    if font['color'] == '#FF6600':
                        class_name = font.string

                    if font['color'] == '#0000FF':
                        if font.string != "班主任":
                            teacher_name = name

                    if font['color'] == '#800000' or font['color'] == '#990000':
                        student_name = name
                        student_name = trim(student_name)
                        if student_name != "":
                            print("%s,%s,%s,%s" % (str(i), class_name, teacher_name, student_name))
                            writer.write("%s,%s,%s,%s\n" % (str(i), class_name, teacher_name, student_name))


    except Exception as e:
        print("Exception")
        print(e)

writer.close()