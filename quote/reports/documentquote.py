from django.conf import settings
from fpdf import FPDF

import datetime, os, time

def export_quote_pdf(document_header, document_line):

    title = "PQR S.A.S."
    city = "Santiago de Cali"
    nit  = "901.111.111-1"
    address = "Cra 37a # 3 29 Universidad Libre"
    telephone = "+57 (2) 847 2222"
    mail = "pqr@universidadlibre.com"
    hora = datetime.datetime.now()
    hora = hora.strftime('%d%m%Y%H%M%S')
    pdfname = "report_quote_"+hora+".pdf"

    pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
    
    def addPage():
        pdf.add_page()
        pdf.set_font('Arial', 'B', 9)
        pdf.set_author('cristian gomez')

    addPage()

    """ informacion del encabezado """
    pdf.set_xy(10, 10)
    pdf.set_font('Arial', 'B', 20)
    pdf.multi_cell(w = 190, h = 8, txt = title, border = 0, align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 10)
    pdf.multi_cell(w = 190, h = 5.5, txt = nit, border = 0, align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 8)
    pdf.multi_cell(w = 190, h = 4, txt = address, border = 0, align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 8)
    pdf.multi_cell(w = 190, h = 4, txt = telephone, border = 0, align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 8)
    pdf.multi_cell(w = 190, h = 4, txt = mail, border = 0, align = 'C', fill = 0) 
    pdf.set_font('Arial', 'B', 8)
    pdf.multi_cell(w = 190, h = 4, txt = city, border = 0, align = 'C', fill = 0)


    """ Informacion del cliente """
    pdf.set_xy(10, 50)
    pdf.set_font('Arial', 'B', 10)
    pdf.multi_cell(w = 190, h = 5, txt = f"Cliente: {document_header['customer_name']}", border = 0, align = 'L', fill = 0)
    pdf.set_font('Arial', 'B', 10)
    pdf.multi_cell(w = 190, h = 5, txt = f"Direccion: {document_header['customer_address']}", border = 0, align = 'L', fill = 0)
    pdf.set_font('Arial', 'B', 10)
    pdf.multi_cell(w = 190, h = 5, txt = f"Teléfono: {document_header['customer_telephone']}", border = 0, align = 'L', fill = 0)

    """ Articulos solicitados """
    pdf.set_xy(10, 70)
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(w = 190, h = 8, txt = "Articulos cotizados", border = 0, align = 'L', fill = 0)

    """ Encabezados de la tabla """
    pdf.set_xy(10, 80)
    pdf.set_font('Arial', 'B', 8)
    pdf.cell(w = 8, h = 6.5, txt = '#', border = 1, align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 8)
    pdf.cell(w = 45.5, h = 6.5, txt = 'Tipo Ventana', border = 1,align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 8)
    pdf.cell(w = 45.5, h = 6.5, txt = 'Cantidad', border = 1,align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 7)
    pdf.cell(w = 45.5, h = 6.5, txt = 'Precio Unidad', border = 1,align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 7)
    pdf.multi_cell(w = 45.5, h = 6.5, txt = 'Precio Total', border = 1,align = 'C', fill = 0)

    """ Información de la tabla """
    #valores tablas
    noLines = 0
    for valor in document_line:
        if noLines == 20: 
            noLines = 0
            addPage()

        noLines = noLines + 1
        pdf.set_font('Arial', '', 6)
        pdf.cell(w = 8, h = 6, txt = "dato", border = 1, align = 'C', fill = 0)
        pdf.set_font('Arial', '', 4)
        pdf.cell(w = 45.5, h = 6, txt = "dato", border = 1, align = 'C', fill = 0)
        pdf.set_font('Arial', '', 6)
        pdf.cell(w = 45.5, h = 6, txt = "dato", border = 1, align = 'C', fill = 0)
        pdf.set_font('Arial', '', 7)
        pdf.cell(w = 45.5, h = 6, txt = "dato", border = 1, align = 'C', fill = 0)
        pdf.set_font('Arial', '', 7)
        pdf.multi_cell(w = 45.5, h = 6, txt = "dato", border = 1, align = 'C', fill = 0)

    #nombre del pdf
    file_path = '../../media/'+pdfname
    #pdf.output( file_path, 'F')
    pdf_buffer = pdf.output(dest="S").encode("latin1")
    return pdf_buffer
