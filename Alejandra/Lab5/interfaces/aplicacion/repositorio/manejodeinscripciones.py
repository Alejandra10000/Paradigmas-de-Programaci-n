
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios 
from aplicacion.modelos.usuario import Usuario 
#---------------------
# Clase storemanager
# NO TIENE VARIABLES
#---------------------
class ManejoDeInscripciones:
    #-----------------------------------------------------------------
    # Decorador staticmethod
    # El objeto solo tiene la funcion sin llamar variables Locales
    #Envuelve la funcion sin llamar variables Locales
    # El objeto ManejoDeInscripciones es la interface intercambiable
    #-----------------------------------------------------------------
    @staticmethod
    def inscribirUsuario(usuario:Usuario, repositorioDeUsuarios:RepositorioDeUsuarios) -> None:
        print("--------> Guardando usuario... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
        
