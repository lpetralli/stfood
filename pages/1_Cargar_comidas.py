import streamlit as st
import pandas as pd
import time

st.title('Cargar comidas')

if 'recetario' not in st.session_state:
        st.session_state.recetario = pd.DataFrame(columns=["Nombre", "Ingrediente", "Cantidad por persona", "Unidad de medida"])

if 'nombre_comida' not in st.session_state:
    st.session_state.nombre_comida = ""

def submit():
    st.session_state.nombre_comida= st.session_state.widget
    st.session_state.widget = ''

with st.expander("🥗 Agregar nueva comida"):
    st.text_input("Nombre de la Comida:", key='widget', on_change=submit)
    # Inicializa un DataFrame vacío para los ingredientes de la nueva comida
    


    # Si el nombre de la comida no está vacío, permite la edición de ingredientes
    if st.session_state.nombre_comida != "":
            ingredientes_df = pd.DataFrame(columns=["Ingrediente", "Cantidad por persona", "Unidad de medida"])
            st.markdown(f'Completar los ingredientes para **{st.session_state.nombre_comida}**')
            ingredientes_df = st.data_editor(ingredientes_df, num_rows= 'dynamic')

            if st.button("Guardar Comida"):
                if ingredientes_df.empty:
                    st.warning("No se pueden guardar comidas sin ingredientes.")
                else:
                # Repite el nombre de la comida en cada fila del DataFrame de ingredientes
                    ingredientes_df["Nombre"] = st.session_state.nombre_comida
                    
                
                    # Reorganiza las columnas
                    ingredientes_df = ingredientes_df[["Nombre", "Ingrediente", "Cantidad por persona", "Unidad de medida"]]
                    
                    # Añade los ingredientes al recetario
                    st.session_state.recetario = pd.concat([st.session_state.recetario, ingredientes_df], ignore_index=True)
                    
                    
                    st.success(f"{st.session_state.nombre_comida} guardado en el recetario!")
                    st.session_state.nombre_comida = ""


with st.expander("📝 Editar recetario"):
    nuevo_recetario =  st.data_editor(st.session_state.recetario, num_rows= 'dynamic')
    if st.button('Actualizar recetario'):
         st.session_state.recetario = nuevo_recetario
         time.sleep(2)
         st.success('Recetario actualizado!')

with st.expander("👀 Ver recetario"):
    st.dataframe(st.session_state.recetario, hide_index= True)

