import random
import time

# 初始化一个包含1到9的列表
numbers = list(range(1, 10))

# 设置延迟时间（例如，0.5秒）
delay_time = 0.5

# 创建一个集合来跟踪已输出的数字
outputted_numbers = set()

while True:
    # 如果已经输出了所有数字，则重置集合并重新填充列表
    if len(outputted_numbers) == len(numbers):
        outputted_numbers.clear()
        random.shuffle(numbers)  # 可选：重新打乱列表
    
    # 从列表中随机选择一个数字，并确保它不在已输出的集合中
    num = None
    while num is None or num in outputted_numbers:
        num = random.choice(numbers)
    
    # 输出这个数字
    print(num)
    
    # 将这个数字添加到已输出的集合中
    outputted_numbers.add(num)
    
    # 暂停一段时间
    time.sleep(delay_time)

# 注意：这是一个无限循环，你需要手动停止它（例如，通过Ctrl+C）
