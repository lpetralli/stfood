import streamlit as st
import pandas as pd
from streamlit_extras.grid import grid
from collections import Counter

if 'df_conteo' not in st.session_state:
    st.session_state['df_conteo'] = pd.DataFrame()

if 'recetario' in st.session_state:
    comidas_disponibles = st.session_state.recetario['Nombre'].unique().tolist()
    comidas_disponibles.insert(0,'Nada')

    st.title('🍴 Menú')
    my_grid = grid(5,5,5,5, vertical_align= 'center')
    # Día 1
    desayuno1 = my_grid.subheader('Día 1')
    my_grid.selectbox("Desayuno", comidas_disponibles, key='Desayuno1')
    my_grid.selectbox("Almuerzo", comidas_disponibles, key='Almuerzo1')
    my_grid.selectbox("Merienda", comidas_disponibles, key='Merienda1')
    my_grid.selectbox("Cena", comidas_disponibles, key='Cena1')

    # Día 2
    my_grid.subheader('Día 2')
    my_grid.selectbox("Desayuno", comidas_disponibles, key='Desayuno2')
    my_grid.selectbox("Almuerzo", comidas_disponibles, key='Almuerzo2')
    my_grid.selectbox("Merienda", comidas_disponibles, key='Merienda2')
    my_grid.selectbox("Cena", comidas_disponibles, key='Cena2')

    # Día 3
    my_grid.subheader('Día 3')
    my_grid.selectbox("Desayuno", comidas_disponibles, key='Desayuno3')
    my_grid.selectbox("Almuerzo", comidas_disponibles, key='Almuerzo3')
    my_grid.selectbox("Merienda", comidas_disponibles, key='Merienda3')
    my_grid.selectbox("Cena", comidas_disponibles, key='Cena3')

    # Día 4
    my_grid.subheader('Día 4')
    my_grid.selectbox("Desayuno", comidas_disponibles, key='Desayuno4')
    my_grid.selectbox("Almuerzo", comidas_disponibles, key='Almuerzo4')
    my_grid.selectbox("Merienda", comidas_disponibles, key='Merienda4')
    my_grid.selectbox("Cena", comidas_disponibles, key='Cena4')
   
    # Lista para almacenar las keys
    elecciones = []

    # Lista de comidas
    comidas = ['Desayuno', 'Almuerzo', 'Merienda', 'Cena']

    # Bucle para los números del 1 al 4
    for i in range(1, 5):
        # Bucle para cada comida en la lista de comidas
        for comida in comidas:
            # Formatea la key combinando la comida y el número, y agrega la key a la lista de elecciones
            key = f'{comida}{i}'
            elecciones.append(st.session_state[key])


    # Obtiene un conteo de cada elemento único en la lista
    
    if st.button('Guardar Menú'):
    
        conteo = Counter(elecciones)

        # Convierte el conteo en un DataFrame
        df_conteo = pd.DataFrame(conteo.items(), columns=['Comidas', 'Veces que se come'])
        df_conteo = df_conteo[df_conteo['Comidas'] != 'Nada']
        st.title(" ")

        # Ahora 'df_conteo' es un DataFrame que contiene el conteo de cada elemento único
        
        # st.dataframe(df_conteo, hide_index = True)
        st.session_state['df_conteo'] = df_conteo

    st.subheader('Menú actual: ')
    st.dataframe(st.session_state['df_conteo'], hide_index = True)

else:
    st.error('No hay recetas')