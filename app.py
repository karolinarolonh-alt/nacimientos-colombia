import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Nacimientos en Colombia",
    layout="centered"
)

st.title("Comportamiento de los nacimientos en Colombia")
st.write(
    "Esta aplicación presenta una visualización sencilla del número de nacimientos "
    "registrados en Colombia durante los últimos años, tomando como referencia "
    "información publicada por el DANE en sus Estadísticas Vitales."
)

datos = {
    "Año": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Nacimientos": [660999, 647521, 656704, 649115, 642660, 629402, 616914, 573625, 515549, 445011]
}

df = pd.DataFrame(datos)

st.subheader("Datos utilizados")
st.dataframe(df, use_container_width=True)

total_inicial = df["Nacimientos"].iloc[0]
total_final = df["Nacimientos"].iloc[-1]
variacion = ((total_final - total_inicial) / total_inicial) * 100

col1, col2, col3 = st.columns(3)

col1.metric("Año inicial", "2015")
col2.metric("Año final", "2024")
col3.metric("Variación", f"{variacion:.1f}%")

st.subheader("Gráfico de línea")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df["Año"], df["Nacimientos"], marker="o", linewidth=2)

ax.set_title("Nacimientos en Colombia 2015 - 2024")
ax.set_xlabel("Año")
ax.set_ylabel("Número de nacimientos")
ax.grid(True, alpha=0.3)

st.pyplot(fig)

st.subheader("Análisis")
st.write(
    "De acuerdo con la información observada, los nacimientos en Colombia muestran "
    "una tendencia decreciente durante el periodo analizado. Aunque entre 2015 y "
    "2019 el comportamiento fue relativamente estable, a partir de 2020 se evidencia "
    "una disminución más marcada, especialmente en los años 2023 y 2024."
)

st.write(
    "Este comportamiento puede estar relacionado con cambios sociales, económicos "
    "y demográficos, como la decisión de postergar la maternidad y la reducción "
    "de la fecundidad en el país."
)

st.caption("Fuente: DANE - Estadísticas Vitales, nacimientos en Colombia.")
