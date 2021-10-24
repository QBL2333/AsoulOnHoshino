import random
from os import path
import json
from hoshino import Service, priv

config_path = path.join(path.dirname(__file__),"jjz.json")
with open(config_path,"r",encoding="utf8")as fp:
    data = json.load(fp)
emo = data['emotions']
emoji = emo['emoji']
#xhs = emo['xiaohongshu']
symbols = data['symbols']
auxiliary_words = data['auxiliaryWords']
dividers = data['dividers']
begin = data['beginning']
who = data['who']
someone = data['someone']
todo = data['todosth']
#another = data['another']
end = data['ending']
collect = data['collections']
attr = data['attribute']
fashion = data['fashion']

def ran(ilist):
    random.shuffle(ilist)
    return ilist[0]

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
    name = '绝绝子',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #是否可见
    enable_on_default = True, #是否默认启用
    bundle = '查询', #属于哪一类
    help_ = sv_help #帮助文本
    )

#jjz = on_command('绝绝子', aliases={'jjz'}, rule=to_me(), priority=1)

@sv.on_rex(r'^jjz|^绝绝子(.*)')
async def _(bot, ev):
    keyword = ev['match'].group(1)

    if not keyword:
        await bot.send(ev,"格式不对啦，请加空格和事件",at_sender=True)
    else:
        tmp = str()
        tmp += ran(begin)
        tmp += ran(emoji) + ran(dividers)
        tmp += ran(fashion) + ran(dividers)
        tmp += ran(todo) + ran(dividers)
        tmp += ran(attr) + ran(symbols)
        tmp += ran(collect) + ran(dividers)
        tmp += ran(fashion) + ran(dividers)
        tmp += ran(auxiliary_words)*3 + ran(dividers)
        tmp += ran(end) + ran(emoji)

        tmp = tmp.replace("who",ran(who))
        tmp = tmp.replace("someone",ran(someone))
        tmp = tmp.replace("dosth",str(keyword))
        await bot.send(ev,tmp,at_sender=True)
