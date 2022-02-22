print("1. To find the area and volume of cube")
print("2.To find the area and volume of sphere")
print("3.To find the area and volume of cylinder")
print("4.To exit")
import geometry as g
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        side=int(input("Enter the side of cube:"))
        print("Surface area of cube is ",g.cubearea(side))
        print("Volume of cube is ",g.cubevol(side))
    elif ch==2:
        rad=int(input("Enter the radius:"))
        print("Surface area of sphere is ",g.sph_area(rad))
        print("Volume of sphere is ",g.sph_vol(rad))
    elif ch==3:
        rad=int(input("Enter the radius of cylinder:"))
        h=int(input("Enter the height of cylinder:"))
        print("Surface area of cylinder is ",g.cyl_area(rad,h))
        print("Volume of cylinder is ",g.cyl_vol(rad,h))
    elif ch==4:
        print("bye")
        break
    else:
        print("invalid choice")

