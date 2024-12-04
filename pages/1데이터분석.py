import streamlit as st
import pandas as pd

st.set_page_config(page_title="page1", page_icon="🎉")

st.sidebar.header("데이터 분석")



st.markdown('''
    ## 붓꽃 데이터 분석 
                
    특성은 "sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)" 순서로 나열됩니다.
            '''
    )
    
st.markdown("<hr>", unsafe_allow_html=True)

st.header("## 데이터 내용 ")   

st.markdown(""" 
            
        -sepal length: 꽃받침 길이  \n
        -sepal width: 꽃받침 넓이 \n
        -petal length: 꽃잎 길이 \n
        -petal width: 꽃잎 넓이 \n
        -species:붓꽃 종류 
         
                """)


df = pd.read_csv('iris.csv')

tab1, tab2, tab3, tab4 = st.tabs(["상위데이터", "데이터통계", "컬럼데이터", "조건데이터"])

with tab1:
    dh=df.head(10)
    st.write(dh)

with tab2:
    dd=df.describe()
    st.write(dd)

with tab3:
    col=df.columns.tolist()
    col=col[0: ]
    se_col = st.multiselect('select column',col)
    new_df = df.loc[:,se_col]
    st.write(new_df)


with tab4:
    col=st.selectbox('select Species',('setosa', 'versicolor', 'virginica'))
          
    condition=df['Species'] == col

    c_df=df.loc[condition]

    st.write(c_df)
   


