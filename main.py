import argparse
from datetime import datetime
from monthdelta import monthmod


def add_years(start_date: datetime, years: int):
    try:
        return start_date.replace(year=start_date.year + years)
    except ValueError:
        # 👇️ preseve calendar day (if Feb 29th doesn't exist, set to 28th)
        return start_date.replace(year=start_date.year + years, day=28)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--birth_day",
        "-b",
        type=str,
        default="",
        help="yyyymmdd形式で入れてください(ex. 20000101)",
        required=True,
    )
    parser.add_argument(
        "--limit_years",
        "-l",
        type=int,
        default=80,
        help="yy形式で入れてください(ex. 80)",
        required=False,
    )
    args = parser.parse_args()
    date_format = "%Y/%m/%d"
    print(f"想定寿命: {args.limit_years}歳")
    exec_date = datetime.now()
    print(f"本日: {exec_date.strftime(date_format)}")
    birth_day = datetime.strptime(args.birth_day, "%Y%m%d")
    print(f"誕生日: {birth_day.strftime(date_format)}")
    limit_day = add_years(birth_day, args.limit_years)
    print(f"想定寿命: {limit_day.strftime(date_format)}")
    current_date = exec_date - birth_day
    print(f"本日までの経過時間:\t{current_date.days*24}時間")
    print(f"本日までの経過日数:\t{current_date.days}日")
    current_month = monthmod(birth_day, exec_date)
    print(f"本日までの経過月数:\t{current_month[0].months}月")
    print(f"本日までの経過年数:\t{current_month[0].months//12}年")
    remaining_date = limit_day - exec_date
    print(f"想定寿命までの残り時間:\t{remaining_date.days*24}時間")
    print(f"想定寿命までの残り日数:\t{remaining_date.days}日")
    remaining_month = monthmod(exec_date, limit_day)
    print(f"想定寿命までの残り月数:\t{remaining_month[0].months}月")
    print(f"想定寿命までの残り年数:\t{remaining_month[0].months//12}年")
    all_date = limit_day - birth_day
    print(f"経過した人生の割合:\t{round((current_date/all_date)*100,2)}%")
    print(f"残りの人生の割合:\t{round((remaining_date/all_date)*100,2)}%")


if __name__ == "__main__":
    main()
