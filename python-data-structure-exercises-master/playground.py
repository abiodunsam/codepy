#%%
L = [4,5,6,6]
print(L[0])
# %%
for i in L:
    print(i)
# %%

# %%

mydict = {
    "key1":"value1"
}
# %%
ans = mydict.keys()
print(ans)
# %%
ans = mydict.values()
print(ans)
# %%
for i,j in mydict.items():
    print(i,j)
# %%
print(mydict.items())
# %%

def Capitalize_name(name):
    return name.upper()
# %%
Capitalize_name("eric")
# %%

def addtwo(l,b):
    return l + b
# %%
addtwo(5,6)
# %%
addtwo(3,2)
# %%



def formular(a,d,m,x):
    return a * d + m * x **5
# %%
formular(4,2,0.5,4)
# %%

def Qfn(a, b,c):
    x1 = -b +  (((b**2 - (4 *a *c) )**0.5 )/ 2* a)
    x2 = -b -  (((b**2 - (4 *a *c) )**0.5 )/ 2* a)
    return (x1,x2)

#a, b== rugtfggygyhgyhgyg == result

# %%
Qfn(1,16,15)
# %%
from bets import *
import math



# %%
Hubets = Betting()
# %%
Ngjabets = Betting()
# %%
Hubets.addbet("Chelsea vs Locus United",[1,0], 0)
# %%
Hubets.listBets
# %%
Hubets.placebets(0,0,"Eric")
# %%
Hubets.decidebet(0,0)
# %%
Hubets.claim(0, "Eric")
# %%
Hubets.placeBets
# %%
Ngjabets.addbet("N vs K", [], 0)
# %%
Ngjabets.listBets
# %%
