import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import streamlit as st

# 데이터 불러오기

df = pd.read_csv('iris.csv')

st.sidebar.header('🌸 머신러닝 보고서')
# 시각화
st.header('🌸 아이리스 데이터 상관관계 분석',divider='rainbow')
st.write(df)

st.markdown(''' 
            
- 꽃잎 petal과 꽃받침 sepal의 길이화 폭을 통해 아이리스 꽃의
  세가지 품종을 분류할 수 있습니다.            
- 모델의 정확도를 비교하여
- 어느 모델이 가장 좋은 성능을 보이는지 확인할 수 있습니다.
- 데이터의 전처리와 모델 학습, 평가 성능을 확인합니다.
- Confusion Matrix 시각화를 통해 모델의 성능을 파악합니다.

            
''')


# 모델 학습
X = df.drop(columns=['Species'])  # Features
y = df['Species']  # Target variable

#split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluation du modèle
accuracy = accuracy_score(y_test, y_pred)
st.write(f'Accuracy: {accuracy:.2f}')

# Rapport de classification
st.write(classification_report(y_test, y_pred))

# Matrice de confusion
conf_matrix = confusion_matrix(y_test, y_pred)
fig=plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap="YlGnBu", fmt='d', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
st.pyplot(fig)

