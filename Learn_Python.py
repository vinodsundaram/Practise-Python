# -*- coding: utf-8 -*-
"""
Created on Sun Jul 09 16:18:11 2017

@author: Vinod
https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y
"""

## READ TABLE
import pandas as pd
tbl=pd.read_table('http://bit.ly/chiporders')
tbl.head()

## READ SERIES
ufo= pd.read_table("http://bit.ly/uforeports",sep=",")
ufo= pd.read_csv("http://bit.ly/uforeports")

type(ufo)
type(ufo.City)
type(ufo['City'])

ufo['Colors Reported'] 
## Bonus
## 1. those cols with space cant be used as attributes. with dot notation
## 2. If you are assigning, it will not work .dot format


## some with paranthasis and some done
movies = pd.read_csv("http://bit.ly/imdbratings")
movies.head() ## methods
movies.describe() ## methods
movies.shape  ## these are attributes
movies.dtypes ## aatributes

# Methods describe who to do..like eat sleep walk
# Attributes describe who you are. age, name, etc

## Rename columns
ufo.columns
ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported':'Shape_Reported'},inplace=True)

ufo.columns

## Bonus
# If all columns want to replace  space with _
ufo.columns.str.replace(" ","_")


## Drop col - AXIS =0 for row, axis=1 column
ufo.drop("Colors_Reported", axis=1,inplace=True) 

## SORT
movies.title.sort_values()
movies.title.sort_values(ascending=False)
movies.sort_values('title')

movies.sort_values(['content_rating','duration'])


## FILTER BY CERTAIN COLUMNS 

movies.head()
## Mthod 1
booleans= []
for len in movies.duration:
    if len >=200:
        booleans.append(True)
    else:
        booleans.append(False)
booleans[0:5]

is_long=movies[booleans]
is_long.head()

## method2
is_long = movies.duration>=200
movies[is_long]

## better
movies[movies.duration >=200]  ## returns df
movies[movies.duration >=200]['genre']
movies[(movies.duration >=200) & (movies.genre=='Drama')] ## multi condition

movies[(movies.genre=='Drama') | (movies.genre=='Crime') | (movies.genre=='Action')]

movies[movies.genre.isin(['Drama','Crime','Action'])]  ## multi

       
## ITErate through rows
for index, row in ufo.iterrows():
    print index, row.City, row.State

## AXIS
No specific dropby row or column. we use axis =0 and axis=1 as reference

movies.mean()
movies.mean(axis=1)
movies.mean(axis=0)


## string functions in pandas
tbl.head()
tbl.item_name.str.upper()
tbl[tbl.item_name.str.contains('Veggie')]['item_name']
tbl[tbl.item_name.str.contains('Veggie')]['item_name']


## Convert dtypes

drinks =pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()
drinks.dtypes

drinks['beer_servings']=drinks.beer_servings.astype(float)
tbl.item_price.str.replace('$','').astype(float).mean()



## GROUP BY
drinks.head()
drinks.beer_servings.mean()
## used to analyze by categories - For each continent, wht is the content
drinks.groupby(by='continent').beer_servings.mean()
drinks.groupby(by='continent').beer_servings.max()
drinks.groupby(by='continent').beer_servings.agg(['count','min','mean','max'])

drinks.groupby(by='continent').mean().plot(kind='bar')


movies.genre.value_counts()
movies.genre.value_counts(normalize=True)
movies.genre.unique()
movies.genre.nunique()


## Cross tab
pd.crosstab(movies.genre, movies.rating)
movies.duration.plot(kind='hist')





## MISSING VALUES
ufo= pd.read_csv("http://bit.ly/uforeports")
ufo.tail()

ufo.isnull().tail()
ufo.notnull().tail()

ufo.isnull().sum()

ufo.shape ##18241,5
ufo.dropna(how='any').shape
ufo.dropna(how='all').shape
ufo.dropna(subset=['City','Shape Reported'],how='all').shape

## Index
# 1. identification 2. selection 3.Alignment

drinks[drinks.country=="India"] 

getindex
setindex


drinks.continent.head()
drinks.set_index('country',inplace=True)
drinks.head()
drinks.continent.head()


ppl = pd.Series([3000000,5000],index=['Albania','Andorra'],name='population')
ppl

drinks.beer_servings * ppl
