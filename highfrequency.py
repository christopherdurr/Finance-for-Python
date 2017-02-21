import numpy as np
import pandas as pd
import datetime as dt
from urllib import urlretrieve

url1 = 'http://hopey.netfonds.no/posdump.php?'
url2 = ‘date=%s%s%s&paper=AAPL.O&csv_format=csv’
url = url1 + url2

year = '2014'
month = '09'
days = ['22', '23', '24', '25']

AAPL = pd.DataFrame()
for day in days:
  AAPL = AAPL.append(pd.read_csv(url % (year, month, day), index_col = 9, header = 0, parse_dates = True))
AAPL.columns = ['bid', 'bdepth', 'bdeptht', offer', 'odepth', 'odeptht']
AAPL.info()

AAPL['bid'].plot()

to_plot = AAPL[['bid', 'bdeptht']][
  (AAPL.index > dt.datatime(2014, 9, 22, 0, 0))
  & (AAPL.index < dt.datetime(2014, 9, 23, 2, 59))]
  # adjust dates to given data set
to_plot.plot(subplots = True, style = 'b', figsize = (8,5))

