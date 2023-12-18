from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kivi_sakset_paperi import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ekan_siirto)
        print(f'Tietokone valitsi: {tokan_siirto}')
        return tokan_siirto
