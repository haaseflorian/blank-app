import streamlit as st
import pandas as pd

# Beispiel-Daten für die Tabelle der Spaces
spaces_data = {
    'Space': ['Space 1', 'Space 2', 'Space 3', 'Space 4'],
    'Description': ['Beschreibung 1', 'Beschreibung 2', 'Beschreibung 3', 'Beschreibung 4']
}
spaces_df = pd.DataFrame(spaces_data)

# Beispiel-Daten für die Liste der Apps
apps_data = ['App 1', 'App 2', 'App 3', 'App 4']

st.title('Zugriffsanfrage für Programm')

# Eingabefelder für Name und Organisation
name = st.text_input('Name')
organization = st.text_input('Organisation')

# Mehrfachauswahl für den gewünschten Space
spaces = st.multiselect('Gewünschter Space', spaces_df['Space'])

# Mehrfachauswahl für die gewünschten Apps
apps = st.multiselect('Gewünschte Apps', apps_data)

# Button zum Absenden der Anfrage
if st.button('Anfrage absenden'):
    if name and organization and spaces and apps:
        st.success(f'Anfrage erfolgreich gesendet von {name} ({organization}) für die Spaces: {", ".join(spaces)} und Apps: {", ".join(apps)}')
    else:
        st.error('Bitte füllen Sie alle Felder aus.')
