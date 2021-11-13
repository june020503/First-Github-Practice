from string import *

def preprocess(inFName,outFName,startTag,lastTag):
    #소설책 데이터 전처리
    #구두점 제거를 위한 map table 생성
    map_dict={}
    for ch in punctuation:
        map_dict[ch]=''
    map_dict['-']=' '
    map_dict['!']='.'
    map_dict['?']='.'
    map_dict['.']='.'
    map_dict['“']=''
    map_dict['”']=''
    table=str.maketrans(map_dict)

    #목차 제거를 위한 배열
    num=['','i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv']
    
    f_r=open(inFName, 'r', encoding="utf-8")
    f_w=open(outFName, 'w', encoding="utf-8")

    #텍스트의 본문만 추출
    sent=""
    for line in f_r:
        if line.startswith(startTag):
            break

    for line in f_r:
        if line.startswith(lastTag):
            break

        line=line.lower()
        
        p=line.find("'s")
        if p!=-1 and line[p-1]!=" ":
            line=line.replace("'s","")

        line=line.replace("mr.", "mr")
        line=line.replace("mrs.", "mrs")

        line=line.translate(table)
        
        #온점을 기준으로 문장 구분
        idx=line.find(".")
        while idx!=-1:
            sent+=line[:idx]
            sent+=" ."
            line=line[idx+1:].strip()
            idx=line.find(".")            
            f_w.write(sent+"\n")
            sent=""

        if line.replace('\n','') not in num:
            sent+=line.replace('\n','')+' '

    f_r.close()
    f_w.close()

def countBigrams(inFName):
    #소설책에 등장하는 bigram 수집
    f_r=open(inFName, 'r', encoding="utf-8")

    bigrams={}
    
    for line in f_r:
        L=line.split()
        for i in range(len(L)-1):
            if i==0:
                b='<s>'+' '+L[i]
            elif i==len(L)-2:
                b=L[i]+' '+'</s>'
            else:
                b=L[i]+' '+L[i+1]

            bigrams[b]=bigrams.get(b,0)+1

    f_r.close()

    return bigrams

def my_sort(list):
    #merge sort를 이용해 구현한 내림차순 정렬 함수_1
    if len(list) <= 1:
        return list
    
    mid = len(list)//2
    
    leftList = list[:mid]
    rightList = list[mid:]
    
    leftList = my_sort(leftList)
    rightList = my_sort(rightList)
    
    return merge(leftList, rightList)

def merge(left, right):
    #merge sort를 이용해 구현한 내림차순 정렬 함수_2
    result = []
    
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
                
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
            
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
            
    return result

def sortBigrams(bDict):
    #사전을 내림차순으로 정렬, (사용횟수, 단어)의 리스트 반환
    bList=[]
    for key, val in bDict.items():
        bList.append((val,key))
        
    return my_sort(bList)

def outBigramsStat(bDict):
    #학습한 bigram LM의 통계를 출력
    bList=sortBigrams(bDict)

    print(f"사용된 Bigram의 개수 : {len(bList):,}\n")
    print(f"Bigram 별 사용회수 (내림차순)")
    for i in range(int(len(bList)*0.01)):
        print(f"{bList[i][1]:<20}{bList[i][0]:>5,}")

def outShannonVisualization(bDict, fName):
    #Shannon Visualization 결과를 출력
    bList=sortBigrams(bDict)
    bLM=[]
    for i in range(len(bList)):
        bLM.append(bList[i][1].split()[0])
        
    result=[]
    result.append(bList[0][1].split()[1])

    i=0
    while '</s>' not in result:
        word=result[i]
        j=bLM.index(word)
        result.append(bList[j][1].split()[1])
        
        i+=1

    SV=""
    for k in range(len(result)):
        SV+=result[k]
        SV+=' '

    SV=SV.capitalize()
    SV=SV.replace('</s>','')
    print(f"\n{inFName}의 Shannon Visualization:")
    print(SV)


inFName="Little_Lord_Fauntleroy.txt"
startTag="By Frances"
lastTag="End of Project"
preprocessed="preprocessed_Little_Lord_Fauntleroy.txt"

print(f"전자서적 이름: {inFName}\n")

#Preprocessing
preprocess(inFName,preprocessed,startTag,lastTag)

#Bigram Count
bi_gram=countBigrams(preprocessed)
outBigramsStat(bi_gram)

#Shannon Visualization
outShannonVisualization(bi_gram, inFName)
