from utils.Functions import *

if __name__ == '__main__':
    df = pd.read_csv("Resources/drug_deaths.csv", sep=",")
    plotYearOnDeath(df)
    plotBySex(df)
    plotDrugs(df)


