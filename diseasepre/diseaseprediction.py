import numpy as np
#to work on array and matrices and including mathematical function in them
import pandas as pd
#to work with data sets. manipulating and cleaning them
import os
#creating , removing, changing and fetching contents of a folder
def predict(s1, s2, s3, s4, s5, s6, s7):
    strr="no disease"
    for dirname, _, filenames in os.walk('/kaggle/input'):
         for filename in filenames:
              print(os.path.join(dirname, filename))
                #including multiple data set from a folder
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    # plotting function in a graph . plot lines etc
    from sklearn.model_selection import train_test_split
    # train the model and test the output
    from sklearn.metrics import f1_score, accuracy_score, confusion_matrix, classification_report
    # f1 score : measure performance : 0/1
    # accuracy score : no of correct prediction/total no of prediction
    # confusion matrix:tp fp fn tn
    # classification report : performance evaluation matrix
    from sklearn.ensemble import RandomForestClassifier
    # random forest classifier

    data = pd.read_csv("dataset.csv")
    data_sevrity = pd.read_csv("Symptom-severity.csv")

    for ind in data_sevrity.index:  # index in data.index
        continue
        # used to skip the remaining code inside a loop for the current iteration only.
    # print(data_sevrity['Symptom'][ind],data_sevrity['weight'][ind])

    data_dict = data_sevrity.set_index('Symptom').T.to_dict()
    # convert data frame to dict

    def remove_space_between_word(dataset):
        for col in dataset.columns:
            for i in range(len(dataset[col])):
                if (type(dataset[col][i]) == str):
                    dataset[col][i] = dataset[col][i].strip()  # remove white space
                    dataset[col][i] = dataset[col][i].replace(" ", "_")
        return data

    new_df = remove_space_between_word(data)
    new_df.head()

    def enc(dataset):
        for ind in data_sevrity.index:
            dataset = dataset.replace(data_sevrity["Symptom"][ind], data_sevrity["weight"][ind])
        dataset = dataset.fillna(0)  # put empty cell to 0
        dataset = dataset.replace("foul_smell_of_urine", 5)
        dataset = dataset.replace("dischromic__patches", 6)
        dataset = dataset.replace("spotting__urination", 6)
        return dataset

    def encode_data(dataset, data_dict_weigth):
        cols = dataset.columns
        for columnName in cols:
            for i in range(len(dataset[columnName])):
                try:
                    # print(data_dict[data2[columnName][i]]["weight"])
                    dataset[columnName][i] = data_dict[dataset[columnName][i]]["weight"]
                except:
                    pass
        dataset = dataset.fillna(0)  # put empty cell to 0
        dataset = dataset.replace("foul_smell_of_urine", 5)
        dataset = dataset.replace("dischromic__patches", 6)
        dataset = dataset.replace("spotting__urination", 6)
        return dataset

    df = encode_data(new_df, data_dict)
    df.head()

    df_data = df.drop('Disease', axis=1)
    label = data["Disease"]

    x_train, x_test, y_train, y_test = train_test_split(df_data, label, shuffle=True, train_size=0.70)
    randomFC = RandomForestClassifier()
    randomFC.fit(x_train, y_train)
    result = randomFC.predict(x_test)
    #print(randomFC)
    #print(classification_report(y_true=y_test, y_pred=result))
    #print('F1-score% =', f1_score(y_test, result, average='macro') * 100, '|', 'Accuracy% =',
     #     accuracy_score(y_test, result) * 100)

    qw = pd.DataFrame([[s1,s2,s3,s4,s5,s6,s7,0,0,0,0,0,0,0,0,0,0]],
                      columns=['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4', 'Symptom_5',
                               'Symptom_6', 'Symptom_7', 'Symptom_8', 'Symptom_9', 'Symptom_10',
                               'Symptom_11', 'Symptom_12', 'Symptom_13', 'Symptom_14', 'Symptom_15',
                               'Symptom_16', 'Symptom_17'])

    output = randomFC.predict(qw)

    print(output[0])
    strr= output[0]

    return strr