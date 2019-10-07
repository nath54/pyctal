#coding:utf-8
import os,time,cv2
from PIL import Image

path_img="images/"
nbc=5


if not "images" in os.listdir("./"): os.mkdir("images/")
for o in os.listdir("images/"):
    os.remove("images/"+o)


def methode1(x1,x2,y1,y2,iteration_max,itx,ity):
    t1=time.time()
    image_x=itx
    image_y=ity
    zoom_x = image_x/(x2 - x1)
    zoom_y = image_y/(y2 - y1)
    img=Image.new("RGB",[itx,ity])
    im=img.load()
    for x  in range(0,image_x,1):
        for y  in range(0,image_y,1):
            c_r = x / zoom_x + x1
            c_i = y / zoom_y + y1
            z_r = 0
            z_i = 0
            i = 0
    
            while z_r*z_r + z_i*z_i < 4 and i < iteration_max:
                tmp = z_r
                z_r = z_r*z_r - z_i*z_i + c_r
                z_i = 2*z_i*tmp + c_i
                i = i+1
                
            if i/iteration_max <= 0.2:
                vc=int(i/iteration_max*255)
                im[x,y]=(0,vc,0)
            elif i/iteration_max <= 0.4:
                vc=int(i/iteration_max*255)
                im[x,y]=(0,int(vc/2),int(vc/2))
            elif i/iteration_max <= 0.6:
                vc=int(i/iteration_max*255)
                im[x,y]=(0,0,vc)
            elif i/iteration_max <= 0.8:
                vc=int(i/iteration_max*255)
                im[x,y]=(int(vc/2),0,int(vc/2))
            elif i < iteration_max:
                vc=int(i/iteration_max*255)
                im[x,y]=(vc,0,0)
            else:
                im[x,y]=(0,0,0)
    nn=str(len(os.listdir("images/")))
    for x in range(nbc-len(nn)): nn="0"+nn
    nm="images/fractal"+nn+".png"
    img.save(nm)
    tt=(time.time()-t1)
    print("Fait en "+str(tt)+" secondes")
    return tt


tex,tey=1024,1024
x,y=-0.10,0.9063
n=0
n1,n2=10000,1000000
pas=10000
ratio=700000
nt=(n2-n1)/pas
for w in range(n1,n2,pas)[::-1]:
    n+=1
    print("\nIMAGE "+str(n)+"/"+str(nt))
    www=w/ratio
    ww=www
    x1=x-ww
    x2=x+ww
    y1=y-ww
    y2=y+ww
    itmax=200
    tt=methode1(x1,x2,y1,y2,itmax,tex,tey)
    ttt=tt*(nt-n)*1.5
    txt="temps restant : environ "
    if ttt >= 3600:
        txt+=str(int(ttt//3600))+" heures "
        ttt=ttt%3600
    if ttt >= 60:
        txt+=str(int(ttt//60))+" minutes "
        ttt=ttt%60
    if tt >= 1:
        txt+=str(int(ttt//1))+" secondes "
        ttt=ttt%1
    txt+=str(int(ttt*1000))+" milisecondes"
    print(txt)

fps=24
print('Création de la vidéo')
liste=sorted(os.listdir(path_img))
frame=cv2.imread(path_img+liste[0])
h,l,c=frame.shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videos/fractal'+str(len(os.listdir("videos/")))+'.avi',fourcc, fps, (l,h))
for i in range(len(liste)):
	frame=cv2.imread(path_img+liste[i])
	out.write(frame)
print('vidéo créée')
out.release()

os.system("dir")
os.system("git add *")
os.system("git commit -m 'aaaa'")
os.system("git push")

