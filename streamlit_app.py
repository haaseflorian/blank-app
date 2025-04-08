import streamlit as st
import pandas as pd

# Beispiel-Daten für die Tabelle
data = {
    'Space': ['Space 1', 'Space 2', 'Space 3', 'Space 4'],
    'App': ['App A', 'App B', 'App C', 'App D']
}
df = pd.DataFrame(data)

st.title('Zugriffsanfrage für Programm')

# Eingabefelder für Name und Organisation
name = st.text_input('Name')
organization = st.text_input('Organisation')

# Auswahl des Filtertyps
filter_type = st.radio('Filter nach:', ('Spaces', 'Apps'))

# Filter basierend auf der Auswahl
if filter_type == 'Spaces':
    selected_spaces = st.multiselect('Gewünschter Space', df['Space'].unique())
    filtered_df = df[df['Space'].isin(selected_spaces)]
else:
    selected_apps = st.multiselect('Gewünschte App', df['App'].unique())
    filtered_df = df[df['App'].isin(selected_apps)]

# Button zum Absenden der Anfrage
if st.button('Anfrage absenden'):
    if name and organization and not filtered_df.empty:
        st.success(f'Anfrage erfolgreich gesendet von {name} ({organization}) für die Auswahl: {filtered_df.to_dict(orient="records")}')
    else:
        st.error('Bitte füllen Sie alle Felder aus und treffen Sie eine Auswahl.')
