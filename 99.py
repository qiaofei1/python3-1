for i in range(1,10):
    string = '';
    for j in range(1,10):
        if j<=i:
            string += str(j)+'X'+str(i)+'='+str(i*j)+' '
    print(string)
