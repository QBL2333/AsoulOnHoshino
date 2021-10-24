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
新功能补充中，搬运自Nonebot的Asoulbot项目
代码重写迁移：晚暗 Q757994086

'''.strip()

sv = Service(
    name = '发病',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #是否可见
    enable_on_default = True, #是否默认启用
    bundle = '查询', #属于哪一类
    help_ = sv_help #帮助文本
    )

@sv.on_rex(r'A-SOUL帮助')
async def help(bot, ev):
    await bot.send(ev,sv_help,at_sender=True)

#dis = on_command('发病', rule=to_me(), priority=1)

config_path = path.join(path.dirname(__file__),"disease.json")
with open(config_path,"r",encoding="utf8")as fp:
    data = json.load(fp)
begin = data['begin']
follow = data['follow']
aw = data['aw']
emoji = data['emoji']
sth = data['sth']
ath = data['ath']
dosth = data['dosth']
name = data['name']
dxw = data['dxw']

def ran(ilist):
    random.shuffle(ilist)
    return ilist[0]

@sv.on_fullmatch(["发病"])
async def _(bot, ev):
        k = random.random()
        if k<0.5:
            tmp = str()
            tmp += ran(begin) + '，'
            tmp += ran(aw)*3 + '，'
            tmp += ran(follow)

            tmp = tmp.replace("xx",ran(name))
            tmp = tmp.replace("sth",ran(sth))
            tmp = tmp.replace("ath",ran(ath))
            tmp = tmp.replace("doth",ran(dosth))
            tmp = tmp.replace("+",ran(emoji))
            await bot.send(ev,tmp,at_sender=True)
        else:
            tmp = str()
            tmp += ran(dxw)
            tmp = tmp.replace("name",ran(name))
            await bot.send(ev,tmp,at_sender=True)
