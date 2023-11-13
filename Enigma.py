import random

s = "abcdefghijklmnopqrstuvwxyz"
s2 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
s2.lower()
rotor3_a = list(s)
rotor3_b = list(s2.lower())
s4 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor2_a = list(s)
rotor2_b = list(s4.lower())
s5 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor1_a = list(s)
rotor1_b = list(s5.lower())
s6 = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
reflector_a = list(s)
reflector_b = list(s6.lower())
rotor4_a = list(s)
s7 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotor4_b = list(s7.lower())
rotor5_a = list(s)
s8 = "VZBRGITYUPSDNHLXAWMJQOFECK"
rotor5_b = list(s8.lower())
s9 = "JPGVOUMFYQBENHZRDKASXLICTW"
rotor6_a = list(s)
rotor6_b = list(s9.lower())
s10 = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
rotor7_a = list(s)
rotor7_b = list(s10.lower())
s11 = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
rotor8_a = list(s)
rotor8_b = list(s11.lower())





##################################################################################################################################


class Rotor():
    
    og_list = list("abcdefghijklmnopqrstuvwxyz")
    
    def __init__(self, a, b, n, m):
        self.face_a = a
        self.face_b = b
        self.offset = 0
        self.notch = n
        self.notch2 = m
        self.roffset=0
        self.now = 0
        
    def map_a_to_b(self, x):
        #print(self.og_list.index(x))
        #print(self.face_b)
        return self.og_list[(self.og_list.index(self.face_b[(self.face_a.index(x)+self.offset)%len(self.face_a)])-self.offset)%len(self.face_a)]
    
    def map_b_to_a(self, x):
        #return self.face_a[self.face_b.index(x)]
        x = self.face_a[self.og_list.index(x)-self.roffset]
        return self.og_list[(self.og_list.index(self.face_a[(self.og_list.index(x)+self.offset)%len(self.face_b)]) - self.offset+self.roffset)%len(self.face_a)]
        #return self.face_a[]
        
    def map_a_to_b2(self, x):
        x = self.face_a[(self.og_list.index(x)-self.roffset)%26]
        return self.og_list[(self.og_list.index(self.face_b[self.face_a.index(x)])-self.offset+self.roffset)%26]
    
    def map_b_to_a2(self, x):
        return self.og_list[(self.og_list.index(self.face_a[self.face_b.index(self.og_list[(self.og_list.index(x)+self.offset-self.roffset)%26])])-self.offset+self.roffset)%26]
           
    def transform_forward(self, x):
        return self.og_list[self.face_a.index(x)]
    
    def transform_backward(self, x):
        return self.og_list[self.face_a.index(x)]
    
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
        '''st = self.og_list[0]
        for i in range(0,len(self.og_list)):
            
            if i!=len(self.og_list)-1:
               self.og_list[i] = self.og_list[i+1]

            
            else:
                self.og_list[i] = st'''
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
        #print("before plg: ",s)
        s1 =s
        if s in self.plg.up:
           s1 = self.plg.map_u_to_l(s)
        #if(self.r1.offset%26==self.r1.notch):
         #   self.r2.shift()
        elif s in self.plg.low:
            s1 = self.plg.map_l_to_u(s)
        #print("after plg: ",s1)
        self.r1.shift()
        a = self.r1.map_a_to_b2(s1)
        #print("wheel3 :",a)
        #print("offset",self.r1.offset)
        if(self.r1.notch==26 and self.r1.offset!=0):
            if(((self.r1.offset)%self.r1.notch==0 or self.r1.offset%26==self.r1.notch2 or self.r2.offset%26 == self.r2.notch-1 or self.r2.offset%26 == self.r2.notch2-1)) : #(self.r1.offset%26==self.r2.notch) ):# and self.r1.now!=3: #and self.r1.now==0)
                self.r2.shift()
                self.r2.now=2
                self.r1.now=3
        elif((self.r1.offset)%26==self.r1.notch or self.r1.offset%26==self.r1.notch2 or self.r2.offset%26 == self.r2.notch-1 or self.r2.offset%26 == self.r2.notch2-1) : #(self.r1.offset%26==self.r2.notch) ):# and self.r1.now!=3: #and self.r1.now==0)
            self.r2.shift()
            self.r2.now=2
            self.r1.now=3
            #self.r1.offset=0
        
        b = self.r2.map_a_to_b2(a)
        #print("wheel2: ",b)
        if(self.r2.notch==26 and self.r2.offset!=0):
            if(((self.r2.offset)%self.r2.notch==0 or self.r2.offset%26==self.r2.notch2 or (self.r3.offset%26==self.r3.notch-1) or self.r3.offset%26==self.r3.notch2-1) and self.r2.now!=3) :
                self.r3.shift()
                self.r2.now=3
        elif (((self.r2.offset)%26==self.r2.notch or self.r2.offset%26==self.r2.notch2 or (self.r3.offset%26==self.r3.notch-1) or self.r3.offset%26==self.r3.notch2-1) and self.r2.now!=3) :#and self.r2.now==0):
            self.r3.shift()
            self.r2.now=3
            #self.r2.offset=0
            #self.r3.offset=0

        c = self.r3.map_a_to_b2(b)
        #print("wheel1: ",c)
        d = self.ref.map_a_to_b(c)
        #print(d)
        a = self.r3.map_b_to_a2(d)
        #print(a)
        a1 = self.r2.map_b_to_a2(a)
        #print(a1)
        a = self.r1.map_b_to_a2(a1)
        #print("before plg: ",a)
        #print(a)
        a1 =a
        if a in self.plg.up:
            a1 = self.plg.map_u_to_l(a)
        elif a in self.plg.low:
            a1 = self.plg.map_l_to_u(a)
        #print("after plg:",a1)
        #if(self.r1.offset%26==self.r1.notch):
         #   self.r2.shift()
        #if(self.r2.offset%26==self.r2.notch):
         #   self.r3.shift()
        
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
                
    
    
##################################################################################################################################
Rotor8 = Rotor(rotor8_a,rotor8_b,26,13)
Rotor7 = Rotor(rotor7_a,rotor7_b,26,13)
Rotor6 = Rotor(rotor6_a,rotor6_b, 26, 13)
Rotor5 = Rotor(rotor5_a,rotor5_b, 26,-10)
Rotor4 = Rotor(rotor4_a,rotor4_b, 10,-10)
Rotor3 = Rotor(rotor3_a,rotor3_b, 22,-10)
Rotor2 = Rotor(rotor2_a,rotor2_b, 5,-10)
Rotor1 = Rotor(rotor1_a,rotor1_b, 17,-10)

ReflectorB = Reflector(reflector_a,reflector_b)
Plugboard = PlugBoard(list(s),list(s))

print("Enter rotor order from left to right: ")
s = list(map(int,input()))
rl = [Rotor1,Rotor2,Rotor3,Rotor4,Rotor5,Rotor6,Rotor7,Rotor8]
    

r1 = rl[s[0]-1]
r2 = rl[s[1]-1]
r3 = rl[s[2]-1]
og = list("abcdefghijklmnopqrstuvwxyz")
rotors = [r1,r2,r3]

print("Enter Rotor Settings: ")           # FIX THIS
s = list(input())
for i in range(len(s)):
    j = og.index(s[i])
    for x in range(j):
        rotors[i].shift_initial()
        '''if(i!=0):
            if(rotors[i].offset%26==rotors[i].notch):
                rotors[i-1].shift()
                if(i==2):
                    if(rotors[i-1].offset%26==rotors[i-1].notch):
                        rotors[i-2].shift()'''


print("Enter ring settings: ")            # FIX THIS
s = list(input())

for i in range(len(s)):
    j = og.index(s[i])
    for x in range(j):
        rotors[i].shift_ring()


print("Enter plugboard configuration as pairs of letters. Press nop if do not want plugboard: ")
s= input()

if s.lower()!="nop":
    l = s.split()
    pu = [x[0] for x in l]
    pl = [x[1] for x in l]
    Plugboard = PlugBoard(pu,pl)
    
    

EnigmaMachine = Enigma(r1,r2,r3,ReflectorB,Plugboard)
print("Enigma Machine initialised...")

print("Choose: ")
print("1. Encrypt")
print("2. Decrypt")
i = int(input())

xl = ""
if(i==1):
    print("Enter text to encrypt: ")
    s = input()
    print("Encrypting...")
    print("Encrypted message: ")
    xl = EnigmaMachine.encrypt_text(s)
    print(xl)
else:
    print("Enter text to decrypt: ")
    s = input()
    print("Decrypting...")
    print("Decrypted message: ")
    print(EnigmaMachine.encrypt_text(s))
    
