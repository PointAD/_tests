##This Program Start Or Stop Services By Their Name Using Inputs From User
while True : 
    import subprocess
    ## Gets Input From User
    args = ['sc' , str(input("Start Or Stop : ")) , str(input("Enter Service Name : "))]
    result = subprocess.run(args)
    