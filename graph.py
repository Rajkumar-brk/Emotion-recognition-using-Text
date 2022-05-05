import numpy as np 
import matplotlib.pyplot as plt 

def main(data):
# creating the dataset
    #data = {'C':20, 'C++':15, 'Java':30,
            #'Python':35}
    courses = list(data.keys())
    values = list(data.values())
      
    fig = plt.figure(figsize = (6, 4))
     
    # creating the bar plot
    plt.bar(courses, values, color ='green',
            width = 0.2)
     
    plt.xlabel("Review Emotion")
    plt.ylabel("No of reviews")
    plt.title("total reviews for the movie")
   # plt.show()
    plt.savefig('user/static/graph.png')
    
#main([1,1,1,1,1,1,1,1],[2,1,0,0,0,0,0,0])