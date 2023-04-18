import pandas as pd
def create_companyDF(income, expenses, years):
    res=pd.DataFrame({'Income':income,'Expenses':expenses})
    res.index=years
    return res
def get_profit(df, year):
    res=df.iloc[[year],['income']]
    return res

print (df = create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020]))
 print(get_profit(year = 2018, df = create_companyDF([612, 516, 329, 158], [136,163,250,361], [2017,2018,2019,2020])))
