import json
def main(a,j):
    print("j value in rating is",j)
    with open("joy.json", 'r') as f:
        score1 = json.load(f)
            

    with open("anger.json", 'r') as f:
        score2 = json.load(f)
        
    with open("neutral.json", 'r') as f:
        score3 = json.load(f)
            

    with open("fear.json", 'r') as f:
        score4 = json.load(f)
        
    with open("sadness.json", 'r') as f:
        score5 = json.load(f)
        

    if a==0:
        score1[j-1]=score1[j-1]+1
        with open('joy.json', 'w') as f:
                json.dump(score1, f)
    elif a==1:
        score2[j-1]=score2[j-1]+1
        with open('anger.json', 'w') as f:
               json.dump(score2, f)
    elif a==2:
        score3[j-1]=score3[j-1]+1
        with open('neutral.json', 'w') as f:
               json.dump(score3, f)
    elif a==3:
        score4[j-1]=score4[j-1]+1
        with open('fear.json', 'w') as f:
               json.dump(score4, f)
    elif a==4:
        score5[j-1]=score5[j-1]+1
        with open('sadness.json', 'w') as f:
               json.dump(score5, f)