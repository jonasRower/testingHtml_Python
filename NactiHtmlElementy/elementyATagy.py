
# tato trida priradi nalezene elementy k tagum
# dohleda prvni a posledni radek tagu obsahujici dany element

class elementyData:

    def __init__(self, vsechnyElementy, dataZExcelu):

        self.dataZExcelu = dataZExcelu
        self.vsechnyElementy = vsechnyElementy

        self.vsechnyElementyTagy = self.vratNejuzsiTagyKeVsemElementum(dataZExcelu, vsechnyElementy)
        self.dataDoExelu = self.upravDataDoExcelu(self.vsechnyElementyTagy)

        print("")


    def getVsechnyElementyTagy(self):
        return(self.vsechnyElementyTagy)


    def getDataDoExcelu(self):
        return(self.dataDoExelu)


    # upravi data na pole 2D aby mohl zapisovat data do Excelu
    # ostatni data lze prohlizet jen s pomoci breakpointu
    def upravDataDoExcelu(self, vsechnyElementyJednoradkove):

        tabulkaDoExcelu = []

        for i in range(0, len(vsechnyElementyJednoradkove)):
            elementData = vsechnyElementyJednoradkove[i]
            indexRadku = elementData[0]
            elementPopis = elementData[1]
            elementPopis = elementPopis[0]

            radekDoExcelu = []
            radekDoExcelu.append(indexRadku)
            radekDoExcelu.append(elementPopis)

            tabulkaDoExcelu.append(radekDoExcelu)

        return(tabulkaDoExcelu)


    def vratNejuzsiTagyKeVsemElementum(self, dataZExcelu, vsechnyElementy):

        vsechnyElementyTagy = []

        for i in range(0, len(vsechnyElementy)):
            elementData = vsechnyElementy[i]
            indexRadku = elementData[0]

            nejuzsiTagy = self.vratPouzeNejUzsiTagyKDanemuIndexuRadku(dataZExcelu, indexRadku)

            # prida ke stavajicim datum tagy
            elementData.append(nejuzsiTagy)

            # zapise do noveho pole
            vsechnyElementyTagy.append(elementData)

        return(vsechnyElementyTagy)


    def vratPouzeNejUzsiTagyKDanemuIndexuRadku(self, dataZExcelu, indexradku):

        otevreneAZavreneTagyOkoloIndexuVsechnyTagy = self.vyhledejVsechnyTagyZahrnujiciIndexRadku(dataZExcelu, indexradku)
        nejuzsiIndexyTagu = self.vratPouzeNejUzsiIndexyTagu(otevreneAZavreneTagyOkoloIndexuVsechnyTagy)
        tagMin = self.vratTagMin(nejuzsiIndexyTagu)
        nejuzsiTagy = self.odeberSirsiTagyNezTagMin(nejuzsiIndexyTagu, tagMin)

        return(nejuzsiTagy)




    # z pole "otevreneAZavreneTagyOkoloIndexuVsechnyTagy" vrati jen ty tagy, ktere jsou nejuzsi nalezejici danemu elementu
    def vratPouzeNejUzsiIndexyTagu(self, otevreneAZavreneTagy):

        nejuzsiIndexyTagu = []

        for i in range(0, len(otevreneAZavreneTagy)):
            otevereneAZavreneIndexyTagu = otevreneAZavreneTagy[i]
            nejuzsiTag = self.vratNejuzsiTag(otevereneAZavreneIndexyTagu)

            if(len(nejuzsiTag) > 0):
                nazevTagu = otevereneAZavreneIndexyTagu[0]
                nejuzsiTagNazev = []
                nejuzsiTagNazev.append(nazevTagu)
                nejuzsiTagNazev.append(nejuzsiTag)
                nejuzsiIndexyTagu.append(nejuzsiTagNazev)

        return(nejuzsiIndexyTagu)



    def odeberSirsiTagyNezTagMin(self, nejuzsiIndexyTagu, tagMin):

        nejuzsiTagy = []
        otevrenyTagMin = tagMin[0]
        zavrenyTagMin = tagMin[1]

        for i in range(0, len(nejuzsiIndexyTagu)):
            tagData = nejuzsiIndexyTagu[i]
            otevrenyAZavrenyTag = tagData[1]

            otevrenyTag = otevrenyAZavrenyTag[0]
            zavrenyTag = otevrenyAZavrenyTag[1]

            if(otevrenyTag == otevrenyTagMin):
                if(zavrenyTag == zavrenyTagMin):
                    nejuzsiTagy.append(tagData)

        return(nejuzsiTagy)



    # pole nejuzsich tagu obsahuje sice nejuzsi tagy, ale neuzsi tagy v ramci jednoho tagu
    # je vsak potreba vratit pouze neuzsi tagy, tak ze sirsi tagy budou odebrany
    def vratTagMin(self, nejuzsiTagy):

        rozdilTaguMin = -1

        for i in range(0, len(nejuzsiTagy)):
            tagData = nejuzsiTagy[i]
            otevrenyAZavrenyTag = tagData[1]

            otevrenyTag = otevrenyAZavrenyTag[0]
            zavrenyTag = otevrenyAZavrenyTag[1]
            rozdilTagu = zavrenyTag - otevrenyTag

            if(i == 0):
                rozdilTaguMin = rozdilTagu
                otevrenyTagMin = otevrenyTag
                zavrenyTagMin = zavrenyTag
            else:
                if(rozdilTagu < rozdilTaguMin):
                    rozdilTaguMin = rozdilTagu
                    otevrenyTagMin = otevrenyTag
                    zavrenyTagMin = zavrenyTag

        tagMin = []

        tagMin.append(otevrenyTagMin)
        tagMin.append(zavrenyTagMin)

        return(tagMin)



    def vratNejuzsiTag(self, otevereneAZavreneIndexyTagu):

        rozdilIndexuMin = -1
        otevrenyIndexMin = -1

        for i in range(1, len(otevereneAZavreneIndexyTagu)):
            otevrenyAZavrenyIndex = otevereneAZavreneIndexyTagu[i]
            otevrenyIndex = otevrenyAZavrenyIndex[0]
            zavrenyIndex = otevrenyAZavrenyIndex[1]

            rozdilIndexu = zavrenyIndex - otevrenyIndex
            if(rozdilIndexuMin == -1):      # jedna se o 1. cyklus
                rozdilIndexuMin = rozdilIndexu
                otevrenyIndexMin = otevrenyIndex
                zavrenyIndexMin = zavrenyIndex
            else:
                if(rozdilIndexu < rozdilIndexuMin):
                    rozdilIndexuMin = rozdilIndexu
                    otevrenyIndexMin = otevrenyIndex
                    zavrenyIndexMin = zavrenyIndex


        nejuzsiTag = []

        if(otevrenyIndexMin > -1):
            nejuzsiTag.append(otevrenyIndexMin)
            nejuzsiTag.append(zavrenyIndexMin)

        return(nejuzsiTag)


    # vyhleda prislusny tag, ktery obsahuje otevreny a uzavreny tag obklopujici dany index radku
    def vyhledejVsechnyTagyZahrnujiciIndexRadku(self, dataZExcelu, indexRadku):

        otevreneAZavreneTagyOkoloIndexuVsechnyTagy = []

        for i in range(0, len(dataZExcelu)):
            otevreneAZavreneIndexyTagu = dataZExcelu[i]
            otevreneAZavreneTagyOkoloIndexuExp = self.vyhledejIndexRadkuMeziOtevrenymAZavrenymTagem(otevreneAZavreneIndexyTagu, indexRadku)

            otevreneAZavreneTagyOkoloIndexuVsechnyTagy.append(otevreneAZavreneTagyOkoloIndexuExp)

        return(otevreneAZavreneTagyOkoloIndexuVsechnyTagy)



    def vyhledejIndexRadkuMeziOtevrenymAZavrenymTagem(self, otevreneAZavreneIndexyTagu, indexExp):

        otevreneAZavreneTagyOkoloIndexuExp = []

        nazevTagu = otevreneAZavreneIndexyTagu[0]
        otevreneTagy = otevreneAZavreneIndexyTagu[1]
        zavreneTagy = otevreneAZavreneIndexyTagu[2]

        otevreneAZavreneTagyOkoloIndexuExp.append(nazevTagu)

        for i in range(0, len(otevreneTagy)):
            indexOtevreny = otevreneTagy[i]
            indexZavreny = zavreneTagy[i]

            if(indexExp >= indexOtevreny):
                if(indexExp <= indexZavreny):
                    otevrenyAzavrenyIndexOkoloIndexExp = []
                    otevrenyAzavrenyIndexOkoloIndexExp.append(indexOtevreny)
                    otevrenyAzavrenyIndexOkoloIndexExp.append(indexZavreny)

                    otevreneAZavreneTagyOkoloIndexuExp.append(otevrenyAzavrenyIndexOkoloIndexExp)

        return(otevreneAZavreneTagyOkoloIndexuExp)

