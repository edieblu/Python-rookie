def computepay(h,r):
    if h > 40:
        x=h-10
        total= (40*r)+(1.5*r*x)
 
        
    else:
        total= 40*r

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_intpu ("Enter Rate:")
r = float (rate)

p = computepay(h,r)
p

    
 
