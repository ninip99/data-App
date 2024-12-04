import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="graph", page_icon="🎉")
st.sidebar.header("데이터 시각화")


st.markdown("## 시각화 개요 \n"
"본 프로젝트는     를 알려주는 대시보드입니다. "
"여기에 추가 내용을 더 넣을 수 있습니다.")


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 연관성 파악을 위한 시각화 ")

df = pd.read_csv('../iris.csv')

st.write(df.head())

tab1, tab2, tab3, tab4 = st.tabs(["SepalLength", "SepalWidth", "PetalLength","Species"])

with tab1: #total bill
    fig = plt.figure(figsize=(20,10))
    st.header("SepalLength 히스토그램")
    # sns.barplot(x='sex', y='ejection_fraction', data=df)
    sns.histplot(x='SepalLength', data=df, hue='Species', kde=True)
    
    st.pyplot(fig)

with tab2:
    st.header("SepalWidth 히스토그램")
    fig = plt.figure(figsize=(20,10))
    sns.histplot(x='SepalLength',y='SepalWidth', data=df, hue='Species', kde=True)
    #sns.scatterplot(df, x = 'creatinine_phosphokinase', y = 'DEATH_EVENT')
    # sns.countplot(x='age', hue='DEATH_EVENT', data=df)
    st.pyplot(fig)

with tab3:
    st.header("SeLength PeLength Scatter")
    fig = plt.figure(figsize=(20,10))
    sns.scatterplot(x='SepalLength', y='PetalLength', data=df)

    #sns.histplot(x='ejection_fraction', data=df, bins=13, hue='DEATH_EVENT', kde=True)

    #sns.violinplot(x='DEATH_EVENT',y='ejection_fraction', data=df, hue='DEATH_EVENT')
    st.pyplot(fig)

with tab4:
    st.header("Species PetalLength Boxplot")
    fig = plt.figure(figsize=(20,10))
    # sns.jointplot(x='platelets', y='creatinine_phosphokinase',data=df, kind='kde', hue='DEATH_EVENT')
    sns.boxplot(x='Species', y='PetalLength', data=df)
    st.pyplot(fig)
        
