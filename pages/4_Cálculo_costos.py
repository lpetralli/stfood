import streamlit as st
import pandas as pd

# Asumiendo que tus DataFrames ya están cargados en st.session_state
if 'recetario' in st.session_state:
    # Asignando los DataFrames a variables
    recetario = st.session_state.recetario
    df_conteo = st.session_state.df_conteo
    df_costos = st.session_state.df_costos

    # Combinando los DataFrames
    df_combinado = recetario.merge(df_conteo, left_on='Nombre', right_on='Comidas').merge(df_costos, on='Ingrediente')

    # Añadiendo la columna de total de personas
    total_personas = st.number_input("Introduce el número de personas", value=1, min_value=1)
    df_combinado['Total Personas'] = total_personas

    # Asegurando que las columnas sean del tipo correcto
    df_combinado[['Cantidad por persona', 'Total Personas', 'Costo', 'Veces que se come']] = df_combinado[['Cantidad por persona', 'Total Personas', 'Costo', 'Veces que se come']].astype(float)

    # Calculando el costo total por ingrediente
    df_combinado['Costo Total'] = (
        df_combinado['Cantidad por persona'] *
        df_combinado['Total Personas'] *
        df_combinado['Costo'] *
        df_combinado['Veces que se come']
    )

    # Mostrando el DataFrame resultante
    # st.dataframe(df_combinado, hide_index= True)

    # Calculando y mostrando el costo total, costo por comida, y costo por ingrediente
    costo_total = df_combinado['Costo Total'].sum()
    st.write(f"Costo Total: ${round(costo_total,2)}")

    costo_por_persona = costo_total / total_personas
    st.write(f"Costo por persona: ${round(costo_por_persona,2)}")

    costo_por_comida = df_combinado.groupby('Nombre')['Costo Total'].sum()
    st.write("Costo por Comida:", round(costo_por_comida,2))

    costo_por_ingrediente = df_combinado.groupby('Ingrediente')['Costo Total'].sum()
    st.write("Costo por Ingrediente:", costo_por_ingrediente)

else:
    st.error('No hay recetas')