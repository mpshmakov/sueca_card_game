#filename = str
#f = open (filename, mode='r', encoding='utf-8')
y = 0
#for i in range(133):                 # fix this part so it automatically knows the range
 #           x = f.read(1)
  #          if x =="\n":
   #             y+=1
                               
#f.seek(0)
#nnn = str(f.readline())
#mainsuit = nnn[1]
#print(mainsuit)
#print(y)
        
        #def scores():
            
def valid_suit(s):
            if s[1] == "D" or s[1] == "H" or s[1] == "C" or s[1] == "S":
                return True
            else:
                return False
            
def valid_rank(r):
            if r[0] == "A" or r[0] == "7" or r[0] == "K" or r[0] == "J" or r[0] == "Q" or r[0] == "6" or r[0] == "5" or r[0] == "4" or r[0] == "3" or r[0] == "2":
                return True
            else:
                return False
            
def suit_full_name(s):
            if s[1] == "D":
                return "Diamond"
            elif s[1] == "H":
                return "Hearts"
            elif s[1] == "C":
                return "Clubs"
            elif s[1] == "S":
                return "Spades"
            else:
                raise ValueError("invalid suit symbol", s[1])
            
def rank_points(r):
            if r[0] == "A":
                return 11
            elif r[0] == "7":
                return 10
            elif r[0] == "K":
                return 4
            elif r[0] == "J":
                return 3
            elif r[0] == "Q":
                return 2
            elif r[0] == "6" or r[0] == "5" or r[0] == "4" or r[0] == "3" or r[0] == "2":
                return 0
            else:
                raise ValueError("invalid rank symbol", r[0])
           
def rank_higher_than(r1, r2):
            if rank_points(r1) > rank_points(r2):
                return True
            else:
                return False
            
#for i in range(y):
 #           f.readline()
            
        
firstteam = 0 # players 1 and 3
secondteam = 0 # players 2 and 4
        
#roundg = f.readline()
