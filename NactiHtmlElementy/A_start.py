import ziskejDataZExcelu
import NactiSoubor
import atributyAParametry
import elementyHtml
import elementyATagy
import zapisDataDoExcelu


adresaExcelu = 'rows_Of_First_Last_Tags.xlsx'
adresaHtml = 'C:\\Users\\jonas\\OneDrive\\Dokumenty\\2021\\Python\\Data\\Pánské sporttestery _ Alza.cz.html'

# ziska data z Excelu
dataExcel = ziskejDataZExcelu.dataZexcelu(adresaExcelu)
dataZExcelu = dataExcel.getPoleVsechTabulek()

# ziska data z html
htmlClass = NactiSoubor.txt(adresaHtml)
htmldata = htmlClass.getPole()

# ziska atributy a parametry
#atributyParametry = atributyAParametry.atributyParametryData(dataZExcelu, htmldata)
#AtributyAParametryVsechTagu = atributyParametry.getAtributyAParametryVsechTagu()

# ziska elementy
elementyData = elementyHtml.elementyData(htmldata)
vsechnyElementy = elementyData.getVsechnyElementy()

# priradi elementy k tagum
elementyData = elementyATagy.elementyData(vsechnyElementy, dataZExcelu)

# ziska data - tyto data lze prohlizet jen s pozastavenim pomoci breakpointu
vsechnyElementyTagy = elementyData.getVsechnyElementyTagy()

# ziska data pro zapis do Excelu
dataDoExcelu = elementyData.getDataDoExcelu()

# zapise data do Excelu
zapisDataDoExcelu.dataDoExcelu(dataDoExcelu)



print("")