def get_dynasty(year):
    dynasties = [
        {"name": "夏朝", "start": -2070, "end": -1600},
        {"name": "商朝", "start": -1600, "end": -1046},
        {"name": "西周", "start": -1046, "end": -771},
        {"name": "东周", "start": -770, "end": -256},
        {"name": "秦朝", "start": -221, "end": -206},
        {"name": "西汉", "start": -206, "end": 8},
        {"name": "新朝", "start": 9, "end": 23},
        {"name": "玄汉", "start": 23, "end": 25},
        {"name": "东汉", "start": 25, "end": 220},
        {"name": "三国", "start": 220, "end": 280},
        {"name": "西晋", "start": 266, "end": 317},
        {"name": "东晋", "start": 317, "end": 420},
        {"name": "十六国", "start": 304, "end": 439},
        {"name": "南北朝", "start": 420, "end": 589},
        {"name": "隋朝", "start": 581, "end": 618},
        {"name": "唐朝", "start": 618, "end": 907},
        {"name": "五代十国", "start": 907, "end": 960},
        {"name": "宋朝", "start": 960, "end": 1279},
        {"name": "元朝", "start": 1271, "end": 1368},
        {"name": "明朝", "start": 1368, "end": 1644},
        {"name": "清朝", "start": 1644, "end": 1912},
        {"name": "中华民国", "start": 1912, "end": 1949},
    ]

    for dynasty in dynasties:
        if dynasty["start"] < 0 and dynasty["end"] > 0:
            # 处理跨越公元前后的朝代
            if (year < 0 and year >= dynasty["start"]) or (year > 0 and year <= dynasty["end"]):
                return dynasty["name"]
        else:
            # 处理其他朝代
            if dynasty["start"] <= year <= dynasty["end"]:
                return dynasty["name"]

    return "未知朝代"

def main():
    try:
        year = int(input("请输入年份: "))
        dynasty = get_dynasty(year)
        print(f"{year}年对应的中国朝代是: {dynasty}")
    except ValueError:
        print("请输入一个有效的年份（整数）。")

if __name__ == "__main__":
    main()