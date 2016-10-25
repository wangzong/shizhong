#!C:\Program Files\Python35\python.exe
import requests
from bs4 import BeautifulSoup
import re

def trim(string):
    string = string.strip()
    string = re.sub('\s+', '', string)
    # string = string.replace(' ','')
    return (string)

# url = "http://past.nths.cn:8080/xiaoyou/xiaoyou/01-1-1.htm"
url = "http://past.nths.cn:8080/xiaoyou/xiaoyou/01/2004.htm"


html_doc = """
    <td class="xl24" width="72" style="width:54pt"><font size="2" color="#0000FF">孙<font class="font7"><span style="mso-spacerun: yes">&nbsp;
      </span></font><font class="font6">敏</font></font></td>
"""




# # for i in range(1950,2016,1):
# url = "http://past.nths.cn:8080/xiaoyou/xiaoyou/01/" + str(i) + ".htm"
try:

    soup = BeautifulSoup(html_doc,"lxml")

    out_file = r"test.txt"
    writer = open(out_file, 'w', encoding='utf-8')

    fonts = soup.find_all("font")


    for font in fonts:
        # newfont = font.replace(u'\xa0',' ')
        # print(newfont)
        # font.replace_with(newfont)
        # print(font.encode('gbk'))


        if font.string:
            print("Font String:%s(%d)" % (font.string,len(font.string)))

            if font['color'] == '#FF6600' and font['size'] == '2':
                class_name = font.string
                print(class_name)
                # writer.write(class_name)
                # print("Grade and class:",font.string)
            if font['color'] == '#0000FF':
                teacher_name = ""
                for item in font.contents:
                    print("debug:: ",item.string)
                    teacher_name = teacher_name + item.string
                # if font.string != "班主任":
                #     teacher_name = font.string
                    # writer.write(teacher_name)
                    print(teacher_name)
                    # print("Teacher:",font.string)
            if font['color'] == '#800000':
                student_name = font.string
                # student_name = student_name.strip()
                student_name = trim(student_name)
                # writer.write(student_name)
                print(student_name)
                # print("%s,%s,%s" % (class_name,teacher_name,student_name))
                writer.write("%s,%s,%s,%s\n" % ('2012', class_name, teacher_name, student_name))


    writer.close()
except Exception as e:
    print(e)


