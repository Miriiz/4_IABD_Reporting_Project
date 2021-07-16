# import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as mtick

MAX_VAL = 7


def plotDrugsByYears(df):
    list = []
    column_names = []
    list.append(drugsByYears(df, 2012))
    for k in drugsByYears(df, 2012):
        column_names.append(k)
    deathsByYears(df, 2012)
    finalDf = pd.DataFrame(columns=column_names)
    list.append(drugsByYears(df, 2013))
    list.append(drugsByYears(df, 2014))
    list.append(drugsByYears(df, 2015))
    list.append(drugsByYears(df, 2016))
    list.append(drugsByYears(df, 2017))
    list.append(drugsByYears(df, 2018))
    finalDf = finalDf.append(list)
    ax = finalDf.plot.bar(stacked=True, x='Year')
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()

    ax.yaxis.set_major_formatter(mtick.PercentFormatter())

    plt.show()


def drugsByYears(df, years):


    if years < 2012:
        years = 2012
    if years > 2018:
        years = 2018

    strStart = str(years) + '-01-01'
    strEnd = str(years) + '-12-31'
    dateStart = pd.to_datetime(strStart, format='%Y-%M-%d')
    dateEnd = pd.to_datetime(strEnd, format='%Y-%M-%d')
    var = df[(df['Date'] > dateStart) & (df['Date'] < dateEnd)]
    var = var.sum()
    sum = getTotalDrughsDeathByYears(var)
    df2 = {'Heroin': (int(var['Heroin']) * 100) / sum, 'Cocaine': (int(var['Cocaine']) * 100) / sum,
           'Fentanyl_Analogue': (int(var['Fentanyl_Analogue']) * 100) / sum,
           'Oxycodone': (int(var['Oxycodone']) * 100) / sum, 'Oxymorphone': (int(var['Oxymorphone']) * 100) / sum,
           'Ethanol': (int(var['Ethanol']) * 100) / sum, 'Hydrocodone': (int(var['Hydrocodone']) * 100) / sum,
           'Benzodiazepine': (int(var['Benzodiazepine']) * 100) / sum, 'Methadone': (int(var['Methadone']) * 100) / sum,
           'Amphet': (int(var['Amphet']) * 100) / sum, 'Tramad': (int(var['Tramad']) * 100) / sum,
           'Hydromorphone': (int(var['Hydromorphone']) * 100) / sum, 'OpiateNOS': (int(var['OpiateNOS']) * 100) / sum,
           'Year': years}

    return df2


def getTotalDrughsDeathByYears(df):
    column_names = ['Heroin', 'Cocaine', 'Fentanyl_Analogue', 'Oxycodone', 'Oxymorphone', 'Ethanol', 'Hydrocodone',
                    'Benzodiazepine', 'Methadone', 'Amphet', 'Tramad', 'Hydromorphone', 'OpiateNOS']
    sum = 0
    for k,v in df.items():
        if k in column_names:
            sum += df[k]
    return sum


def deathsByYears(df, year):
    if year < 2012:
        year = 2012
    if year > 2018:
        year = 2018

    dates = pd.to_datetime(df['Date'])
    death_by_years = []
    for year in np.arange(year, year + 1):
        death_by_years.append(dates.where(dates.dt.year == year).dropna().size)

    return death_by_years[0]


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


def createMap(df):
    dfPos = pd.DataFrame()
    dfPos['lat'], dfPos['long'] = getLongLat(df["DeathCityGeo"])
    BBox = (dfPos.long.min(), dfPos.long.max(), dfPos.lat.min(), dfPos.lat.max())

    ruh_m = plt.imread('Resources/map.png')
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(dfPos.long, dfPos.lat, zorder=1, alpha=0.2, c='b', s=10)
    ax.set_title("Emplacement des personnes retrouvés morte d'overdose")
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])
    ax.imshow(ruh_m, zorder=0, extent=BBox, aspect='equal')
    plt.show()


def getLongLat(df):
    long = []
    lat = []
    for i in df:
        x = i.split('(')
        y = x[1].split(',')
        y = y[1][0::len(y) - 1]
        lat.append(float(y.rstrip(y[-1])))
        long.append(float((x[1].split(','))[0]))

    return long, lat


def getStatsByCountry(df):
    myDf = df['ResidenceCounty'].value_counts()
    labels = myDf.keys()
    plt.pie(myDf[0:5], labels=labels[0:5], autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("Les 5 villes les plus touchés par les overdoses, au Connecticut")
    plt.show()
