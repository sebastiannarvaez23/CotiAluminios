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

        """ informacion del encabezado """
        pdf.set_xy(10, 20)
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
        pdf.set_xy(10, 60)
        pdf.set_font('Arial', 'B', 10)
        pdf.multi_cell(w = 190, h = 5, txt = f"Cliente: {document_header['customer_name']}", border = 0, align = 'L', fill = 0)
        pdf.set_font('Arial', 'B', 10)
        pdf.multi_cell(w = 190, h = 5, txt = f"Direccion: {document_header['customer_address']}", border = 0, align = 'L', fill = 0)
        pdf.set_font('Arial', 'B', 10)
        pdf.multi_cell(w = 190, h = 5, txt = f"Teléfono: {document_header['customer_telephone']}", border = 0, align = 'L', fill = 0)

        """ Articulos solicitados """
        pdf.set_xy(10, 80)
        pdf.set_font('Arial', 'B', 16)
        pdf.multi_cell(w = 190, h = 10, txt = "Articulos cotizados", border = 0, align = 'L', fill = 0)

    addPage()

    """ Encabezados de la tabla """
    pdf.set_xy(10, 90)
    pdf.set_font('Arial', 'B', 8)
    pdf.cell(w = 8, h = 6.5, txt = '#', border = 1, align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 8)
    pdf.cell(w = 45.5, h = 6.5, txt = 'Tipo Ventana', border = 1,align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 8)
    pdf.cell(w = 45.5, h = 6.5, txt = 'Cantidad', border = 1,align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 8)
    pdf.cell(w = 45.5, h = 6.5, txt = 'Precio Unidad', border = 1,align = 'C', fill = 0)
    pdf.set_font('Arial', 'B', 8)
    pdf.multi_cell(w = 45.5, h = 6.5, txt = 'Precio Total', border = 1,align = 'C', fill = 0)

    """ Información de la tabla """
    #valores tablas
    noLines = 0
    for line in document_line:
        if noLines == 20: 
            noLines = 0
            addPage()

        noLines = noLines + 1
        pdf.set_font('Arial', '', 8)
        pdf.cell(w = 8, h = 6, txt = str(line['id']), border = 1, align = 'C', fill = 0)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w = 45.5, h = 6, txt = str(line['name']), border = 1, align = 'C', fill = 0)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w = 45.5, h = 6, txt = str(line['quantity']), border = 1, align = 'C', fill = 0)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w = 45.5, h = 6, txt = "$ " + str("{:,}".format(int(line['priceUnit']))), border = 1, align = 'C', fill = 0)
        pdf.set_font('Arial', '', 8)
        pdf.multi_cell(w = 45.5, h = 6, txt = "$ " + str("{:,}".format(int(line['price']))), border = 1, align = 'C', fill = 0)
    
    """ Ultima linea TOTAL """

    pdf.set_font('Arial', '', 11)
    pdf.cell(w = 144.5, h = 10, txt = "TOTAL COTIZACIÓN", border = 1, align = 'R', fill = 0)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(w = 45.5, h = 10, txt = document_header['total_quote'], border = 1, align = 'C', fill = 0)

    

    pdf_buffer = pdf.output(dest="S").encode("latin1")
    return pdf_buffer
