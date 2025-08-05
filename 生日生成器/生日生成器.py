import random

def generate_random_numbers():
    # 生成第一个随机数，范围是1-12
    random_number_1 = random.randint(1, 12)
    
    # 生成第二个随机数，范围是1-31
    random_number_2 = random.randint(1, 31)
    
    return random_number_1, random_number_2

# 调用函数并打印结果
num1, num2 = generate_random_numbers()
print(f"{num1}月{num2}日")