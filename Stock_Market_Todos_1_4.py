from google.colab import files
import numpy as np
import copy
import yfinance as yf
import pandas as pd

# Functions
def collect_data(Name, Start, End):
  global name_array

  name_df = yf.download(Name,  start = Start , end = End) 
  #name_df = name_df.head()
  name_newdf = name_df.reset_index() 
  name_array_1 = name_newdf.to_numpy()
  rows, columns = name_array_1.shape
  tcs_array = np.array([['Date', 'Open','High','Low','Close','Adj Close','Volume']])

  for a in range(rows):
    mod = name_array_1[a, 0]
    name_array_1[a, 0] = str(mod)

  name_array = np.append(tcs_array, name_array_1, axis = 0)
  #print(name_array)

def get_average(obj_arr):
  global avg_array
  global obj_arr_mod
  avg_array = (obj_arr[1:, 2]+obj_arr[1:, 3])/2
  avg_array = np.append([["Average"]], avg_array)
  avg_array = avg_array.reshape(avg_array.shape[0], -1)

  obj_array_p2 = obj_arr[:, 4:]
  obj_arr_mod = np.append(obj_arr[:, :4], avg_array, axis = 1)
  obj_arr_mod = np.append(obj_arr_mod, obj_array_p2, axis = 1)

#Todo 1+2
collect_data('TCS', '2014-01-01', '2022-01-01')
tcs_array = name_array

collect_data('MSFT', '2012-01-01', '2022-01-01')
msft_array = name_array

collect_data('AMZN', '2012-01-01', '2022-01-01')
amzn_array = name_array

collect_data('GOOGL', '2012-01-01', '2022-01-01')
googl_array = name_array

collect_data('FB', '2012-01-01', '2022-01-01')
fb_array = name_array

#Todo 3+4

get_average(tcs_array)
tcs_array = obj_arr_mod

get_average(msft_array)
msft_array = obj_arr_mod

get_average(amzn_array)
amzn_array = obj_arr_mod

get_average(googl_array)
googl_array = obj_arr_mod

get_average(fb_array)
fb_array = obj_arr_mod

#Download
df = pd.DataFrame(tcs_array[1:, :], columns = list(tcs_array[0, :]))
print(df)

df.to_csv('TCS_Data.csv', mode='w')

df = pd.DataFrame(msft_array[1:, :], columns = list(msft_array[0, :]))
print(df)

df.to_csv('MSFT_Data.csv', mode='w')

df = pd.DataFrame(amzn_array[1:, :], columns = list(amzn_array[0, :]))
print(df)

df.to_csv('AMZN_Data.csv', mode='w')

df = pd.DataFrame(googl_array[1:, :], columns = list(googl_array[0, :]))
print(df)

df.to_csv('GOOGL_Data.csv', mode='w')

df = pd.DataFrame(fb_array[1:, :], columns = list(fb_array[0, :]))
print(df)

df.to_csv('FB_Data.csv', mode='w')

files.download('TCS_Data.csv')
files.download('MSFT_Data.csv')
files.download('AMZN_Data.csv')
files.download('GOOGL_Data.csv')
files.download('FB_Data.csv')





