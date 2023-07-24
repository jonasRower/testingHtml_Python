
class atributyParametryData:

    def __init__(self, dataZExcelu, htmldata):

        self.htmldata = htmldata

        # ziska data
        self.atributyAParametryVsechTagu = self.ziskejDataProVsechnyTagy(dataZExcelu)



    def getAtributyAParametryVsechTagu(self):
        return(self.atributyAParametryVsechTagu)



    def ziskejDataProVsechnyTagy(self, dataZExcelu):

        atributyAParametryVsechTagu = []

        for i in range(0, len(dataZExcelu)):
            dataDleTagu = dataZExcelu[i]

            atributyAParametryJednohoTaguPoRadcich = self.ziskejDataProIndexyTagu(dataDleTagu)
            atributyAParametryVsechTagu.append(atributyAParametryJednohoTaguPoRadcich)

        return(atributyAParametryVsechTagu)




    def ziskejDataProIndexyTagu(self, dataDleTagu):

        nazevTagu = dataDleTagu[0]
        otevreneIndexy = dataDleTagu[1]

        atributyAParametryJednohoTaguPoRadcich = []
        atributyAParametryJednohoTaguPoRadcich.append(nazevTagu)

        for i in range(0, len(otevreneIndexy)):
            indexRadku = otevreneIndexy[i]
            radekHtml = self.htmldata[indexRadku]

            atributyAParametryTagu = self.vratVsechnyAtributyParametryRadkuProDanyRadekTag(radekHtml, nazevTagu)

            if(atributyAParametryTagu != -1):
                atributyAParametryJednohoTaguPoRadcich.append(atributyAParametryTagu)

        return(atributyAParametryJednohoTaguPoRadcich)



    def vratVsechnyAtributyParametryRadkuProDanyRadekTag(self, radekHtml, nazevTagu):

        atributyAParametryTagu = []

        radekSTagem = self.vratCastRadkuPodleTagu(radekHtml, nazevTagu)

        if(radekSTagem != -1):
            radekBezTagu = radekSTagem.replace(nazevTagu, "")
            radekBezTagu = radekBezTagu.replace("<", "")
            radekBezTagu = radekBezTagu.replace(">", "")

            parametryAtributyRadku = radekBezTagu.split(" ")

            for i in range(0, len(parametryAtributyRadku)):
                PA = parametryAtributyRadku[i]
                atributAParametr = self.rozdelRadekNaAtributAParametr(PA)

                if(atributAParametr != -1):
                    atributyAParametryTagu.append(atributAParametr)

        else:
            atributyAParametryTagu = -1

        return(atributyAParametryTagu)



    def rozdelRadekNaAtributAParametr(self, radek):

        if("=" in radek):
            atributAParametr = radek.split("=")
        else:
            atributAParametr = -1

        return(atributAParametr)



    # pokud je na radku vice tagu, pak vrati tu aktualni cast radku
    def vratCastRadkuPodleTagu(self, radekHtml, nazevTagu):

        # na jednom radku muze byt vic tagu, rozdeli tedy radek pomoci "><"
        radekRozdelenyNaTagy = radekHtml.split("><")
        radekSTagem = -1

        for i in range(0, len(radekRozdelenyNaTagy)):
            castRadkuSTagem = radekRozdelenyNaTagy[i]
            if (nazevTagu in castRadkuSTagem):
                radekSTagem = castRadkuSTagem
                break

        return(radekSTagem)


