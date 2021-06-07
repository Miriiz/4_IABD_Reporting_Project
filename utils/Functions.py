import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt


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
    print(val)
    plt.pie(val, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, explode=[0,0.1,0.0])
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
