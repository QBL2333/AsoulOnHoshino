import random
from os import path
import json
from hoshino import Service, priv

sv_help = '''
欢迎使用基于Hoshino的A-SOUL插件
现有功能关键字：
发病
remake/重开
小作文
表情包
bilibili视频链接解析（自动）
A-SOUL日程表
QA/qa
新功能补充中，移植自基于Nonebot的Asoulbot项目
代码重写迁移：晚暗 Q757994086

'''.strip()

sv = Service(
    name = 'h帮助',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #是否可见
    enable_on_default = True, #是否默认启用
    bundle = '查询', #属于哪一类
    help_ = sv_help #帮助文本
    )


@sv.on_fullmatch(["帮助"])
async def _(bot, ev):
    rely = "\n" + sv_help
    await bot.send(ev,rely,at_sender=True)

