#Cristina Chu
#cchu43@gatech.edu
#902853856
#"I worked on the homework assignment alone, using only this semester's course materials."


from myro import *
init()

#Part 1
light = []

n = 0
for i in range(9):
    turnLeft(1,.2)

    pic = takePicture()
    savePicture(pic, 'pic'+str(n)+'.gif')
    n = n+1

    a,b,c = getLight()
    average = (a+b+c)/3.0
    light.append(average)


#Part 2
f = open("myPage.html", 'w')

text1 = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title> Picture Time! </title></head>
<body>
<h1> Welcome to the Amazing Photograph Page! </h1>
<p>Made by Cristina Chu</p>

<p></p>

<table>
    <tr>
        <td><p><img src="pic0.gif" alt="Robot Pic 0"/></p>
            <p>%.3f</p></td>
        <td><p><img src="pic1.gif" alt="Robot Pic 1"/></p>
            <p>%.3f</p></td>
        <td><p><img src="pic2.gif" alt="Robot Pic 2"/></p>
            <p>%.3f</p></td>
    </tr>

    <tr>
        <td><p><img src="pic3.gif" alt="Robot Pic 3"/></p>
            <p>%.3f</p></td>
        <td><p><img src="pic4.gif" alt="Robot Pic 4"/></p>
            <p>%.3f</p></td>
        <td><p><img src="pic5.gif" alt="Robot Pic 5"/></p>
            <p>%.3f</p></td>
    </tr>

    <tr>
        <td><p><img src="pic6.gif" alt="Robot Pic 6"/></p>
            <p>%.3f</p></td>
        <td><p><img src="pic7.gif" alt="Robot Pic 7"/></p>
            <p>%.3f</p></td>
        <td><p><img src="pic8.gif" alt="Robot Pic 8"/></p>
            <p>%.3f</p></td>
    </tr>


</table>

<p></p>

<p> Pictures taken by %s </p>
</body>
</html>""" %(light[0],light[1],light[2],light[3],light[4],light[5],light[6],light[7],light[8],getName())


f.write(text1)
f.close()

f = open('myPage.html', 'r')
