import math

def calculate_distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

def main():
    # 输入第一个坐标
    coord1 = input("请输入第一个坐标（格式：x y z）：").split()
    coord1 = (float(coord1[0]), float(coord1[1]), float(coord1[2]))
    
    # 输入第二个坐标
    coord2 = input("请输入第二个坐标（格式：x y z）：").split()
    coord2 = (float(coord2[0]), float(coord2[1]), float(coord2[2]))
    
    # 计算距离
    distance = calculate_distance(coord1, coord2)
    
    # 输出结果
    print(f"两个坐标点之间的距离是：{distance:.2f}")

if __name__ == "__main__":
    main()