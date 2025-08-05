def main():
    while True:
        # 提示用户选择模式
        print("请选择模式:")
        print("1. 下界坐标转换为主世界坐标")
        print("2. 主世界坐标转换为下界坐标")
        print("输入0退出程序")
        
        # 获取用户输入的模式
        mode = input("请输入模式 (1/2/0): ")
        
        # 检查用户是否选择退出
        if mode == '0':
            print("程序已退出。")
            break
        
        # 检查输入的模式是否有效
        if mode not in ['1', '2']:
            print("无效的模式，请重新输入。")
            continue
        
        # 提示用户输入坐标
        coordinate_input = input("请输入坐标 (格式如 x,z): ")
        
        # 尝试解析坐标
        try:
            # 替换中文逗号为英文逗号，然后进行分割和转换
            x, z = map(float, coordinate_input.replace('，', ',').split(','))
        except ValueError:
            print("无效的坐标，请输入有效的坐标格式")
            continue
        
        # 根据模式进行运算
        if mode == '1':
            x_result = x * 8
            z_result = z * 8
            print(f"对应的主世界坐标为({x_result},{z_result})")
        elif mode == '2':
            x_result = x / 8
            z_result = z / 8
            print(f"对应的下界坐标为({x_result},{z_result})")

if __name__ == "__main__":
    main()