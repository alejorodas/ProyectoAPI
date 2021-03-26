import pandas as pd
from sodapy import Socrata



# Example authenticated client (needed for non-public datasets):
# client = Socrata(www.datos.gov.co,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
client = Socrata("www.datos.gov.co", None)

def consultar(limite_registros, departamento):
  results = client.get("gt2j-8ykr", limit=limite_registros, departamento_nom=departamento)
  
  # Convert to pandas DataFrame
  results_df = pd.DataFrame.from_records(results)
  return  results_df

def filtrar_datos(datos_consultados):
  datos_filtrados = datos_consultados[['ubicacion', 'departamento_nom', 'edad', 'estado','tipo_recuperacion','pais_viajo_1_nom']]
  return datos_filtrados