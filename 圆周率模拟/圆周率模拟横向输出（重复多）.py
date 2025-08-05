import random
import time

# 设置每个数字之间的延时（秒）
DELAY_BETWEEN_NUMBERS = 0.1  # 0.1秒

try:
    while True:  # 无限循环
        num = random.randint(0, 9)  # 生成0-9之间的随机整数
        print(num, end='', flush=True)  # 横向输出数字，不添加换行符，并立即刷新输出
        time.sleep(DELAY_BETWEEN_NUMBERS)  # 等待一段时间以便观察输出

# 捕获KeyboardInterrupt异常（即用户按下Ctrl+C）以优雅地退出程序
except KeyboardInterrupt:
    print("\n程序已停止。")
