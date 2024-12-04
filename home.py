import streamlit as st

st.set_page_config(page_title="Home", page_icon="👋")



st.write("# Iris 붓꽃 데이터 웹앱 프로젝트 👋")


st.header("붓꽃 데이터 분석 ")
st.subheader("데이터 세트 개요")

st.write("-" * 50) # print()

st.markdown(
             
    "kaggle 데이터를 분석해보자.iris.csv 데이터 참조 "
    "아이리스 품종 중 Setosa, Versicolor, Virginica 분류에 대한"
    "  로널드 피셔의 1936년 논문에서 사용된 데이터 셋"
    "붓꽃 iris는 3가지 종류 Setosa, Versicolor, Virginica를 가지고 있다."
    "각 데이터 포인트는 꽃받침(sepal)과 꽃잎(petal)의 길이와 너비를 
    "        나타내는 4개의 특성을 가지고 있습니다."
            )
