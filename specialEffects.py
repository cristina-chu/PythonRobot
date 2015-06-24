## special effect hw
## Kaiwen Lv, klv6@gatech.edu, 902828316
## Cristina Chu,

def showPicture(alist): #to show series of pictures 
    for i in alist:
        show(i)
        wait(0.2)

#Special Effects     
     
def seeRed():
    pic=takePicture()
    show(pic)
    for pix in getPixels(pic):
        avg=(getRed(pix)+getGreen(pix)+getBlue(pix))/3
        setRed(pix,avg)
        setGreen(pix,0)
        setBlue(pix,0)
    show(pic)
    savePicture(pic,"SeeingRed.gif")

def RobotZoom():
    picture=[]
    for i in range(8):
        P=takePicture()
        picture.append(P)
        forward(.5,.3)
    showPicture(picture)
    savePicture(picture,"RobotZoomIn.gif")

def a360view():
    picture= []
    rotate(0.3)
    while timeRemaining(12.6):
        p=takePicture()
        
        picture.append(p)

    stop()
    showPicture(picture)
    
    savePicture(picture,"360view.gif")

def TempoChange():
         alist=[]
	 for i in range(0,5):
		 P=takePicture()
                 show(P)
                 P2=copyPicture(P)
		 alist.append(P2)
		 turnLeft(1,0.2)
		 wait(0.1)
	 blist=alist[::-1]
         wait(1.5)
	 for item in alist:
		 show(item)
		 wait(1.5)
	 clist=alist+blist
	 savePicture(clist,"TempoChange.gif") 

def screenShake1(aNum): #shaking robot to make scene shake
    pictures = []

    while timeRemaining(aNum):
        p = takePicture()
        pictures.append(p)
        turnLeft(.2)

        p=takePicture()
        pictures.append(p)
        turnRight(.2)

    stop()
    savePicture(pictures,"shake.gif")

def screenShake2(): #shaking one picture
    p=takePicture()
    pic = copyPicture(p)
    win = GraphWin("Shake", 550,500)
    pixmap = makePixmap(pic)
    point1 = Point(275,250)
    image = Image(point1,pixmap)
    image.draw(win)
    while timeRemaining(5):
        image.move(20,0)
        wait(0.1)
        image.move(-40,0)
        wait(0.1)
        image.move(20,0)
    savePicture(pic, "screenShake.gif")

def greenScreen(scene): #loading scene, taking picture of new background
    p1 = takePicture()
    p2 = loadPicture(scene)

    h = getHeight(p1)
    w = getWidth(p1)

    for x in range(w):
        for y in range (h):
            pix1 = getPixel(p1,x,y)
            pix2 = getPixel(p2,x,y)

            if getRed(pix2)<110 and getBlue(pix2)<110 and getGreen(pix2)>100:
                setRed(pix2,getRed(pix1))
                setGreen(pix2,getGreen(pix1))
                setBlue(pix2,getBlue(pix1))
    savePicture(p2, "GreenScreen.gif")

def fade():
    pic=loadPicture("rca3.gif")
    copy=copyPicture(pic)
    newpic=loadPicture("rca1.gif")
    newcopy=copyPicture(pic)
    alist=[]
    alist.append(pic)
    for n in range(9):
        copy=copyPicture(copy)
        newcopy=copyPicture(newpic)
        
        for pix in getPixels(copy):
            for pix2 in getPixels(newcopy):
                
                setRed(pix,getRed(pix)*0.7+(getRed(pix2)*(9-n)))
                setGreen(pix,getGreen(pix)*0.7+(getGreen(pix2)*(9-n)))
                setBlue(pix,getBlue(pix)*0.7+(getBlue(pix2)*(9-n)))
        alist.append(copy)
        
    copy2=copyPicture(newcopy)
    
    alist.append(newpic)
    savePicture(alist,"fade.gif")
    return alist

####


def crossFade(picture1,picture2):
    P1=loadPicture(picture1)
    P2=loadPicture(picture2)
    P3=copyPicture(P1)

    num=0
    aList=[P1]
    show(P1)

    for item in range(5):
        num=num+0.2
        P3=copyPicture(P3)
        for a in range(0,getWidth(P3)):
            for b in range(0,getHeight(P3)):
                pix1=getPixel(P1,a,b)
            
                pix2=getPixel(P2,a,b)
                pix3=getPixel(P3,a,b)
                r1=getRed(pix1)
                g1=getGreen(pix1)
                b1=getBlue(pix1)
                
                r2=getRed(pix2)
                g2=getGreen(pix2)
                b2=getBlue(pix2)
                value1=r2*num+r1*(1-num)
                value2=g2*num+g1*(1-num)
                value3=b2*num+b1*(1-num)
                
            
                setRed(pix3,value1)
                setGreen(pix3,value2)
                setBlue(pix3,value3)
        aList.append(P3)   
                
        show(P3)
    
        
        wait(0.2)
    savePicture(aList,"crossfade.gif")
      
