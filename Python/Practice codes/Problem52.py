with open ("lod.txt","r") as f :
    s = f.read() 

with open ("lod_copy.txt" , "w" ) as f :
    f.write(s)