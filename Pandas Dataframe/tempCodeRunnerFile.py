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
print(res1)
res2= pd.pivot_table(result, values="Sales", index="Category", columns="City", aggfunc="sum")
print(res2)
