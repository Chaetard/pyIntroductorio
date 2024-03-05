
for i  in range(20):
        var = i + 1
        print(var, end="")
        print("||",end="")
        print(var*var, end="")
        print("||",end="")
        if i + 1 <= 10:
            print(var*var*var, end="")
        else:
            print("num no val", end = "")
            
        print()
    
   