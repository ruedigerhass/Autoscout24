import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Daten laden
df = pd.read_csv("/Users/ruedi/Data_Insitute/Autoscout/autoscout24.csv")

# Data cleaning
df = df.dropna()
df = df.drop_duplicates(keep='first')

# Ausreißer eliminieren
min_price, max_price = df.price.quantile([0.001, 0.999])
df = df[(df.price < max_price) & (df.price > min_price)]

min_mileage, max_mileage = df.mileage.quantile([0.001, 0.999])
df = df[(df.mileage < max_mileage) & (df.mileage > min_mileage)]

# Top 5 Hersteller
top_5_hersteller = df['make'].value_counts().head(5).index.tolist()
print("Top 5 Hersteller:", top_5_hersteller)

# Filtern nach den Top 5 Herstellern
df = df[df['make'].isin(top_5_hersteller)]
print(df.shape)

# Nur Gebrauchtwagen behalten
print(df['offerType'].unique())
df = df[df['offerType'] == 'Used']

# Modelle
X = df[['mileage', 'hp']].values
y = df['price'].values

# Aufteilung in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modellinitialisierung
linear_model = LinearRegression()

# Modelltraining
linear_model.fit(X_train, y_train)

# Streamlit-Anwendung
st.title("Auto Preisvorhersage Modell: Lineare Regression")

# Sidebar mit Durchschnittspreisen pro Hersteller
st.sidebar.title("Durchschnittspreise pro Hersteller")
# Filtern nach den Top 5 Herstellern
df_top5 = df[df['make'].isin(top_5_hersteller)]
# Berechnung der Durchschnittspreise pro Hersteller und Sortierung
durchschnittspreise_pro_hersteller = df_top5.groupby('make')['price'].mean().sort_values(ascending=False)
# Runden auf zwei Nachkommastellen
durchschnittspreise_pro_hersteller = durchschnittspreise_pro_hersteller.round(2)
# Anzeige der Ergebnisse in einer Tabelle
durchschnittspreise_pro_hersteller.index.name = 'Hersteller'
durchschnittspreise_pro_hersteller.name = 'Preis'
st.sidebar.write(durchschnittspreise_pro_hersteller)

# Eingabefeld für Kilometerstand und PS
mileage_input = st.number_input("Kilometerstand", min_value=0, key="mileage_input")
hp_input = st.number_input("Pferdestärke", min_value=0, key="hp_input")

# Modellvorhersage
linear_prediction = linear_model.predict([[mileage_input, hp_input]])[0]

# Ausgabe der Vorhersage
st.write("# Preis:", round(linear_prediction))

# Auswertung des Modells
linear_predict_test = linear_model.predict(X_test)
linear_rmse = np.sqrt(mean_squared_error(y_test, linear_predict_test))
linear_r2 = r2_score(y_test, linear_predict_test)

st.write("Linear Regression RMSE:", round(linear_rmse,2))
st.write("Linear Regression R²:", round(linear_r2,2))
