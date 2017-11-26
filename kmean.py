import random
import math

K = 3
TOTAL_NUMBER_OF_DATA = 150
centroids = []
yeks=[]
dos =[]
ses =[]
chars = []

clusters = []
def load_data():
    input_data = []
    output_data = []
    with open("iris.txt") as file:
        content = file.readlines()
        for line in content:
            line = line.split()
            '''
            yeks.append(line[0])
            dos.append(line[1])
            ses.append(line[2])
            chars.append(line[3])
    '''
            input_data.append([line[0],line[1],line[2],line[3]])
            output_data.append(line[4])
        return (input_data , output_data)

class DataPoint:
    def __init__(self, a , b , c, d ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b
    
    def get_c(self):
        return self.c

    def get_d(self):
        return self.d
    
    def set_cluster(self, clusterNumber):
        self.clusterNumber = clusterNumber
    
    def get_cluster(self):
        return self.clusterNumber


class Centroid:
    def __init__(self, a, b , c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def set_a(self, a):
        self.a = a
    
    def get_a(self):
        return self.a

    def set_b(self, b):
        self.b = b
    def get_b(self):
        return self.b

    def set_c(self, c):
        self.c = c
    def get_c(self):
        return self.c

    def set_d(self, d):
        self.d = d
    def get_d(self):
        return self.d

def initialize_centroids():
    #print("Centroids initialized at:")
    for k in range(K):
        c1 = Centroid(random.uniform(4,8) , random.uniform(1.5,4.5) , random.uniform(0.5,7) ,random.uniform(0,3))
        centroids.append(c1)
        clusters.append(0)
        #print("(" , c1.get_a() , " , " , c1.get_b() , " , " , c1.get_c() , " , " , c1.get_d() , ")")
    return


def get_distance(datapoint , centroid):
    return math.sqrt(math.pow(datapoint.get_a()-centroid.get_a(),2)+ math.pow(datapoint.get_b()-centroid.get_b(),2)+ math.pow(datapoint.get_c()-centroid.get_c(),2)
                     + math.pow(datapoint.get_d()-centroid.get_d(),2))


def calculate_centroids():
    (inputs , outputs) = load_data()
    for i in range(150):
        d = DataPoint(float(inputs[i][0]) , float(inputs[i][1]) , float(inputs[i][2]) ,float(inputs[i][3]))
        #print("data centoid:             (" , d.get_a() , " , " , d.get_b() , " , " , d.get_c() , " , " , d.get_d() , ")")
        distances = []
        for k in range(K):
            distances.append(get_distance(d , centroids[k]))
        #print('distances : ' , distances)
        min_index = distances.index(min(distances))
        #print("centroid number " , min_index , " is selected")
        centroids[min_index].set_a((d.get_a()+ (clusters[min_index]*centroids[min_index].get_a()))/(clusters[min_index]+1))
        centroids[min_index].set_b((d.get_b()+ (clusters[min_index]*centroids[min_index].get_b()))/(clusters[min_index]+1))
        centroids[min_index].set_c((d.get_c()+ (clusters[min_index]*centroids[min_index].get_c()))/(clusters[min_index]+1))
        centroids[min_index].set_d((d.get_d()+ (clusters[min_index]*centroids[min_index].get_d()))/(clusters[min_index]+1))
        clusters[min_index] += 1
        #print("Updated centoid:             (" , centroids[min_index].get_a() , " , " , centroids[min_index].get_b() , " , " , centroids[min_index].get_c() , " , " , centroids[min_index].get_d() , ")")
        #print("point number " , i+1 , 'belongs to class ' , min_index+1)
    return

def show_centroids():
    print("updated centroids : ")
    for c1 in centroids:
        print("(" , c1.get_a() , " , " , c1.get_b() , " , " , c1.get_c() , " , " , c1.get_d() , ")")

def show_results():
    miss_classified_data = 0
    for number in clusters:
        print(number, " data points belong to cluster number ", clusters.index(number)+1)
        if(number - 50 > 0):
            miss_classified_data += number - 50
    print('Accuracy : ' , 100-((miss_classified_data/150.0)*100) , '%')
def calculate_entropy():
    global clusters
    entropy =0
    for number in clusters:
        if number != 0:
            entropy += (number/150.0)*math.log(number/150.0)
    print("Entropy: ",entropy)
def kmean():
    initialize_centroids()
    calculate_centroids()
    #show_centroids()
    show_results()
    calculate_entropy()
kmean()








