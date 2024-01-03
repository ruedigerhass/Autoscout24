# Autoscout24 Analyse und Preisvorhersage

Willkommen bei meiner Analyse und Preisvorhersage für Gebrauchtwagen auf Basis von Autoscout24-Daten. In diesem Projekt habe ich die Top 5 Autohersteller (Volkswagen, Opel, Ford, Skoda, Renault) analysiert und ein Modell für die Vorhersage von Autopreisen mithilfe von Linearer Regression erstellt.

## Inhalt

- **Analyse.ipynb**: Jupyter Notebook mit dem Datenbereinigungs- und Analyseprozess.
- **Modelle.ipynb**: Jupyter Notebook mit dem Trainingsprozess des Linearen Regressionsmodells.
- **autoscout24.csv**: Die bereinigten Daten, die für die Analyse und das Modell verwendet wurden.
- **Autoscout.py**: Streamlit-Anwendung für die Preisvorhersage und Durchschnittspreise pro Hersteller.

## Anwendung starten

1. Installieren Sie die erforderlichen Python-Bibliotheken mit `pip install -r requirements.txt`.
2. Führen Sie die Anwendung mit `streamlit run Autoscout.py` aus.

## Durchschnittspreise pro Hersteller

In der Streamlit-Anwendung finden Sie in der Seitenleiste Durchschnittspreise pro Hersteller für die Top 5 Hersteller.

## Preisvorhersage

Geben Sie den Kilometerstand und die Pferdestärke in die Eingabefelder ein, und die Anwendung sagt Ihnen den geschätzten Preis des Autos voraus.

