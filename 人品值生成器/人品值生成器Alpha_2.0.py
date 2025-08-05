#输出时添加时间
import os
import random
from datetime import datetime

# 文件名用于存储日期和随机数
data_file = 'run_data.txt'

# 获取当前日期，格式为年-月-日
current_date = datetime.now().strftime('%Y-%m-%d')

# 尝试读取上次的日期和随机数
last_date = None
last_random_number = None
if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        # 假设文件中的内容是 "日期 随机数" 格式，用空格分隔
        saved_data = file.read().strip().split()
        if len(saved_data) == 2:
            last_date, last_random_number_str = saved_data
            last_random_number = int(last_random_number_str)

# 检查是否是同一天
if last_date == current_date:
    # 如果是同一天，输出上次的随机数和日期
    print(f"Same day: Last random number was {last_random_number} (on {last_date})")
else:
    # 如果不是同一天，生成一个新的随机数并保存
    new_random_number = random.randint(1, 100)  # 生成1到100之间的随机数
    print(f"Different day: New random number is {new_random_number} (on {current_date})")
    
    # 将当前日期和随机数写入文件
    with open(data_file, 'w') as file:
        file.write(f"{current_date} {new_random_number}\n")