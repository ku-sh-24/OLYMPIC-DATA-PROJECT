import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import preprocessor1
import helper1
import plotly.express as px
import numpy as np
import plotly.figure_factory as ff
import seaborn as sns

df = pd.read_csv('athlete_events.csv')
noc = pd.read_csv('noc_regions.csv')

df = preprocessor1.preprocess(df, noc)
st.sidebar.title("Olympics Analysis")
st.sidebar.image('olympicrings.png')
st.sidebar.title("USER PREFERENCE")
user_choice = st.sidebar.radio(
    'SELECT AN OPTION',
    ('MEDAL ANALYSIS', 'OLYMPIC OVERALL ANALYSIS', 'COUNTRY-WISE ANALYSIS','ATHLETE-WISE ANALYSIS')
)

if user_choice == 'MEDAL ANALYSIS':
    st.sidebar.header("MEDALS")
    season, years, country = helper1.season_year_country(df)

    selected_season = st.sidebar.selectbox("SELECT SEASON", season)
    selected_year = st.sidebar.selectbox("SELECT YEAR", years)
    selected_country = st.sidebar.selectbox("SELECT COUNTRY", country)

    medals = helper1.fetch_medal(df, selected_year, selected_country, selected_season)
    if selected_country == 'All' and selected_year == 'All' and selected_season == 'ALL': #1
        st.title('OVERALL')
    if selected_country == 'All' and selected_year == 'All' and selected_season != 'ALL': #2
        st.title('SEASON WISE')
    if selected_country != 'All' and selected_year != 'All' and selected_season == 'ALL':#3
        st.title('MEDAL TALLY IN' + str(selected_year) +' OF ' + str(selected_country) + ' IN BOTH SEASON')
    if selected_country != 'All' and selected_year != 'All' and selected_season != 'ALL':#4
        st.title('MEDAL TALLY IN' + str(selected_year) +' OF ' + str(selected_country) + ' IN ' + str(selected_season) + ' OLYMPIC')
    if selected_country != 'All' and selected_year == 'All' and selected_season == 'ALL':#5
        st.title('ANALYSIS OF ' + str(selected_country) + 'THROUGH OUT ALL OLYMPIC IN ALL SEASONS')
    if selected_country != 'All' and selected_year == 'All' and selected_season != 'ALL':#6
        st.title('ANALYSIS OF ' + str(selected_country) + 'THROUGHOUT ALL ' + str(selected_season) + ' OLYMPIC')
    if selected_country == 'All' and selected_year != 'All' and selected_season == 'ALL':#7
        st.title('ANALYSIS OF ' + str(selected_year) + ' IN ALL OLYMPIC SEASONS')
    if selected_country == 'All' and selected_year != 'All' and selected_season != 'ALL':#8
        st.title('ANALYSIS OF ' + str(selected_year) + ' IN ALL ' + str(selected_season) + ' OLYMPIC')
    st.table(medals)

if user_choice == 'OLYMPIC OVERALL ANALYSIS':

    st.title("TOP STATISTIC")
    seasons = helper1.select_season(df)
    selected_season = st.sidebar.selectbox('SELECT SEASON', seasons)

    df_winter = df[(df['Season'] == 'Winter')]
    df_summer = df[(df['Season'] == 'Summer')]

    if selected_season == 'Summer':
        editions = df_summer['Year'].unique().shape[0]-1
        cities = df_summer['City'].unique().shape[0]
        names = df_summer['Name'].unique().shape[0]
        nations =df_summer['region'].unique().shape[0]
        sports = df_summer['Sport'].unique().shape[0]
        events = df_summer['Event'].unique().shape[0]

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("EDITIONS")
            st.title(editions)
        with col2:
            st.header("HOSTS")
            st.title(cities)
        with col3:
            st.header("SPORTS")
            st.title(sports)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("EVENTS")
            st.title(events)
        with col2:
            st.header("NATIONS")
            st.title(nations)
        with col3:
            st.header("ATHLETES")
            st.title(names)

        nations_over_time = helper1.data_over_time(df_summer, 'region')
       # st.table(nations_over_time)
        fig = px.line(nations_over_time, x='Edition', y='region')
        st.title("PARTICIPATING NATIONS OVER TIME")
        st.plotly_chart(fig)

        events_over_time = helper1.data_over_time(df_summer, 'Event')
        fig = px.line(events_over_time, x='Edition', y='Event')
        st.title("EVENTS OVER TIME")
        st.plotly_chart(fig)

        athletes_over_time = helper1.data_over_time(df_summer, 'Name')
        fig = px.line(athletes_over_time, x='Edition', y='Name')
        st.title("ATHLETES OVER TIME")
        st.plotly_chart(fig)

        st.title("No. of events over all sports over time")
        Sevent_list = df_summer['Sport'].unique().tolist()
        Sevent_list.sort()
        Sevent_list.insert(0, 'Overall')

        selected_sport = st.selectbox('Select a event', Sevent_list)
        x_df = helper1.event_calc(df_summer, selected_sport)
        #st.table(x)
        fig = px.line(x_df, x='Year', y='Total Events', title=f"Events OVER TIME for {selected_sport}")
        st.plotly_chart(fig)

        st.title("MOST SUCCESSFUL")
        sport_list = df_summer['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0, 'Overall')

        selected_sport = st.selectbox('Select a sport', sport_list)
        x=helper1.most_successful_sport(df_summer, selected_sport, 10)
        st.table(x)

    if selected_season == 'Winter':
        editions = df_winter['Year'].unique().shape[0]
        cities = df_winter['City'].unique().shape[0]
        names = df_winter['Name'].unique().shape[0]
        nations = df_winter['region'].unique().shape[0]
        sports = df_winter['Sport'].unique().shape[0]
        events = df_winter['Event'].unique().shape[0]

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Editions")
            st.title(editions)
        with col2:
            st.header("Hosts")
            st.title(cities)
        with col3:
            st.header("Sports")
            st.title(sports)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Events")
            st.title(events)
        with col2:
            st.header("Nations")
            st.title(nations)
        with col3:
            st.header("Athletes")
            st.title(names)

        nations_over_time = helper1.data_over_time(df_winter, 'region')
        fig = px.line(nations_over_time, x='Edition', y='region')
        st.title("PARTICIPATING NATIONS OVER TIME")
        st.plotly_chart(fig)

        events_over_time = helper1.data_over_time(df_winter, 'Event')
        fig = px.line(events_over_time, x='Edition', y='Event')
        st.title("EVENTS OVER TIME")
        st.plotly_chart(fig)

        athletes_over_time = helper1.data_over_time(df_winter, 'Name')
        fig = px.line(athletes_over_time, x='Edition', y='Name')
        st.title("ATHLETES OVER TIME")
        st.plotly_chart(fig)

        st.title("No. of events over all sports over time")
        Sevent_list = df_winter['Sport'].unique().tolist()
        Sevent_list.sort()
        Sevent_list.insert(0, 'Overall')

        selected_sport = st.selectbox('Select a event', Sevent_list)
        x_df = helper1.event_calc(df_winter, selected_sport)
        #st.table(x)
        fig = px.line(x_df, x='Year', y='Total Events', title=f"Events OVER TIME for {selected_sport}")
        st.plotly_chart(fig)

        st.title("MOST SUCCESSFUL")
        sport_list = df_winter['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0, 'Overall')
        selected_sport = st.selectbox('Select a sport', sport_list)
        x = helper1.most_successful_sport(df_winter, selected_sport, 10)
        st.table(x)

if user_choice == 'COUNTRY-WISE ANALYSIS':
    st.title("COUNTRY WISE ANALYSIS")
    seasons = helper1.select_season(df)
    selected_season = st.sidebar.selectbox('SELECT SEASON', seasons)

    df_winter = df[(df['Season'] == 'Winter')]
    df_summer = df[(df['Season'] == 'Summer')]

    if selected_season == 'Summer':
        countries = np.unique(df_summer['region'].dropna().values).tolist()
        countries.sort()
        countries.insert(0, 'All')
        selected_country = st.sidebar.selectbox('Select a country', countries)
        country = helper1.country_analysis(df_summer,selected_country)
        fig = px.line(country, x='Year', y='Medal', title=f"Medals OVER TIME for {selected_country}")
        st.plotly_chart(fig)

        final = helper1.ideal_sport(df_summer,selected_country)
        fig = px.bar(final, x='Sport', y='Total Medal', title=f"Events OVER TIME for {selected_country}")
        st.plotly_chart(fig)

        x = helper1.most_successful_country(df_summer,selected_country, 10)
        st.table(x)

    if selected_season == 'Winter':
        countries = np.unique(df_winter['region'].dropna().values).tolist()
        countries.sort()
        countries.insert(0, 'All')
        selected_country = st.sidebar.selectbox('Select a country', countries)
        country = helper1.country_analysis(df_winter,selected_country)
        fig = px.line(country, x='Year', y='Medal', title=f"Medals OVER TIME for {selected_country}")
        st.plotly_chart(fig)

        final = helper1.ideal_sport(df_winter,selected_country)
        fig = px.bar(final, x='Sport', y='Total Medal', title=f"Events OVER TIME for {selected_country}")
        st.plotly_chart(fig)

        x = helper1.most_successful_country(df_winter,selected_country, 10)
        st.table(x)

if user_choice == 'ATHLETE-WISE ANALYSIS':

    df_new = df.drop_duplicates(subset = ['Name','region'])

    x1 = df_new['Age'].dropna()
    x2 = df_new[df_new['Medal'] == 'Gold']['Age'].dropna()
    x3 = df_new[df_new['Medal'] == 'Silver']['Age'].dropna()
    x4 = df_new[df_new['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1,x2,x3,x4],['Overall age','Gold Medalist','Silver Medalist','Bronze medalist'],show_hist=False,show_rug=False)
    fig.update_layout(width=1000, height=600)
    st.plotly_chart(fig)


    x = []
    name =[]
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
    'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
    'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
    'Water Polo', 'Hockey', 'Rowing', 'Fencing',
    'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
    'Tennis', 'Golf', 'Softball', 'Archery',
    'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
    'Rhythmic Gymnastics', 'Rugby Sevens'
    'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = df_new[df_new['Sport'] == sport]
        gold_age = temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna()
        if not gold_age.empty:
            x.append(list(gold_age))
            name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(width=1000, height=600)
    st.plotly_chart(fig)


    sport_list = df_new['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a sport', sport_list)

    df_new['Medal'].fillna('No Medal', inplace=True)
    temp_df_athlete = df_new[df_new['Sport']== selected_sport]
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x=temp_df_athlete['Weight'], y=temp_df_athlete['Height'], hue=temp_df_athlete['Medal'], style=temp_df_athlete['Sex'], s=50)
    st.pyplot(fig)

    df_winter = df[(df['Season'] == 'Winter')]
    df_summer = df[(df['Season'] == 'Summer')]

    final = helper1.men_vs_women(df_summer)
    fig1 = px.line(final, x='Year', y=['Male', 'Female'], title='Male vs. Female Athletes Over the Years (Summer)')
    st.plotly_chart(fig1)

    final = helper1.men_vs_women(df_winter)
    fig2 = px.line(final, x='Year', y=['Male', 'Female'], title='Male vs. Female Athletes Over the Years (Winter)')
    st.plotly_chart(fig2)
