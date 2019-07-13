import random

worlds = ['第四世界','第八世界','第九世界','第十一世界']
jobs = ['戦士','ナイト','暗黒騎士','ガンブレイカー','モンク','忍者','竜騎士','侍',\
        '吟遊詩人','機工士','踊り子','黒魔道士','赤魔道士','召喚士',\
        '白魔道士','学者','占星術師']

main_hero_num = random.randint(0,len(jobs)-1)
summon_num = 100000
j = 0
role_balance = []
world_balance = []
job_balance = []
hero = {}
hero_world = {}

while j < summon_num:
    hero[j] = []
    hero_world[j] = []    
    role_set = []
    world_set = []    
    for i in range(7):
        hero[j].append(random.randint(0,len(jobs)-1))
        hero_world[j].append(random.randint(0,len(worlds)-1))
    hero[j].append(main_hero_num)
    if sum(x<4 for x in hero[j]) == 2 and sum(13<x for x in hero[j]) == 2:
        role_balance.append(1)
    else:
        role_balance.append(0)    
    world_4_count = hero_world[j].count(0)
    world_8_count = hero_world[j].count(1)
    world_9_count = hero_world[j].count(2)
    world_11_count = hero_world[j].count(3)
    if world_4_count * world_8_count * world_9_count * world_11_count == 0:
        world_balance.append(0)
    else:
        world_balance.append(1)
    job_dup = [x for x in set(hero[j]) if hero[j].count(x) > 1]
    if len(job_dup) > 0:
        job_balance.append(0)
    else:
        job_balance.append(1)
    j += 1

good_role_b = sum(role_balance)
good_world_b = sum(world_balance)
good_job_b = sum(job_balance)

good_r_w = 0
good_r_w_j = 0

for j in range(summon_num):
    good_r_w += role_balance[j] * world_balance[j]
    good_r_w_j += role_balance[j] * world_balance[j] * job_balance[j]

print('水晶公に' + str(summon_num) + '回召喚していただきました')
print('--------------------------')
print('①T2D4H2構成になった回数:' + str(good_role_b))
print('②4つの鏡像世界から少なくとも1人英雄を召喚した回数:' + str(good_world_b))
print('③ジョブ被りがなかった回数:' + str(good_job_b))
print('--------------------------')
print('①の回数(再掲):' + str(good_role_b))
print('①かつ②の回数:' + str(good_r_w))
print('①かつ②かつ③の回数:' + str(good_r_w_j))
print('--------------------------')
print('①の統計確率:' + str(good_role_b / summon_num))
print('②の統計確率:' + str(good_world_b / summon_num))
print('③の統計確率:' + str(good_job_b / summon_num))
print('--------------------------')
print('①の統計確率(再掲):' + str(good_role_b / summon_num))
print('①かつ②の統計確率:' + str(good_r_w / summon_num))
print('①かつ②かつ③の統計確率:' + str(good_r_w_j / summon_num))