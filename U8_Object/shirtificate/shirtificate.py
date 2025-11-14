from fpdf import FPDF




def main():
    name = input ("Name: ")
    #create pdf objects
    #P = portrait, mmm = millimeters, A4 = 210 x 297mm
    pdf =FPDF (orientation ="P", unit ="mm", format ="A4")
    #add a blank page
    pdf.add_page()
    #disable auto page breaks
    pdf.set_auto_page_break(auto= False, margin = 0)

    #add page title
    pdf.set_font ("Arial","B",24) #set font
    pdf.set_text_color(0,0,0) #set text to black
    pdf.cell (w=0, h=0, text = "CS50 Shirtificate", align = "C", ln =1)

    #add shirt image, position left corner 10, 30 and width 190mm
    pdf.image("shirtificate.png", x=10, y = 30, w=190)

    #write on T-shirt
    pdf.set_font("Arial","B",16) # set font
    pdf.set_text_color(255,255,255) #set color to white
    pdf.set_y(100) #set cursor to middle of the page
    pdf.cell (w=0,h=0,text =f"{name} took CS50",align ="C")

    #save the file
    pdf.output("shirtificate.pdf")

if __name__=="__main__":
    main()
