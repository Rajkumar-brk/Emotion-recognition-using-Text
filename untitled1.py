import json
def main():

    with open("pr.json", 'r') as f:
        score = json.load(f)
            
    pr = score
    with open("nr.json", 'r') as f:
        score = json.load(f)
    
    nr = score
    
    print(nr)
    print(pr)
