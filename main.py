from utils.Functions import *

if __name__ == '__main__':
    df = pd.read_csv("Resources/drug_deaths.csv", sep=",")
    plotDeathsByMonth(df, 2016)
    plotYearOnDeath(df)
    plotBySex(df)
    plotDrugs(df)
