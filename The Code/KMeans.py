import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

#Choose random number from the dataset
def init_cen(X,k):
    
    centroids = np.zeros(  ( k ,  X.shape[1] )   )
    ids = np.random.randint(0, X.shape[0], k )
    
    for i in range(k):
        centroids[i,:] = X[ ids[i] ,:]
    
    return centroids
    


#Assign every point to it's nearest centroid
def find_closest_centroid(X,centroids):
    
    centroid_for_each = np.zeros( X.shape[0]  )
    
    for i in range( X.shape[0]  ):
        
        min_dist = 500000
        
        for h in range( centroids.shape[0] ):
            
            dist = np.sum(  ( X[i,:] - centroids[h,:] ) **2  )
            print('Before')
            print(X[i,:])
            if dist < min_dist:
                min_dist = dist
                centroid_for_each[i] = h
        print('After')
        print(X[i,:])
                
                
        
    return centroid_for_each
    


def compute_centroids(X , centroid_for_each , k ):
    
   centroids = np.zeros(   (  k, X.shape[1]   )  ) 
   
   for i in range( k ):
       onlyOneCentroid = np.where(centroid_for_each == i)
       
       centroids[i,:] = np.sum( X[onlyOneCentroid,:] , axis = 1) / len(onlyOneCentroid[0].ravel()) 
       
       
   return centroids    
    
    
    

    
    



data = loadmat(r'C:\Users\NADY\Desktop\DataS.mat')
print(data['X'].shape)


k = 3
initial_centroids = init_cen(data['X'],k)
print(initial_centroids)


c = find_closest_centroid(data['X'], initial_centroids)


o = compute_centroids(data['X'], c, k)
print('=====\n NEW')
print(o)




iters = 1
for q in range(iters):
    centroid_for_each = find_closest_centroid(data['X'], initial_centroids)
    initial_centroids = compute_centroids(data['X'], centroid_for_each, k)
    
    cluster1 = data['X'][np.where(centroid_for_each == 0)[0],:]
    cluster2 = data['X'][np.where(centroid_for_each == 1)[0],:]
    cluster3 = data['X'][np.where(centroid_for_each == 2)[0],:]
    
    fig, ax = plt.subplots(figsize=(9,6))
    ax.scatter(cluster1[:,0], cluster1[:,1], s=10, color='r', label='Cluster 1')
    ax.scatter(initial_centroids[0,0],initial_centroids[0,1],s=500,marker = '^' ,  color='r')
    
    ax.scatter(cluster2[:,0], cluster2[:,1], s=10, color='g', label='Cluster 2')
    ax.scatter(initial_centroids[1,0],initial_centroids[1,1],s=500, color='g')
    
    ax.scatter(cluster3[:,0], cluster3[:,1], s=10, color='b', label='Cluster 3')
    ax.scatter(initial_centroids[2,0],initial_centroids[2,1],s=500,marker = 's' , color='b')
    
    ax.legend()

    
    
    
    
    







