def is_valid_date(month, day):
    # 检查月份是否在1到12之间
    if month < 1 or month > 12:
        return False
    
    # 检查日期是否在合理范围内，根据月份的不同而不同
    if month in [1, 3, 5, 7, 8, 10, 12]:
        # 这些月份有31天
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        # 这些月份有30天
        return 1 <= day <= 30
    elif month == 2:
        # 2月最多有29天（闰年），但这里为了简化，只考虑非闰年的情况
        return 1 <= day <= 28
    else:
        # 理论上不应该进入这里，因为月份已经在1到12之间校验过了
        return False

def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "水瓶座"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "双鱼座"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "白羊座"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "金牛座"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "双子座"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "巨蟹座"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "狮子座"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "处女座"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "天秤座"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "天蝎座"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "射手座"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "摩羯座"
    else:
        # 理论上不应该进入这里，因为所有的星座条件都已经被覆盖了
        return "未知星座"

# 输入生日日期
while True:
    try:
        birth_month = int(input("请输入月份："))
        birth_day = int(input("请输入日期："))
        
        if is_valid_date(birth_month, birth_day):
            break
        else:
            print("输入的日期无效，请重新输入。")
    except ValueError:
        print("输入的不是有效的数字，请重新输入。")

# 输出对应的星座
zodiac_sign = get_zodiac_sign(birth_day, birth_month)
print(f"你的星座是：{zodiac_sign}")