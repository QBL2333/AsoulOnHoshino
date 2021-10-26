from os import path
import json
from hoshino import Service, priv
from bilibili_api import user
import re
from hoshino.typing import MessageSegment, NoticeSession, CQEvent

sv_help = '''
日程表
'''.strip()

sv = Service(
    name = '日程表',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #是否可见
    enable_on_default = True, #是否默认启用
    bundle = '查询', #属于哪一类
    help_ = sv_help #帮助文本
    )

@sv.on_fullmatch(["A-SOUL日程表"])
async def return_shedule(bot, ev):
    u = user.User(703007996)
    page = await u.get_dynamics(0)
    nxt = page['next_offset']
    page2 = await u.get_dynamics(nxt)
    dynamic1 = page['cards']
    dynamic2 = page2['cards']
    dynamic = dynamic1 + dynamic2
    dy_len = len(dynamic)
    for i in range(0,dy_len):
        dy = dynamic[i]
        desc = dy['desc']
        type = desc['type']
        if type != 2:
            pass
        else:
            card = dy['card']
            item = card['item']
            des = item['description']
            des = des.encode('utf-8')
            sche = '日程表'
            sche = sche.encode('utf-8')
            matchobj = re.search(sche, des, re.M|re.I)
            if matchobj:
                pic = item['pictures']
                url = pic[0]['img_src']
                rely = MessageSegment(type_ = 'image',
                          data = {
                                "file" : url
                          })
                await bot.send(ev,rely,at_sender=True)
                break
            else:
                pass
