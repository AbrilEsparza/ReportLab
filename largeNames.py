from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm, mm, inch
import pandas

##      Paths

path = r"C:\Users\developer\Documents\TygaSmartOffice\Atmosphere TV - Demo\Label Generation\unnamed.jpg"   #atmosphere logo                           
filename = r'C:\Users\developer\Documents\TygaSmartOffice\Atmosphere TV - Demo\Label Generation\com.tygabox.Workstations.csv' #workstation csv
assetsfile =  r'C:\Users\developer\Documents\TygaSmartOffice\Atmosphere TV - Demo\Label Generation\com.tygabox.Assets_v3.csv' #workstation csv

dfAssets = pandas.read_csv(assetsfile, header=0)
asset = dfAssets.loc[:,['supplier','sku','item', 'location']]


def AssetLabel(c, image, data):
   
    c.drawImage(image, 8.5, 1.84*inch, 21*mm, 21*mm, mask=[240, 255, 240, 255, 240, 255])
    c.setDash(4,2)
    c.setFillColor("#404040")

    c.rect(5.10236, 10*mm, 23.6*mm, 10.5*mm, stroke = 0, fill = 1)  ## Location Int (23.6mm * 9.5mm )
    c.rect(73.7008, 0.0, 31.1811, 2.88*inch, stroke = 0, fill = 1)     ## Location Ext   
    

    if (str(data["sku"])== "nan"): 
        data["sku"] = " "
    if (str(data["supplier"])== "nan"): 
        data["supplier"] = " "
    
    data["location"] = data["location"].replace("Conference", "conf")


    item = data["item"].upper().split(' ')
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(37.98425, 31*mm,  item[0])
    c.drawCentredString(37.98425, 28*mm, item[1])
    c.drawCentredString(37.98425, 25*mm, " ".join(item[2:]))

    c.setFillColor(colors.white)   #Location in int
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(37.98425, 14.5*mm, data["location"].upper())

    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(37.98425, 40*mm, str(data["supplier"]).upper())    
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(37.98425, 35*mm, str(data["sku"]).upper())


    c.setFillColor(colors.white)
    c.rotate(90)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(120, -95, data["location"].upper())
   # c.drawString(120, -95, "conf 5-3".upper())
    c.drawString(15, -95, data["location"].upper())  
   # c.drawString(15, -95, "conf 5-3".upper())  
    

def createPDF(ws): 
    path = r"C:\Users\developer\Documents\TygaSmartOffice\Atmosphere TV - Demo\Label Generation\logo.png"
    fileName = "AssetLabel_106.pdf"
    c = canvas.Canvas(fileName, pagesize=(1.5*inch,2.88*inch)) #w/o diecut space 3mm
    #Label(c, path, ws)
    AssetLabel(c, path, ws)
    c.showPage()
    c.save()


ws = asset.iloc[106]
createPDF(ws)














# word = "Stand Conference Table Dos"
# texto = " "
# arreglo = word.split(" ")
# print(arreglo)
# if (len(arreglo)%2 ==0): 
#     newarreglo = arreglo[0:len(arreglo)//2]
#     for pal in newarreglo: 
#         texto += " " + pal
 

# print(texto)