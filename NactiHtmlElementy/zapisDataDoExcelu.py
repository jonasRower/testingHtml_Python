import pandas as pd

class dataDoExcelu:

    def __init__(self, dataNaList):

        self.zapisDataDoExcelu(dataNaList)


    def zapisDataDoExcelu(self, dataNaList):

        nazevSesitu = 'rows_elements.xlsx'

        writer = pd.ExcelWriter(nazevSesitu, engine='xlsxwriter')
        df = pd.DataFrame(dataNaList)
        df.to_excel(writer, sheet_name="data")

        workbook = writer.book

        workbook.filename = nazevSesitu
        writer.save()