with open("file/log.txt","r") as f:
    
    lines=f.readlines()
    linen =1
    for line in lines:
        if "python" in line:
            print(f"python found in line {linen}")
            break
        linen+=1
    else:
         print("python not found")
        
            
       