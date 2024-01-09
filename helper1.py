import numpy as np
import pandas as pd


def medals(df):
    medals = df.drop_duplicates(subset=['Team','NOC','Games','Year','Season','City','Sport','Event','Medal'])
    medals = medals.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending = False)
    medals['tot'] = medals['Gold'] + medals['Silver'] + medals['Bronze']

    medals['Gold'] = medals['Gold'].astype(int)
    medals['Silver'] = medals['Silver'].astype(int)
    medals['Bronze'] = medals['Bronze'].astype(int)
    medals['tot'] = medals['tot'].astype(int)

    return medals

def season_year_country(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'All')

    df['region'].isnull()
    countries = np.unique(df['region'].dropna().values).tolist()
    countries.sort()
    countries.insert(0, 'All')

    season = df['Season'].unique().tolist()
    season.insert(0,'ALL')

    return season,years,countries

def fetch_medal(df,year,country,season):
    medal_df = df.drop_duplicates(subset=['Team','NOC','Games','Year','Season','City','Sport','Event','Medal','region'])
    f =0
    if country == 'All' and year == 'All' and season == 'ALL':#1
        temp_df = medal_df
    if country != 'All' and year != 'All' and season == 'ALL':#2
        f =1
        temp_df = medal_df[(medal_df['region'] == country) & (medal_df['Season'] == season)]
    if country != 'All' and year != 'All' and season != 'ALL':#3
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['Season'] == season)]
    if country != 'All' and year == 'All' and season == 'ALL':#4
        temp_df = medal_df[medal_df['region'] == country]
    if country != 'All' and year == 'All' and season != 'ALL':#5
        temp_df = medal_df[(medal_df['region'] == country) & (medal_df['Season'] == season)]
    if country == 'All' and year != 'All' and season == 'ALL':#6
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if country == 'All' and year != 'All' and season != 'ALL':#7
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['Season'] == season)]
    if country == 'All' and year == 'All' and season != 'ALL':#8
        temp_df = medal_df[medal_df['Season'] == season]
    if f ==1:
        z = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year').reset_index()
    else:
        z = temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending = False).reset_index()

    z['Total'] = z['Gold'] + z['Silver'] + z['Bronze']

    z['Gold'] = z['Gold'].astype(int)
    z['Silver'] = z['Silver'].astype(int)
    z['Bronze'] = z['Bronze'].astype(int)
    z['Total'] = z['Total'].astype(int)

    return z

def select_season(df):
    df['Season'].isnull()
    seasons = np.unique(df['Season'].dropna().values).tolist()
    seasons.sort()
    return seasons

def data_over_time(df,col):
    nations_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index()
    nations_over_time=nations_over_time.sort_values(by=['Year'])
    nations_over_time.rename(columns={'count': col, 'Year': 'Edition'}, inplace=True)
    return nations_over_time

def most_successful_sport(df,sport,n):
    temp_df = df.dropna(subset=['Medal'])

    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    athlete_counts = temp_df['Name'].value_counts().reset_index()
    athlete_counts.columns = ['Name', 'Medals']
    top_athletes = athlete_counts.head(n)
    merged_df = pd.merge(top_athletes, temp_df, left_on='Name', right_on='Name', how='left')
    result_df = merged_df[['Name', 'Medals', 'Sport', 'region']].drop_duplicates('Name')
    return result_df

def event_calc(df,sport):
    temp_df = df.dropna(subset=['Event'])
    temp_df = temp_df[temp_df['Sport'] == sport]
    events_by_sport_per_year = temp_df.groupby(['Year', 'Sport'])['Event'].nunique().reset_index(name='Total Events')

    return events_by_sport_per_year

def country_analysis(df,region):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset = ['Games','City','Sport','Event','Team','Year','Medal','NOC'],inplace =True)
    new_df = temp_df[temp_df['region'] == region]
    new_df = new_df.groupby('Year').count()['Medal'].reset_index()
    return new_df

def ideal_sport(df,region):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df[temp_df['region'] == region]
    final = temp_df.groupby(['Year', 'Sport'])['Medal'].nunique().reset_index(name='Total Medal')
    return final

def most_successful_country(df,country,n):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df[temp_df['region'] == country]

    athlete_counts = temp_df['Name'].value_counts().reset_index()
    athlete_counts.columns = ['Name', 'Medals']
    top_athletes = athlete_counts.head(n)
    merged_df = pd.merge(top_athletes, temp_df, left_on='Name', right_on='Name', how='left')
    result_df = merged_df[['Name', 'Medals', 'Sport']].drop_duplicates('Name')
    return result_df

def men_vs_women(df):
    df = df.drop_duplicates(subset =['Name','region'])

    df_men=df[df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    df_women=df[df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = df_men.merge(df_women,on='Year',how='left')
    final.rename(columns={'Name_x':'Male','Name_y':'Female'},inplace=True)

    final.fillna(0,inplace=True)

    return final
