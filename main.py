from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import red, Color, gray, black

def hello(c):
    c.setFont("Helvetica-Bold", 10)
    c.drawString(6.9*inch, 11.3*inch, "OS/WO")
    # c.drawString(6.9*inch, 11.3*inch, "OS/WO")
    c.drawString(0.7*inch, 11.3*inch, "ELEB")
    c.rect(0.25*inch, 11*inch, 7.7*inch, 0.6*inch, fill=0)
    c.rect(0.25*inch, 11*inch, 1.2*inch, 0.6*inch, fill=0)
    c.rect(0.25*inch, 11*inch, 6.1*inch, 0.6*inch, fill=0)

    c.drawString(2.5*inch, 10.5*inch, "DADOS DO COMPONENTE(COMPONENT DATA)")
    c.setFillColor(gray, alpha=0.5)
    c.rect(0.4*inch, 10.4*inch, 7.4*inch, 0.3*inch, fill=True, stroke=False)

    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(0.6*inch, 9.7 * inch, "2- Número de Parte/ (P/N)")
    c.drawString(3.05 * inch, 9.7 * inch, "Part Number:")  #
    c.rect(0.4*inch, 9.5 * inch, 7.4 * inch, 0.6*inch, fill=0)

    c.drawString(0.6 * inch, 8.8 * inch, "3- Número de Série/ (S/N)")
    c.drawString(3.05 * inch, 8.8 * inch, "Serial Number:")  #
    c.rect(0.4*inch, 8.6*inch, 7.4 * inch, 0.6*inch, fill=0)

    c.drawString(0.6 * inch, 7.9 * inch, "4- Descrição / ")
    c.drawString(1.9 * inch, 7.9 * inch, "Description:")  #
    c.rect(0.4 * inch, 7.7 * inch, 7.4*inch, 0.6*inch, fill=0)

    c.drawString(0.6 * inch, 7 * inch, "5- Quantidade / ")
    c.drawString(2.1 * inch, 7 * inch, "Quantity:")  #
    c.rect(0.4*inch, 6.8*inch, 7.4*inch, 0.6*inch, fill=0)

    c.drawString(0.6 * inch, 6.1 * inch, "6- Programa / ")
    c.drawString(1.9 * inch, 6.1 * inch, "Program:")  #
    c.rect(0.4*inch, 5.9*inch, 7.4*inch, 0.6*inch, fill=0)

    c.drawString(0.6 * inch, 5.2 * inch, "7- Cliente / ")
    c.drawString(1.65 * inch, 5.2 * inch, "Customer:")  #
    c.rect(0.4 * inch, 5*inch, 7.4*inch, 0.6*inch, fill=0)

    c.drawString(0.6 * inch, 4.55 * inch, "8- Atendimento / ")
    c.drawString(2.2 * inch, 4.55 * inch, "Priority:")  #
    c.drawString(0.6 * inch, 4.15 * inch, "Normal /")
    c.drawString(1.6 * inch, 4.15 * inch, "Normal:")  #
    c.drawString(0.6 * inch, 3.6 * inch, "Urgente /")
    c.drawString(1.6 * inch, 3.6 * inch, "Urgent:")  #
    c.drawString(4.2 * inch, 4.55 * inch, "9- Tipo de Serviço / ")
    c.drawString(6.05 * inch, 4.55 * inch, "Type of Service:")  #

    # Small Squares
    c.rect(2.55 * inch, 4.1 * inch, 0.3 * inch, 0.3 * inch, fill=0)
    c.rect(2.55 * inch, 3.55 * inch, 0.3 * inch, 0.3 * inch, fill=0)

    # 8 - 9
    c.rect(0.4 * inch, 3.3 * inch, 3.7 * inch, 1.5 * inch, fill=0)
    c.rect(0.4 * inch, 3.3 * inch, 7.4 * inch, 1.5 * inch, fill=0)

    c.drawString(0.6 * inch, 2.55 * inch, "10- Situação Comercial / ")
    c.drawString(2.9 * inch, 2.55 * inch, "Order Status:")  #
    c.rect(0.4 * inch, 2.2 * inch, 7.4 * inch, 0.8 * inch, fill=0)

    c.drawString(0.6 * inch, 1.5 * inch, "11- Cotação / ")
    c.drawString(1.9 * inch, 1.5 * inch, "Quotation:")  #
    c.rect(0.4 * inch, 1.3 * inch, 7.4 * inch, 0.6 * inch, fill=0)

    c.drawString(4.2 * inch, 1.5 * inch, "12- Ordem de Venda / ")
    c.setFont("Helvetica", 14)
    c.drawString(6.25 * inch, 1.5 * inch, "Customer Order:")  #
    c.rect(0.4 * inch, 1.3 * inch, 3.7 * inch, 0.6 * inch, fill=0)


"""c = canvas.Canvas("Hello.pdf")
hello(c)
c.showPage()  # Finish the current page
c.save()"""
