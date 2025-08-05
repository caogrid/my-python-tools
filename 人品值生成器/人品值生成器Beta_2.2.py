import os
import random
from datetime import datetime

# 文件名用于存储日期和随机数（即人品值）
data_file = 'luck_value.txt'

# 获取当前日期，格式为年-月-日
current_date = datetime.now().strftime('%Y-%m-%d')

# 尝试读取上次的日期和随机数（人品值）
last_date = None
last_luck_value = None
if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        # 假设文件中的内容是 "日期 人品值" 格式，用空格分隔
        saved_data = file.read().strip().split()
        if len(saved_data) == 2:
            last_date, last_luck_value_str = saved_data
            last_luck_value = int(last_luck_value_str)

# 检查是否是同一天
if last_date == current_date:
    # 如果是同一天，输出上次的人品值和日期
    if 0<last_luck_value < 10:
        print(f"你今天的人品值是：{last_luck_value}……（是百分制哦）（on {last_date}）")
    elif last_luck_value == 100:
        print(f"你今天的人品值是：{last_luck_value}!100！100！（on {last_date}）")
    elif 90<last_luck_value<100:
        print(f"你今天的人品值是：{last_luck_value}!好评如潮！（on {last_date}）")
    else:
        print(f"你今天的人品值是：{last_luck_value}（on {last_date}）")
else:
    # 如果不是同一天，生成一个新的随机数作为人品值，并保存
    new_luck_value = random.randint(1, 100)  # 生成1到100之间的人品值
    if 0<new_luck_value < 10:
        print(f"你今天的人品值是：{new_luck_value}……（是百分制哦）（on {current_date}）")
    elif new_luck_value == 100:
        print(f"你今天的人品值是：{new_luck_value}!100！100！（on {current_date}）")
    elif 90<new_luck_value<100:
        print(f"你今天的人品值是：{new_luck_value}!好评如潮！（on {current_date}）")        
    else:
        print(f"你今天的人品值是：{new_luck_value}（on {current_date}）")
    
    # 将当前日期和人品值写入文件
    with open(data_file, 'w') as file:
        file.write(f"{current_date} {new_luck_value}\n")