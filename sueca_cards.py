import sueca_suits_ranks as r

class CardInvalid(Exception):
    def __init__(self, card):
        str = "Invalid card {k}"
        self.msg = str.format(k=card)
        super().__init__(self.msg)

def parseCard(cs):

    if r.valid_suit(cs) == True and r.valid_rank(cs) == True:       
        return Card(cs)
    elif r.valid_suit(cs) == False or r.valid_rank(cs) == False:       
        raise CardInvalid(cs)
    
class Card:
    
    def __init__(self, card):
        self.card = card
        
    def points(self):
        return r.rank_points(self.card)
    
    def higher_than(self,other,s,t):
        
            if self.card == t and other.card == t:
                if r.rank_points(self.card) > r.rank_points(other.card):
                    return True
                elif r.rank_points(self.card) < r.rank_points(other.card):
                    return False
            
            elif (self.card[1] == t and other.card[1] == s) or (self.card[1] == t and other.card[1] != s):
                return True
            
            elif (self.card[1] == s and other.card[1] == t) or (self.card[1] != s and other.card[1] == t):
                return False
            
            elif self.card[1] == s and other.card[1] == s:
                if r.rank_points(self.card) > r.rank_points(other.card):
                    return True
                elif r.rank_points(self.card) < r.rank_points(other.card):
                    return False
            
            elif other.card[1] == s and (self.card[1] != s and self.card[1] != t):
                return False
            
            elif self.card[1] == s and (other.card[1] != s and other.card[1] != t):
                return True
            
            elif (self.card[0] == "6" and other.card[0] == "1") and (self.card[1] == other.card[1]):
                return True
        
            elif (self.card[0] == "1" and other.card[0] == "6") and (self.card[1] == other.card[1]):
                return False

        
    def show(self):
        return self.card
    
c1 = Card("QD")
c2 = Card("AH")
        