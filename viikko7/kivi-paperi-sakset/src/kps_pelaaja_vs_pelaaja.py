from kivi_sakset_paperi import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self):
        pass
    
    def _toisen_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")
