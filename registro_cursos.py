# Importar librerías necesarias
import streamlit as st  # Streamlit para crear aplicaciones web interactivas
import pandas as pd  # Pandas para manejar datos en forma de tablas (DataFrames)


# Cargar el logo
logo_path = r"D:\JOEL\Downloads\APP\logo.png"


# Título de la aplicación con el logo y texto
col1, col2 = st.columns([1, 5])  # Crear dos columnas: una para el logo y otra para el texto
with col1:
    st.image(logo_path, width=160)  # Mostrar el logo con un tamaño específico
with col2:
    st.markdown("<h1 style='text-align: left;'>UNIVERSIDAD CESAR VALLEJO - Raza Distinta</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left;'>Registros de Cursos</h3>", unsafe_allow_html=True)



#Cargar los cursos desde el archivo Excel

ruta_excel_cursos_admi= r"D:\JOEL\Downloads\APP\cursos_admi.xlsx"

try:
    df_cursos_admi = pd.read_excel(ruta_excel_cursos_admi)
    lista_cursos_admi = df_cursos_admi["Curso"].dropna().tolist()  # Convertimos la columna 'Curso' en lista
except Exception as e:
    st.error(f"Error cargando el archivo de cursos: {e}")
    lista_cursos = []  # Si hay error, dejamos la lista vacía para evitar errores posteriores


# Crear un DataFrame vacío en la sesión para almacenar los cursos
# Si no existe aún, se inicializa con las columnas especificadas
if 'cursos' not in st.session_state:
    st.session_state.cursos = pd.DataFrame(columns=["Curso", "Hora Inicio", "Hora Fin", "Turno", "Carrera", "Ciclo"])

# Crear un formulario para registrar nuevos cursos
with st.form("form_curso"):

    # Campo para buscar/seleccionar curso con autocompletado
    curso = st.selectbox("Nombre del Curso", options=lista_cursos_admi, placeholder="Selecciona o escribe un curso...")

    # Campos de entrada del formulario

    hora_inicio = st.time_input("Hora de Inicio")  # Campo para seleccionar hora de inicio
    hora_fin = st.time_input("Hora de Fin")  # Campo para seleccionar hora de fin
    turno = st.selectbox("Turno", ["Mañana", "Tarde", "Noche"])  # Menú desplegable para seleccionar turno
    carrera = st.text_input("Carrera")  # Campo para ingresar la carrera asociada al curso
    
    # Nuevo campo para seleccionar el Ciclo
    ciclo = st.selectbox("Ciclo", [
        "1er Ciclo", "2do Ciclo", "3er Ciclo", "4to Ciclo", "5to Ciclo",
        "6to Ciclo", "7mo Ciclo", "8vo Ciclo", "9no Ciclo", "10mo Ciclo"
    ])


    # Botón para enviar el formulario
    submit = st.form_submit_button("Registrar Curso")

    # Si el usuario presiona el botón "Registrar Curso"
    if submit:
        # Crear un nuevo registro en formato diccionario
        nuevo_curso = {
            "Curso": curso,
            "Hora Inicio": hora_inicio.strftime("%H:%M"),  # Formatear la hora de inicio a "HH:MM"
            "Hora Fin": hora_fin.strftime("%H:%M"),  # Formatear la hora de fin a "HH:MM"
            "Turno": turno,
            "Carrera": carrera,
            "Ciclo": ciclo
        }
        # Agregar el nuevo curso al DataFrame de la sesión
        st.session_state.cursos = pd.concat(
            [st.session_state.cursos, pd.DataFrame([nuevo_curso])],
            ignore_index=True
        )
        # Mostrar un mensaje de éxito
        st.success("✅ Curso registrado exitosamente")

# Mostrar en pantalla los cursos que han sido registrados
st.subheader("Cursos Registrados")
st.dataframe(st.session_state.cursos)





