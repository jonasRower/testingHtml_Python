
class elementyData:

    def __init__(self, htmldata):

        self.znakyZaSebou = self.definujZnakyZaSebou()
        self.vsechnyElementy = self.vratElementyNaVsechRadcich(htmldata, self.znakyZaSebou)



    def getVsechnyElementy(self):
        return(self.vsechnyElementy)



    def vratElementyNaVsechRadcich(self, htmldata, znakyZaSebou):

        znakyZaSebou = self.definujZnakyZaSebou()
        vsechnyElementy = []

        for i in range(0, len(htmldata)):
            radek = htmldata[i]
            elementyNaRadku = self.vratObsahyElementu(radek, znakyZaSebou)

            if(len(elementyNaRadku) >0):
                indexRadkuAElementy = []
                indexRadkuAElementy.append(i)
                indexRadkuAElementy.append(elementyNaRadku)

                vsechnyElementy.append(indexRadkuAElementy)

        return(vsechnyElementy)


    # vrati vsechny obsahy elementu, tj. substringy mezi ">" a "<"
    def vratObsahyElementu(self, radek, znakyZaSebou):

        poleIndexuKJednotlivymSubstringum = self.vratPoleIndexuKJednotlivymSubStringum(radek, znakyZaSebou)
        indexyChronologicky = self.seradIndexyChronologicky(poleIndexuKJednotlivymSubstringum)
        subStringyBezStringu = self.seradZnakyChronologickyZaSebe(poleIndexuKJednotlivymSubstringum, znakyZaSebou, indexyChronologicky)

        polePrvnichAPoslednichIndexu = self.vratIndexySubPole(subStringyBezStringu, znakyZaSebou)
        polePrvniAPosledniIndexRadku = self.vratPrvniAPosledniIndexyElementu(indexyChronologicky, polePrvnichAPoslednichIndexu)

        elementyNaRadku = self.vratElementyNaRadku(radek, polePrvniAPosledniIndexRadku)

        return(elementyNaRadku)



    def vratElementyNaRadku(self, radek, polePrvniAPosledniIndexRadku):

        elementyNaRadku = []

        for i in range(0, len(polePrvniAPosledniIndexRadku)):
            prvniAPosledniIndexy = polePrvniAPosledniIndexRadku[i]
            prvniIndex = prvniAPosledniIndexy[0]
            posledniIndex = prvniAPosledniIndexy[1]

            obsahElementu = radek[prvniIndex+1:posledniIndex]
            obsahElementu.strip()

            if(obsahElementu != ""):
                elementyNaRadku.append(obsahElementu)


        return(elementyNaRadku)



    def vratPrvniAPosledniIndexyElementu(self, indexyChronologicky, polePrvnichAPoslednichIndexu):

        polePrvniAPosledniIndexRadku = []

        for i in range(0, len(polePrvnichAPoslednichIndexu)):
            prvniAPosledniIndex = polePrvnichAPoslednichIndexu[i]
            prvniIndex = indexyChronologicky[prvniAPosledniIndex[0]]
            posledniIndex = indexyChronologicky[prvniAPosledniIndex[1]]

            prvniAPosledniIndexRadku = []
            prvniAPosledniIndexRadku.append(prvniIndex)
            prvniAPosledniIndexRadku.append(posledniIndex)

            polePrvniAPosledniIndexRadku.append(prvniAPosledniIndexRadku)

        return(polePrvniAPosledniIndexRadku)



    def vratIndexySubPole(self, pole, subPoleExp):

        delkaSubPoleExp = len(subPoleExp)
        polePrvnichAPoslednichIndexu = []

        for i in range(1, len(pole)):
            prvniIndex = i-1
            posledniIndex = delkaSubPoleExp+i-1
            subPole = pole[prvniIndex:posledniIndex]

            if(subPole == subPoleExp):
                prvniAPosledniIndex = []
                prvniAPosledniIndex.append(prvniIndex)
                prvniAPosledniIndex.append(posledniIndex-1)

                polePrvnichAPoslednichIndexu.append(prvniAPosledniIndex)

        return(polePrvnichAPoslednichIndexu)




    def seradZnakyChronologickyZaSebe(self, poleIndexuSubstringy, znakyZaSebou, indexyChronologicky):

        znakyBezStringu = []

        for i in range(0, len(indexyChronologicky)):
            index = indexyChronologicky[i]
            indexSubpole = self.vratIndexSubPoleObsahujiciHodnotu(poleIndexuSubstringy, index)
            znakZPoleZnakyZaSebou = znakyZaSebou[indexSubpole]
            znakyBezStringu.append(znakZPoleZnakyZaSebou)

        return(znakyBezStringu)



    def vratIndexSubPoleObsahujiciHodnotu(self, pole, hodnota):

        for i in range(0, len(pole)):
            subPole = pole[i]
            if(hodnota in subPole):
                indexSubpole = i
                break

        return(indexSubpole)


    def seradIndexyChronologicky(self, poleIndexuSubstringy):

        indexyVektor = []

        for i in range(0, len(poleIndexuSubstringy)):
            indexySubString = poleIndexuSubstringy[i]
            indexyVektor = indexyVektor + indexySubString

        indexyVektor.sort()

        return (indexyVektor)


    def vratPoleIndexuKJednotlivymSubStringum(self, radek, poleSubStringu):

        poleIndexuKJednotlivymSubstringum = []

        for i in range(0, len(poleSubStringu)):
            subString = poleSubStringu[i]

            poleVsechSubStringu = self.vratPoleIndexuVsechSubStringu(radek, subString)
            poleIndexuKJednotlivymSubstringum.append(poleVsechSubStringu)

        return(poleIndexuKJednotlivymSubstringum)


    def vratPoleIndexuVsechSubStringu(self, radek, subString):

        poleIndexuSubStringu = []
        hledejOdIndexu = 0

        for i in range(0, len(radek)):
            indexZnaku = self.vratIndexZnaku(radek, subString, hledejOdIndexu)

            if(indexZnaku > -1):
                poleIndexuSubStringu.append(indexZnaku)
                hledejOdIndexu = indexZnaku + 1
            else:
                break

        return(poleIndexuSubStringu)


    def vratIndexZnaku(self, radek, subStringExp, hledejOdIndexu):

        try:
            indSubStr = radek.index(subStringExp, hledejOdIndexu)
        except:
            indSubStr = -1

        return(indSubStr)



    def definujZnakyZaSebou(self):

        prvniZnak = ">"
        druhyZnak = "<"

        znakyZaSebou = []
        znakyZaSebou.append(prvniZnak)
        znakyZaSebou.append(druhyZnak)

        return (znakyZaSebou)
