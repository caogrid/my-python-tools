import random

def generate_random_letter():
    letters = ['A', 'B', 'C', 'D']
    return random.choice(letters)

# 示例使用
print(generate_random_letter())