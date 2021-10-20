import traceback, config, time, json, sys
from datetime import date as dt
from datetime import time as tm

with open('lessons.json', 'r') as j:
    data = json.load(j)

mon = 0; tue = 1; wed = 2; thu = 3; fri = 4; sat = 5; sun = 6
def mond(cls_num, day='monday'):
    for t in data[str(cls_num)]:
        res = t[str(mon)]
    return ''.join(res)
def tues(cls_num, day='tuesday'):
    for t in data[str(cls_num)]:
        res = t[str(tue)]
    return ''.join(res)
def wedn(cls_num, day='wednesday'):
    for t in data[str(cls_num)]:
        res = t[str(wed)]
    return ''.join(res)
def thur(cls_num, day='thursday'):
    for t in data[str(cls_num)]:
        res = t[str(thu)]
    return ''.join(res)
def frid(cls_num, day='friday'):
    for t in data[str(cls_num)]:
        res = t[str(fri)]
    return ''.join(res)
def satu(cls_num, day='saturday'):
    for t in data[str(cls_num)]:
        res = t[str(sat)]
    return ''.join(res)
def sund(cls_num, day='sunday'):
    for t in data[str(cls_num)]:
        res = t[str(sun)]
    return ''.join(res)
adm10 = mond(10)+'\n\n'+tues(10)+'\n\n'+wedn(10)+'\n\n'+thur(10)+'\n\n'+frid(10)+'\n\n'+satu(10)+'\n\n'+sund(10)
adm11 = mond(11)+'\n\n'+tues(11)+'\n\n'+wedn(11)+'\n\n'+thur(11)+'\n\n'+frid(11)+'\n\n'+satu(11)+'\n\n'+sund(11)