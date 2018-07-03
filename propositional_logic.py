'''
Created on May 16, 2017
@author: Sneha Mule
'''

saveInfo=[]
def tell(input):
    if(str(input[0]).lower().strip()=='implies'):
            saveInfo.append(["or", ["not", input[1]], input[2]])
    elif(str(input[0]).lower().strip()=='biconditional'):
        TELL(["implies",input[1], input[2]])
        TELL(["implies",input[2], input[1]])
    else:    
        saveInfo.append(input)

        
def resolve(newListOne,newListTwo):
    newListOne=(str(newListOne).replace('[','' ).replace(']', '').replace("'",'')).split(",")
    newListTwo=(str(newListTwo).replace('[','' ).replace(']','').replace("'",'')).split(",")
    newListOne=[x.strip() for x in newListOne if x.strip()]
    newListTwo=[x.strip() for x in newListTwo if x.strip()]
    flag=False
    loopCount=0
    for i in newListOne[:]:
        if(str(i).lower().strip()=="or"):
            continue
        for j in newListTwo[:]:
            if(str(i).strip() == str(j).strip()):
                flag=True
                if(str(newListTwo[newListTwo.index(j)-1].lower()).strip()=="not"):
                    loopCount+=1
                    del newListOne[newListOne.index(i)]
                    del newListTwo[newListTwo.index(j)-1]
                    del newListTwo[newListTwo.index(j)]
                    continue
                if(str(newListOne[newListOne.index(i)-1].lower()).strip()=="not"):
                    loopCount+=1
                    del newListOne[newListOne.index(i)-1]
                    del newListOne[newListOne.index(i)]
                    del newListTwo[newListTwo.index(j)]
                    continue
    if((len(newListTwo)==1 or len(newListTwo)== 2) and str(newListTwo[0]).lower().strip()=='or'):
        del newListTwo[0]
    if((len(newListOne)==1 or  len(newListOne)== 2) and str(newListOne[0]).lower().strip()=='or'):
        del newListOne[0]
    resultingStr=''       
    if(flag!=False and loopCount<=1):
        if (len(newListOne)==0):
            if(len(newListOne)==1):
                resultingStr=str(newListTwo)[2:-2]
                resultingStr=resultingStr.strip()
            else:
                resultingStr=str(newListTwo)
        elif(len(newListTwo)==0):
            if(len(newListOne)==1):
                resultingStr=str(newListOne)[2:-2]
                resultingStr=resultingStr.strip()
            else:
                resultingStr=str(newListOne)
        else:
            result = newListOne + [i for i in newListTwo if i not in newListOne] 
            resultingStr=str(result)
        return resultingStr
    else:
        return False
    
    
def ask(input):
    saveInfoList=list(saveInfo)
    flag= True
    if((input[0]).lower().strip()!='implies'):
        if(str(input[0]).strip()=='not'):
                saveInfoList.append([input[0]])
        else:    
            saveInfoList.append(["not",input])
            
    if(str(input[0]).lower().strip()=='implies' or str(input[0]).lower().strip()=='biconditional') :
        if(str(input[0]).lower().strip()=='implies'):
            answer=ASK(input[1])
            if(answer==False):
                return True
            else:
                print('input[2]',input[2])
                answer=ASK(input[2])
                if(answer==False):
                    return True
                else:
                    return False
        if (str(input[0]).lower().strip()=='biconditional'):
            answer=ASK(["implies", input[1], input[2]])
            if(answer==False):
                return True
            else:
                answer=ASK(["implies", input[2], input[1]])
                if(answer==False):
                    return True
                else:
                    return False
        
            
    outputList=[saveInfoList[0]]
    while(outputList and flag==True ):
        firstNode=outputList.pop()
        for i in range (len(saveInfoList)-1):
            loopCount=0
            result=resolve(firstNode,saveInfoList[i+1])
            resultList=str(result).replace('[','' ).replace(']', '').replace("'",'').split(",")
            if(str(resultList[0]).strip()!='False'):
                outputList.append(str(result))
                del saveInfoList[saveInfoList.index(saveInfoList[i+1])]
                loopCount=loopCount+1
                if(loopCount == 0):
                    del saveInfoList[saveInfoList.index(firstNode)]
                break;
            else:
                if(saveInfoList[len(saveInfoList)-1]==saveInfoList[i+1]):
                    outputList.append(str(result))
                    flag = False
            break
    if(len(outputList)==0):
        return True
    else:
        return False

   
def clear():
    del saveInfo[:]


 
