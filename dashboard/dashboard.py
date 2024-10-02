import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


wheather_file_df = pd.read_csv("dashboard/Pertanyaan1.csv")
wheather_file_df["dteday"] = pd.to_datetime(wheather_file_df["dteday"])
filtered_hour_df = pd.read_csv("dashboard/Pertanyaan2.csv")

st.header("Projek Analisis Data")

st.subheader("Jumlah Rental pada Kondisi Cuaca Tertentu Setiap Bulannya")

wheather_df = wheather_file_df.groupby([pd.Grouper(key='dteday', freq='M'), wheather_file_df.weathersit, wheather_file_df.weathersit_label]).cnt.sum()
wheather_df = wheather_df.reset_index()

plt.figure(figsize=(12, 6))
wheather_df['dteday'] = wheather_df['dteday'].dt.strftime('%Y-%m')
sns.barplot(x='dteday', y='cnt', hue='weathersit_label', data=wheather_df)
plt.xlabel('Bulan')
plt.ylabel('Jumlah Rental')
plt.yscale('log')
plt.xticks(rotation=45)
plt.legend(title='Kondisi Cuaca')

st.pyplot(plt)
st.write(
          """
dari plot yang sudah dibuat, hampir setiap bulan jumlah pengguna sepeda paling banyak ketika cuaca cerah yang kemudian diikuti dengan cuaca berkabut atau berawan dan mengalami penurunan yang signifikan ketika cuaca mulai mulai hujan
          """
)

st.subheader("Jumlah Rental Sepeda setiap jam pada bulan september")

df = filtered_hour_df.groupby(by="hr").cnt.sum()

plt.figure(figsize=(10,6))
df.plot(kind='bar')
plt.xlabel('Jam ')
plt.xticks(rotation=0)
plt.ylabel('Jumlah Rental')
st.pyplot(plt)

st.write(
          """
pada plot kedua bisa disimpulkan bahwa ketika memasuki jam 6 akan mengalami peningkatan jumlah pengguna hingga puncak pertama yaitu jam 8 yang bisa menandai rush hour, kemudian akan mengalami penurunan yang tidak terlalu signifikan lalu akan kembali meningkat hingga puncak jumlah pengguna tertinggi pada jam 5 sore yang bisa menandai jam pulang dan akan mengalami penurunan hingga jam 4 pagi.         
          """
)
