import sueca_cards as c
import sueca_suits_ranks as s

#def parseTrick(cs):
    
    
class Trick:
    def __init__(self, trick):
        self.trick = [trick[0] + trick[1], trick[3] + trick[4], trick[6]+trick[7], trick[9] + trick[10]]
        
    def points(self):
        return s.rank_points(self.trick[0]) + s.rank_points(self.trick[1]) + s.rank_points(self.trick[2]) + s.rank_points(self.trick[3])
    
    def trick_winner(self):
        
        c1 = c.parseCard(self.trick[0])
        c2 = c.parseCard(self.trick[1])
        c3 = c.parseCard(self.trick[2])
        c4 = c.parseCard(self.trick[3])
        alll = [c1, c2, c3, c4]
        for i in range(3):
            ref = " "            
            if c.alll[i].higher_than(alll[i+1], s, t):
                ref = alll[i]
                alll[i] = alll[i+1]
                alll[i+1] = ref
        if alll[3] == c1:
            return 1
        if alll[3] == c2:
            return 2
        if alll[3] == c3:
            return 3
        if alll[3] == c4:
            return 4
        
        
    def show(self):
        return self.trick