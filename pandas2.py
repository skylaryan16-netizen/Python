# %%
import pandas as pd

# %%
# GROUP BY

# %%
companies = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\fortune1000.csv")

companies.head()

# %%
companies

# %%
sec_grp = companies.groupby('Sector')

# %%
type(sec_grp), type(companies)

# %%
sec_grp.head()

# %%
sec_grp

# %%
sec_grp.size()

# %%
sec_grp.first()

# %%
sec_grp.last()

# %%
sec_grp.sum(True)

# %%
companies.groupby('Sector').mean(True)

# %%
sec_grp[['Revenue', 'Profits']].mean(True)

# %%
df = sec_grp['Revenue'].std(True)

df

# %%
type(df)

# %%
df = df.reset_index(name = 'Std_Revenue')

df

# %%
sec_grp[["Revenue","Profits","Employees"]].agg(['mean','max','min'])

# %%
sec_grp[['Revenue','Profits']].agg(['mean','max','min','median','std'])

# %%
sec_grp['Revenue'].describe()

# %%
sec_grp.agg({'Revenue':'mean', 'Profits':'max','Employees':'median'})

# %%
sec_grp.groups

# %%
sec_grp.groups['Technology']

# %%
tech_index = sec_grp.groups['Technology']

tech_index

# %%
companies[companies.index.isin(tech_index)]

# %%
sec_grp.get_group('Health Care')

# %%
# JOINS



# 1. Concat -  (as Union in SQL)

foods = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Restaurant - Foods.csv")

foods

# %%
customers = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Restaurant - Customers.csv")

customers.head()

# %%
wk1 = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Restaurant - Week 1 Sales.csv")

wk1

# %%
wk2 = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Restaurant - Week 2 Sales.csv")

wk2

# %%
sattisfaction = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Restaurant - Week 1 Satisfaction.csv")

sattisfaction.head()


# %%
# Concatenation (Concat)

comb_wk = pd.concat(objs = [wk1 , wk2], ignore_index = True)

comb_wk

# %%

comb_wk = pd.concat(objs = [wk1 , wk2], keys = ('wk1','wk2'))

comb_wk

# %%
wk1['indicator'] ='wk1'
wk2['indicator'] ='wk2'

# %%
wk_data = pd.concat(objs=[wk1,wk2], ignore_index = True)

wk_data

# %%
wk_data['Food ID'].value_counts()

# %%
len(wk_data['Customer ID'].unique())

# %%
#2. Megre ( as Joins in SQL)

# syntax:-   merged_data = df1.merge(df2,how = 'left', on =[])


# %%
wk_join = wk1.merge(wk2,how = 'inner', on= ['Customer ID'])

wk_join

# %%
wk_join = wk1.merge(wk2,how = 'inner', on= ['Customer ID'], suffixes = ('_wk1','_wk2'))

wk_join

# %%
wk_join = wk1.merge(wk2,how = 'outer', on= ['Customer ID'], suffixes = ('_wk1','_wk2'))

wk_join

# %%
outer_wk_join = wk1.merge(wk2,how = 'outer', on= ['Customer ID'], suffixes = ('_wk1','_wk2'), indicator = True)

outer_wk_join

# %%
outer_wk_join['_merge'].value_counts()

# %%
outer_wk_join = wk1.merge(wk2,how = 'outer', left_index = True, right_index = True, suffixes = ('_wk1','_wk2'), indicator = True)

outer_wk_join

# %%
wk1 = wk1.set_index('Customer ID')

wk1.head()

# %%
wk2 = wk2.set_index('Customer ID')

wk2.head()

# %%
index_wise_merge = wk1.merge(wk2, left_index = True, right_index = True)

index_wise_merge

# %%
wk1[wk1.index == 77]

# %%
wk2[wk2.index == 77]

# %%
index_wise_merge[index_wise_merge.index == 77]

# %%
wk1 = wk1.reset_index()

wk1.head()

# %%
wk2 = wk2.reset_index()

wk2.head()

# %%
# 3) JOIN

wk1.head()

# %%
sattisfaction.head()

# %%
wk1.join(sattisfaction).head()


# %%
wk1.to_csv('learning_output.csv')

# %%
import pandas as pd

# %%
# reading data from excel


excel_df = pd.read_excel(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Data - Single Worksheet.xlsx")


excel_df

# %%
multi_excel_df = pd.read_excel(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Data - Multiple Worksheets.xlsx")

multi_excel_df

# %%
multi_excel_df = pd.read_excel(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Data - Multiple Worksheets.xlsx", sheet_name = None)

multi_excel_df

# %%
multi_excel_df['Data 2']

# %%
type(multi_excel_df)

# %%
multi_excel_df = pd.read_excel(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Data - Multiple Worksheets.xlsx", sheet_name = 'Data 2')

multi_excel_df

# %%
multi_excel_df = pd.read_excel(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Data - Multiple Worksheets.xlsx", sheet_name = [1,0])

multi_excel_df

# %%
multi_excel_df = pd.read_excel(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Data - Multiple Worksheets.xlsx", sheet_name = ['Data 2','Data 1'])

multi_excel_df

# %%
excel_df = pd.read_excel(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\Data - Single Worksheet.xlsx")

excel_df

# %%
male_baby_name = excel_df[excel_df['Gender'] == 'M'][['First Name']]

male_baby_name

# %%
female_baby_name = excel_df[excel_df['Gender'] == 'F'][['First Name']]

female_baby_name

# %%
excel_file = pd.ExcelWriter('baby_names.xlsx')

# %%
male_baby_name.to_excel(excel_file,sheet_name = 'male_baby_name', index = False)

female_baby_name.to_excel(excel_file,sheet_name = 'female_baby_name', index = False)

excel_file.close()

# %%
#Regular Expression  (use cheat sheet from - towards data science)

# to search for special keywords/ pattern in a given input text

# pratice by own

# %%
# Timeseries

# %%
salesmen = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\salesmen.csv")

salesmen.head()

# %%
import datetime as dt

# %%
somedate = dt.date(2020,12,13)
somedate

# %%
somedate.day, somedate.month, somedate.year

# %%
somedate = dt.date(2020,12,13)
somedate

# %%
somedate = dt.date(2020)
somedate

# %%
somedate = dt.date(2020,12,13,4,34,35)
somedate

# %%
somedatetime = dt.datetime(2020,12,13,4,34,35)
somedatetime

# %%
type(somedatetime)

# %%
type(somedate)

# %%
str(somedatetime), str(somedate)

# %%
# datetime in Pandas

# %%
pd.Timestamp(2020)

# %%
pd.Timestamp(year =2023, month = 4, day =2)

# %%
pd.Timestamp(3600, unit = 's')

# %%
pd.Timestamp(365, unit = 'D')

# %%
# to_datetime --> to convert strings into datetime

timeseries = pd.Series(['2022-01-01','2023-09-15','2021/05/25','2030'])

timeseries

# %%
pd.to_datetime(timeseries, format="mixed")

# %%
    timeseries2 = pd.Series(['2022-01-01','2023-09-15','2021/05/25','2030', 'abc'])

timeseries2

# %%
pd.to_datetime(timeseries2, format="mixed")

# %%
pd.to_datetime(timeseries2,format="mixed", errors = 'coerce')

# %%
pd.to_datetime(timeseries2,format="mixed", errors = 'ignore')

# %%
salesmen.head()

# %%
salesmen['Date'] = pd.to_datetime(salesmen['Date'])

salesmen.head()

# %%
salesmen.dtypes

# %%
salesmen_pivot = salesmen.pivot(index = 'Date', columns = 'Salesman', values = 'Revenue')

salesmen_pivot

# %%
# Vizualization

# pip install matplotlib
# pip install seaborn
#pip install plotly
# pip intall folium
# pip install ggplot

# %%
import matplotlib.pyplot as plt

plt.plot([2,4,6,4])
plt.ylabel("Numbers")
plt.xlabel("Indices")
plt.title("Myplot")
plt.show()

# %%
plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel("Squares")
plt.xlabel("Numbers")
plt.title("Myplot_squares")
plt.grid()
plt.show()

# %%
plt.plot([1,2,3,4],[1,4,9,16],"go")
plt.ylabel("Squares")
plt.xlabel("Numbers")
plt.title("Myplot_squares")
plt.grid()
plt.show()

# %%
import numpy as np

t = np.arange(0.,5.,0.2)
# blue dashes(b--), red squares(rs), green triangle(g^)
plt.plot(t,t**2,'b--',label='^2')
plt.plot(t,t**3,'rs',label='^3')
plt.plot(t,t**4,'g^',label='^4')
plt.grid()
plt.legend()    #add legend based on the line labels
plt.show()

# %%
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y,linewidth=8.0)
plt.show()

# %%
x1 = [1,2,3,4]
y1 = [1,4,9,16]
x2 = [1,2,3,4]
y2 = [2,4,6,8]

lines = plt.plot(x1, y1, x2, y2)

plt.setp(lines[0],color = 'r', linewidth = 2.0)   #Python style string value pairs

plt.setp(lines[1],'color','g', 'linewidth','2.0')  #MATLAB style string value pairs

plt.grid()

# %%
import matplotlib.pyplot as plt
import numpy as np
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)

plt.subplot(221)
plt.grid()
plt.plot(t1,f(t1),'b--')

plt.subplot(222)
plt.grid()
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)

plt.subplot(121)
plt.grid()
plt.plot(t1,f(t1),'b-')

plt.subplot(122)
plt.grid()
plt.plot(t2,np.cos(2*np.pi*t2),'r--')
plt.show()

# %%
plt.figure(1)
plt.subplot(121)
plt.plot([1,2,3])
plt.subplot(122)
plt.plot([4,5,6])

plt.figure(2)
plt.plot([4,5,6])

plt.figure(1)
plt.subplot(121)
plt.title("easy 1,2,3")
plt.show()

# %%
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# %%
sales = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\salesmen.csv")
sales.head()

# %%
sales.plot()

# %%
sales[sales['Salesman'] == 'Bob'].plot()

# %%
sales[sales['Date'] > '1/8/16'][sales['Salesman'] == 'Bob'].plot()

# %%
msp = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\MSFT.csv", index_col = 'Date')

msp.head()

# %%
msp.index.max()

# %%
msp.index.min()

# %%
msp.plot()

# %%
msp['High'].plot()

# %%
msp[['High','Close']].plot()

# %%
msp['datetime'] = pd.to_datetime(msp.index)

msp.head()

# %%
msp['year'] = msp['datetime'].dt.year

msp['month'] = msp['datetime'].dt.month

msp.head()

# %%
monthly_open_mean = msp.groupby(['year','month'])['Open'].mean().reset_index(name = 'mean_open')

# %%
monthly_open_mean

# %%
monthly_open_mean['mean_open'].plot(kind = 'bar')

# %%
monthly_open_mean['year/month'] = monthly_open_mean['year'].astype(str) + '/' + monthly_open_mean['month'].astype(str)

monthly_open_mean.head()

# %%
monthly_open_mean.plot( x ='year/month', y = 'mean_open', kind = 'bar')

# %%
# For Pie- Chart

def status_func(val):
    if val <= 280:
        status = 'BAD'
    
    elif val > 280 and val < 300:
        status = 'AVERAGE'
        
    else:
        status = 'GOOD'
        
    return status

monthly_open_mean['status'] = monthly_open_mean['mean_open'].apply(status_func)

monthly_open_mean


# %%
monthly_open_mean['status'].value_counts()

# %%
monthly_open_mean['status'].value_counts().plot(kind = 'pie')

# %%
plt.style.available

# %%
plt.style.use('classic')

# %%
monthly_open_mean['status'].value_counts().plot(kind = 'pie')

# %%
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

# %%




