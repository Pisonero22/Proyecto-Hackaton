import pickle
import streamlit as st
import numpy as np

# Función para cambiar el idioma y recargar la página
def change_language(lang):
    st.session_state.language = lang
    st.experimental_rerun()  # Recarga la página para aplicar el nuevo idioma

# Inicializar el idioma en session_state
if 'language' not in st.session_state:
    st.session_state.language = 'en'  # Idioma por defecto

# Función para traducir textos
def translate(text_key):
    translations = {
        'en': {
            'header': '📚 Book Recommender System',
            'select_book': '📖 Select a book to get recommendations:',
            'show_recommendations': '📚 Show Recommendations',
            'history': '📜 **Book Selection History**:'
        },
        'es': {
            'header': '📚 Sistema de Recomendación de Libros',
            'select_book': '📖 Selecciona un libro para obtener recomendaciones:',
            'show_recommendations': '📚 Mostrar Recomendaciones',
            'history': '📜 **Historial de Selección de Libros**:'
        },
        'zh': {
            'header': '📚 图书推荐系统',
            'select_book': '📖 选择一本书以获取推荐:',
            'show_recommendations': '📚 显示推荐',
            'history': '📜 **书籍选择历史**:'
        },
        'fr': {
            'header': '📚 Système de Recommandation de Livres',
            'select_book': '📖 Sélectionnez un livre pour obtenir des recommandations :',
            'show_recommendations': '📚 Montrer les Recommandations',
            'history': '📜 **Historique des Sélections de Livres** :'
        },
        'ar': {
            'header': '📚 نظام توصيات الكتب',
            'select_book': '📖 اختر كتابًا للحصول على توصيات:',
            'show_recommendations': '📚 عرض التوصيات',
            'history': '📜 **تاريخ اختيار الكتب**:'
        }
    }
    return translations[st.session_state.language][text_key]

# Estilos CSS personalizados
st.markdown("""
    <style>
        body {
            background-color: #001F3F;  /* Color de fondo añil */
            color: #FFFFFF;  /* Color de texto blanco */
            font-family: 'Poppins', sans-serif;
        }
        .stApp {
            background-color: #0074D9;  /* Color de fondo azul medio para la app */
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
        .custom-title {
            font-size: 60px;
            color: #FFFFFF;  /* Color blanco para el título */
            text-align: center;
            font-weight: bold;
            font-family: 'Poppins', sans-serif;
            margin-bottom: 0px;
            text-shadow: 2px 2px 4px #000000;  /* Sombra negra para el texto */
        }
        .title-container {
            background-color: transparent;
            margin-bottom: 30px;
        }
        .flag {
            cursor: pointer;
            width: 35px;
            margin: 0 10px;
            transition: transform 0.3s ease;
            background-color: transparent;
            border: none;
        }
        .flag:hover {
            transform: scale(1.2);
        }
        .recommendation-box {
            background-color: #17D7E8; 
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #001F3F;  /* Borde añil */
        }
        img {
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        }
        .book-title {
            font-size: 22px;
            color: #001F3F;  /* Color añil para los títulos de los libros */
            text-align: center;
            margin-top: 15px;
            font-family: 'Roboto Mono', monospace;
        }
        .scrollable-container {
            height: 250px;
            overflow-y: auto;
            background-color: #F3F8FF;  /* Color de fondo azul medio para el historial */
            border-radius: 10px;
            padding: 15px;
            margin-top: 25px;
            border: 1px solid #001F3F;  /* Borde añil */
        }
        .historial-item {
            font-size: 18px;
            color: #001F3F;  /* Color añil para el historial */
            margin-bottom: 12px;
        }
        .stButton>button {
            background-color: #0074D9;  /* Color azul medio para otros botones */
            color: #FFFFFF;  /* Color de texto blanco */
            padding: 14px 30px;
            border: none;
            font-size: 17px;
            margin-top: 25px;
            transition: background-color 0.3s ease;
            border-radius: 10px;  /* Bordes redondeados para los botones */
        }
        .stButton>button:hover {
            background-color: #0056b3;  /* Color más oscuro al pasar el mouse */
        }
        .recommend-button {
            background-color: #F3F8FF;  /* Color específico para el botón de recomendaciones */
            color: #001F3F;  /* Color de texto añil */
            padding: 14px 30px;
            border: none;
            font-size: 17px;
            margin-top: 25px;
            border-radius: 10px;  /* Bordes redondeados para el botón de recomendaciones */
            cursor: pointer;
            display: inline-block;  /* Para permitir el margen */
        }
        .recommend-button:hover {
            background-color: #e0e7ec;  /* Color más oscuro al pasar el mouse para el botón de recomendaciones */
        }
        .stSelectbox label {
            font-size: 19px;
            color: #FFFFFF;  /* Color de texto blanco para las etiquetas */
            margin-bottom: 12px;
        }
        .stSelectbox .css-1wa3eu0-placeholder {
            color: #FFFFFF;  /* Color de texto blanco para el placeholder */
        }
    </style>
""", unsafe_allow_html=True)

# Añadir el título personalizado sin foto de fondo
st.markdown("""
    <div class="title-container">
        <h1 class="custom-title">C•SPIDE</h1>        
    </div>
""", unsafe_allow_html=True)

# Botones para cambiar idioma, con fondo transparente
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1:
    if st.button("🇪🇸", key="es_button"):
        change_language('es')
with col2:
    if st.button("🇺🇸", key="en_button"):
        change_language('en')
with col3:
    if st.button("🇨🇳", key="zh_button"):
        change_language('zh')
with col4:
    if st.button("🇫🇷", key="fr_button"):
        change_language('fr')
with col5:
    if st.button("🇦🇪", key="ar_button"):
        change_language('ar')

# Cargar modelos y datos
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

# Inicializar historial en session_state
if 'historial' not in st.session_state:
    st.session_state.historial = []

# Función para obtener imágenes de libros
def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url

# Función para recomendar libros
def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=5)

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    
    return books_list, poster_url

# Selección de libro por el usuario
selected_books = st.selectbox(
    translate('select_book'),
    book_names
)

# Botón para ver la recomendación utilizando HTML
if st.markdown(f'<button class="recommend-button">{translate("show_recommendations")}</button>', unsafe_allow_html=True):
    recommended_books, poster_url = recommend_book(selected_books)

    # Actualizar el historial con el libro seleccionado
    if selected_books not in st.session_state.historial:
        st.session_state.historial.append(selected_books)

    # Mostrar las recomendaciones en 4 columnas
    num_recommendations = min(4, len(recommended_books))
    columns = st.columns(num_recommendations)

    for i in range(num_recommendations):
        with columns[i]:
            st.markdown(f'<p class="book-title">{recommended_books[i]}</p>', unsafe_allow_html=True)
            st.image(poster_url[i], use_column_width=True)

    # Mostrar el historial como un scroll en la parte inferior
    st.write(translate('history'))

    # Contenedor con scroll para el historial
    historial_content = '<div class="scrollable-container">'
    for book in st.session_state.historial:
        historial_content += f'<p class="historial-item">{book}</p>'
    historial_content += '</div>'

    st.markdown(historial_content, unsafe_allow_html=True)
