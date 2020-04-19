import pandas as pd
import math
from tabulate import tabulate

FILENAME = "master.xlsx"


def read_and_convert():
    """
    Since prophet wants a dataframe with two columns [ds, y] a conversion is needed.

    :return: dataframe with the data in a prophet-friendly manner.
    """
    df = pd.read_excel(FILENAME, index_col=0)
    # loop over years
    converted_df = pd.DataFrame(columns=['ds', 'y'])
    for year, row in df.iterrows():
        # loop over months
        for month, value in row.items():
            if math.isnan(value):
                continue
            # ds becomes YYYY-MM-DD. Setting day to 15 to represent monthly average.
            converted_df = converted_df.append(
                {'ds': '-'.join((str(year), str(month), "15")), 'y': value},
                ignore_index=True,
            )
    return converted_df


def read_and_convert_month(month):
    """

    :param month: month represented by a string using two ints, as according to 'master.xlsx'.
    :return: dataframe with columns [ds, y] with only the given months data.
    """
    df = pd.read_excel(FILENAME, index_col=0)
    # loop over years
    converted_df = pd.DataFrame(columns=['ds', 'y'])
    for year, row in df.iterrows():
        # loop over months
        for m, value in row.items():
            if m != month:
                continue
            if math.isnan(value):
                continue
            converted_df = converted_df.append(
                {'ds': '-'.join((str(year), str(m), "15")), 'y': value},
                ignore_index=True,
            )
    return converted_df


def print_data():
    '''
    Helper to print head and tail of dataframe for README :)
    :return:
    '''
    df = pd.read_excel(FILENAME, index_col=0)
    headers = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    print(tabulate(df.head(), tablefmt="github", headers=headers))


if __name__ == "__main__":
    print_data()
