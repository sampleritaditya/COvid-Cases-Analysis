# top 10 countries with high cases
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go
data = pd.read_csv("transformeddata.csv")
code = data["CODE"].unique().tolist()
country = data["COUNTRY"].unique().tolist()
hdi = []
tc = []
td = []
sti = []
population = data["POP"].unique().tolist()
gdp = []

for i in country:
    hdi.append((data.loc[data["COUNTRY"] == i, "HDI"]).sum()/294)
    tc.append((data.loc[data["COUNTRY"] == i, "TC"]).sum())
    td.append((data.loc[data["COUNTRY"] == i, "TD"]).sum())
    sti.append((data.loc[data["COUNTRY"] == i, "STI"]).sum()/294)
    population.append((data.loc[data["COUNTRY"] == i, "POP"]).sum()/294)

aggregated_data = pd.DataFrame(list(zip(code, country, hdi, tc, td, sti, population)), 
                               columns = ["Country Code", "Country", "HDI", 
                                          "Total Cases", "Total Deaths", 
                                          "Stringency Index", "Population"])
print(aggregated_data.head())
sortdata = aggregated_data.sort_values(by='Total Cases',ascending= False)
totalcases = sortdata.head(10)[['Country','Total Cases']]
plt.bar(totalcases['Country'],totalcases['Total Cases'])
plt.show()


#2  top 10 countries with high deaths
sortdata = aggregated_data.sort_values(by='Total Deaths',ascending=False)
totaldeath = sortdata.head(10)[['Country','Total Deaths']]
plt.bar(totaldeath['Country'],totaldeath['Total Deaths'])
plt.show()


# # #3 total cases and total death
# # print(data.info())
cases = data["TC"].sum() 
deaths = data["TD"].sum()
labels = ['Cases', 'Deaths']
values = [cases, deaths]
plt.pie(values,labels=labels,autopct='%1.1f%%')
plt.show()


# 4 gdp according to country
plt.figure(figsize=(8, 6))
sns.histplot(data['GDPCAP'], bins=20, kde=True)
plt.title('Histogram of GDP per Capita')
plt.xlabel('GDP per Capita')
plt.ylabel('Frequency')
plt.show()

gr = data.groupby('COUNTRY')['GDPCAP'].mean().reset_index()
gr_sorted = gr.sort_values(by='GDPCAP',ascending=False).head(10)
plt.figure(figsize=(12, 6))
plt.plot(gr_sorted['COUNTRY'], gr_sorted['GDPCAP'], marker='o',linestyle='-')
plt.show()


#5 cases according to country
data['DATE'] = pd.to_datetime(data['DATE'])
sns.lineplot(x='DATE', y='TC', data=data)
plt.show()


# 6 HDI ,tc,and population of country
fig = px.bar(data, x='COUNTRY', y='TC',
             hover_data=['POP', 'TD'], 
             color='HDI', height=400, 
             title="Human Development Index during Covid-19")
fig.show()

# 7 sti,tc,td,pop of country
fig = px.bar(data, x='COUNTRY', y='TC',
             hover_data=['POP', 'TD'], 
             color='STI', height=400, 
             title= "Stringency Index during Covid-19")
fig.show()

# 8 total cases of country india
countryname = 'India'
dc=data[data["COUNTRY"]== countryname]
data['DATE'] = pd.to_datetime(data['DATE'])
sns.lineplot(x='DATE', y='TC', data=dc)
plt.show()
