class Maquina:
    def __init__(self, encender, apagar, configurar):
        self.encender = encender  
        self.apagar = apagar
        self.__configurar = configurar
        self.fichas_configuradas=0
    
    def encender_maquina(self):
        return (f" la maquina esta encendida. ")
    
    def get_configurar(self):
        return self.__configurar
    
    def set_configurar(self,fichas_personalizadas):
        self.__configurar=fichas_personalizadas
        
    def add_fichas(self,cantidad_fichas):
        self.fichas_configuradas += cantidad_fichas
        return (f" fichas configuradas:{self.fichas_configuradas}")
    
    def apagar_maquina(self):
        return (f"la maquina esta apagada.")    

if __name__ == "__main__":  
    maquina1 = Maquina("encendido", "apagado", "configuración predeterminada")

    print(maquina1.encender_maquina()) 
    print(maquina1.get_configurar())     
    print(maquina1.set_configurar("fichas personalizadas"))  
    print(maquina1.get_configurar())     
    print(maquina1.add_fichas(500))      
    print(maquina1.apagar_maquina())     