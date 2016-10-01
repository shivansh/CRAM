from sklearn.neighbors import NearestNeighbors
import csv
from numpy import genfromtxt
import numpy as np

dat_mat_3 = genfromtxt('dat_3.csv', delimiter=',')
dat_mat_4 = genfromtxt('dat_4.csv', delimiter=',')
dat_mat_5 = genfromtxt('dat_5.csv', delimiter=',')
dat_mat_6 = genfromtxt('dat_6.csv', delimiter=',')
dat_mat_7 = genfromtxt('dat_7.csv', delimiter=',')
dat_mat_8 = genfromtxt('dat_8.csv', delimiter=',')
with open('crvocab.csv', 'rb') as f:
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

licrs = ['MSO201A','TA201A','TA202A','TA101A','AE201A']

def kmfunc(licrs,roll_no,neighbours):
    onehot = np.zeros((1,786))
    for course in licrs:
        for i in range(786):
            if(voc[i][0] == course):
                onehot[0,i] = 1
                break

    querry=onehot
    reco= list()
    ml =  predict_courses(querry,roll_no,neighbours)
    for i in range(neighbours):
        xxx = list()
        for j in range(786):
            if ml[i,j] == 1:
                xxx.append(voc[j][0])
        reco.append(xxx)
    f = gandkichul(reco,neighbours)
    return f
def gandkichul(reco,neighbours):
    y = list()
    for launda in reco:
        for crs in launda:
            if crs not in y:
                y.append(crs)
    return y
x  = kmfunc(licrs,13450,10)
x
