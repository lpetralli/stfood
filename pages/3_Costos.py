import streamlit as st
import pandas as pd
import numpy as np  # Importado para usar np.nan



# Obtener ingredientes únicos y unidades de medida
if 'recetario' in st.session_state:
    
    if 'df_costos' not in st.session_state: 
        ingredientes_unicos = st.session_state.recetario[['Ingrediente', 'Unidad de medida']].drop_duplicates()
        ingredientes_unicos['Costo'] = np.nan  # inicializa la columna de Costo con NaN
        st.session_state['df_costos'] = ingredientes_unicos

    if st.button('♻️ Cargar ingredientes'):
        ingredientes_unicos = st.session_state.recetario[['Ingrediente', 'Unidad de medida']].drop_duplicates()
        ingredientes_unicos['Costo'] = np.nan  # inicializa la columna de Costo con NaN
        st.session_state['df_costos'] = ingredientes_unicos


    st.title('💰 Costos de Ingredientes')
    with st.expander("📝 Editar Costos de Ingredientes"):
            # Muestra el data_editor para editar los costos de los ingredientes
        nuevo_df_costos = st.data_editor(st.session_state['df_costos'], num_rows= 'dynamic', disabled=("Ingrediente", "Unidad de medida"))

            # Si el botón Guardar es presionado, actualiza df_costos en el estado de la sesión con el nuevo DataFrame
        if st.button('Guardar'):
            st.session_state['df_costos'] = nuevo_df_costos
            st.success('Costos guardados exitosamente!')

    with st.expander("👀 Ver Costos de Ingredientes"):
            # Muestra el DataFrame actual de costos de ingredientes
        st.dataframe(st.session_state['df_costos'], hide_index= True)

else:
    st.error('No hay recetas')