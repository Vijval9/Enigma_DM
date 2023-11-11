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



##################################################################################################################################


class Rotor():
    
    og_list = list("abcdefghijklmnopqrstuvwxyz")
    
    def __init__(self, a, b, n):
        self.face_a = a
        self.face_b = b
        self.offset = 0
        self.notch = n
        self.roffset=0
        
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
        if s in self.plg.up:
           s = self.plg.map_u_to_l(s)
        self.r1.shift()
        a = self.r1.map_a_to_b2(s)
        if(self.r1.offset%26==self.r1.notch or self.r1.offset%26==self.r2.notch):
            self.r2.shift()
            self.r2.now=2
        b = self.r2.map_a_to_b2(a)
        if((self.r2.offset%26==self.r2.notch or self.r2.offset%26==self.r3.notch) and self.r2.now!=3):
            self.r3.shift()
            self.r2.now=3
        c = self.r3.map_a_to_b2(b)
        d = self.ref.map_a_to_b(c)
        a = self.r3.map_b_to_a2(d)
        a1 = self.r2.map_b_to_a2(a)
        a = self.r1.map_b_to_a2(a1)
        if a in self.plg.low:
            a = self.plg.map_l_to_u(a)
        
        return a
    
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


Rotor5 = Rotor(rotor5_a,rotor5_b, 26)
Rotor4 = Rotor(rotor4_a,rotor4_b, 10)
Rotor3 = Rotor(rotor3_a,rotor3_b, 22)
Rotor2 = Rotor(rotor2_a,rotor2_b, 5)
Rotor1 = Rotor(rotor1_a,rotor1_b, 17)
ReflectorB = Reflector(reflector_a,reflector_b)
Plugboard = PlugBoard(list(s),list(s))

print("Enter rotor order from left to right: ")
s = list(map(int,input()))
rl = [Rotor1,Rotor2,Rotor3,Rotor4,Rotor5]
    

r1 = rl[s[0]-1]
r2 = rl[s[1]-1]
r3 = rl[s[2]-1]
og = list("abcdefghijklmnopqrstuvwxyz")
rotors = [r1,r2,r3]

print("Enter Rotor Settings: ")           
s = list(input())
for i in range(len(s)):
    j = og.index(s[i])
    for x in range(j):
        rotors[i].shift()


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

if(i==1):
    print("Enter text to encrypt: ")
    s = input()
    print("Encrypting...")
    print("Encrypted message: ")
    print(EnigmaMachine.encrypt_text(s))
else:
    print("Enter text to decrypt: ")
    s = input()
    print("Decrypting...")
    print("Decrypted message: ")
    print(EnigmaMachine.encrypt_text(s))

