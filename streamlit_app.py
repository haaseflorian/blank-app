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

# Kontrollkästchen für die Auswahl
df['Auswählen'] = False
for i in range(len(df)):
    df.at[i, 'Auswählen'] = st.checkbox(f"{df.at[i, 'Space']} - {df.at[i, 'App']}", key=i)

# Button zum Absenden der Anfrage
if st.button('Anfrage absenden'):
    selected_rows = df[df['Auswählen']]
    if name and organization and not selected_rows.empty:
        st.success(f'Anfrage erfolgreich gesendet von {name} ({organization}) für die Auswahl: {selected_rows.to_dict(orient="records")}')
    else:
        st.error('Bitte füllen Sie alle Felder aus und treffen Sie eine Auswahl.')
