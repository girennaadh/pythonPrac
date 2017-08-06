#!/usr/bin/python
class bahubali:
    def __init__(self,remuneration):
        self.remun=remuneration
   
        

    def actor(self,remuneration):
        self.remun=remuneration
       
        print "actor prabhas"
        print remuneration
        return

    def actress(self,remun):
        print "actress Anuska"
        print self.remun+5000
        return

    def vilan(self,remun):
        print "Rana"
        print self.remun-remun
        return

Rajamouli=bahubali("dsd")
Rajamouli.actor(2000)
Rajamouli.actress(100000)
Rajamouli.vilan(100)
    
