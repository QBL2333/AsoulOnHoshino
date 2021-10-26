from os import path
import json
from hoshino import Service, priv
from bilibili_api import user
import re

sv_help = '''
QA
'''.strip()

sv = Service(
    name = 'QA',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #是否可见
    enable_on_default = True, #是否默认启用
    bundle = '查询', #属于哪一类
    help_ = sv_help #帮助文本
    )


@sv.on_fullmatch(["QA","qa"])
async def return_qa(bot, ev):

    ret_qa = await get_qa()
    await bot.send(ev,ret_qa,at_sender=True)


async def get_qa():

    u = user.User(703007996)
    page = await u.get_articles(0)
    articles = page['articles']
    ar_len = len(articles)
    for i in range(0,ar_len):
        push = articles[i]
        title = push['title']
        matchobj = re.search( r'QA', title, re.M|re.I)
        if matchobj:
            id = push['id']
            url = r'https://www.bilibili.com/read/cv' + str(id)
            summary = push['summary']
            rely=title + '\n' + url + '\n' + summary
            return rely
        else:
            pass
