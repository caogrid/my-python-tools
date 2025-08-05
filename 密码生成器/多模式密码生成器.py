import random
import string

def generate_password(length, password_type):
    if password_type == '纯数字':
        characters = string.digits
    elif password_type == '纯字母':
        characters = string.ascii_letters
    elif password_type == '混合型':
        characters = string.ascii_letters + string.digits
    else:
        raise ValueError("无效的密码种类")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("请输入密码位数: "))
        if length < 1:
            raise ValueError("密码位数必须大于0")
        
        password_type = input("请输入密码种类（纯数字，纯字母，混合型）: ")
        
        password = generate_password(length, password_type)
        print(f"生成的随机密码是: {password}")
    
    except ValueError as e:
        print(f"输入错误: {e}")

if __name__ == "__main__":
    main()