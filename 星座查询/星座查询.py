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
        return "输入日期有误"

# 输入生日日期
birth_month = int(input("请输入月份："))
birth_day = int(input("请输入日期："))

# 输出对应的星座
zodiac_sign = get_zodiac_sign(birth_day, birth_month)
print(f"你的星座是：{zodiac_sign}")