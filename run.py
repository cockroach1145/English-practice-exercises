import random
from 题库 import *


score = int(0)
all_modules  =[module_1, module_2, module_3, module_4]


all_modules_shuffled = []
for mod in all_modules:
    random.shuffle(mod)
    all_modules_shuffled.extend(mod)


print(f'共{len(all_modules_shuffled)}题')
#  逐个列出
for idx, q in enumerate(all_modules_shuffled):
    q_type = q["type"]
    question = q["question"]
    answers_raw = q["answers"]
    knowledge = q["knowledge"]

    #处理答案
    correct_list = [a.strip().lower() for a in answers_raw.split('&')]
    correct_display = answers_raw.lower()

    print(f'第{idx}题，{question}')
    #开始
    while True:
        user = input('回答：').strip()
        if user:
            break
        print('不能为空')
    user_lower = user.lower()
    if user_lower in correct_list:
        print('正确，+1')
        score += 1
    else:
        print('错误')
        print(f"请照着正确答案，重新写1遍：{answers_raw}")
        while True:
            user_new = input(f'仿写回答：').strip()
            if user_new:
                break
            print('不能为空')

        user_new_lower = user_new.lower()
        if user_new_lower in correct_list:
            print('正确')
        else:
            print('错误')
        if knowledge:
            while True:
                choice = input('查看知识点？(y/n):').strip().lower()
                if choice in ("y", "n"):
                    break
                print("请输入 y 或 n")
            if choice == "y":
                print(f"📖 知识点：{knowledge}")

print(f'当前得分：{score}/{len(all_modules_shuffled)}')
