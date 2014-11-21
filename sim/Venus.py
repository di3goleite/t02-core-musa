arquivo = open('code.txt' , 'r')

r_type = {'ADD':'000000','SUB':'000000','MUL':'000000','DIV':'000000','AND':'000000','OR':'000000','NOT':'000000','CMP':'000000'}
i_type = {'ADDi':'001000', 'SUBi':'001001', 'ANDi':'001100','ORi':'001101', 'LW':'100011','SW':'101011'}
j_type = {'JR':'111111', 'JPC':'', 'BRFL':'010001', 'CALL':'000011', 'RET':'', 'HALT':'', 'NOP':''}

func = {'ADD':'100000','SUB':'100010','MUL':'011000','DIV':'011010','AND':'100100','OR':'100101','NOT':'100111','CMP':'011011'}
registers = {"$t0":'00000', "$t1":'00001', "$t2":'00010', "$t3":'00011', "$t4":'00100', "$t5":'00101', "$t6":'00110', "$t7":'00111', "$t8":'01000', "$t9":'01001' }



for linha in arquivo:
    linha.replace(","," ")
    linha = linha.split(" ")
    start (linha)


def start(linha):
    lista_r = r_type.keys()
    lista_i = i_type.keys()
    lista_j = j_type.keys()
    if  linha[0] in lista_r :
        print  r_type()
    elif linha[0] in lista_j:
        print  j_type()
    elif linha[0] in lista_i:
        print j_type()
    #TODO ESCREVER NO ARQUIVO


def jtype( linha ):
    bina = bin(int(linha[1]))[2:]
    bina2 = ''

    for i in range(26-len(bina)):                        #Completa com 0 a esquerda o valor do imediato vulgo extensor de sinal
        bina2 = bina2 + '0'

    nova_linha = j_type.get(linha[0]) +bina2+ bina    #OPCODE + 000.. + ENDEREÇO
    return nova_linha

def rtype ( linha ):
    nova_linha = r_type.get(linha[0])                          #OPCODE
    nova_linha = nova_linha + registers.get(linha[1])  #RS
    nova_linha = nova_linha + registers.get(linha[2])  #RT
    nova_linha = nova_linha + registers.get(linha[3])  #RD
    nova_linha = nova_linha + '00000'                       #SHAMT
    nova_linha = nova_linha + func.get(linha[0])        #FUNCT
    return nova_linha

def itype( linha ):
    #TODO
