import turtle
import math
xPos = -180
yPos = -120
penSize = 10
turtle.pensize(penSize)
turtle.ht()
turtle.end_fill()
turtle.goto(xPos,yPos)
turtle.clear()
centerX = 0
centerY = 0
centerZ = 0
sphereX = 0
sphereY = 0
sphereZ = 0
penColorR = 0
penColorG = 0
penColorB = 0
nearest = 10000
rayX = xPos
rayY = yPos
rayZ = 0 - centerZ
centerX = 0
centerY = 0
centerZ = -100

def sphere(x,y,z,radius,r,g,b):
  penColorR = 0
  penColorG = 0
  penColorB = 0
  global nearest
  global centerX
  global centerY
  global centerZ
  sphereX = x - centerX
  sphereY = y - centerY
  sphereZ = z - centerZ
  dot = sphereX * rayX + sphereY * rayY + sphereZ * rayZ
  length = sphereX ** 2 + sphereY ** 2 + sphereZ ** 2
  print("dot: {}".format(dot))
  print("length: {}".format(length))
  if dot > 0 and length - dot ** 2 < radius ** 2:
    near = math.sqrt(abs(radius ** 2 - (length - dot ** 2)))
    print("near: {}".format(near))
    if length > radius ** 2 and dot - near < nearest:
      nearest = dot - near
      penColorR = r
      penColorG = g
      penColorB = b
  return nearest,penColorR,penColorG,penColorB

def calculateDistances():
  #sphere positions
  return sphere(-50,-40,-20,50,0,1,0)

def raytracePoint(x,y):
  #So basically just determines pixel color ig
  rayX = x
  rayY = y
  rayZ = 0 - centerZ
  distance = math.sqrt(rayX ** 2 + rayY ** 2 + rayZ ** 2)
  rayX /= distance
  rayY /= distance
  rayZ /= distance
  print("distance: {}".format(distance))
  nearest = 10000
  nearest,penColorR,penColorG,penColorB = calculateDistances()
  print("nearest: {}".format(nearest))
  if nearest < 10000:
    turtle.color(penColorR,penColorG,penColorB)
  else:
    turtle.color(0,0,0)
  turtle.pendown()

for i in range(round(240 / penSize)):
  xPos = -180
  turtle.setx(xPos)
  for j in range(round(320 / penSize)):
    raytracePoint(xPos,yPos)
    #turtle.pendown()
    xPos += penSize
    turtle.setx(xPos)
    print(xPos, yPos)
  yPos += penSize
  turtle.sety(yPos)
