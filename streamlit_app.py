import streamlit as st
import pandas as pd

# Beispiel-Daten für die Tabelle
data = {
    'Space': ['Space 1', 'Space 2', 'Space 3', 'Space 4'],
    'Description': ['Beschreibung 1', 'Beschreibung 2', 'Beschreibung 3', 'Beschreibung 4']
}
df = pd.DataFrame(data)

st.title('Zugriffsanfrage für Programm')

# Eingabefelder für Name und Organisation
name = st.text_input('Name')
organization = st.text_input('Organisation')

# Mehrfachauswahl für den gewünschten Space
spaces = st.multiselect('Gewünschter Space', df['Space'])

# Button zum Absenden der Anfrage
if st.button('Anfrage absenden'):
    if name and organization and spaces:
        st.success(f'Anfrage erfolgreich gesendet von {name} ({organization}) für die Spaces: {", ".join(spaces)}')
    else:
        st.error('Bitte füllen Sie alle Felder aus.')

# Anzeige der Tabelle
st.write('Verfügbare Spaces:')
st.dataframe(df)
