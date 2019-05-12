from random import *

def randomno():
    a=randrange(1,51,1)
    return a

def randomlist(a=10):
    l=[]
    x=0
    while (x<a):
        b=randrange(1,51,1)
        if b in l:
            pass
        else:
            l.append(b)
            x+=1
    return l


class Channel:


    def __init__(self,a=5):
        self.no_of_channels=a
        self.timeslots=[]
        self.common=[]

    # i not in self.common -> check

    def timeslotinit(self,l):
        for i in l:
            if i not in self.timeslots:
                self.timeslots.append(i)
            elif i in self.timeslots and i not in self.common:
                self.common.append(i)
                self.common.sort()
        self.timeslots.sort()

    def timeslotadd(self,n):
        if n not in self.timeslots:
            self.timeslots.append(n)
        elif n in self.timeslots and n not in self.common:
            self.common.append(n)
            self.common.sort()
        self.timeslots.sort()
        print(self.timeslots,"  ",n," added")

    def ischannelfree(self,time):
        if time not in self.timeslots:
            return True
        else:
            return False

    def displaychannelstatus(self):
        print("Channel : ",self.timeslots)
        print("Collisions : ",self.common)




class Station:


    def __init__(self):
        self.no_of_requests=0
        self.frameslots={}
        self.frameslotorig=[]
        self.sentframes=[]
        self.k=0

    def frameslotinit(self,framelist):
        framelist.sort()
        '''for i in range(1,6):
            self.frameslots[i]=list(framelist[i-1])'''
        i=1
        while i!=6:
            self.frameslots[i]=[framelist[i-1]]
            i+=1
        self.frameslotorig=framelist

    def frameslotadd(self,newtime,i):
        #True False not needed? Verify
        '''if newtime in self.frameslots[i]:
            print(newtime," not added to frame ",i)
            return False
        else:
            self.frameslots[i].append(newtime)
            print(newtime, "added to frame ", i)
            print(self.frameslots)
            return True'''
        a=self.getframeno(newtime)
        if a==-1:
            self.frameslots[i].append(newtime)
            print(newtime," added to frame ",i)
            print(self.frameslots)
            return True
        else:
            print(newtime," not added to frame ",i)
            return False


    def frameslotdel(self,time):
        self.frameslots.remove(time)

    def display_station(self):
        print(self.frameslots)

    def display_orig(self):
        print(self.frameslotorig)

    def display_sent(self):
        disp=[]
        for i in self.frameslots.keys():
            #print(i,":",self.frameslots[i][-1],end='  |  ')
            disp.append(self.frameslots[i][-1])
        print(disp)

    '''def getframeno(self,time):
        for i in (self.frameslots.keys()):
           if time in self.frameslots[i]:
               return i
           else:
               return -1'''

    def getframeno(self,time):
        i=1
        found=0
        while i!=6:
            if time in self.frameslots[i]:
                found=1
                print(time," found in ",i," th frame" )
                return i
            i+=1
        if found!=1:
            return -1





class Reciever:


    def __init__(self):
        self.recieved={}

        #self.recieved=[0,0,0,0,0]


    def sendack(self):
        return self.recieved[-1]

    def recieveframe(self,time,i):
        #self.recieved[i-1]=time
        self.recieved[i]=time
        print(i,"th frame recieved, time = ",time)

    def displayreciever(self):
        print(self.recieved)

t=0

A=Station()
B=Station()
C=Station()
D=Station()

time=0

W=Reciever()
X=Reciever()
Y=Reciever()
Z=Reciever()

channel=Channel()


print("Initialisation")

l=randomlist(5)
A.frameslotinit(l)
channel.timeslotinit(l)
l=randomlist(5)
B.frameslotinit(l)
channel.timeslotinit(l)
l=randomlist(5)
C.frameslotinit(l)
channel.timeslotinit(l)
l=randomlist(5)
D.frameslotinit(l)
channel.timeslotinit(l)


def backoff(S,t,i):
    print("Back off algorithm for time t = ",t,"| newtime = ",end=' ')
    S.k+=1
    if S.k<=15:
        R=randrange(0,2**(S.k),1)
        newtime=t+R*5
        print(newtime)
        if (S.frameslotadd(newtime,i))==True:
            channel.timeslotadd(newtime)
        else:
            abort(S,t,i)
    else:
        abort(S,t,i)

def abort(S,t,i):
    print("abort sequence called")
    S.k=0
    newtime=1000+t
    S.frameslotadd(newtime,i)
    channel.timeslotadd(newtime)


while(t<10000):
    t+=1
    if t not in channel.timeslots:
        pass
    else:
        if t in channel.common:
            temp=t+10 #Changelog -> replaced t by temp in backoff functions
            Aframeno=A.getframeno(t)
            Bframeno=B.getframeno(t)
            Cframeno=C.getframeno(t)
            Dframeno=D.getframeno(t)

            '''if t in A.frameslots:
                #A.frameslotdel(t)
                backoff(A,temp)
            if t in B.frameslots:
                #B.frameslotdel(t)
                backoff(B,temp)
            if t in C.frameslots:
                #C.frameslotdel(t)
                backoff(C,temp)
            if t in D.frameslots:
                #D.frameslotdel(t)
                backoff(D,temp)'''


            if Aframeno!=-1:
                print("back off for A : ")
                backoff(A,temp,Aframeno)
            if Bframeno!=-1:
                print("back off for B : ")
                backoff(B,temp,Bframeno)
            if Cframeno!=-1:
                print("back off for C : ")
                backoff(C,temp,Cframeno)
            if Dframeno!=-1:
                print("back off for D : ")
                backoff(D,temp,Dframeno)


        else:
            temp=t+10
            Aframeno = A.getframeno(t)
            Bframeno = B.getframeno(t)
            Cframeno = C.getframeno(t)
            Dframeno = D.getframeno(t)

            '''if t in A.frameslots:
                A.sentframes.append(t)
                W.recieveframe(temp)
            if t in B.frameslots:
                B.sentframes.append(t)
                X.recieveframe(temp)
            if t in C.frameslots:
                C.sentframes.append(t)
                Y.recieveframe(temp)
            if t in D.frameslots:
                D.sentframes.append(t)
                Z.recieveframe(temp)
            '''

            if Aframeno!=-1:
                print("A sent at time",t)
                W.recieveframe(temp,Aframeno)
            if Bframeno!=-1:
                print("B sent at time", t)
                X.recieveframe(temp,Bframeno)
            if Cframeno!=-1:
                print("C sent at time", t)
                Y.recieveframe(temp,Cframeno)
            if Dframeno!=-1:
                print("D sent at time", t)
                Z.recieveframe(temp,Dframeno)


def display():
    print("\n\n\n\nWe have considered time taken for frame to travel from sender to reciever = 5 seconds")
    print("\nWe have considered  vulnerable time = 1 second , initial time = 0 seconds")

    print("\n\nInitial time of sending frames\n")
    print("Station A : ", end=' ');A.display_orig()
    print("Station B : ", end=' ');B.display_orig()
    print("Station C : ", end=' ');C.display_orig()
    print("Station D : ", end=' ');D.display_orig()


    print("\n\nActual Sent Frames Times\n")
    print("Station A : ", end=' ');A.display_sent()
    print("Station B : ", end=' ');B.display_sent()
    print("Station C : ", end=' ');C.display_sent()
    print("Station D : ", end=' ');D.display_sent()


    print("\n\nRecieved Frames Times at reciever\n")
    print("Reciever of A : ", end=' ');W.displayreciever()
    print("Reciever of B : ", end=' ');X.displayreciever()
    print("Reciever of C : ", end=' ');Y.displayreciever()
    print("Reciever of D : ", end=' ');Z.displayreciever()


    print("\n\nTime at which frames are sent by each station \n")
    print("Station A : ",end=' ');A.display_station()
    print("Station B : ",end=' ');B.display_station()
    print("Station C : ",end=' ');C.display_station()
    print("Station D : ",end=' ');D.display_station()
    print("\n\nChannel status : Time slots at which channel were busy and collision times : \n")
    channel.displaychannelstatus()


display()