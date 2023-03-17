#입출력 예
# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5, 3, 2, 7, 5]
# result = "TCMA"



def solution(survey, choices):
    arr ={"R":0, "T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    result = ""
    
    for i,j in zip(survey, choices) :
        if j < 4 :
            arr[i[0]] += (4 - j)
        elif j > 4 :
            arr[i[1]] += (j - 4)
            
    arr2 = list(arr.items())

    for i in range(0,len(arr2),2) :
        if arr2[i+1][1] > arr2[i][1] :
            result += arr2[i+1][0]
        else :
            result += arr2[i][0]

    return result
