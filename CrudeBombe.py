# Some basic Initializations

import copy


l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rotor3_a = l.copy()
rotor3_b = ['b', 'd', 'f', 'h', 'j', 'l', 'c', 'p', 'r', 't', 'x', 'v', 'z', 'n', 'y', 'e', 'i', 'w', 'g', 'a', 'k', 'm', 'u', 's', 'q', 'o']
r3b = ['b', 'd', 'f', 'h', 'j', 'l', 'c', 'p', 'r', 't', 'x', 'v', 'z', 'n', 'y', 'e', 'i', 'w', 'g', 'a', 'k', 'm', 'u', 's', 'q', 'o']
rotor2_a = l.copy()
rotor2_b = ['a', 'j', 'd', 'k', 's', 'i', 'r', 'u', 'x', 'b', 'l', 'h', 'w', 't', 'm', 'c', 'q', 'g', 'z', 'n', 'p', 'y', 'f', 'v', 'o', 'e']
r2b = ['a', 'j', 'd', 'k', 's', 'i', 'r', 'u', 'x', 'b', 'l', 'h', 'w', 't', 'm', 'c', 'q', 'g', 'z', 'n', 'p', 'y', 'f', 'v', 'o', 'e']
rotor1_a = l.copy()
rotor1_b = ['e', 'k', 'm', 'f', 'l', 'g', 'd', 'q', 'v', 'z', 'n', 't', 'o', 'w', 'y', 'h', 'x', 'u', 's', 'p', 'a', 'i', 'b', 'r', 'c', 'j']
r1b = ['e', 'k', 'm', 'f', 'l', 'g', 'd', 'q', 'v', 'z', 'n', 't', 'o', 'w', 'y', 'h', 'x', 'u', 's', 'p', 'a', 'i', 'b', 'r', 'c', 'j']
rotor4_a = l.copy()
rotor4_b = ['e', 's', 'o', 'v', 'p', 'z', 'j', 'a', 'y', 'q', 'u', 'i', 'r', 'h', 'x', 'l', 'n', 'f', 't', 'g', 'k', 'd', 'c', 'm', 'w', 'b']
rotor5_a = l.copy()
rotor5_b = ['v', 'z', 'b', 'r', 'g', 'i', 't', 'y', 'u', 'p', 's', 'd', 'n', 'h', 'l', 'x', 'a', 'w', 'm', 'j', 'q', 'o', 'f', 'e', 'c', 'k']
reflector_a = l.copy()
reflector_b = ['y', 'r', 'u', 'h', 'q', 's', 'l', 'd', 'p', 'x', 'n', 'g', 'o', 'k', 'm', 'i', 'e', 'b', 'f', 'z', 'c', 'w', 'v', 'j', 'a', 't']
ref_b = ['y', 'r', 'u', 'h', 'q', 's', 'l', 'd', 'p', 'x', 'n', 'g', 'o', 'k', 'm', 'i', 'e', 'b', 'f', 'z', 'c', 'w', 'v', 'j', 'a', 't']


##########################################################################################################################################################

# Creating the Required Classes

class Rotor():
    
    og_list = list("abcdefghijklmnopqrstuvwxyz")
    
    def __init__(self, a, b, n):
        self.face_a = a
        self.face_b = b
        self.offset = 0
        self.notch = n
        self.roffset=0
        self.now = 0
        
    def map_a_to_b2(self, x):
        x = self.face_a[(self.og_list.index(x)-self.roffset)%26]
        return self.og_list[(self.og_list.index(self.face_b[self.face_a.index(x)])-self.offset+self.roffset)%26]
    
    def map_b_to_a2(self, x):
        return self.og_list[(self.og_list.index(self.face_a[self.face_b.index(self.og_list[(self.og_list.index(x)+self.offset-self.roffset)%26])])-self.offset+self.roffset)%26]
    
    def shift(self):
        st_b = self.face_b[0]
        st_a = self.face_a[0]
        
        for i in range(0,len(self.face_a)):
            
            if i!=len(self.face_a)-1:
               self.face_b[i] = self.face_b[i+1]
               self.face_a[i] = self.face_a[i+1]
            
            else:
                self.face_b[i] = st_b
                self.face_a[i] = st_a
                
        self.offset+=1
        self.now=3
        
    def shift_ring(self):
        self.roffset+=1
        
    def shift_initial(self):
        st_b = self.face_b[0]
        st_a = self.face_a[0]
        
        for i in range(0,len(self.face_a)):
            
            if i!=len(self.face_a)-1:
               self.face_b[i] = self.face_b[i+1]
               self.face_a[i] = self.face_a[i+1]
            
            else:
                self.face_b[i] = st_b
                self.face_a[i] = st_a
                
        self.offset+=1
        self.now=1
              


class Reflector():
    
    def __init__(self, a, b):
        self.face_a = a
        self.face_b = b
        
    def map_a_to_b(self, x):
        return self.face_b[self.face_a.index(x)]
    
    def map_b_to_a(self, x):
        return self.face_a[self.face_b.index(x)]
    

class PlugBoard():
    
    def __init__(self, u, l):
        self.up = u
        self.low = l
        
    def map_u_to_l(self, x):
        return self.low[self.up.index(x)]
    
    def map_l_to_u(self, x):
        return self.up[self.low.index(x)]



class Enigma():
    
    def __init__(self, r3, r2, r1, ref, plgb):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.ref = ref
        self.plg = plgb
        
    def encrypt_letter(self,s):
        s1 =s
        if s in self.plg.up:
           s1 = self.plg.map_u_to_l(s)
        elif s in self.plg.low:
            s1 = self.plg.map_l_to_u(s)
        self.r1.shift()
        a = self.r1.map_a_to_b2(s1)
        if(self.r1.notch==26 and self.r1.offset!=0):
            if(((self.r1.offset)%self.r1.notch==0 or self.r2.offset%26 == self.r2.notch-1)) : #(self.r1.offset%26==self.r2.notch) ):# and self.r1.now!=3: #and self.r1.now==0)
                self.r2.shift()
                self.r2.now=2
                self.r1.now=3
        elif((self.r1.offset)%26==self.r1.notch or self.r2.offset%26 == self.r2.notch-1) : #(self.r1.offset%26==self.r2.notch) ):# and self.r1.now!=3: #and self.r1.now==0)
            self.r2.shift()
            
            self.r2.now=2
            self.r1.now=3
    
        b = self.r2.map_a_to_b2(a)
        if(self.r2.notch==26 and self.r2.offset!=0):
            if((self.r2.offset)%self.r2.notch==0 or (self.r3.offset%26==self.r3.notch-1 and (self.r2.offset%26==self.r2.notch)) and self.r2.now!=3) :
                self.r3.shift()
                print(self.r2.offset)
                self.r2.now=3
        elif (((self.r2.offset)%26==self.r2.notch or (self.r3.offset%26==self.r3.notch-1 and (self.r2.offset%26==self.r2.notch))) and self.r2.now!=3) :#and self.r2.now==0):
            self.r3.shift()
            self.r2.now=3  

        c = self.r3.map_a_to_b2(b)
        d = self.ref.map_a_to_b(c)
        a = self.r3.map_b_to_a2(d)
        a1 = self.r2.map_b_to_a2(a)
        a = self.r1.map_b_to_a2(a1)
        a1 =a
        if a in self.plg.up:
            a1 = self.plg.map_u_to_l(a)
        elif a in self.plg.low:
            a1 = self.plg.map_l_to_u(a)
        
        return a1
    
    def encrypt_string(self, s):
        l = list(s)
        final = ""
        for i in l:
            final+=self.encrypt_letter(i)  
        return final
    
    def encrypt_text(self, t):
        l = list(t)
        final = ""
        for i in l:
            if(i!=" "):
                final+=self.encrypt_string(i)
            else:
                final+=i
                
        return final
    
        
def match(s,t):
    fl=0
    for i in range(len(s)):
        if(s[i]==t[i]):
            fl=1
            #print(l[i])
            break
    if(fl==1):
        return 1
    else:
        return 0

def crib(l ,m):
    fin = []
    ms = len(m)
    ls = len(l)
    fl=0
    ind = 0
    for y in range(ls-ms+1):
        #print("y: ",y)
        #print(l[y:y+ms])
        if(match(l[y:y+ms],m)==0):
            fl=1
            #print(l[y:y+ms])
            fin.append(y)
            ind = y
    if(fl==1):
        return fin
        



    
      
    
          
    
    
##################################################################################################################################

# Starting the Simulation of the Enigma Machine

Rotor5 = Rotor(rotor5_a,rotor5_b, 26)
Rotor4 = Rotor(rotor4_a,rotor4_b, 10)
Rotor3 = Rotor(rotor3_a,rotor3_b, 22)
Rotor2 = Rotor(rotor2_a,rotor2_b, 5)
Rotor1 = Rotor(rotor1_a,rotor1_b, 17)

ReflectorB = Reflector(reflector_a,reflector_b)
Plugboard = PlugBoard(l.copy(),l.copy())

print("Bombe initialised...")

ct = input("Enter text to be fed: ").lower()
cr = input("Enter hint: ").lower()
mm=0

dictofkeys = {}


while(mm==0):



    print("Enter rotor order from left to right: ")
    ss = list(map(int,input().split()))
    rl = [copy.deepcopy(Rotor1),copy.deepcopy(Rotor2),copy.deepcopy(Rotor3),copy.deepcopy(Rotor4),copy.deepcopy(Rotor5)]
        

    r1 = rl[ss[0]-1]
    r2 = rl[ss[1]-1]
    r3 = rl[ss[2]-1]
    og = list("abcdefghijklmnopqrstuvwxyz")
    rotors = [copy.deepcopy(r1),copy.deepcopy(r2),copy.deepcopy(r3)]

    rotors = [copy.deepcopy(r1),copy.deepcopy(r2),copy.deepcopy(r3)]
    EnigmaMachine = Enigma(rotors[0],rotors[1],rotors[2],ReflectorB,Plugboard)

    start = crib(ct,cr)

    matc=0
    s=["a","a","a"]
    og = list("abcdefghijklmnopqrstuvwxyz")
    i=0
    for a in range(26):
        aa=0
        for b in range(26):
            bb=0
            for c in range(26):
                cc=0
                s = [og[a],og[b],og[c]]
                print("rotors: ",s)
                rotors = [copy.deepcopy(r1),copy.deepcopy(r2),copy.deepcopy(r3)]
                for i in range(len(s)):
                    j = og.index(s[i])
                    for x in range(j):
                        rotors[i].shift_initial()
                #print("rotor1: ",rotors[2].face_a)
                EnigmaMachine = Enigma(rotors[0],rotors[1],rotors[2],ReflectorB,Plugboard)
                #print(EnigmaMachine.r1.face_a)
                for i in start:
                    rotors = [copy.deepcopy(r1),copy.deepcopy(r2),copy.deepcopy(r3)]
                    for z in range(len(s)):
                        j = og.index(s[z])
                        for x in range(j):
                            rotors[z].shift_initial()
                #print("rotor1: ",rotors[2].face_a)
                    EnigmaMachine = Enigma(rotors[0],rotors[1],rotors[2],ReflectorB,Plugboard)
                    #print("crib: ",i)
                    xy=0
                    if(i!=0):
                        EnigmaMachine.encrypt_text("a"*(i))
                    #print("state: ",EnigmaMachine.r3.face_a[0],EnigmaMachine.r2.face_a[0],EnigmaMachine.r1.face_a[0])
                    sss = EnigmaMachine.encrypt_text(ct[i:i+len(cr)])
                    #print("guess: ",sss)
                    if(sss==cr):
                       st = ""
                       for i in ss:
                           st+=str(i)
                       dictofkeys[st] = s
                       print("one key found: ",s)
                       search = input("continue to search ? [y/n]: ")
                       if((a==25 and b==25 and c==25) or search=="n"):
                           xy=1
                           break
                if(xy==1):
                    if((a==25 and b==25 and c==25) or search=="n"):
                        bb=1
                        break
            if(bb==1):
                if((a==25 and b==25 and c==25) or search=="n"):
                    aa=1
                    break
        if aa==1:
            if((a==25 and b==25 and c==25) or search=="n"):
                matc=1
                break
    if((matc==1 and a==25 and b==25 and c==25) or search=="n"):
        mm=1
        print("Cracked.")
        print("rotor settings: ",s)
        print("Rotor order: ",ss[0],ss[1],ss[2])
        break
    else:
        print("No more solutions")

print("Final possible solutions : ")
for i in dictofkeys:
    print(f"{i} : {dictofkeys[i]}")


        

