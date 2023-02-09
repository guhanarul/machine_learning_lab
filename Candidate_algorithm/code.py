import pandas as pd
# COMPLETE CODE FOR THE CANDIDATE ALGORITHM:
def candidate_algo(d,s,g):
    final=[]
    for _ in d:
        if(_[-1]=='yes'):
            if(s[0]=='Null'):
                s=_[:len(_)-1]
            else:
                for i in range(len(s)):
                    if(_[i]!=s[i]):
                        s[i]='?'
        else:
            for i in range(len(s)):
                if(_[i]!=s[i]):
                    g[i][i]=s[i]
    for i in s:
        for j in g:
            if(i in j and i!='?'):
                final.append(j)
    return f'this is generalized space={g}',f'this is specialised space={s}'
    

# HERE WE ARE CHNAGING THE GIVEN DATAFRAME AS A LIST:
dataset=pd.read_csv("dataset2.csv")     
dataset=dataset.loc[:,dataset.columns!='index']
d1=dataset.values.tolist()
# THE VALUES OF THE TWO SPACES ARE INITIALISED HERE:
spec=['Null']*(len(d1[0])-1)
gen=[['?']*len(d1[0]) for i in range(len(d1[0]))]

#CALLING THE FUNCTION HERE:   
a,b=candidate_algo(d1,spec,gen)
print(a)
print(b)

#a,b are the results!



