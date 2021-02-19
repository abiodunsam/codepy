class Betting():

    listBets = []
    placeBets = []

    def addbet(self, betdesc, options,betId):
        self.betdesc = betdesc
        self.options = options
        self.betId = betId
        data = {
            "betdesc":self.betdesc,
             "options":self.options,
             "betId" : self.betId,
             "wops":None
        }
        self.listBets.append(data)

        return data

    def placebets(self, betId, wopts, who):
        self.betId = betId
        self.wopts = wopts
        self.who = who 
        data = {
            "wopts":self.wopts,
             "who":self.who,
             "betId" :  self.betId
        }
        self.placeBets.append(data)

        return data

    def decidebet(self, betId, wops):
        bet2b = self.listBets[betId]
        bet2b["wops"] = wops

    def claim(self, betId,who):
        self.b1 = self.placeBets[betId]
        self.b2 = self.listBets[betId]
        if self.b1["who"] != who:
            print("You  cant claim this bet")
        else:
            if self.b1["wopts"] == self.b2["wops"]:
                print("You won")
            else:
                print("you loss")
