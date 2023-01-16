'''
    pagesize=( 2.67*inch,  4.17*inch)
    
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


# sheet size 
pageWidth, pageHeight =  2.67*inch,  4.17*inch

# Dataframes / information of assets and workspaces
df = pandas.read_csv(filename, header=0)
dfAssets = pandas.read_csv(assetsfile, header=0)

data  = df.loc[:,['bldgName','description','floor']]
assets = dfAssets.loc[:,['supplier','sku','item', 'location']]


# Drawing Functions

def Label(c, image, data):
    
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 14)
       
    c.drawCentredString(25*mm, 40*mm, data["bldgName"].upper())
    c.drawCentredString(25*mm,  35*mm, "Floor " + str(data["floor"]).upper())
    
    size =16
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", size)


    c.setFillColor(colors.white)
    c.rotate(90)
    c.setFont("Helvetica-Bold", 8)  
    loc = 2.98*inch + 2.5*mm
    c.drawString(loc, -60*mm, data["description"].upper())
    c.setFont("Helvetica-Bold", 14)  
    c.drawString(45, -60*mm, data["description"].upper())

    
def Label2(c, data):
    
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 18)
       
    c.drawCentredString(pageWidth/2, 50*mm, data["bldgName"].upper())
    c.drawCentredString(pageWidth/2,  40*mm, "Floor " + str(data["floor"]).upper())
    
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 16)  
    loc = 2.98*inch + 2.5*mm
    c.drawCentredString(pageWidth/2, 16*mm, data["description"].upper()) 

    


    

def AssetLabel(c, data):

    if (str(data["sku"])== "nan"): 
        data["sku"] = " "
       # print("done")
    if (str(data["supplier"])== "nan"): 
        data["supplier"] = " "

    if ( len(data["item"])>=14 ): 
        item = data["item"].upper().split(' ')

        partOne = item[0:len(item)//2]
        partTwo = item[len(item)//2:]
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 12)
        #print(partOne)
        print("large")
        c.drawCentredString(pageWidth/2, 45*mm,  " ".join(partOne))
        c.drawCentredString(pageWidth/2, 40*mm, " ".join(partTwo))
    
    # elif (len(data["item"])>=18): 
    #     item = data["item"].upper().split(' ')

    #     partOne = item[0:len(item)//2]
    #     partTwo = item[len(item)//2: (len(item)//2)*2]
    #     partThree = item[(len(item)//2)*2 :]
    #     c.setFillColor(colors.black)
    #     c.setFont("Helvetica-Bold", 7)
    #     #print(partOne)
    #     #print(partTwo)
    #     c.drawCentredString(37.98425, 31*mm,  " ".join(partOne))
    #     c.drawCentredString(37.98425, 28*mm, " ".join(partTwo))
    #     c.drawCentredString(37.98425, 25*mm, " ".join(partThree))
    else: 
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(pageWidth/2, 45*mm, data["item"].upper())

    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(pageWidth/2, 16*mm, data["location"].upper())

    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(pageWidth/2, 55*mm, str(data["supplier"]).upper())    
    c.drawCentredString(pageWidth/2, 50*mm, data["sku"].upper())
    #c.drawCentredString(pageWidth/2, 45*mm, str(data["item"]).upper())

    #     ## DONT MOVE 
    # c.setFillColor(colors.white)
    # c.rotate(90)
    # c.setFont("Helvetica-Bold", 10)
    # c.drawString(120, -95, data["location"].upper())
    # c.drawString(15, -95, data["location"].upper())  
    

# def createPDF_v1(cont, ws): #linea parada
#     pageWidth, pageHeight =  2.67*inch,  4.17*inch
#     path = r"C:\Users\developer\Documents\TygaSmartOffice\Atmosphere TV - Demo\Label Generation\logo.png"
#     fileName = "moveLabel_ v3 " + ws["description"] + ".pdf"
    
#     c = canvas.Canvas(fileName, pagesize=(pageWidth,pageHeight)) #w/o diecut space 3mm
#     c.setDash(4,2)
#     c.setFillColor("#404040")
    
#     c.drawImage(path, 0.93*inch, 3.22*inch, 21*mm,  21*mm, mask=[240, 255, 240, 255, 240, 255])
#     c.roundRect(0.93*inch, 3.22*inch, 22*mm, 22*mm, 5, stroke =1, fill = 0) 
#     c.rect(50*mm, 0.0, 16*mm, 2.98*inch , stroke = 0, fill = 1)     ## Location Ext   2.98*inch  / pageHeight
#     c.line(0,  2.98*inch, pageWidth, 2.98*inch )
    
#     Label(c, path, ws)
#     #AssetLabel(c, path, ws)
   
#     c.showPage()
#     c.save()

def createPDF_v2(cont, ws, type):   #Linea acostada
    pageWidth, pageHeight =  2.67*inch,  4.17*inch
    path = r"C:\Users\developer\Documents\TygaSmartOffice\Atmosphere TV - Demo\Label Generation\logo.png"
    # fileName = "locationLabel_" + str(ws["description"]) + ".pdf"
    fileName = "assetLabel_" + str(cont) + ".pdf"

    c = canvas.Canvas(fileName, pagesize=(pageWidth,pageHeight)) #w/o diecut space 3mm
    c.setDash(4,2)
    c.setFillColor("#404040")
    
    c.drawImage(path, 0.93*inch, 3.22*inch, 21*mm,  21*mm, mask=[240, 255, 240, 255, 240, 255])  # Logo
    c.rect(0, 10*mm, pageWidth, 15*mm, stroke = 0, fill = 1)  ## Location Int 
    
    #c.line(0,  2.98*inch, pageWidth, 2.98*inch )
    
    if type == 1: 
        Label2(c, ws)
    elif type == 2: 
        AssetLabel(c, ws)

    
    c.showPage()
    c.save()




#   Creating lables

# for index, ws in data.iterrows(): 
#   createPDF_v2(index, ws, 1)


for index, ws in assets.iterrows(): 
  createPDF_v2(index, ws, 2)


# ws = assets.iloc[110]
# createPDF_v2(0, ws, 2)
