from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", size=48)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.ln(0)
        

def shirt(name):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=36)
    pdf.set_text_color(255,255,255)
    pdf.cell(0,250,f"{name} took CS50",align="C")
    pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ").strip().title()
    shirt(name)

if __name__ == "__main__":
    main()