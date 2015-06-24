#Cristina Chu & Kaiwen Lv
#cchu43
#902853856
#klv6@gatech.edu
#902828316
#"We worked on the homework assignment alone, using only this semester's course materials."




from myro import *
init()


def findYellowWall():
    p = takePicture()
    total=0
    yellow=0
    for pix in getPixels(p):
        r = getRed(pix)
        g = getGreen(pix)
        b = getBlue(pix)
        total=total+1

        if r > 200 and g > 200 and b < 150:
            yellow=yellow+1

    pct=(float(yellow)/total)*100
    
    if pct<3.0:
        turnRight(1,.3)
        findYellowWall()
    else:
        l,c,r = getObstacle()
	d = (l+c+r)/3
	while d<900:
		translate(1)
		l,c,r=getObstacle()
		d = (l+c+r)/3
	stop()    

        beep(2,1100)
        backward(.5,.5)
        rotate(1)
        beep(3,800,801)
        rotate(-1)
        beep(3,700,701)
        stop()

findYellowWall()
stop()
                

            
        
        
