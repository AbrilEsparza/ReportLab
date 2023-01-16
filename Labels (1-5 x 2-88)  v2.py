'''
    pagesize=(107.717,205.185827)
    
    ASSETS LABEL INFO
    1.Supplier
    2.SKU
    3.Item 

    LOCATIONS LABEL 
    1.Building
    2.Floor

'''
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm, mm, inch
import pandas

##      Paths

path = r"C:\Users\developer\Documents\TygaSmartOffice\Atmosphere TV - Demo\Label Generation\unnamed.jpg"   #atmosphere logo                           
filename = r'C:\Users\developer\Documents\TygaSmartOffice\Atmosphere TV - Demo\Label Generation\com.tygabox.Workstations.csv' #workstation csv
assetsfile =  r'C:\Users\developer\Documents\TygaSmartOffice\Atmosphere TV - Demo\Label Generation\com.tygabox.Assets_v3.csv' #workstation csv



df = pandas.read_csv(filename, header=0)
dfAssets = pandas.read_csv(assetsfile, header=0)

data  = df.loc[:,['bldgName','description','floor']]
assets = dfAssets.loc[:,['supplier','sku','item', 'location']]





def Label(c, image, data):
    
    #c.roundRect(5.10236, 5, 66.89764, 196.1575, 5, stroke =1, fill = 0) 
    #c.roundRect(8.22047, 11.5, 60, 60, 5, stroke =1, fill = 0)          #Logo
    #c.drawImage(image, 8.5, 11.9055, 58.5, 58.5)

    c.drawImage(image, 8.5, 1.84*inch, 21*mm, 21*mm, mask=[240, 255, 240, 255, 240, 255])
    c.setDash(4,2)
    c.setFillColor("#404040")
    c.rect(5.10236, 10*mm, 23.6*mm, 10.5*mm, stroke = 0, fill = 1)  ## Location Int 
    c.rect(73.7008, 0.5, 10*mm,  2.88*inch, stroke = 0, fill = 1)     ## Location Ext   
    
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 12)
       
    c.drawCentredString(37.98425, 40*mm, data["bldgName"].upper())
    c.drawCentredString(37.98425,  35*mm, "Floor " + str(data["floor"]).upper())
    
    size =10
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", size)


    if(len(data["description"]) > 10):
        size = 7
        c.setFont("Helvetica-Bold", size)
    c.drawCentredString(37.98425, 14.5*mm, data["description"].upper())
    
    if (data["description"]== "Mother's Room"):

        c.setFillColor(colors.white)
        c.rotate(90)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(120, -90, data["description"].upper())
        c.drawString(15, -90, data["description"].upper())
    else: 
        c.setFillColor(colors.white)
        c.rotate(90)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(120, -90, data["description"].upper())
        c.drawString(15, -90, data["description"].upper())
   # c.drawCentredString(37.98425, 84.614173, data["description"].upper())
    

def AssetLabel(c, image, data):
   
    c.drawImage(image, 8.5, 1.84*inch, 21*mm, 58.5, mask=[240, 255, 240, 255, 240, 255])

    c.setDash(4,2)
    c.setFillColor("#404040")


    #c.rect(5.10236, 73.7008, 66.89764, 26.9291, stroke = 0, fill = 1)  ## Location Int (23.6mm * 9.5mm )
    c.rect(5.10236, 10*mm, 23.6*mm, 10.5*mm, stroke = 0, fill = 1)  ## Location Int 
    c.rect(73.7008, 0.0, 31.1811, 2.88*inch, stroke = 0, fill = 1)     ## Location Ext   
    

    if (str(data["sku"])== "nan"): 
        data["sku"] = " "
       # print("done")
    if (str(data["supplier"])== "nan"): 
        data["supplier"] = " "
     
    data["location"] = data["location"].replace("Conference", "conf")

    if (18 > len(data["item"])>12 ): 
        item = data["item"].upper().split(' ')

        partOne = item[0:len(item)//2]
        partTwo = item[len(item)//2:]
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 7)
        #print(partOne)
        #print(partTwo)
        c.drawCentredString(37.98425, 31*mm,  " ".join(partOne))
        c.drawCentredString(37.98425, 28*mm, " ".join(partTwo))
    
    elif (len(data["item"])>=18): 
        item = data["item"].upper().split(' ')

        partOne = item[0:len(item)//2]
        partTwo = item[len(item)//2: (len(item)//2)*2]
        partThree = item[(len(item)//2)*2 :]
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 7)
        #print(partOne)
        #print(partTwo)
        c.drawCentredString(37.98425, 31*mm,  " ".join(partOne))
        c.drawCentredString(37.98425, 28*mm, " ".join(partTwo))
        c.drawCentredString(37.98425, 25*mm, " ".join(partThree))
    else: 
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(37.98425, 31*mm, data["item"].upper())

    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(37.98425, 14.5*mm, data["location"].upper())

    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(37.98425, 40*mm, str(data["supplier"]).upper())    
    #c.drawCentredString(37.98425, 130, data["item"].upper())
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(37.98425, 35*mm, str(data["sku"]).upper())

        ## DONT MOVE 
    c.setFillColor(colors.white)
    c.rotate(90)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(120, -95, data["location"].upper())
    c.drawString(15, -95, data["location"].upper())  
    

def createPDF(cont, ws): 
    path = r"C:\Users\developer\Documents\TygaSmartOffice\Atmosphere TV - Demo\Label Generation\logo.png"
    fileName = "AssetLabel_" + str(cont) + ".pdf"
    c = canvas.Canvas(fileName, pagesize=(1.5*inch,2.88*inch)) #w/o diecut space 3mm
    #Label(c, path, ws)
    AssetLabel(c, path, ws)
    c.showPage()
    c.save()



for index, ws in assets.iterrows(): 
   createPDF(index, ws)




