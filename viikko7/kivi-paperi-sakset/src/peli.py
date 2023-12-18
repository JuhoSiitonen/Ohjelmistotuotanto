
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Peli:
    @staticmethod
    def pvp():
        return KPSPelaajaVsPelaaja()
    
    @staticmethod
    def tekoaly():
        return KPSTekoaly()
    
    @staticmethod
    def parempi_tekoaly():
        return KPSParempiTekoaly()