testcase=int(input())

for i in range(testcase):
    
    len_of_col=[]
    for col in range(2):
        lens=int(input())
        len_of_col.append(lens)
    c={}
    def create_scores(leng):
        scores=[]    
        for k in range(leng):
            score=int(input())
            scores.append(score)
        return scores


    c['C1']=sum(create_scores(len_of_col[0]))
    c['C2']=sum(create_scores(len_of_col[1]))
    
    colmax= max(c,key=c.get)
    print(colmax)
