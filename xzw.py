import random
from os import path
import json
from hoshino import Service, priv
from urllib import parse

sv_help = '''
输入小作文
懒得写了
'''.strip()

sv = Service(
    name = '小作文',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #是否可见
    enable_on_default = True, #是否默认启用
    bundle = '查询', #属于哪一类
    help_ = sv_help #帮助文本
    )

#xzw = on_command("小作文", rule=to_me(), priority=1)

@sv.on_fullmatch(["小作文"])
async def return_xzw(bot, ev):

    ret_xzw = await get_xzw()
    await bot.send(ev,ret_xzw,at_sender=True)


async def get_xzw():

    config_path = path.join(path.dirname(__file__),"xzw.json")
    with open(config_path,"r",encoding="utf8")as fp:
        xzw_list = json.load(fp)
    #obj = open(r'xzw.json', 'r')  #from the root of the project not the current file
    #xzw_list = json.load(obj)
    length = len(xzw_list)
    i = random.randint(0,length-1)
    title_o = xzw_list[i]
    title = parse.quote_plus(title_o)
    url = url = r'https://asoul.icu/articles/' + title
    """ rely = {
        "type": "share",
        "data": {
            "url": url,
            "title": title_o
            }
        } """
    rely = {
        "type":"text",
        "data":{
            "text":title_o + '\n' + url
        }
    }
    return rely
