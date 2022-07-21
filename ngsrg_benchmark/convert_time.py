#!/usr/bin/env python3
"""Convert time in multiple format.

Usage:
======

./convert_time.py [-h] [--time TIME] [--time_type TIME_TYPE] [-S SECOND]
                  [-M MINUTE] [-H HOUR] [-D DAY]

Options:
    -h, --help                  show this help message and exit
    --time TIME                 Time to convert in D:HH:MM:SS format
    --time_type TIME_TYPE       format of time (default : second)
    -S SECOND, --second SECOND  number of second
    -M MINUTE, --minute MINUTE  number of minute
    -H HOUR, --hour HOUR        number of hour
    -D DAY, --day DAY           number of day
"""

import argparse
import sys


def get_arg_and_option() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert time")
    parser.add_argument("--time", help="Time to convert in D:HH:MM:SS format")
    parser.add_argument("--time_type", type=str, default="s",
                        help="format of time")
    parser.add_argument("-S", "--second", type=int, default=0,
                        help="number of second")
    parser.add_argument("-M", "--minute", type=int, default=0,
                        help="number of minute")
    parser.add_argument("-H", "--hour", type=int, default=0,
                        help="number of hour")
    parser.add_argument("-D", "--day", type=int, default=0,
                        help="number of day")

    return parser.parse_args()


def convert_in_second(time: int, time_type: str) -> int:
    if time_type == "m":
        return (time * 60)
    elif time_type == "h":
        return (time * 3600)
    elif time_type == "d":
        return (time * 86400)


def convert_time(time: float, time_type: str) -> str:
    final_time = []
    day, hour, minute = (0, 0, 0)

    if time_type != "s":
        time = convert_in_second(time, time_type)

    if time >= 86400:
        day = int(time / 86400)
        time %= 86400
    final_time.append(str(day))

    if time >= 3600:
        hour = int(time / 3600)
        time %= 3600
    if hour < 10:
        hour = f"0{hour}"
    final_time.append(str(hour))

    if time >= 60:
        minute = int(time / 60)
        time %= 60
    if minute < 10:
        minute = f"0{minute}"
    final_time.append(str(minute))

    time = int(time)
    if time < 10:
        time = f"0{time}"
    final_time.append(str(time))

    return ":".join(final_time)


def convert_time2(second: int, minute: int, hour: int,
                  day: int, time_type: str) -> float:
        if time_type == "s":
            time = second + (minute * 60) + (hour * 3600) + (day * 86400)
        elif time_type == "m":
            time = (second / 60) + minute + (hour * 60) + (day * 1440)
        elif time_type == "h":
            time = (second / 1440) + (minute / 60) + hour + (day * 24)
        elif time_type == "d":
            time = (second / 86400) + (minute / 1440) + (hour / 24) + day
        if time % 1 == 0:
            return int(time)
        return time


def split_time(time_split: list) -> tuple:
    if len(time_split) > 4:
        sys.exit("\nError : unexpected time format expected format are "+
                 "D:HH:MM:SS or HH:MM:SS or MM:SS or S\n")

    second, minute, hour, day = (0, 0, 0, 0)

    if len(time_split) == 2:
        second, minute = (time_split[1], time_split[0])
    elif len(time_split) == 3:
        second, minute, hour = (time_split[2], time_split[1], time_split[0])
    elif len(time_split) == 4:
        second, minute, hour, day = (time_split[3], time_split[2],time_split[1],
                                     time_split[0])

    return (int(second), int(minute), int(hour), int(day))


if __name__ == "__main__":
    args = get_arg_and_option()

    if not (args.time or args.second or args.minute or args.hour or args.day):
        sys.exit("\nError !!!\n\nNo option specified (used one or more of the "+
                 "following options: --time --time_type -S -M -H -D)\n\n ---\n"+
                 " View option with : ./convert_time.py -h\n ---\n\n"
                )

    if not (args.time_type == "s" or args.time_type =="m"
            or args.time_type == "h" or args.time_type == "d"):
        sys.exit("\nError : unexpected --time_type. --time_type expected "+
                 "are s, m or h\n\n")

    try:
        time_split = args.time.split(":")
    except:
        time_split = []

    if len(time_split) == 1:
        time = convert_time(float(time_split[0]), args.time_type)
    elif not (args.time and (args.second or args.minute or args.hour or args.day)):
        if (len(time_split) > 1):
            (second, minute, hour, day) = split_time(time_split)
        else:
            (second, minute, hour, day) = (args.second, args.minute, args.hour,
                                           args.day, args.time_type)
        time = convert_time2(second, minute, hour, day, args.time_type)
    else:
        sys.exit("\nError : Defined --time and -S -M -H -D options, "+
                 "but expected define is --time or -S -M -H -D options\n")

    print(time)
