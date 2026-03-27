cidade = [
    [1, 0, 2, 0, 1],  
    [0, 9, 2, 1, 3],  
    [1, 0, 1, 9, 2],  
    [9, 3, 0, 2, 1],  
    [0, 1, 2, 0, 9] 
]

for i in range(len(cidade)):
    for n in range(len(cidade)):
        if cidade[i][n] == 2:
            perigo = False

            if i > 0 and cidade[i-1][n] == 9:
                perigo = True
            if i < len(cidade)-1 and cidade[i+1][n] == 9:
                perigo = True
            if n > 0 and cidade[i][n-1] == 9:
                perigo = True
            if n < len(cidade[0])-1 and cidade[i][n+1] == 9:
                perigo = True
            
            if perigo:
                print(f"Hospital em ({i},{n}): esta em perigo")
            else:
                print(f"Hospital em ({i},{n}): esta seguro")