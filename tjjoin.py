import base64,os
d=[]
for i in range(1,9):
    f=open(f"/data/data/com.termux/files/home/.tj{i}.txt")
    d.append(f.read().replace("\n",""))
    f.close()
html=base64.b64decode("".join(d))
out=open("/data/data/com.termux/files/home/tj2/index.html","wb")
out.write(html)
out.close()
for i in range(1,9):
    os.remove(f"/data/data/com.termux/files/home/.tj{i}.txt")
print("PRONTO ticiajeans!")
