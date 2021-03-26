from prettytable import PrettyTable



def mensaje_bienvenida():
  print("""
  |-------------------------------------------------------------------|
  | BIENVENIDO AL SISTEMA DE CONSULTA CASOS DE COVID - 19 EN COLOMBIA |
  |-------------------------------------------------------------------|
  """
  )
 

def menu_principal():
  mensaje_bienvenida()
  limite_registros = input("Digite limite registro: ")
  departamento = input("Digite Departamento: ").upper()
  return [limite_registros, departamento]

def mostrar_datos(datos_df):
    pretty = PrettyTable()
    pretty.field_names = ['Ubicacion', 'NombreDepartamento', 'Edad', 'Estado','TipoRecuperacion','PaisProcedencia']
    for registro in range(len(datos_df)):
      pretty.add_row([
                    datos_df.loc[registro, 'ubicacion'],
                    datos_df.loc[registro, 'departamento_nom'],
                    datos_df.loc[registro, 'edad'],
                    datos_df.loc[registro, 'estado'],
                    datos_df.loc[registro, 'tipo_recuperacion'],
                    datos_df.loc[registro, 'pais_viajo_1_nom']
                    ])
    print(pretty)