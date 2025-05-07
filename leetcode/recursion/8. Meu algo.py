#funcao que retorna o valor de uma variavel ou lista da memoria

memory = {'lista': [0, 0, 0, 0, 0, 'NICE', 0, 0], 'index1': [0, 0, 0, 5, 0, 0, 0, 0], 'index2': 3, 'bosta': 'NICE'}

def getvalue(var):#Obter o valor de uma variavel
    if var[-1] == ">":
        for i, char in enumerate(var):
            if char == "<":
                try:
                    index = int(var[i+1:-1])
                except:
                    if var[i+1:-1][0] == "@":
                        index = int(getvalue(var[i+2:-1]))
                list = var[:i]
                return(memory[list][index])
    else:
        try:
            return(memory[var])
        except:
            return("nao há")
        
print(getvalue("lista<@index1<@index2>>"))