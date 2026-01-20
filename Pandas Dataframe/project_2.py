'''
🔹 Project 2: Sales Data Report

Create a DataFrame with columns:
OrderID, Product, Category, Sales, Quantity, City.

Perform the following:

Filter all orders where Sales > 1000 and Quantity > 3.

Create a Pivot Table showing total Sales by Category and City.

Sort products by Sales in descending order.

Concatenate with another DataFrame that contains OrderID and CustomerName.
'''
import pandas as pd
print('\n\n\n\n-----------------SALES DATA REPORT------------------------\n\n\n\n')
data={
    'OrderID':[101,102,103,104,105],
    'Product':['Apple','Banana','Water','Ice','Coca-cola'],
    'Category':['Fruit','Fruit','Drinks','Drinks','Drinks'],
    'Sales':[1600,100,250,1100,90],
    'Quantity':[5,4,10,9,8],
    'City':['Waling','Pokhara','Kathmandu','Chitwan','Butwal']
}
result=pd.DataFrame(data)
print(result,'\n\n\n')
print('----------DATA where Sales > 1000 and Quantity > 3-----------------\n\n\n')
res = result[(result["Sales"] > 1000) & (result["Quantity"] > 3)]
print(res,'\n\n\n')
print('------------Pivot Table showing total Sales by Category and City-------------')
res1=result.pivot_table(index=['Category'],values=['Sales'],aggfunc='mean')
print('\n\n\n\n---------BY SALES ------------\n\n\n',res1)
res2= pd.pivot_table(result, values="Sales", index="Category", columns="City", aggfunc="sum")
print('\n\n\n\n---------BY BOTH ------------\n\n\n\n',res2)
print("\n\n\n\n---------SORTED  DATA IN DESCENDING ORDER IS ------------\n\n\n\n\n")
sorted_data=result.sort_values(by='Sales',ascending=False)
print(sorted_data)
data1={
    'OrderID':[101,102,103,104,105],
    'NAME':['sanjog','ANIL','SAM CARAN','Ram','shyam']
}
result2=pd.DataFrame(data1)
print('\n\n\n--------THE LIST OF CUSTUMER AND THEIR ORDER ID IS --------\n\n\n\n',result2)
frames=[result,result2]
print('\n\n\n\n-------AFTER CONCATING THE DATA WITH NAME IS ------------\n\n\n\n')
print(pd.concat(frames))
