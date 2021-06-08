import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt

MAX_VAL = 7

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
