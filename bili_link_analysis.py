#To Do......
import re
from os import path
import json
from hoshino import Service, priv
import requests
from hoshino.typing import MessageSegment

sv_help = '''
懒得写了
'''.strip()

sv = Service(
    name = '啊b',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #是否可见
    enable_on_default = True, #是否默认启用
    bundle = '查询', #属于哪一类
    help_ = sv_help #帮助文本
    )

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
    }
#analysis_bili = on_regex(r"(b23.tv)|(bili(22|23|33|2233).cn)|(live.bilibili.com)|(bilibili.com/(video|read|bangumi))|(^(av|cv)(\d+))|(^BV([a-zA-Z0-9])+)|(\[\[QQ小程序\]哔哩哔哩\])|(QQ小程序&amp;#93;哔哩哔哩)|(QQ小程序&#93;哔哩哔哩)", flags=re.I)
#analysis_bili = on_regex(r"(b23.tv)|(bilibili.com/video)|(^BV([a-zA-Z0-9])+)", flags=re.I)

@sv.on_rex(r'bilibili.com/video/(.*)', normalize = False)
async def analysis_main1(bot, ev):
    text = ev['match'].group(1)
    
    if re.search(r"^BV([a-zA-Z0-9])+", text, re.I):
        text = r'https://www.bilibili.com/video/' + text
    text = re.sub(r'bv','BV',text)
    resp = requests.get(text,headers=headers)
    #print(text)
    t = resp.text
    #print(t)
    #a='''
    title = re.findall(r'name="title" content=".*?_哔哩哔哩_bilibili">',t)
    if (len(title)==0):
        title = re.findall(r'name="title" content=".*?">',t)
    title = re.sub(r'name="title" content="','',title[0])
    title = re.sub(r'_哔哩哔哩_bilibili">','',title)
    up = re.findall(r'name="author" content=".*?">',t)
    up = re.sub(r'name="author" content="', '',up[0])
    up = re.sub(r'">','',up)
    pic = re.findall(r'itemprop="image" content=".*?">',t)
    pic = re.sub(r'itemprop="image" content="', '', pic[0])
    pic = re.sub(r'">','',pic)
    rely = MessageSegment(type_ = 'image',
                          data = {
                                "file" : pic
                            })
    await bot.send(ev,'标题：' + title + '\n' + 'up主：' + up + '\n' + '链接：' + text)
    await bot.send(ev,rely)
    #'''

@sv.on_rex(r'b23.tv/(.*)', normalize = False)
async def analysis_main1(bot, ev):
    text = ev['match'].group(1)
    text = r'http://b23.tv/' + text
    resp = requests.get(text,headers=headers)
    #print(text)
    t = resp.text
    #print(t)
    #a='''
    title = re.findall(r'name="title" content=".*?_哔哩哔哩_bilibili">',t)
    if (len(title)==0):
        title = re.findall(r'name="title" content=".*?">',t)
    title = re.sub(r'name="title" content="','',title[0])
    title = re.sub(r'_哔哩哔哩_bilibili">','',title)
    up = re.findall(r'name="author" content=".*?">',t)
    up = re.sub(r'name="author" content="', '',up[0])
    up = re.sub(r'">','',up)
    pic = re.findall(r'itemprop="image" content=".*?">',t)
    pic = re.sub(r'itemprop="image" content="', '', pic[0])
    pic = re.sub(r'">','',pic)
    rely = MessageSegment(type_ = 'image',
                          data = {
                                "file" : pic
                            })
    await bot.send(ev,'标题：' + title + '\n' + 'up主：' + up + '\n' + '链接：' + text)
    await bot.send(ev,rely)

    
@sv.on_rex((r'(^BV([a-zA-Z0-9])+)'), normalize = False)
async def analysis_main(bot, ev):
    text = ev['match'].group(1)
    text = r'https://www.bilibili.com/video/' + text
    resp = requests.get(text,headers=headers)
    #print(text)
    t = resp.text
    #print(t)
    #a='''
    title = re.findall(r'name="title" content=".*?_哔哩哔哩_bilibili">',t)
    if (len(title)==0):
        title = re.findall(r'name="title" content=".*?">',t)
    title = re.sub(r'name="title" content="','',title[0])
    title = re.sub(r'_哔哩哔哩_bilibili">','',title)
    up = re.findall(r'name="author" content=".*?">',t)
    up = re.sub(r'name="author" content="', '',up[0])
    up = re.sub(r'">','',up)
    pic = re.findall(r'itemprop="image" content=".*?">',t)
    pic = re.sub(r'itemprop="image" content="', '', pic[0])
    pic = re.sub(r'">','',pic)
    rely = MessageSegment(type_ = 'image',
                          data = {
                                "file" : pic
                            })
    await bot.send(ev,'标题：' + title + '\n' + 'up主：' + up + '\n' + '链接：' + text)
    await bot.send(ev,rely)
