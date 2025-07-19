def main():
    time_str = input("What time is it? ").strip()
    time_float = convert(time_str)

    if 7.00 <= time_float <= 8.00:
        print("breakfast time")
    elif 12.00 <= time_float <= 13.00:
        print("lunch time")
    elif 18.00 <= time_float <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()
