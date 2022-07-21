"""Generate benchmark graph of ngs-rg mgi lite pipeline.

Usage:
======

./graph_benchmark_ngsrg_mgi_lite.py [--file FILE]

Options:
    --file FILE     CSV file of benchmark metrics of ngs-rg mgi pipeline lite
"""

import argparse
import sys
import pandas as pd
import seaborn as sns
import convert_time
import matplotlib.pyplot as plt


def get_arg_and_option() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate benchmark graph of "
                                     "ngs-rg mgi lite")
    parser.add_argument("--file", help="csv file of benchmark metrics of ngs-rg "
                        "mgi pipeline lite", type=str)
    return parser.parse_args()


def parse_csv_file(file: str) -> dict:
    dtf = pd.read_csv(file, sep=",")
    return dtf


def create_barplot(x: list, y: list, title: str, xlab: str, ylab: str) -> None:
    sns.set_theme(style="darkgrid")
    plt.bar(x, y)
    plt.show()
    # plt.savefig(title + ".png")



if __name__ == "__main__":
    args = get_arg_and_option()
    file = args.file
    dtf = parse_csv_file(file)
    dtf = dtf.dropna()
    list_time = [str(time).split(":") for time in dtf["Time"]]
    print(list_time)
    list_time = [convert_time.convert_time2(int(time[2]), int(time[1]), int(time[0]), 0, time_type="h") for time in list_time]
    print(list_time)
    create_barplot(dtf["Run"], list_time, "barplot_test", "xlab", "ylab")
