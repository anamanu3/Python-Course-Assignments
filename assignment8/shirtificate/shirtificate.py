from fpdf import FPDF

name = input("Name: ").strip()

pdf = FPDF("P", "mm", "A4")
pdf.add_page()

pdf.set_font("Helvetica", "B", 24)
pdf.cell(0, 20, "CS50 Shirtificate", ln=1, align="C")

pdf.image("shirtificate.png", x=15, y=40, w=180)

pdf.set_text_color(255, 255, 255)
pdf.set_y(130)
pdf.cell(0, 10, f"{name} survived CS50! <3", align="C")

pdf.output("shirtificate.pdf")
