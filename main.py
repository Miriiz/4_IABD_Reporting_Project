import pandas as pd

from utils.Functions import *


def updateDate(df):
    dates = []
    for d in df['Date']:
        d = str(d)
        size = len(d)
        temp = d[: size - 12]
        if temp != '' :
            dates.append(pd.to_datetime(temp, format="%M/%d/%Y"))
        else:
            dates.append('')
    df['Date'] = dates

    return df


if __name__ == '__main__':
    df = pd.read_csv("Resources/drug_deaths.csv", sep=",")
    # # Month
    # #print(df2.head())
    # plotDeathsByMonth(df, 2016)
    # # Years
    # plotYearOnDeath(df)
    # # Sex per death
    # plotBySex(df)
    # #Function to generate information from drug's kill
    # plotDrugs(df)
    # # Function to generate map
    # createMap(df)
    # getStatsByCountry(df)
    df = updateDate(df)
    plotDrugsByYears(df)
