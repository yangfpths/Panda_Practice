import sklearn
import csv
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


pd.read_csv()




'''

def read_file(name):
    text = []
    label = []
    count = 0
    with open(name+".csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if count!=0:
                if len(row)>1:
                    text.append(re.sub('[^\w\s]+', '',row[1]))
                    if name =="train":
                        label.append(row[2])
            count+=1
    return text,label
train_text,train_label = read_file("train")
print(train_text)
test_text,test_label = read_file("test")

tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 3), min_df=1, max_df=.9,lowercase = True).fit(train_text)
tfidf_matrix = tfidf_vectorizer.transform(train_text)
rep = tfidf_vectorizer.transform(test_text)
guess_matrix = tfidf_matrix.dot(rep.T).T
guess_indices = (-guess_matrix).toarray().argsort(axis=1)[:, 0]
count = 0
with open("result.csv",'w') as csv_file:
    csv_file.write("ID,Pred\n")
    for indices in guess_indices:
        test_indice = train_label[indices]
        count+=1
        csv_file.write(str(count)+","+str(float(test_indice=="Positive"))+"\n")
'''
