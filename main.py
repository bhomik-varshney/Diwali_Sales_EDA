import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from pandas import DataFrame

warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')
data = pd.read_csv('./Details.csv')
data1 = np.array(data)
print(data.columns)
print(data.isnull().sum()) #there are no null values in this csv file.
print(data1[0:5])

#Analysis of Category of Product and the Subcategory.

data.rename(columns = {'Sub-Category':'Sub_Category'}, inplace= True)
print(data.columns)
x = data.Category.describe()
print(x)
x1 = data.groupby(['Category','Sub_Category'])['Sub_Category'].count()
print(x1)
# x2 = pd.DataFrame(x1)
# x3 = sns.countplot(x = 'Category', data = x2,alpha = 0.7)
# plt.show()
#Most buyed Category is Clothing followed by Electronics and Furniture.
print(data.Sub_Category.describe())

# plt1 = sns.countplot(x = 'Sub_Category', data = data[data['Category']=='Clothing'])
# x18 = plt1.set_title('Sub_Category vs Number of Orders')
# x19 = plt1.set_ylabel('Number of Orders')
# plt.show()
#
# plt2 = sns.countplot(x = 'Sub_Category', data = data[data['Category']=='Electronics'])
# x20 = plt2.set_title('Sub_Category vs Number of Orders')
# x21 = plt2.set_ylabel('Number of Orders')
# plt.show()
#
# plt3 = sns.countplot(x = 'Sub_Category', data = data[data['Category']=='Furniture'])
# x22 = plt3.set_title('Sub_Category vs Number of Orders')
# x23 = plt3.set_ylabel('Number of Orders')
# plt.show()
#
#
# f, ax = plt.subplots(2,2,figsize=(18,8))
# x7 = sns.countplot(x = 'Category', data = data, ax = ax[0,0])
# x8 = ax[0,0].set_title('Category vs Number of orders')
# x9 = ax[0,0].set_ylabel('Number of Orders')
# x6 = sns.countplot(x = 'Category',hue ='Sub_Category',data = data[data['Category']=='Clothing'], ax =ax[0,1])
# x10 = ax[0,1].set_title('Sub_Category vs Number of orders')
# x11 = ax[0,1].set_ylabel('Number of Orders')
# x15 = sns.countplot(x = 'Category',hue ='Sub_Category',data = data[data['Category']=='Electronics'], ax =ax[1,0])
# x16 = ax[1,0].set_title('Sub_Category vs Number of orders')
# x17 = ax[1,0].set_ylabel('Number of Orders')
# x19 = sns.countplot(x = 'Category',hue ='Sub_Category',data = data[data['Category']=='Furniture'], ax =ax[1,1])
# x20 = ax[1,1].set_title('Sub_Category vs Number of orders')
# x21 = ax[1,1].set_ylabel('Number of Orders')
# x22 = plt.subplots_adjust(wspace = 0.4, hspace = 0.5)
# plt.show()

#from the above observation
#top subcategory of clothing (category) is Saree, Handkerchief, Stole.
#top subcategory of Electronics (category) is phone, electronic games and printer.
#top subcategory of furniture(category) is bookcases, chairs and Furnishings.

#Profit in Categories and Sub_Categories
y1 = data.groupby(['Category'])['Profit'].sum()
y2 = data.groupby(['Category','Sub_Category'])['Profit'].sum()
print(y1)
print(y2)
# f, ax = plt.subplots(1,2,figsize=(18,8))
# y3 = data[['Category','Profit']].groupby(['Category'])['Profit'].sum().plot.bar(ax=ax[0])
# y4 = data[['Category','Profit','Sub_Category']].groupby(['Sub_Category'],as_index=False)['Profit'].sum().sort_values(by ='Profit', ascending = False).head(5).plot.bar(ax=ax[1], x = 'Sub_Category')
# plt.xticks(rotation =0, ha = 'center')
# plt.show()
#high profittable category is Clothing followed by Electronics and Furniture.
#high profittable Sub_Category is printers from Electronics Category.

# plt1 = pd.DataFrame(data[data['Category']=='Clothing'].groupby(['Sub_Category'])['Profit'].sum())
# plt2 = sns.barplot(x = 'Sub_Category',y ='Profit', data=plt1)
# plt.show()
#Sub_Category :- Saree has the highest profit in the Clothing Category.
# plt3 = pd.DataFrame(data[data['Category']=='Electronics'].groupby(['Sub_Category'])['Profit'].sum())
# plt4 = sns.barplot(x = 'Sub_Category',y ='Profit', data=plt3)
# plt.show()
#Sub_Category :- Printers(overall highest profit Sub_Category) has the highest profit in the Electronics Category.
# plt5 = pd.DataFrame(data[data['Category']=='Furniture'].groupby(['Sub_Category'])['Profit'].sum())
# plt6 = sns.barplot(x = 'Sub_Category',y ='Profit', data=plt5)
# plt.show()
#Sub_Category :- Bookcases has the highest profit in the Furniture Category.

#Quantity vs Profit

# z1 = pd.crosstab([data.Sub_Category,data.Quantity],[data.Profit])
# print(z1)

# z2 = data[data['Category']=='Clothing'].groupby(['Sub_Category','Profit','Quantity'])['Profit'].sum()
# print(z2)

# f, ax = plt.subplots(1,3,figsize=(18,8))
# z2 = pd.DataFrame(data[data['Category']=='Clothing'].groupby(['Quantity'])['Profit'].sum())
# z3 = pd.DataFrame(data[data['Category']=='Electronics'].groupby(['Quantity'])['Profit'].sum())
# z4 = pd.DataFrame(data[data['Category']=='Furniture'].groupby(['Quantity'])['Profit'].sum())
# plt3 = sns.catplot(kind ='point', x = 'Quantity', y = 'Profit', data = z2, ax = ax[0])
# plt4 = sns.catplot(kind ='point', x = 'Quantity', y = 'Profit', data = z3, ax = ax[1])
# plt5 = sns.catplot(kind ='point', x = 'Quantity', y = 'Profit', data = z4, ax = ax[2])
# plt.show()
#its is clearly seen that as the quantity increases, profit decreases for all three types of Categories.

# f, ax = plt.subplots(1,2,figsize=(18,8))
# z2 = pd.DataFrame(data[data['Sub_Category']=='Saree'].groupby(['Quantity'])['Profit'].sum())
# z3 = pd.DataFrame(data[data['Sub_Category']=='Hankerchief'].groupby(['Quantity'])['Profit'].sum())
# plt8 = sns.barplot(x='Quantity', y ='Profit', data = z2, ax = ax[0])
# plt9 = sns.barplot(x='Quantity', y ='Profit', data = z3, ax = ax[1])
# title1 = ax[0].set_title('Ouantity of Saree vs Profit')
# title2 = ax[1].set_title('Ouantity of Hankerchief vs Profit')
# plt.show()
#from the observation above ,profit doesnot depend on the Quantity of a Sub_category, it can decrease or increase as we change the Quantity of a particular Sub_Category..

print(data.Quantity.describe())
#maximum Quantity taken = 14

# s1 = pd.DataFrame(data.groupby(['Category'])['Amount'].sum())
# s2 = sns.barplot(x='Category',y ='Amount',data= s1)
# print(s1)
# plt.show()
#Total Amount of Electronics(166267) items is more than Clothing and Furniture Categories.
# s6 = data.groupby(['Sub_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending= False).head(7).plot.bar(x='Sub_Category')
# plt.xticks(rotation=0,ha='center')
# plt.show()
#highest total Amount of Sub_Category is Printers.
# s3 = data[data['Category']=='Electronics'].groupby(['Sub_Category'])['Amount'].sum().plot.bar()
# s4 = plt.xticks(rotation =0, ha ='center')
# s5 = plt.ylabel('Total Amount')
# plt.show()

#Amount vs Profit

# f, ax = plt.subplots(1,2,figsize=(18,8))
# plt1= data.groupby(['Category'])['Amount'].sum().plot.bar(x = 'Category', ax = ax[0])
# plt2 = data.groupby(['Category'])['Profit'].sum().plot.bar(x = 'Profit',ax = ax[1])
# plt.show()
#Clothing seems to be very successful because of high total Profit.

#Mode of Payment

# print(data.PaymentMode.describe())
# u1 = pd.DataFrame(data.groupby(['PaymentMode','Category'])['PaymentMode'].count())
# print(u1)
#Most of the People used COD payment option.

# plt4 = sns.countplot(x='PaymentMode',hue ='Category',data = data)
# plt.show()
#for clothing items, most people paid Cash On Delivery Payment Mode.

print(data.Amount.describe())
print(np.where(data['Amount']==5729))
print(data[1:2])
#most Expensive order is Chairs(Furniture, quantity = 14, amount = 5729, PaymentMode= EMI)

#PaymentMode vs Quantity:-

# i1 = data.groupby(['PaymentMode','Quantity'])['Quantity'].sum()
# print(i1)
# plt6 = sns.countplot(x='Quantity', hue = 'PaymentMode', data = data)
# plt.show()
#when there is a high quantity people usually buy using PaymentMode COD or EMI

# i2 = pd.DataFrame(data.groupby(['PaymentMode','Quantity'])['Amount'].sum())
# plt7 = sns.barplot(x ='Quantity', y ='Amount', hue ='PaymentMode',data = i2)
# print(i2)
# plt.show()

data3: DataFrame = pd.read_csv('./Orders.csv')
data4 = np.array(data3)
print(data3.columns)
print(data3.isnull().sum()) #no null Value.


# l2 = data3['State'].value_counts().reset_index(name ='Count').head(7).plot.bar(x='State')
# plt.xticks(rotation=0,ha='center')
# plt.xlabel('States')
# plt.ylabel('Number of Orders')
# l3 = l2.set_title('Top 7 States')
# plt.show()
#Top 3 States are :- Maharashtra, Madhya Pradesh, and Rajasthan.


#Analysis of the Month of the Year 2018
l5 = data3.rename(columns= {'Order Date':'Order_Date'},inplace = True)
print(data3.columns)

data5 = pd.DataFrame(data3['Order_Date'])
data3['Month'] = data5['Order_Date'].str.slice(3, 5).astype(int)
print(data3.columns) #Created a column for Month.

w1 = data3.loc[(data3['Month']==1),'Month']='January'
w2 = data3.loc[(data3['Month']==2),'Month']='February'
w3 = data3.loc[(data3['Month']==3),'Month']='March'
w4 = data3.loc[(data3['Month']==4),'Month']='April'
w5 = data3.loc[(data3['Month']==5),'Month']='May'
w6 = data3.loc[(data3['Month']==6),'Month']='June'
w7 = data3.loc[(data3['Month']==7),'Month']='July'
w8 = data3.loc[(data3['Month']==8),'Month']='August'
w9 = data3.loc[(data3['Month']==9),'Month']='September'
w10 = data3.loc[(data3['Month']==10),'Month']='October'
w11 = data3.loc[(data3['Month']==11),'Month']='November'
w12 = data3.loc[(data3['Month']==12),'Month']='December'
print(data3.head(10))
r2 = data3.groupby(['Month'],as_index=True)['Month'].count().sort_values(ascending = False)
r1 = data3['Month'].value_counts().head(7).plot.bar()
plt.xticks(rotation =0, ha ='center')
plt.show()
print(r2)
#from the graph, people mostly bought things either at the beginning or end of the year 2018.(reason meaybe Festive seasons)

merged_data = data.merge(data3, on='Order ID',how='left')
print(merged_data.head(10))
print(merged_data.isnull().sum())  #we can also use that to merge the data of 2 csv files.

