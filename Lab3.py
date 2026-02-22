# This code is for Lab 3 of the course "Data analytics" Johnny Sewell
# -------------------------------------------
# 1. Import Required Libraries
# -------------------------------------------
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------------------
# 2. Download Microsoft (MSFT) Stock Data
# -------------------------------------------
df = yf.download(
    "MSFT",
    start="2020-01-01",
    end="2020-12-31",
    auto_adjust=False,
    progress=False
)


# -------------------------------------------
# 3. Calculate Daily Simple Returns
# -------------------------------------------
df["simple_rtn"] = df["Adj Close"].pct_change()


# -------------------------------------------
# 4. Remove Missing Values
# -------------------------------------------
df = df.dropna()


# -------------------------------------------
# 5. Plot Stock Price and Returns 
# -------------------------------------------
(
df[["Adj Close", "simple_rtn"]]
.plot(subplots=True, sharex=True, title="MSFT Stock in 2020")
)

plt.show()


# -------------------------------------------
# 6. Plot Using Object-Oriented Matplotlib
# (More Control Over Visualization)
# -------------------------------------------
fig, ax = plt.subplots(2, 1, sharex=True)

df["Adj Close"].plot(ax=ax[0])
ax[0].set(title="MSFT Time Series", ylabel="Stock Price ($)")

df["simple_rtn"].plot(ax=ax[1])
ax[1].set(ylabel="Return (%)")


plt.show()

