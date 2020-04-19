from fbprophet import Prophet
from convert_data import read_and_convert_month
import matplotlib.pyplot as plt
import pandas as pd


def main():
    for m in range(1, 13):
        plot_months_forecast("{:02}".format(m))
        plot_months_components("{:02}".format(m))


def plot_months_forecast(month):
    df = read_and_convert_month(month)
    m = Prophet(yearly_seasonality=False).fit(df)
    future = m.make_future_dataframe(periods=10, freq="Y")
    fcst = m.predict(future)
    fig = plt.figure(facecolor='w', figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.set_title(month)
    fig = m.plot(fcst, ax=ax, xlabel="year", ylabel="Temp [Celsius]")
    fig.savefig("".join((month, ".png")))


def plot_months_components(month):
    df = read_and_convert_month(month)
    m = Prophet(yearly_seasonality=False).fit(df)
    future = m.make_future_dataframe(periods=10, freq="Y")
    fcst = m.predict(future)
    fig = m.plot_components(fcst)
    fig.savefig("".join((month, "_components", ".png")))


def plot_data():
    df = pd.read_excel("master.xlsx", index_col=0)
    fig = plt.figure(facecolor='w', figsize=(10, 6))
    ax = fig.add_subplot(111)
    df.plot(ax=ax, legend=False, title="monthly average temperature [°]")
    fig.legend(loc="right")
    fig.savefig("plots/df.png")


def boxplot():
    '''

    :return:
    '''
    df = pd.read_excel("master.xlsx", index_col=0)
    fig = plt.figure(facecolor='w', figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.set_title("Box plot for each month")
    df.boxplot(ax=ax)
    fig.savefig("plots/boxplot.png")


if __name__ == "__main__":
    boxplot()
