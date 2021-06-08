import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np

MAX_VAL = 7


def plotDeathsByMonth(df, min_year=2012, max_year=2018):
    if min_year < 2012:
        min_year = 2012
    if max_year > 2018:
        max_year = 2018

    months = np.arange(1, 13)
    dates = pd.to_datetime(df['Date'])
    death_by_years = {}
    for year in np.arange(min_year, max_year + 1):
        death_by_month = []
        for month in months:
            death_by_month.append(dates.where((dates.dt.month == month) & (dates.dt.year == year)).dropna().size)
        death_by_years[year] = death_by_month

    for key, value in death_by_years.items():
        plt.plot(months, value, label=str(key))
    plt.legend()
    plt.title("Morts par overdose en fonction du mois entre " + str(min_year) + " et " + str(max_year))
    plt.show()


def plotYearOnDeath(df):
    hist = df['Age']
    plt.hist(hist, edgecolor='black')
    plt.xlabel("Age")
    plt.ylabel("Nombre de décès")
    plt.title("Plage d'age des personnes décédé d'overdose")
    plt.show()


def plotBySex(df):
    mydf = df['Sex']
    myNewDf = TransformDataSex(mydf)
    labels = ['Homme', 'Femme', 'Other']
    val = myNewDf["Sex"].value_counts()
    plt.pie(val, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, explode=[0, 0.1, 0.0])
    plt.title("Répartition des sexes en fonction des décès par overdose")

    plt.show()


def TransformDataSex(df):
    newDf = pd.DataFrame()
    temp = []
    for i in range(0, len(df)):
        if df[i] == "Male":
            temp.append(0)
        elif df[i] == "Female":
            temp.append(1)
        else:
            temp.append(2)

    newDf["Sex"] = temp
    return newDf


def plotDrugs(df):
    myDict = createFinal(df)
    labels = list(myDict.keys())
    val = list(myDict.values())

    plt.pie(val[0:MAX_VAL], labels=labels[0:MAX_VAL], autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("Les 7 drogues qui ont crée le plus d'overdose")
    plt.show()


def createFinal(df):
    myDict = {"Heroin": getCountDrugs("Heroin", df), "Cocaine": getCountDrugs("Cocaine", df),
              "Fentanyl": getCountDrugs("Fentanyl", df), "Oxycodone": getCountDrugs("Oxycodone", df),
              "Oxymorphone": getCountDrugs("Oxymorphone", df), "Ethanol": getCountDrugs("Ethanol", df),
              "Hydrocodone": getCountDrugs("Hydrocodone", df), "Benzodiazepine": getCountDrugs("Benzodiazepine", df),
              "Methadone": getCountDrugs("Methadone", df), "Amphet": getCountDrugs("Amphet", df),
              "Tramad": getCountDrugs("Tramad", df), "Morphine_NotHeroin": getCountDrugs("Morphine_NotHeroin", df),
              "Hydromorphone": getCountDrugs("Hydromorphone", df), "Other": getCountDrugs("Other", df)}

    sorted_values = sorted(myDict.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for k in myDict.keys():
            if myDict[k] == i:
                sorted_dict[k] = myDict[k]

    return sorted_dict


def getCountDrugs(drugsName, df):
    return (df[drugsName].value_counts())[1]
