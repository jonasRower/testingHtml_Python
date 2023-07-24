
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


# nacte data z excelu
class dataZexcelu:

    def __init__(self, adresaExcelu):

        self.xl = pd.ExcelFile(adresaExcelu)
        self.nazvyListu = self.ziskejNazvyListu()
        self.poleVsechTabulek = self.ziskejPoleVsechTabulek(self.nazvyListu)



    def getPoleVsechTabulek(self):
        return(self.poleVsechTabulek)

    def ziskejNazvyListu(self):
        nazvyVsechListu = self.xl.sheet_names

        return(nazvyVsechListu)


    def ziskejPoleVsechTabulek(self, nazvyListu):

        tabulkyVsechListu = []

        for i in range(0, len(nazvyListu)):
            nazevListu = nazvyListu[i]
            tabulkaDanehoListu = self.ziskejDataDanehoListu(nazevListu)
            tabulkyVsechListu.append(tabulkaDanehoListu)

        return(tabulkyVsechListu)


    def ziskejDataDanehoListu(self, nazevListu):

        dataListu = self.xl.parse(nazevListu)
        dataTabulky = dataListu.values
        dataReShape = dataTabulky.reshape(dataListu.shape).T
        tabulkaAll = dataReShape.tolist()

        #vzhledem k tomu, ze tabulka zacina 2. sloupcem, data jsou redukovana o 1. sloupec
        tabulka = []
        tabulka.append(nazevListu)
        tabulka.append(tabulkaAll[1])
        tabulka.append(tabulkaAll[2])


        return(tabulka)