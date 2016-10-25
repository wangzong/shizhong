#!C:\Program Files\Python35\python.exe
import requests
from bs4 import BeautifulSoup
import re


def trim(string):
    string = string.strip()
    string = re.sub('\s+', '', string)
    # string = string.replace(' ','')
    return (string)


# url = "http://past.nths.cn:8080/xiaoyou/xiaoyou/01/1991.htm"

out_file = r"test.txt"
writer = open(out_file, 'w', encoding='utf-8')

for i in range(2000, 2016, 1):
    url = 'http://past.nths.cn:8080/xiaoyou/xiaoyou/01/' + str(i) + ".htm"
    try:
        print(url)
        response = requests.get(url)
        page = response.content
        unicode_page = page.decode('gbk')

        soup = BeautifulSoup(unicode_page, "lxml")

        fonts = soup.find_all(re.compile("font"))  # use tag:font to get the names

        for font in fonts:
            if font.string:
                if font['color'] == '#FF6600' and font['size'] == '2':
                    class_name = font.string

                if font['color'] == '#0000FF':
                    if font.string != "班主任":
                        teacher_name = font.string

                if font['color'] == '#800000':
                    student_name = font.string
                    student_name = trim(student_name)
                    print("%s,%s,%s,%s" % (str(i), class_name, teacher_name, student_name))
                    writer.write("%s,%s,%s,%s\n" % (str(i), class_name, teacher_name, student_name))


    except Exception as e:
        print(e)

writer.close()