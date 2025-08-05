import random
import string

def generate_password(length=16, digit_ratio=0.4):
    """
    生成一个包含大写字母、小写字母和数字的随机密码，其中数字的占比由digit_ratio控制
    :param length: 密码长度
    :param digit_ratio: 数字在密码中的占比（0-1之间）
    :return: 随机生成的密码
    """
    # 确保digit_ratio在0-1之间
    digit_ratio = max(0, min(1, digit_ratio))
    
    # 计算每种字符的数量
    uppercase_count = int(length * (1 - digit_ratio) * 0.6)  # 剩余字符中，大写字母占60%
    lowercase_count = int(length * (1 - digit_ratio) * 0.4)  # 剩余字符中，小写字母占40%
    digit_count = int(length * digit_ratio)
    
    # 如果小写和大写字母的数量之和小于总长度减去数字数量，则调整它们的数量
    if uppercase_count + lowercase_count < length - digit_count:
        # 根据需要增加大写或小写字母的数量
        extra_count = length - digit_count - uppercase_count - lowercase_count
        uppercase_count += extra_count // 2
        lowercase_count += extra_count - extra_count // 2
    
    # 生成密码字符列表
    password_list = []
    password_list.extend(random.choices(string.ascii_uppercase, k=uppercase_count))
    password_list.extend(random.choices(string.ascii_lowercase, k=lowercase_count))
    password_list.extend(random.choices(string.digits, k=digit_count))
    
    # 打乱密码字符列表的顺序
    random.shuffle(password_list)
    
    # 将字符列表转换为字符串
    password = ''.join(password_list)
    
    # 如果由于四舍五入导致生成的密码长度不对，则通过随机插入一个字符来修正
    if len(password) < length:
        password_list.insert(random.randint(0, length - 1), random.choice(string.ascii_letters + string.digits))
        password = ''.join(password_list)
    
    return password

# 示例：生成一个长度为20的随机密码，其中数字的占比约为40%
password = generate_password(20, digit_ratio=0.4)
print(f"生成的密码是：{password}")
