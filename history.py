import requests, zipfile, io

symbols = ["AUDUSD", "EURUSD", "GBPUSD", "NZDUSD", "USDCAD", "USDCHF", "USDJPY"]
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
for i, symbol in enumerate(symbols):
    for _, year in enumerate(years):
        print("Download ", symbol, " ", year)
        print("Downloading...")
        request = "https://ticks.exness.info/ticks/{symbol}/{year}/Exness_{symbol}_{year}.zip".format(symbol=symbol, year=str(year))
        r = requests.get(request, allow_redirects=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("./data/{sym}/".format(sym=symbol))
        print("Done download ", symbol, " ", year)


symbols = ["AUDUSD_Raw_Spread", "EURUSD_Raw_Spread", "GBPUSD_Raw_Spread", "NZDUSD_Raw_Spread",
            "USDCAD_Raw_Spread", "USDCHF_Raw_Spread", "USDJPY_Raw_Spread", "XAUUSD_Raw_Spread",
            "AUDUSD_Zero_Spread", "EURUSD_Zero_Spread", "GBPUSD_Zero_Spread", "NZDUSD_Zero_Spread",
            "USDCAD_Zero_Spread", "USDCHF_Zero_Spread", "USDJPY_Zero_Spread", "XAUUSD_Zero_Spread"]
years = [2020, 2021]

for i, symbol in enumerate(symbols):
    for _, year in enumerate(years):
        print("Download ", symbol, " ", year)
        print("Downloading...")
        request = "https://ticks.exness.info/ticks/{symbol}/{year}/Exness_{symbol}_{year}.zip".format(symbol=symbol, year=str(year))
        r = requests.get(request, allow_redirects=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("./data/{sym}/".format(sym=symbol))
        print("Done download ", symbol, " ", year)