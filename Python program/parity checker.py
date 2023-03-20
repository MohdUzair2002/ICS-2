def messagepackets(Bits):
    listofbits=list(Bits)
    i=0
    Noofparitybits=5
    hammingbitsindex=[]
    returninglist=[]
    while (i<Noofparitybits):
        positionofhammingbit=(2**i)-1
        hammingbitsindex.append(positionofhammingbit)
        listofbits.insert(positionofhammingbit, 'h')
        i+=1
    print(listofbits)
    meassagepackets= ','. join(listofbits)
    print(meassagepackets)
    returninglist.append(meassagepackets)
    returninglist.append(hammingbitsindex)
    return returninglist
def parityverifying (Bits):
    ##    messagepackets (Bits)
    Bits='10011101010011'
    ##listofbits=['h', 'h', '1', 'h', '0', '0', '1', 'h', '1', '1', '0', '1', '0', '1', '0', 'h', '0', '1', '1']
    ##    meassagepackets=returninglist[0]
    ##    hammingbitsindex=returninglist[1]
    hammingbitswithparticularbits=[]
    hammingbitsindex=[0,1,3,7,15]
    meassagepackets=['h', 'h', '1', 'h', '0', '0', '1', 'h', '1', '1', '0', '1', '0', '1', '0', 'h', '0', '1', '1']
    j=0
    lengthofhammingbitsindex=len(hammingbitsindex)
    while(j<lengthofhammingbitsindex):
        z=0
        bitsofparticularhammingbit=[]
        listofbits=list(Bits)
        while(z<len(Bits)+1):
            if z==0:
                hammingbitnumber=(f"h{j+1}")
                listofbits.insert(j, hammingbitnumber)
                z=j
    ##            bitsofparticularhammingbit2=int(hammingbitsindex[z])
    ##            bitsofparticularhammingbit3=(bitsofparticularhammingbit2)
            
            noofdigitstobeskip=(int(hammingbitsindex[j]))+1
            bitsofparticularhammingbit1=listofbits[z:z+noofdigitstobeskip]
            bitsofparticularhammingbit.append(bitsofparticularhammingbit1)
            z+=(noofdigitstobeskip+1)
            combinigtoonelist=sum(bitsofparticularhammingbit,[])
        hammingbitswithparticularbits.append(combinigtoonelist)    
##        print(combinigtoonelist)
        j+=1
    print (hammingbitswithparticularbits)
    return hammingbitswithparticularbits
def parityschemechecker (hammingbitswithparticularbits,parityschemetype):            
    h=[['h1', '0', '1', '1', '1', '1', '0', '1'], ['h2', '0', '1', '1', '0', '1', '1', '0', '1', '1'], ['h3', '0', '1', '1', '0', '1', '0', '1', '0', '1', '1'], ['h4', '1', '1', '1', '0', '1', '0', '1', '0', '1', '1'], ['h5', '1', '1', '0', '1', '0', '1', '0', '0', '1', '1']]
##    hammngbitquantity=5
##    parityschemetype='odd'
    i=0
    while(i<hammngbitquantity):
        j=1
        listofoneinlist=[]
        lengthofparticularhammingbits=len(h[i])
        while(j<lengthofparticularhammingbits):
            elementofparticularhammingbitslist=h[i][j]
            intofelementofparticularhammingbitslist=int(elementofparticularhammingbitslist)
            if(intofelementofparticularhammingbitslist==1):
                listofoneinlist.append(intofelementofparticularhammingbitslist)
            else:
                k=0
            j+=1
        countofones=len(listofoneinlist)
        if(parityschemetype=='odd'):
             countofones1=countofones%2
             if countofones1==0:
                 h[i][0]=1
             else:
                 h[i][0]=0
        if(parityschemetype=='even'):
             countofones2=countofones%2
             if countofones2==0:
                 h[i][0]=0
             else:
                 h[i][0]=1
        print(h[i])
        i+=1
    print(h)          
Bits='10011101010011'
messagepackets(Bits)
parityverifying (Bits)
parityschemechecker(5,'odd')
