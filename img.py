import random
from os import path
import json
from hoshino import Service, priv
from hoshino.typing import MessageSegment, NoticeSession, CQEvent

#img = on_command('表情包', rule=to_me(), priority=1)

sv_help = '''
表情包
懒得写了
'''.strip()

sv = Service(
    name = '表情包',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #是否可见
    enable_on_default = True, #是否默认启用
    bundle = '查询', #属于哪一类
    help_ = sv_help #帮助文本
    )

@sv.on_fullmatch(["表情包"])
async def _(bot, ev):
    config_path = path.join(path.dirname(__file__),"img.json")
    with open(config_path,"r",encoding="utf8")as fp:
        img_list = json.load(fp)
    length = len(img_list)
    i = random.randint(0,length-1)
    rely = MessageSegment(type_ = 'image',
                          data = {
                                "file" : r'http://' + img_list[i]
                          })
    await bot.send(ev,rely,at_sender=True)
