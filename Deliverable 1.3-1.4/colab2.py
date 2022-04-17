from google.colab import files
import yfinance as yf
import matplotlib.pyplot as plt

def split_plot(stock_name_list, comp_name_list, first_start, first_end, second_start, second_end):
  for i in range(len(stock_name_list)):
    first_start2 = first_start.split("-")
    for a in range(len(first_start2)):
      first_start2[a] = int(first_start2[a])
    start1_year = str(max(first_start2))

    first_end2 = first_end.split("-")
    for a in range(len(first_end2)):
      first_end2[a] = int(first_end2[a])
    end1_year = str(max(first_end2))


    second_start2 = second_start.split("-")
    for a in range(len(second_start2)):
      second_start2[a] = int(second_start2[a])
    start2_year = str(max(second_start2))

    second_end2 = second_end.split("-")
    for a in range(len(second_end2)):
      second_end2[a] = int(second_end2[a])
    end2_year = str(max(second_end2))

    stock_old = yf.download(stock_name_list[i], first_start, first_end, progress=False)
    stock_old_head=stock_old.head()

    stock_new = yf.download(stock_name_list[i], second_start, second_end, progress=False)
    if (stock_old_head.shape != (0, 6)):
      stock_old["Open"].plot(label ="Open prices from " +start1_year +" to " + end1_year)
      stock_new["Open"].plot(label ="Open prices from " + start2_year +" to " + end2_year)
    else:
      stock_new["Open"].plot(label ="Open prices from " + start2_year +" to " + end2_year)

    comp_name_split = comp_name_list[i].split(' ')
    comp_final_name= '_'.join(comp_name_split)
    save_name = 'Open_Prices_for_' + str(comp_final_name) + '.png'

    plt.legend()
    plt.title("Open Prices for " + comp_name_list[i])
    plt.savefig(save_name)
    plt.show()
    #files.download(save_name)
    #print(save_name)

split_plot(['TCS','WIT','MSFT','AMZN','GS','BABA','0656.HK','VTI','MS','BLK','C'], ['TCS','WIPRO','MICROSOFT','AMAZON','Goldman Sachs Group Inc','Alibaba Group Holding Ltd','Fosun International Ltd','Vanguard Group, Inc.','Morgan Stanley','Blackrock Inc.','Citigroup Inc.'], "2010-01-01", "2014-01-01", "2014-01-01", '2019-01-01')
