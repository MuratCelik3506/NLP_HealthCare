from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import logging
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from transformers import pipeline
# import json
# import requests
import pandas as pd
import math
from collections import defaultdict
import operator
from transformers import pipeline


# qa_model = ""
# data_txt = ""
df = pd.DataFrame()
qa_model = ""
# ************************************************************
# ********* Start Page And Headers Arrangment ****************
# ************************************************************

def index(request):
    global df
    global qa_model
    df = pd.read_csv("originial.csv")
    list_of_dicts, page_size = get_3_article_info(1)
    sidebar_keys = header_sidebar()
    qa_model = pipeline("question-answering")
    all_keys = set(all_keywords())
    return render(request, 'articles_page.html', {"articles": list(list_of_dicts), "page_size": page_size, "side_keys" : sidebar_keys, "Keys" : all_keys})


def header_sidebar():
    keywords_list = all_keywords()
    keyword_dict = defaultdict(int)
    for key in keywords_list:
        keyword_dict[key] += 1
    sorted_d = dict(sorted(keyword_dict.items(), key=operator.itemgetter(1), reverse=True))
    list_keys = list()
    for k in list(sorted_d.keys())[:10]:
        list_keys.append(k)
    return list_keys

def all_keywords():
    global df
    df = pd.read_csv("originial.csv")
    keywords_list = list(df["K1"]) + list(df["K2"]) + list(df["K3"]) + list(df["K4"]) + list(df["K5"])
    return keywords_list
# ************************************************************
# ****************** Articles Main Page **********************
# ************************************************************

def articles(request):
    list_of_dicts, page_size = get_3_article_info(1)
    sidebar_keys = header_sidebar()
    all_keys = set(all_keywords())
    return render(request, 'articles_page.html',{"articles" : list(list_of_dicts), "page_size":page_size, "side_keys" : sidebar_keys, "Keys" : all_keys})

def articles_page(request,id):
    list_of_dicts, page_size = get_3_article_info(id)
    sidebar_keys = header_sidebar()
    all_keys = set(all_keywords())
    return render(request, 'articles_page.html',{"articles" : list(list_of_dicts), "page_size":page_size, "side_keys" : sidebar_keys, "Keys" : all_keys})

def get_3_article_info(page_num):
    global df
    desire_page = page_num
    page_numbers = int(math.ceil(len(df) / 3))
    if desire_page > page_numbers:
        desire_page = page_numbers
    page_num *= 3
    if page_numbers >= 10:
        if desire_page <= 5:
            page_size = [i+1 for i in range(10)]
        else:
            if page_numbers - desire_page < 5:
                page_size = [i+1 for i in range(page_numbers-10, page_numbers)]
            else:
                page_size = [i+1 for i in range(desire_page-5, desire_page + 5)]
    else:
        page_size = [i + 1 for i in range(page_numbers)]
    l, h = len(df) - page_num, len(df) - page_num + 3
    if l < 0:
        l, h = 0, 3
        if len(df) < 3:
            h = len(df)
    df_tmp = df[l:h]
    df_tmp = df_tmp.iloc[::-1]
    list_of_dicts = df_tmp.T.to_dict().values()
    return list_of_dicts, page_size


def articles_page_w_tag(request,tag,page):
    list_of_dicts, page_size = get_3_article_info_w_tag(tag,page)
    sidebar_keys = header_sidebar()
    all_keys = set(all_keywords())
    return render(request, 'tags_page.html',{"articles" : list(list_of_dicts), "page_size":page_size, "tag" : tag, "side_keys" : sidebar_keys, "Keys" : all_keys})

def get_3_article_info_w_tag(tag,page):
    desire_page = page
    page *= 3
    global df
    df_tmp = df[(df["K1"] == tag) | (df["K2"] == tag) | (df["K3"] == tag) | (df["K4"] == tag) | (df["K5"] == tag)]
    page_numbers = int(math.ceil(len(df_tmp) / 3))
    if desire_page > page_numbers:
        desire_page = page_numbers
    if page_numbers >= 10:
        if desire_page <= 5:
            page_size = [i + 1 for i in range(10)]
        else:
            if page_numbers - desire_page < 5:
                page_size = [i + 1 for i in range(page_numbers - 10, page_numbers)]
            else:
                page_size = [i + 1 for i in range(desire_page - 5, desire_page + 5)]
    else:
        page_size = [i + 1 for i in range(page_numbers)]
    l,h = len(df_tmp) - page, len(df_tmp) - page + 3
    if l < 0:
        l,h = 0,3
        if len(df) < 3:
            h = len(df)
    df_tmp = df_tmp[l:h]
    df_tmp = df_tmp.iloc[::-1]
    list_of_dicts = df_tmp.T.to_dict().values()
    return list_of_dicts, page_size

# ************************************************************
# *********************** Article Page **********************
# ************************************************************


def show_article(request,name):
    f = open("articles/" + name + ".txt", "r", encoding="utf-8")
    text = f.read()
    f.close()
    global df
    global qa_model
    answer = {"answer":""}
    if request.method == 'POST':
        question = request.POST.get('qa')
        answer = qa_model(question=question, context=text)


    df_tmp = dict(df[df["Name"] == int(name)].iloc[0])
    summary = df_tmp["Summary"]
    tag = [df_tmp["K1"],df_tmp["K2"],df_tmp["K3"],df_tmp["K4"],df_tmp["K5"]]
    title = df_tmp["Title"]
    sidebar_keys = header_sidebar()
    all_keys = set(all_keywords())
    context = {"url_name":name, "Title":title, "Text":text, "Summary":summary, "Tags":tag, "side_keys" : sidebar_keys,"Answer":answer["answer"], "Keys" : all_keys}
    return render(request, 'article.html',context)


# ************************************************************
# ******************* Question Answer Page *******************
# ************************************************************

def qa_main(request):
    global df
    global qa_model
    text = "Welcome"
    title = "Ask AI"
    sidebar_keys = header_sidebar()
    all_keys = set(all_keywords())
    answers_dict = [{"answer":""},{"answer":""}]
    num_articles = ""
    search_if = False
    question = ""
    if request.method == 'POST':
        tag = request.POST.get('brow')
        question = request.POST.get('search_on_page')
        if tag != "" and question != "":
            answers_dict = list()
            df_tmp = df[(df["K1"] == tag) | (df["K2"] == tag) | (df["K3"] == tag) | (df["K4"] == tag) | (df["K5"] == tag)]
            df_tmp = df_tmp.reset_index()
            for i in range(len(df_tmp)):
                name = df_tmp.iloc[i]["Name"]
                f = open("articles/" + str(name) + ".txt", "r", encoding="utf-8")
                text = f.read()
                f.close()
                answer = qa_model(question=question, context=text)
                answers_dict.append(answer)
            num_articles = len(answers_dict)
            answers_dict = sorted(answers_dict, key=lambda l: l["score"], reverse=True)
            search_if = True
    context = {"Title":title, "Text":text,"side_keys" : sidebar_keys, "Keys" : all_keys,"Answer":answers_dict[0]["answer"],"Question":question, "Total_Articles" : num_articles,"Search_First":search_if }
    return render(request, 'qa_articles.html',context)