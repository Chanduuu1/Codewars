def bouncing_ball(h, bounce, window):
    a = 1 #because ek baar th star me hi dikh jaega!
    if h>0 and 1 > bounce > 0 and window < h:
        while(h>0):
            h *= bounce
            
            if h > 1.5:
                a += 2
            elif h == 1.5:
                a += 1
            elif h < 1.5:
                break            
        return a
    else:
        return -1
print(bouncing_ball(10,0.5,1.5))