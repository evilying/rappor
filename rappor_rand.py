
# coding: utf-8

# In[87]:


import pandas as pd
import hashlib
import base64
import numpy as np
import random
seed=1

def Mapping1(clientvalue,cohort,num_hashes,bfsize, X,stringindex):
    return X[(cohort-1)*bfsize:(cohort-1)*bfsize+bfsize,stringindex-1]
    
    

# In[143]:


def FakeBloomFilter(bloom,f,bfsize):
    fakebloomfilter=np.zeros(bfsize)
    for i in range(0,bfsize):
        chc=np.random.choice(np.array([1,2,3]), p=[f/2,f/2,1-f])
        if(chc==1):
           fakebloomfilter[i]=0
        elif(chc==2):
            fakebloomfilter[i]=1
        else:
            fakebloomfilter[i]=bloom[i]
   
    return fakebloomfilter


# In[144]:

def ProcessEachString(word,cohort,f,bfsize,no_hashes, X,stringindex):
    bloom_filter=np.zeros((len(word),bfsize))
    reports = []
    for i in range(len(word)):
        bloom_filter[i]=Mapping1(word[i],cohort[i],no_hashes,bfsize, X,stringindex)
        report=FakeBloomFilter(bloom_filter[i],f,bfsize)
        reports.append(report.astype(int).tolist())

    return reports

    
def mapBloomFilter1(clientvalue, icohort, nhashes, bfsize):
        inptomd=clientvalue+str(icohort)
        encoded=base64.b64encode(inptomd.encode('utf-8'))
        entries=0
        listofindx=[]

        while(entries<nhashes):
            i=np.random.randint(0,len(encoded))
            t=encoded[i] % bfsize
    
            if(t not in listofindx):
               
                listofindx.append(t)
                entries=entries+1
            
        vec = np.zeros(bfsize)
        for ind in listofindx:

            vec[ind] = 1

        return vec
   
#def mapBloomFilter(clientvalue, icohort, nhashes, bfsize):
#
#        inptomd=clientvalue+str(icohort)
#        encoded=base64.b64encode(inptomd.encode('utf-8'))
#        i=0
#        entries=0
#        listofindx=[]
#
#        while(i<len(encoded) and entries<nhashes):
#    
#            t=encoded[i] % bfsize
#    
#            if(t not in listofindx):
#               
#                listofindx.append(t)
#                i=i+1
#                entries=entries+1
#            else:
#                i=i+1
#        vec = np.zeros(bfsize)
#        for ind in listofindx:
#
#            vec[ind] = 1
#
#        return vec 



def ProcessDataAndParameters(saminp,no_cohorts,f,bfsize,no_hash, X):

    matrix = []
    np.random.seed(seed)
    allcohorts=[]
    print(no_cohorts)
    for i in range(0,len(saminp)):
        stringval=saminp['word'].iloc[i]
        stringindex=saminp['Index'].iloc[i]
        curlist=[stringval]*int(saminp['trueFrequency'].iloc[i])
        cohorts=np.array([np.random.randint(1,no_cohorts+1) for i in range(0,len(curlist))])
        allcohorts.extend(cohorts)
        reports = ProcessEachString(curlist,cohorts,f,bfsize,no_hash, X,stringindex)
        matrix.extend(reports)

    return [matrix,np.array(allcohorts)]


# In[146]:
# infile = pd.read_csv('smallcorpus.csv')
# client = infile.sample(frac=0.1)
# print(client)
# print(ProcessDataAndParameters(saminp,4,0.3,32,2))
