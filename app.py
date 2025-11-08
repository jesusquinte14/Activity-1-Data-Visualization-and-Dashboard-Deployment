import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='University Dashboard', layout='wide')

@st.cache_data
def load_data(path='university_student_data.csv'):
    return pd.read_csv(path)

df = load_data()

st.title('University Student Analytics Dashboard')
st.markdown('This dashboard summarizes admissions, enrollment, retention, and satisfaction data.')

# Sidebar filters
years = sorted(df['year'].dropna().unique()) if 'year' in df.columns else []
departments = sorted(df['department'].dropna().unique()) if 'department' in df.columns else []
terms = sorted(df['term'].dropna().unique()) if 'term' in df.columns else []

year_filter = st.sidebar.multiselect('Select year(s):', years, default=years)
dept_filter = st.sidebar.multiselect('Select department(s):', departments, default=departments)
term_filter = st.sidebar.multiselect('Select term(s):', terms, default=terms)

df_f = df.copy()
if year_filter:
    df_f = df_f[df_f['year'].isin(year_filter)]
if dept_filter:
    df_f = df_f[df_f['department'].isin(dept_filter)]
if term_filter:
    df_f = df_f[df_f['term'].isin(term_filter)]

# KPI section
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric('Total Applications', int(df_f['applications'].sum()) if 'applications' in df_f.columns else 'N/A')
with col2:
    st.metric('Total Enrolled', int(df_f['enrolled'].sum()) if 'enrolled' in df_f.columns else 'N/A')
with col3:
    st.metric('Avg Retention Rate', round(df_f['retention_rate'].mean(), 2) if 'retention_rate' in df_f.columns else 'N/A')
with col4:
    st.metric('Avg Satisfaction', round(df_f['satisfaction_score'].mean(), 2) if 'satisfaction_score' in df_f.columns else 'N/A')

st.divider()

# Visualizations
if 'year' in df_f.columns and 'retention_rate' in df_f.columns:
    ret_fig = px.line(df_f.groupby('year')['retention_rate'].mean().reset_index(),
                      x='year', y='retention_rate', title='Retention Rate Over Time')
    st.plotly_chart(ret_fig, use_container_width=True)

col_a, col_b = st.columns(2)
with col_a:
    if 'year' in df_f.columns and 'satisfaction_score' in df_f.columns:
        sat_fig = px.bar(df_f.groupby('year')['satisfaction_score'].mean().reset_index(),
                         x='year', y='satisfaction_score', title='Avg Satisfaction by Year')
        st.plotly_chart(sat_fig, use_container_width=True)
with col_b:
    if 'term' in df_f.columns and 'retention_rate' in df_f.columns:
        term_fig = px.bar(df_f.groupby('term')['retention_rate'].mean().reset_index(),
                          x='term', y='retention_rate', title='Retention Rate by Term')
        st.plotly_chart(term_fig, use_container_width=True)

st.markdown('---')
st.markdown('Data preview:')
st.dataframe(df_f.head())
