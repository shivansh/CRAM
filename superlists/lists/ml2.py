from sklearn.neighbors import NearestNeighbors
import csv
from numpy import genfromtxt
import numpy as np

dat_mat_3 = genfromtxt('lists/dat_3.csv', delimiter=',')
dat_mat_4 = genfromtxt('lists/dat_4.csv', delimiter=',')
dat_mat_5 = genfromtxt('lists/dat_5.csv', delimiter=',')
dat_mat_6 = genfromtxt('lists/dat_6.csv', delimiter=',')
dat_mat_7 = genfromtxt('lists/dat_7.csv', delimiter=',')
dat_mat_8 = genfromtxt('lists/dat_8.csv', delimiter=',')
with open('lists/crvocab.csv', 'r') as f:
    voc = list(csv.reader(f))
##load all the data files
##querry is the binary vector of the courses done by th guy whose roll no. has been entered
def find_neighbr(querry,roll_no,neighbours):
    if ((roll_no>14000) & (roll_no<15000)):
        nbrs_5 = NearestNeighbors(n_neighbors=neighbours, algorithm='auto').fit(dat_mat_5)
        distances_5, indices_5 = nbrs_5.kneighbors(querry)
        return indices_5
    elif ((roll_no>150000) & (roll_no<151000)):
        nbrs_3 = NearestNeighbors(n_neighbors=neighbours, algorithm='auto').fit(dat_mat_3)
        distances_3, indices_3 = nbrs_3.kneighbors(querry)
        return indices_3
    elif ((roll_no>13000) & (roll_no<14000)):
        nbrs = NearestNeighbors(n_neighbors=neighbours, algorithm='auto').fit(dat_mat_7)
        distances, indices = nbrs.kneighbors(querry)
        return indices

def predict_courses(querry,roll_no,neighbours):
    if ((roll_no>14000) & (roll_no<15000)):
        indice=find_neighbr(querry,roll_no,neighbours)
        course_vec=dat_mat_6[indice[0,:],:]-dat_mat_5[indice[0,:],:]
    elif ((roll_no>150000) & (roll_no<151000)):
        indice=find_neighbr(querry,roll_no,neighbours)
        course_vec=dat_mat_4[indice[0,:],:]-dat_mat_3[indice[0,:],:]
    elif ((roll_no>13000)&(roll_no<14000)):
        indice=find_neighbr(querry,roll_no,neighbours)
        course_vec=dat_mat_8[indice[0,:],:]-dat_mat_7[indice[0,:],:]
    return course_vec


def kmfunc(licrs,roll_no,neighbours):
    onehot = np.zeros((786, ))
    for course in licrs:
        for i in range(786):
            if(voc[i][0] == course):
                onehot[i] = 1
                break

    # querry=dat_mat_3[251, :]
    querry = onehot
    reco= list()
    ml =  predict_courses(querry,roll_no,neighbours)
    print(ml)
    for i in range(neighbours):
        xxx = list()
        for j in range(786):
            if ml[i,j] == 1:
                xxx.append(voc[j][0])
        reco.append(xxx)
    y = list()

    for launda in reco:
        for course in launda:
            if course not in y:
                y.append(course)
    return y
