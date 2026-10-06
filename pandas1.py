# %%
import pandas as pd


# %%
pd.__version__

# %%
ser = pd.Series(['mango','banana','orange','chickoo'])

ser

# %%
type(ser)

# %%
ser[1:]

# %%
ser.count()

# %%
type(ser)

# %%
fruits = ['mango','banana','orange','chickoo']

ser = pd.Series(fruits)

ser

# %%
fruits = ['mango','banana','orange','chickoo']
abc = [1,2,3,4]

ser = pd.Series(fruits)
ser = pd.Series(abc)
ser

# %%
fruits = ['mango','banana','orange','chickoo']
abc = [1,2]
d = (3,4)

ser = pd.Series((fruits,abc,d))

ser

# %%
fruits = ['mango','banana','orange','chickoo']

ser = pd.Series(fruits)


ser

# %%
fruits = ['mango','banana','orange','chickoo']

days =  ['mon','tue','wed','thu']


ser2 = pd.Series(data = fruits, index = days)
ser2

# %%
ser[2]

# %%
ser2['thu']

# %%
ser2[3]

# %%
ser3 = pd.Series(data = days, index = fruits)
ser3

# %%
days_fruits_dict = {'mon':'mango','tue':'banana','wed':'orange','thu':'chickoo'}


dict_series = pd.Series(days_fruits_dict)

dict_series

# %%
dict_series.values

# %%
dict_series.value_counts

# %%
dict_series= dict_series.str.upper()

# %%
dict_series

# %%
dict_series = dict_series.index.upper()

dict_series

# %%
dict_series = dict_series.index.str.upper()

dict_series 

# %%
emp_dict = {'id':[1,2,3,4,5], 'initials':['mr','mrs','dr','drs','cr'], 'salary':[100,200,300,400,500]}

emp_dict

# %%
ser3 = pd.Series(emp_dict)
ser3

# %%
df = pd.DataFrame(emp_dict)

df

# %%
type(df)

# %%
df.dtypes

# %%
type(ser)

# %%
df['id']

# %%
df['id'][2]

# %%
print(df[['id','salary']])

# %%
type(df['id'])

# %%
# how to read a data/ file with pandas

# %%
import pandas as pd

# %%
emp_df = pd.read_csv(D:\Data Analyst Classes\Data for Classes\Python\Data Files\employees.csv)

# %%
emp_df = pd.read_csv("D:/Data Analyst Classes/Data for Classes/Python/Data Files/employees.csv")

# %%
emp_df

# %%
emp_df.head(n=10)

# %%
emp_df.tail()

# %%
emp_df.head(10)

# %%
emp_df = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\employees.csv")

emp_df.head()

# %%
emp3_df = pd.read_csv("D:\\Data Analyst Classes\\Data for Classes\\Python\\Data Files\\employees.csv")
emp3_df.head()

# %%
emp_df.info()

# %%
emp_df.dtypes

# %%
abc = emp_df.info()

abc


# %%
type(abc)

# %%
emp_df.isnull()

# %%
emp_df.isnull().sum()

# %%
emp_df.notnull().sum()

# %%
emp_df.sort_values(by = 'Salary', ascending = False, ).head()


# %%
emp_df.head()

# %%
emp_df_sort = emp_df.sort_values(by = 'Salary', ascending = False)

emp_df_sort.head()

# %%
emp_sorted = emp_df.sort_values(by=['First Name', 'Salary'], ascending=[True, False])

emp_sorted.head()

# %%
emp_df.describe()

# %%
emp_df['Salary'].sum()

# %%
emp_df.T

# %%
emp_df['Team'].value_counts()

# %%
emp_df['Team'].value_counts(dropna = True)

# %%
emp_df['Team'].value_counts(dropna = False)

# %%
emp_df['Team'].value_counts(dropna = False, normalize = True)

# %%
emp_df.head()

# %%
emp_df[['Company', 'abc']] = 'Google'

emp_df.tail()

# %%
emp_df.drop(columns=['abc'], inplace = True)
emp_df.head()

# %%
emp_df.columns

# %%
emp_df.drop(columns=[('Company', 'abc')], inplace = True)
emp_df.head()

# %%
emp_df['Company']= 'Microsoft'

emp_df.head(9)

# %%
emp_df['Team'].unique()

# %%
emp_df['Team'].replace(to_replace = 'Client Services' , value = 'CS').head()

# %%
emp_df['Team'].replace(to_replace = NaN , value = 'unknown').head()

# %%
emp_df['Team'].fillna(value = 'unknown').tail()

# %%
emp_df2 = emp_df.dropna(subset = ['First Name'], how = 'all')

emp_df2.head(9)

# %%
emp_df2.info()

# %%
emp_df.isnull().sum()

# %%
emp_df2.isnull().sum()

# %%
emp_df10 = emp_df.dropna(subset = ['Team', 'Gender'], how = 'all')

emp_df10.head(9)

# %%
emp_df10.isnull().sum()

# %%
emp_df3 = emp_df2.drop_duplicates(subset = ['First Name', 'Team'])

emp_df3.head()

# %%
emp_df3.info()

# %%
# data filtering


# dataframe[condition]

emp_df['Gender'] == 'Male'

# %%
emp_df[emp_df['Gender'] == 'Male']

# %%
cond1 = emp_df['Gender'] == 'Male'

emp_df[cond1].head()

# %%
cond1 = emp_df['Gender'] == 'Male'
cond2 = emp_df['Salary'] > 100000

emp_df[cond1 and cond2].head()

# %%
cond1 = emp_df['Gender'] == 'Male'
cond2 = emp_df['Salary'] > 100000

emp_filter = emp_df[cond1 & cond2]

emp_filter.head()

# %%
emp_filter.info()

# %%
cond1 = emp_df['Senior Management'] == "True"
cond2 = emp_df['Bonus %'] >= 10

emp_df[cond1 | cond2].head(10)

# %%
cond3 = emp_df['Salary'] >= 120000

emp_df[(cond1 | cond2) & cond3].head()

# %%
cond4=emp_df['Team']=='Legal'
cond5=emp_df['Team']=='Product'   
cond6=emp_df['Team']=='Finance'

emp_df[cond4|cond5|cond6].head()

# %%
# isin operator

cond = emp_df['Team'].isin(['Legal','Product','Finance'])

emp_df[cond].head()

# %%
cond7 = emp_df['Bonus %'].between(2,5)

emp_df[~cond7].head()

# %%
cond8 = emp_df ['Bonus %'].isin(range(2,5))

emp_df[cond8]

# %%
emp_50 = emp_df.head(50)

emp_50.head()

# %%
cond9 = emp_50['Bonus %'].between(2,5)

emp_50[cond9]

# %%
emp_df.head(50)[cond7]

# %%
emp_df[cond7].head(200)

# %%
emp_df = pd.read_csv("D:/Data Analyst Classes/Data for Classes/Python/Data Files/employees.csv")

# %%
emp_df.head()

# %%
emp_df.info()

# %%
# to covert in date time format

pd.to_datetime(emp_df['Last Login Time']).dt.time.head()

# %%
pd.to_datetime(emp_df['Start Date'],format='mixed',
    dayfirst=False,errors='coerce').dt.date.head()

# %%
pd.to_datetime(emp_df['Start Date'], format='mixed',
    dayfirst=False,errors='coerce').dt.date.isnull().sum()

# %%
emp_df['Start Date'] = pd.to_datetime(emp_df['Start Date'], format='mixed',
    dayfirst=False,errors='coerce').dt.date

emp_df.head()

# %%
emp_df.info()

# %%
emp_df['Last Login Time'] = pd.to_datetime(emp_df['Last Login Time']).dt.time

emp_df.head()

# %%
emp_df.info()

# %%
emp_df['Start Date'].dtypes

# %%
emp_df['Salary'] = emp_df['Salary'].astype('float')
emp_df.head()

# %%
emp_df.info()

# %%
emp_df['Start Date'] = emp_df['Start Date'].astype('datetime64[ns]')

emp_df.head()

# %%
emp_df.info()

# %%
cond10 = emp_df['Team']!= 'Finance'

emp_df[cond10].head()

# %%
cond11 = emp_df['Team'] == 'Finance'

emp_df[~ cond11].head()

# %%
cond7 = emp_df['Bonus %'].between(2,5)

emp_df[~cond7].head()

# %%
cond1 = emp_df['Senior Management'] == True 
cond2 = emp_df['Bonus %'] >= 10

emp_df[~((cond2) | (cond1))].head()

# %%
emp_df[~((emp_df['Bonus %']>=10) | (emp_df['Senior Management']== True))].head()

# %%
c1 = emp_df['First Name'].isnull()

emp_df[~c1].head(9)

# %%
c2 = emp_df['First Name'].notnull()

emp_df[c2].head(9)

# %%
# Axes

# axis = 0 -> rows
# axis =1  -> columns

emp_df.columns

# %%
emp_df.index

# %%
# Q. I want all the data of employees for which we have data for all the fields

# 1. Use dropna and save it to new dataframe - parameter- how- 'any
# 2. use 8 conditions for each column with notnull and then use & operator .



# %%
emp_df.notnull

# %%
emp_df.head()

# %%
emp_df.isnull().sum()

# %%
emp_df.isnull().sum(axis =1).head()

# %%
emp_df_NN = emp_df[emp_df.isnull().sum(axis =1) == 0]
emp_df_NN.head()

# %%
emp_df_NN.info()

# %%
emp_df = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\employees.csv", parse_dates = ['Start Date'], date_format = "mixed")

emp_df.head()

# %%
emp_df.info()

# %%
# Indexing
# by default - 0 to n


# %%
emp_df.set_index('First Name').head()

# %%
emp_df.head()

# %%
import pandas as pd

# %%
pok = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\pokemon.csv")

pok.head()

# %%
pok.loc['Bulbasaur']

# %%
pok.loc[3]

# %%
pok.set_index(keys = 'Pokemon', inplace = True)


# %%
pok.head()

# %%
pok.loc['Bulbasaur']

# %%
pok.iloc[1]

# %%
nba = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\nba.csv")

nba.head()

# %%
nba.loc[4]

# %%
nba.loc[3:10]

# %%
nba.loc[3:10, ['Name','Team','Salary']]

# %%
nba = nba.sort_values(by = 'Salary', ascending = False)

nba.head()

# %%
nba.loc[3:10]

# %%
nba.iloc[3:10]

# %%
nba.loc[:3:3]

# %%
nba.iloc[:3]

# %%
nba.iloc[:3, :5]

# %%
nba.head(10)

# %%
nba.loc[251:294, 'Name':'Age']

# %%
nba.iloc[9,2]

# %%
df = pd.read_clipboard()

df

# %%
df.sort_values('Volume', ascending = False).head()

# %%
bond = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\jamesbond.csv")

bond.head()

# %%
bond.set_index('Film', inplace = True)
bond.head()

# %%
bond.loc['Dr. No']

# %%
bond.loc['Goldfinger','Box Office'] = 820

bond.head()

# %%
bond.loc[bond['Year']< 1967,'Director'] = 'Christopher'

bond.head()

# %%
bond = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\jamesbond.csv")

bond.head()

# %%
bond.axes

# %%
bond.rename(mapper ={'Film':'Movie', 'Box Office': 'Revenue', 'Bond Actor Salary': 'Salary'}, axis =1).head()

# %%
bond.head()

# %%
bond.rename(columns={'Film':'Movie', 'Box Office': 'Revenue', 'Bond Actor Salary': 'Salary'}).head()

# %%
bond.sample(n =10)

# %%
bond.sample(n =10)

# %%
bond.sample(n =10, random_state = 2)

# %%
bond.sample(n =10, random_state = 2)

# %%
bond.sample(random_state = 2)

# %%
bond.sample( n=12, random_state = 2)

# %%
bond.sample( frac = .4, random_state = 2)

# %%
bond.shape

# %%
bond.shape[0]

# %%
bond.nlargest( n = 10, columns = 'Box Office')


# %%
bond.nsmallest( n = 10, columns = 'Box Office')

# %%
bond[bond['Actor'] == 'Daniel Craig']

# %%
bond.where(bond['Actor'] == 'Daniel Craig')

# %%
bond.query('Actor == "Daniel Craig"')

# %%
bond.loc[25, 'Bond Actor Salary'] = 0

bond

# %%
bond.tail()

# %%
bond.info()

# %%
x = 456.7
y = str(x) 
w = int(round(x))
print(w)
z = y + " M$"
z

# %%
def cleaning_data(num):
    num = num*0.8
    num = int(num)
    num = str(num) + '-M$'
    
    return num


bond['Box Office'] = bond['Box Office'].apply(cleaning_data)

bond.head()


# %%
bond['Budget'] = bond['Budget'].apply(cleaning_data)

bond.head()

# %%
bond['Bond Actor Salary'] = bond['Bond Actor Salary'].apply(cleaning_data)

bond.head()

# %%
# to fill the nan values with unknown and add currency digits to the numbers in actors salary

# %%
import pandas as pd

# %%
def cleaning_data(num):
    num = num*0.8
    if pd.isna(num):     # we can also use math.isnan  ( we need to import math librabry), or np.nan (need to import numpy)
        num = 'unknown'
    else:    
        num = int(num)
        num = str(num) + '-M$'
    
    return num


bond['Bond Actor Salary'] = bond['Bond Actor Salary'].apply(cleaning_data)

bond.head()

# %%
bond = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\jamesbond.csv")

bond.head()

# %%
bond.head()

# %%
bond['abc'] = 'xyz'
bond.head()


# %%
def deciciding_outcome(row):
    # BO >= 500M , bud <= 20M  --> blockbuster
    # BO >= 500M , bud > 20M  --> Superhit
    # BO < 500M , bud < 20M  --> Hit
    # BO < 500M , bud >= 20M  --> FLOP
    
    if row['Box Office'] >= 500 and row['Budget'] <= 20:
        row['Outcome'] = 'Blockbuster'
        
    elif row['Box Office'] >= 500 and row['Budget'] > 20:
        row['Outcome'] = 'Superhit'
        
    elif row['Box Office'] < 500 and row['Budget'] <= 20:
        row['Outcome'] = 'Hit'
        
    else:
        row['Outcome'] = 'Flop'
        
    return row


bond = bond.apply(deciciding_outcome, axis = 1)
bond.head()

# %%
# Text Operations


chicago = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\chicago.csv")

chicago.head()

# %%
text = ' I live in Pune'


# %%
text.upper(), text.lower(), text.title()

# %%
chicago['Position Title'] = chicago['Position Title'].lower()

chicago.head()

# %%
chicago['Position Title'] = chicago['Position Title'].str.lower()

chicago.head()

# %%
chicago['Name'] = chicago['Name'].str.title()

chicago.head()

# %%
chicago['Name_length'] = chicago['Name'].str.len()

chicago.head()

# %%
chicago.info()

# %%
chicago['Employee Annual Salary'].describe()

# %%
chicago['Employee Annual Salary'].mean()

# %%
chicago.info()

# %%
chicago['Employee Annual Salary'] = chicago['Employee Annual Salary'].str.replace('$','')

chicago.head()

# %%
chicago.info()

# %%
chicago['Employee Annual Salary'] = chicago['Employee Annual Salary'].astype('int')

chicago.head()


# %%
chicago.isnull().sum()


# %%
chicago.tail()

# %%
chicago.dropna(how = 'all', inplace = True)

chicago.tail()

# %%
chicago['Employee Annual Salary'] = chicago['Employee Annual Salary'].astype('float').astype('int')

chicago.head()


# %%
chicago['Employee Annual Salary'].mean()

# %%


# %%
chicago.info()

# %%
chicago.describe()

# %%
chicago['Department'] = chicago['Department'].str.replace('MGMNT', 'MANAGEMENT')

chicago.head()

# %%
chicago[chicago['Department'].str.contains('FI')].tail()

# %%
chicago[chicago['Department'].str.startswith('FI')].tail()

# %%
chicago[chicago['Department'].str.endswith('CE')].head()

# %%
chicago['Name'].str.split(',', expand = True).head()

# %%
chicago[['First_Name', 'Last_Name']] = chicago['Name'].str.split(',', expand = True)

chicago.head()

# %%
# how to alter index postions of  columns in a dataframe  --- interview question

# how to split the words after second space  -- interview question

# %%
chicago['postiton_len'] = chicago['Position Title'].str.len()
chicago.head()

# %%
chicago.sort_values(by ='postiton_len', ascending = False).head()


# %%
chicago['Position Title'].str.split(' ', expand = True).head()

# %%
chicago['Position Title'].str.split(' ', expand = True, n=1).head()

# %%
chicago[['Postion First title', 'Position Other title']] = chicago['Position Title'].str.split(' ', expand = True, n=1)

chicago.head()

# %%
chicago['Last_Name'].values.tolist()

# %%
#strip

text = ' I live in Pune '

print(len(text))
print(text)

# %%
print(text.strip())
print(len(text.strip()))

# %%
print(text.lstrip())
print(len(text.lstrip()))

# %%
print(text.rstrip())
print(len(text.rstrip()))

# %%
# Multilevel indexes

# %%
import pandas as pd

# %%
chicago = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\chicago.csv")

chicago.head()

# %%
chicago = chicago.sort_values(by = 'Employee Annual Salary', ascending = False)

chicago.head()

# %%
chicago.set_index(keys = ['Department', 'Name']).head(30)

# %%
worldstats = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\worldstats.csv")

worldstats.head()

# %%
worldstats.set_index(keys = ['country', 'year'])

# %%
worldstats.set_index(keys = ['year', 'country'])

# %%
# country is not in index currently

worldstats.country.value_counts()

# %%
unique_countries = worldstats['country'].unique()



num_unique_countries = len(unique_countries)

num_unique_countries


# %%
unique_countries

# %%
my_list = worldstats['country'].tolist()

my_list




# %%
unique_values = set(my_list)

unique_values

# %%
len(unique_values)

# %%
worldstats = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\worldstats.csv", index_col= ['country','year'])

worldstats.head()

# %%
worldstats.loc[('Arab World', 2005)]['GDP']

# %%
worldstats.index

# %%
worldstats.index.get_level_values(0).unique()

# %%
worldstats.index.rename(names = ['Desh','Saal'],inplace = True)


# %%
worldstats.head()

# %%
wdst = worldstats.rename(index={'Desh': 'country', 'Saal': 'year'})


# %%
wdst.head()

# %%
worldstats.index.rename(names = ['Country','Year'],inplace = True)

worldstats.head()

# %%
worldstats.swaplevel('Country','Year').head()

# %%
worldstats.head()

# %%
wdst = worldstats.swaplevel()

wdst.head()

# %%
wdst = worldstats.swaplevel(i = 0, j = -2)

wdst.head()

# %%
wdst = worldstats.swaplevel(i = 1, j = 0)

wdst.head()

# %%
import pandas as pd

# %%
worldstats = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\worldstats.csv")

worldstats.head()

# %%
worldstats.set_index(['country','year'], inplace = True)

# %%
worldstats.head()

# %%
# stack -  converts columns into rows

st_df = worldstats.stack()

st_df

# %%
st_df = st_df.to_frame()

st_df.head()

# %%
st_df.rename(columns = {0: 'Data'} , inplace = True)

st_df.head()

# %%
unst_df = st_df.unstack()

unst_df.head()

# %%
unst_df.columns.levels

# %%
unst_df.index.levels

# %%
unst_df.columns = [col[1] for col in unst_df.columns]

unst_df

# %%
temp_list =[]
for col in unst_df.columns:
    temp_list.append(col[1])
print(temp_list)


unst_df.columns = temp_list

unst_df.head()

# %%
unst_df.rename(columns = {'o': 'Population', 'D':'GDP'} , inplace = True)

unst_df.head()

# %%
salesman = pd.read_csv(R"D:\Data Analyst Classes\Data for Classes\Python\Data Files\salesmen.csv")

salesman.head()

# %%
salesman.Salesman.value_counts()

# %%
salesman.pivot(index= 'Date', columns = 'Salesman', values = 'Revenue')

# %%
salesman.pivot_table(values = 'Revenue', index ='Salesman', aggfunc = 'mean' )

# %%
salesman.pivot_table(values = 'Revenue', index ='Salesman', aggfunc = 'max' )

# %%
salesman.pivot_table(values = 'Revenue', index ='Salesman', aggfunc = 'std' )

# %%




