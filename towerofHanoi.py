def towersofHanoi(n,src,dest,temp):
    if n==0:
        return
    towersofHanoi(n-1,src,temp,dest)
    print("Disk",n,"from",src,"to",dest)
    towersofHanoi(n-1,temp,dest,src)




if __name__ == "__main__":
    #n = int(input())
    towersofHanoi(3,'A','c','B')