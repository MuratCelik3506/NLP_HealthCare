import pandas as pd
import os
import keyword_extractor as qa
import Summarization as sm
import TitleGeneration as tg
df = pd.DataFrame(columns =["Name","Path","Title","Summary","K1","K2","K3","K4","K5"])


for file_name in os.listdir("articles"):
    path = "articles/" + file_name
    f = open(path, "r",encoding="utf-8")
    text = f.read()
    #print(text)
    keywords = qa.keyword(text)
    #print(keywords)
    row = dict()
    row["Name"] = file_name.split(".")[0]
    row["Path"] = path
    row["Title"] = tg.create_title(text)
    row["Summary"] = sm.summarize_text(text)
    row["K1"] = keywords[0][0]
    row["K2"] = keywords[1][0]
    row["K3"] = keywords[2][0]
    row["K4"] = keywords[3][0]
    row["K5"] = keywords[4][0]
    df = df.append(row, ignore_index=True)
    #print(file_name)
    f.close()

    df.to_csv("info_articles_4.csv",index=False)
#print(df)
