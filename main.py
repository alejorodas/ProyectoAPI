from api import datos_abiertos
from ui import interfaz

limite_registros, departamento = interfaz.menu_principal()
datos_consultados = datos_abiertos.consultar(limite_registros, departamento)
datos_filtrados = datos_abiertos.filtrar_datos(datos_consultados)
interfaz.mostrar_datos(datos_filtrados)

