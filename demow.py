class Intro:
    def flight(self):
        print("in intro")
        #demow

class Demow(Intro):
    def flight(self):
        print("demow on.....")
        super().flight()
    
vae=Demow()
vae.flight()
          