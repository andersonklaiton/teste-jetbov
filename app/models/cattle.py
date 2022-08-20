from datetime import datetime, timedelta


class Cattle:
    def __init__(self, brinco:str, peso_inicial:float, area_inicial:str, dias_na_area:int) -> None:
        self.brinco =brinco
        self.peso_inicial = peso_inicial
        self.area_inicial = area_inicial
        self.dias_na_area = dias_na_area
        self.data_de_entrada = datetime.now().strftime("%d/%m/%y")
        self.data_de_saida = (datetime.now()+timedelta(dias_na_area)).strftime("%d/%m/%y")