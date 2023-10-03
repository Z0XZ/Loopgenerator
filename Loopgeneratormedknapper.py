"""
Dette programmet er laget av Jon Bjarne Bø
Hensikten med programmet er å lage ulike oppgaver som settes sammen til looper (løyper)
"""
import random
import math
from fpdf import FPDF
import os
import tkinter as tk
""" Her kommer de ulike autogenererte oppgavemulighetene"""

oppgaveListe = []
svarListe = []

class lageOppgaver():
    def __init__ (self, antall):
        self.antall = antall
        self.sluttverdi = int(round(self.antall / 2))
        self.startverdi = self.sluttverdi * (-1)
        self.lengdePåListe = self.sluttverdi - self.startverdi + 1
         

    def lineæreLikninger (self):      
        self.xverdiListe = []

        self.s = self.startverdi        
        for i in range (self.lengdePåListe):
            self.xverdiListe.append(self.s)
            self.s += 1
            
        if 0 in self.xverdiListe:
            self.xverdiListe.remove(0)
            self.xverdiListe.append(self.sluttverdi + 1)
            
        for i in range(self.antall):
            self.a = random.randint (self.startverdi, self.sluttverdi)
            self.b = random.randint (self.startverdi, self.sluttverdi)
            self.g = random.randint (0, self.lengdePåListe - 1)
            self.x = self.xverdiListe[self.g]
            del self.xverdiListe[self.g]
            self.lengdePåListe -= 1

            if self.a == 0:
                self.a =+ 1

            self.c = self.a*self.x + self.b
            
#Ønsker du likninger uten flere x-ledd kommenter ut herfra til neste kommentar.
            
            self.over = random.randint (-10, 10)
            if self.over == 0:
                self.over += 1
            if self.over*(-1) == self.a:
                self.over += 1
            
            self.a = self.a + self.over
            
            if self.over > 0:
                if self.c > 0:
                    if self.over == 1:
                        self.c = "x + {}".format(self.c)
                    else:
                        self.c = "{}x + {}".format(self.over, self.c)
                else:
                    if self.over == 1:
                        self.c = "x - {}".format(self.c*(-1))
                    else:
                        self.c = "{}x - {}".format(self.over, self.c*(-1))
            else:
                if self.over == -1:
                    self.c = "{} - x".format(self.c)
                else:
                    self.c = "{} - {}x".format(self.c, self.over*(-1))
            
#Kommentarslutt
            
            if self.b == 0:
                if self.a == 1:
                    self.likning = "x = {}".format(self.c)
                elif self.a == -1:
                    self.likning = "-x = {}".format(self.c)
                else:
                    self.likning = "{}x = {}".format(self.a,self.c)
            elif self.b < 0:
                self.b = self.b*(-1)
                if self.a == 1:
                    self.likning = "x - {} = {}".format(self.b,self.c)
                elif self.a == -1:
                    self.likning = "-x - {} = {}".format(self.b,self.c)
                else:
                    self.likning = "{}x - {} = {}".format(self.a,self.b,self.c)
            else:
                if self.a == 1:
                    self.likning = "x + {} = {}".format(self.b,self.c)
                elif self.a == -1:
                    self.likning = "-x + {} = {}".format(self.b,self.c)
                else:
                    self.likning = "{}x + {} = {}".format(self.a,self.b,self.c)

            oppgaveListe.append(self.likning)
            svarListe.append("x = " + str(int(self.x)))

    def andregradslikninger (self):
        self.xverdiListe = []
        
        self.s = 1
        for i in range (self.lengdePåListe):
            self.xverdiListe.append(self.s)
            self.s += 1
        
        for i in range (self.antall):
            self.a = random.randint (int(round(self.startverdi/2)), int(round(self.sluttverdi/2)))
            self.b = random.randint (int(round(self.startverdi/2)), int(round(self.sluttverdi/2)))
            self.c = random.randint (int(round(self.startverdi/2)), int(round(self.sluttverdi/2)))

            self.g = random.randint (0, self.lengdePåListe - 1)
            
            
            self.x = self.xverdiListe[self.g]

            del self.xverdiListe[self.g]
            self.lengdePåListe -= 1          
         
            if self.a == 0:
                self.a =+ self.a + 1

            self.d = self.a*self.x*self.x + self.b*self.x + self.c
            self.nyC = self.c + self.d * (-1)
            
            self.x2 = (self.b*(-1) - math.sqrt(self.b**2 - 4 * self.a * self.nyC))/ (2 * self.a)

            if self.x2 == self.x:
                self.x2 = (self.b*(-1) + math.sqrt(self.b**2 - 4 * self.a * self.nyC))/ (2 * self.a)

            if isinstance(self.x2, float):
                self.x2 = round(float(self.x2), 2)

            if self.x2 == int(self.x2):
                self.x2 = int(self.x2)
            
            if self.b == 0 and self.c > 0:
                if self.a == 1:
                    self.likning = "x² + {} = {}".format(self.c, self.d)
                elif self.a == -1:
                    self.likning = "-x² + {} = {}".format(self.c, self.d)
                else:
                    self.likning = "{}x² + {} = {}".format(self.a, self.c, self.d)
            elif self. b == 0 and self.c == 0:
                if self.a == 1:
                    self.likning = "x² = {}".format(self.d)
                elif self.a == -1:
                    self.likning = "-x² = {}".format(self.d)
                else:
                    self.likning = "{}x² = {}".format(self.a, self.d)
            elif self.b == 0 and self.c < 0:
                if self.a == 1:
                    self.likning = "x² - {} = {}".format(self.c*(-1), self.d)
                elif self.a == -1:
                    self.likning = "-x² - {} = {}".format(self.c*(-1), self.d)
                else:
                    self.likning = "{}x² - {} = {}".format(self.a, self.c*(-1), self.d)
            elif self.b < 0 and self.c > 0:
                if self.a == 1:
                    if self.b == -1:
                        self.likning = "x² - x + {} = {}".format(self.c, self.d)
                    else:
                        self.likning = "x² - {}x + {} = {}".format(self.b*(-1), self.c, self.d)
                elif self.a == -1:
                    if self.b == -1:
                        self.likning = "-x² - x + {} = {}".format(self.c, self.d)
                    else:
                        self.likning = "-x² - {}x + {} = {}".format(self.b*(-1), self.c, self.d)
                else:
                    if self.b == -1:
                        self.likning = "{}x² - x + {} = {}".format(self.a, self.c, self.d)
                    else:
                        self.likning = "{}x² - {}x + {} = {}".format(self.a, self.b*(-1), self.c, self.d)
            elif self.b < 0 and self.c == 0:
                if self.a == 1:
                    if self.b == -1:
                        self.likning = "x² - x = {}".format(self.d)
                    else:
                        self.likning = "x² - {}x = {}".format(self.b*(-1), self.d)
                elif self.a == -1:
                    if self.b == -1:
                        self.likning = "-x² - x = {}".format(self.d)
                    else:
                        self.likning = "-x² - {}x = {}".format(self.b*(-1), self.d)
                else:
                    if self.b == -1:
                        self.likning = "{}x² - x = {}".format(self.a, self.d)
                    else:
                        self.likning = "{}x² - {}x = {}".format(self.a, self.b*(-1), self.d)
            elif self.b < 0 and self.c < 0:
                if self.a == 1:
                    if self.b == -1:
                        self.likning = "x² - x - {} = {}".format(self.c*(-1), self.d)
                    else:
                        self.likning = "x² - {}x - {} = {}".format(self.b*(-1), self.c*(-1), self.d)
                elif self.a == -1:
                    if self.b == -1:
                        self.likning = "-x² - x - {} = {}".format(self.c*(-1), self.d)
                    else:
                        self.likning = "-x² - {}x - {} = {}".format(self.b*(-1), self.c*(-1), self.d)
                else:
                    if self.b == -1:
                        self.likning = "{}x² - x - {} = {}".format(self.a, self.c*(-1), self.d)
                    else:
                        self.likning = "{}x² - {}x - {} = {}".format(self.a, self.b*(-1), self.c*(-1), self.d)
            elif self.c == 0 and self.b > 0:
                if self.a == 1:
                    if self.b == 1:
                        self.likning = "x² + x = {}".format(self.d)
                    else:
                        self.likning = "x² + {}x = {}".format(self.b, self.d)
                elif self.a == -1:
                    if self.b == 1:
                        self.likning = "-x² + x = {}".format(self.d)
                    else:
                        self.likning = "-x² + {}x = {}".format(self.b, self.d)
                else:
                    if self.b == 1:
                        self.likning = "{}x² + x = {}".format(self.a, self.d)
                    else:
                        self.likning = "{}x² + {}x = {}".format(self.a, self.b, self.d)
            elif self.c < 0 and self.b > 0:
                if self.a == 1:
                    if self.b == 1:
                        self.likning = "x² + x - {} = {}".format(self.c*(-1), self.d)
                    else:
                        self.likning = "x² + {}x - {} = {}".format(self.b, self.c*(-1), self.d)
                elif self.a == -1:
                    if self.b == 1:
                        self.likning = "x² + x - {} = {}".format(self.c*(-1), self.d)
                    else:
                        self.likning = "x² + {}x - {} = {}".format(self.b, self.c*(-1), self.d)
                else:
                    if self.b == 1:
                        self.likning = "{}x² + x - {} = {}".format(self.a, self.c*(-1), self.d)
                    else:
                        self.likning = "{}x² + {}x - {} = {}".format(self.a, self.b, self.c*(-1), self.d)
            elif self.c > 0 and self.b > 0:
                if self.a == 1:
                    if self.b == 1:
                        self.likning = "x² + x + {} = {}".format(self.c, self.d)
                    else:
                        self.likning = "x² + {}x + {} = {}".format(self.b, self.c, self.d)
                elif self.a == -1:
                    if self.b == 1:
                        self.likning = "-x² + x + {} = {}".format(self.c, self.d)
                    else:
                        self.likning = "-x² + {}x + {} = {}".format(self.b, self.c, self.d)
                else:
                    if self.b == 1:
                        self.likning = "{}x² + x + {} = {}".format(self.a, self.c, self.d)
                    else:
                        self.likning = "{}x² + {}x + {} = {}".format(self.a, self.b, self.c, self.d)

            oppgaveListe.append(self.likning)
            svarListe.append("x = " + str(int(self.x)) + "  og  x = " + str(self.x2))

    def regnerekkefølge (self):
        self.lengdeStorSvarListe = 120
        self.startStorSvarListe = -20
        self.storSvarListe = []

        self.s = self.startStorSvarListe
        for i in range (self.lengdeStorSvarListe + 1):
            self.storSvarListe.append(self.s)
            self.s += 1
            
        for i in range (self.antall):

            self.g = random.randint (0, self.lengdeStorSvarListe - 1)
            self.e = self.storSvarListe[self.g]
            del self.storSvarListe[self.g]
            self.lengdeStorSvarListe -= 1

            self.regnestykke = random.randint(1,5)
            
            if self.regnestykke == 1:
                self.a = random.randint (-20, 50)
                if self.a == 0:
                    self.a += random.randint (1, 20)
                self.b = random.randint (-10, 10)
                self.c = random.randint (-10, 10)
                self.d = self.e - self.a - self.b * self.c

                if self.b >= 0:
                    if self.c >= 0:
                        if self.d > 0:
                            self.uttrykk = "{} + {} · {} + {}".format(self.a, self.b, self.c, self.d)
                        elif self.d == 0:
                            self.uttrykk = "{} + {} · {}".format(self.a, self.b, self.c)
                        else:
                            self.uttrykk = "{} + {} · {} - {}".format(self.a, self.b, self.c, self.d*(-1))
                    else:
                        if self.d > 0:
                            self.uttrykk = "{} + {} · ({}) + {}".format(self.a, self.b, self.c, self.d)
                        elif self.d == 0:
                            self.uttrykk = "{} + {} · ({})".format(self.a, self.b, self.c)
                        else:
                            self.uttrykk = "{} + {} · ({}) - {}".format(self.a, self.b, self.c, self.d*(-1))
                else:
                    if self.c >= 0:
                        if self.d > 0:
                            self.uttrykk = "{} + ({}) · {} + {}".format(self.a, self.b, self.c, self.d)
                        elif self.d == 0:
                            self.uttrykk = "{} + ({}) · {}".format(self.a, self.b, self.c)
                        else:
                            self.uttrykk = "{} + ({}) · {} - {}".format(self.a, self.b, self.c, self.d*(-1))
                    else:
                        if self.d > 0:
                            self.uttrykk = "{} + ({}) · ({}) + {}".format(self.a, self.b, self.c, self.d)
                        elif self.d == 0:
                            self.uttrykk = "{} + ({}) · ({})".format(self.a, self.b, self.c)
                        else:
                            self.uttrykk = "{} + ({}) · ({}) - {}".format(self.a, self.b, self.c, self.d*(-1))

            if self.regnestykke == 2:
                self.a = random.randint (-20, 50)
                if self.a == 0:
                    self.a += random.randint (1, 20)
                self.b = random.randint (-10, 10)
                self.c = random.randint (-10, 10)
                self.d = self.e - self.a - self.b * self.c

                if self.b >= 0:
                    if self.c >= 0:
                        if self.d > 0:
                            self.uttrykk = "{} + {} + {} · {}".format(self.a, self.d, self.b, self.c)
                        elif self.d == 0:
                            self.uttrykk = "{} + {} · {}".format(self.a, self.b, self.c)
                        else:
                            self.uttrykk = "{} - {} + {} · {}".format(self.a, self.d*(-1), self.b, self.c)
                    else:
                        if self.d > 0:
                            self.uttrykk = "{} + {} + {} · ({})".format(self.a, self.d, self.b, self.c)
                        elif self.d == 0:
                            self.uttrykk = "{} + {} · ({})".format(self.a, self.b, self.c)
                        else:
                            self.uttrykk = "{} - {} + {} · ({})".format(self.a, self.d*(-1), self.b, self.c)
                else:
                    if self.c >= 0:
                        if self.d > 0:
                            self.uttrykk = "{} + {} + ({}) · {}".format(self.a, self.d, self.b, self.c)
                        elif self.d == 0:
                            self.uttrykk = "{} + ({}) · {}".format(self.a, self.b, self.c)
                        else:
                            self.uttrykk = "{} - {} + ({}) · {}".format(self.a, self.d*(-1), self.b, self.c)
                    else:
                        if self.d > 0:
                            self.uttrykk = "{} + {} + ({}) · ({})".format(self.a, self.d, self.b, self.c)
                        elif self.d == 0:
                            self.uttrykk = "{} + ({}) · ({})".format(self.a, self.b, self.c)
                        else:
                            self.uttrykk = "{} - {} + ({}) · ({})".format(self.a, self.d*(-1), self.b, self.c)

            if self.regnestykke == 3:
                self.a = random.randint (-10, 10)
                if self.a == 0:
                    self.a += random.randint (1, 20)
                self.b = random.randint (-10, 10)
                self.c = random.randint (-10, 10)
                while self.a + self.b > 10:
                    self.b -= random.randint (1, 9)
                while self.a + self.b < (-10):
                    self.b += random.randint (1, 9)
                self.d = self.e - (self.a + self.b) * self.c

                if self.b >= 0:
                    if self.c >= 0:
                        if self.d > 0:
                            self.uttrykk = "({} + {}) · {} + {}".format(self.a, self.b, self.c, self.d)
                        elif self.d == 0:
                            self.uttrykk = "({} + {}) · {}".format(self.a, self.b, self.c)
                        else:
                            self.uttrykk = "({} + {}) · {} - {}".format(self.a, self.b, self.c, self.d*(-1))
                    else:
                        if self.d > 0:
                            self.uttrykk = "({} + {}) · ({}) + {}".format(self.a, self.b, self.c, self.d)
                        elif self.d == 0:
                            self.uttrykk = "({} + {}) · ({})".format(self.a, self.b, self.c)
                        else:
                            self.uttrykk = "({} + {}) · ({}) - {}".format(self.a, self.b, self.c, self.d*(-1))
                else:
                    if self.c >= 0:
                        if self.d > 0:
                            self.uttrykk = "({} - {}) · {} + {}".format(self.a, self.b*(-1), self.c, self.d)
                        elif self.d == 0:
                            self.uttrykk = "({} - {}) · {}".format(self.a, self.b*(-1), self.c)
                        else:
                            self.uttrykk = "({} - {}) · {} - {}".format(self.a, self.b*(-1), self.c, self.d*(-1))
                    else:
                        if self.d > 0:
                            self.uttrykk = "({} - {}) · ({}) + {}".format(self.a, self.b*(-1), self.c, self.d)
                        elif self.d == 0:
                            self.uttrykk = "({} - {}) · ({})".format(self.a, self.b*(-1), self.c)
                        else:
                            self.uttrykk = "({} - {}) · ({}) - {}".format(self.a, self.b*(-1), self.c, self.d*(-1))

            if self.regnestykke == 4:
                
                self.b = random.randint (-10, 10)
                self.c = random.randint (-10, 10)
                self.d = random.randint (-20, 20)
                while self.c + self.d > 10:
                    self.d -= random.randint (1, 9)
                while self.c + self.d < (-10):
                    self.d += random.randint (1, 9)
                self.a = self.e - self.b * (self.c + self.d)

                if self.b >= 0:
                    if self.c >= 0:
                        if self.d >= 0:
                            if self.a == 0:
                                self.uttrykk = "{} · ({} + {})".format(self.b, self.c, self.d)
                            else:
                                self.uttrykk = "{} + {} · ({} + {})".format(self.a, self.b, self.c, self.d)
                        else:
                            if self.a == 0:
                                self.uttrykk = "{} · ({} - {})".format(self.b, self.c, self.d*(-1))
                            else:
                                self.uttrykk = "{} + {} · ({} - {})".format(self.a, self.b, self.c, self.d*(-1))
                    else:
                        if self.d >= 0:
                            if self.a == 0:
                                self.uttrykk = "{} · (({}) + {})".format(self.b, self.c, self.d)
                            else:
                                self.uttrykk = "{} + {} · (({}) + {})".format(self.a, self.b, self.c, self.d)
                        else:
                            if self.a == 0:
                                self.uttrykk = "{} · (({}) - {})".format(self.b, self.c, self.d*(-1))
                            else:
                                self.uttrykk = "{} + {} · (({}) - {})".format(self.a, self.b, self.c, self.d*(-1))
                else:
                    if self.c >= 0:
                        if self.d > 0:
                            if self.a == 0:
                                self.uttrykk = "{} · ({} + {})".format(self.b, self.c, self.d)
                            else:
                                self.uttrykk = "{} - {} · ({} + {})".format(self.a, self.b*(-1), self.c, self.d)
                        else:
                            if self.a == 0:
                                self.uttrykk = "{} · ({} - {})".format(self.b, self.c, self.d*(-1))
                            else:
                                self.uttrykk = "{} - {} · ({} - {})".format(self.a, self.b*(-1), self.c, self.d*(-1))
                    else:
                        if self.d > 0:
                            if self.a == 0:
                                self.uttrykk = "{} · (({}) + {})".format(self.b, self.c, self.d)
                            else:
                                self.uttrykk = "{} - {} · (({}) + {})".format(self.a, self.b*(-1), self.c, self.d)
                        else:
                            if self.a == 0:
                                self.uttrykk = "{} · (({}) - {})".format(self.b, self.c, self.d*(-1))
                            else:
                                self.uttrykk = "{} - {} · (({}) - {})".format(self.a, self.b*(-1), self.c, self.d*(-1))

            if self.regnestykke == 5:
                self.a = random.randint (-20, 50)
                if self.a == 0:
                    self.a += random.randint (1, 20)
                self.b = random.randint (-10, 10)
                self.c = random.randint (-10, 10)
                self.d = self.e - self.a - self.b * self.c

                if self.b >= 0:
                    if self.c >= 0:
                        if self.d >= 0:
                            self.uttrykk = "{} + ({} + {} · {})".format(self.a, self.d, self.b, self.c)
                        else:
                            self.uttrykk = "{} - ({} - {} · {})".format(self.a, self.d*(-1), self.b, self.c)
                    else:
                        if self.d >= 0:
                            self.uttrykk = "{} + ({} + {} · ({}))".format(self.a, self.d, self.b, self.c)
                        else:
                            self.uttrykk = "{} - ({} - {} · ({}))".format(self.a, self.d*(-1), self.b, self.c)
                else:
                    if self.c >= 0:
                        if self.d > 0:
                            self.uttrykk = "{} + ({} - {} · {})".format(self.a, self.d, self.b*(-1), self.c)
                        else:
                            self.uttrykk = "{} - ({} + {} · {})".format(self.a, self.d*(-1), self.b*(-1), self.c)
                    else:
                        if self.d > 0:
                            self.uttrykk = "{} + ({} - {} · ({}))".format(self.a, self.d, self.b*(-1), self.c)
                        else:
                            self.uttrykk = "{} - ({} + {} · ({}))".format(self.a, self.d*(-1), self.b*(-1), self.c)

            oppgaveListe.append(self.uttrykk)
            svarListe.append(str(self.e))
        
"""
    def omgjøringsoppgaverProsent (self):
        self.typeOppgave = input("Vil du ha fra prosent til desimaltall (PD), prosent til brøk (PB), ")

        self.a = random.randint (1,5)
        if self.a < 5:
            self.oppgave = random.randint (1,100)
        else:
            self.oppgave = random.randint (100, 300)
"""        

"""Under her kommer selve PDF-oppbyggningen og layouten"""

#A4 er 210 × 297 millimeter
bredde = 297 #A4
høyde = 210 #A4

senterBredde = bredde/2
senterHøyde = høyde/2

oppgavenummer = [1] #en liste som skal inneholde nummerene 1 til a
oppgavenummerIRekkefølge = []

pdf = FPDF("L")
pdf.set_margins(0, 0, 0)
pdf.set_auto_page_break(bool, 0.0)

def tegnIndreSirkelMedPil (radiusStor, radiusLiten, antallPiler):

    radiusPilSirkel = radiusStor - (radiusLiten*2)
    pdf.ellipse(senterBredde-radiusPilSirkel, senterHøyde-radiusPilSirkel, 2*radiusPilSirkel, 2*radiusPilSirkel, "D")

    if antallPiler >= 4:
        """Høyre pil"""
        startpunktPilH_x = senterBredde + radiusPilSirkel - radiusLiten/3
        sluttpunktPilH_x = senterBredde + radiusPilSirkel + radiusLiten/3
        startpunktPilH_y = senterHøyde - radiusLiten/3
    
        while sluttpunktPilH_x - startpunktPilH_x > 0.1:
            pdf.line(startpunktPilH_x, startpunktPilH_y, sluttpunktPilH_x, startpunktPilH_y)
            startpunktPilH_x += 0.1/2
            sluttpunktPilH_x -= 0.1/2
            startpunktPilH_y += 0.1

    if antallPiler >= 3:
        """Venstre pil"""
        startpunktPilV_x = senterBredde - radiusPilSirkel - radiusLiten/3
        sluttpunktPilV_x = senterBredde - radiusPilSirkel + radiusLiten/3
        startpunktPilV_y = senterHøyde + radiusLiten/3
    
        while sluttpunktPilV_x - startpunktPilV_x > 0.1:
            pdf.line(startpunktPilV_x, startpunktPilV_y, sluttpunktPilV_x, startpunktPilV_y)
            startpunktPilV_x += 0.1/2
            sluttpunktPilV_x -= 0.1/2
            startpunktPilV_y -= 0.1

    if antallPiler >= 2:
        """Øvre pil"""
        startpunktPilØ_x = senterBredde - radiusLiten/3
        startpunktPilØ_y = senterHøyde - radiusPilSirkel - radiusLiten/3
        sluttpunktPilØ_y = senterHøyde - radiusPilSirkel + radiusLiten/3
    
        while sluttpunktPilØ_y - startpunktPilØ_y > 0.1:
            pdf.line(startpunktPilØ_x, startpunktPilØ_y, startpunktPilØ_x, sluttpunktPilØ_y)
            startpunktPilØ_x += 0.1
            sluttpunktPilØ_y -= 0.1/2
            startpunktPilØ_y += 0.1/2

    if antallPiler >= 1:
        """Nedre pil"""
        startpunktPilN_x = senterBredde + radiusLiten/3
        sluttpunktPilN_y = senterHøyde + radiusPilSirkel + radiusLiten/3
        startpunktPilN_y = senterHøyde + radiusPilSirkel - radiusLiten/3
    
        while sluttpunktPilN_y - startpunktPilN_y > 0.1:
            pdf.line(startpunktPilN_x, startpunktPilN_y, startpunktPilN_x, sluttpunktPilN_y)
            startpunktPilN_x -= 0.1
            sluttpunktPilN_y -= 0.1/2
            startpunktPilN_y += 0.1/2


def tegnSirklerMedTall (antallOppgaver):
    pdf.add_page()
    
    vinkelGrad = 360/antallOppgaver #Vinkel mellom de små sirklene fra senter
    vinkelRad = math.radians(vinkelGrad)
    retning = 0 #startvinkel i radianer
    maksVinkel = math.radians(359)

    if antallOppgaver > 9:
        radiusStor = senterHøyde-vinkelGrad*1.5 #radius fra senter av arket og ut til sirklene
    else:
        radiusStor = senterHøyde-40

    d = tall
    while radiusStor > senterHøyde-10: #For å holde litt avstand til kanten
        radiusStor -= 1

    radiusLiten = radiusStor*3/antallOppgaver
    diameterLiten = radiusLiten * 2

    tekstStørrelse = round(diameterLiten)
    pdf.set_font("Arial", "B", tekstStørrelse)

    while retning < maksVinkel:
        c = random.randint(0, d)
        xVerdi = senterBredde + math.cos(retning)*radiusStor - radiusLiten
        yVerdi = senterHøyde + math.sin(retning)*radiusStor - radiusLiten
        pdf.ellipse(xVerdi, yVerdi, diameterLiten, diameterLiten, "D")
        pdf.set_xy(xVerdi, yVerdi)
        tekst = str(oppgavenummer[c])
        pdf.cell(diameterLiten, diameterLiten, tekst, 0, 0, "C")
        retning += vinkelRad
        oppgavenummerIRekkefølge.append(oppgavenummer[c])
        del oppgavenummer[c]
        d -= 1

    if a >= 20:
        tegnIndreSirkelMedPil (radiusStor, radiusLiten, 4)
    elif a < 20 and a > 15:
        tegnIndreSirkelMedPil (radiusStor + radiusLiten/2, radiusLiten, 4)
    elif a <= 15 and a > 7:
        tegnIndreSirkelMedPil (radiusStor + radiusLiten/2, radiusLiten, 2)

    if a < 13 and a > 7:
        pdf.set_font_size(radiusStor-radiusLiten)
    elif a < 8:
        pdf.set_font_size(radiusStor-radiusLiten/2)
    else:
        pdf.set_font_size(radiusStor)

    pdf.set_xy(senterBredde-radiusStor, senterHøyde-radiusStor)
    pdf.cell(radiusStor*2, radiusStor*2, "Fasit", 0,  0, "C")

def tegnSirklerUtenTall (antallOppgaver):
    pdf.add_page()
    
    vinkelGrad = 360/antallOppgaver #Vinkel mellom de små sirklene fra senter
    vinkelRad = math.radians(vinkelGrad)
    retning = 0 #startvinkel i radianer
    maksVinkel = math.radians(359)

    if antallOppgaver > 9:
        radiusStor = senterHøyde-vinkelGrad*1.5 #radius fra senter av arket og ut til sirklene
    else:
        radiusStor = senterHøyde-40

    while radiusStor > senterHøyde-10: #For å holde litt avstand til kanten
        radiusStor -= 1

    radiusLiten = radiusStor*3/antallOppgaver
    diameterLiten = radiusLiten * 2
        
    tekstStørrelse = round(diameterLiten)
    pdf.set_font("Arial", "B", tekstStørrelse)

    while retning < maksVinkel:
        xVerdi = senterBredde + math.cos(retning)*radiusStor - radiusLiten
        yVerdi = senterHøyde + math.sin(retning)*radiusStor - radiusLiten
        pdf.ellipse(xVerdi, yVerdi, diameterLiten, diameterLiten, "D")
        pdf.set_xy(xVerdi, yVerdi)
        retning += vinkelRad

    if a < 20 and a > 15:
        tegnIndreSirkelMedPil (radiusStor + radiusLiten/2, radiusLiten, 4)
    elif a <= 15 and a > 7:
        tegnIndreSirkelMedPil (radiusStor + radiusLiten/2, radiusLiten, 2)
    elif a >= 20:
        tegnIndreSirkelMedPil (radiusStor, radiusLiten, 4)

    if a < 13 and a > 7:
        pdf.set_font_size(radiusStor-radiusLiten)
    elif a < 8:
        pdf.set_font_size(radiusStor-radiusLiten/2)
    else:
        pdf.set_font_size(radiusStor)

    pdf.set_xy(senterBredde-radiusStor, senterHøyde-radiusStor)
    pdf.cell(radiusStor*2, radiusStor*2, "Svarark", 0,  0, "C")

def oppgavegenerator (antallOppgaver): #Alle sidene med oppgaver, nummereringer og svar
    f = antallOppgaver
    dLO = 20 #diameter i liten sirkel med oppgavenummer
    
    #Her er fonten som bør brukes, må installeres på andre datamaskiner som skal bruke programmet
    pdf.add_font('sysfont', '', r"C:\Users\joboe\AppData\Local\Microsoft\Windows\Fonts\DejaVuSerif.ttf", uni=True)
    pdf.set_font('sysfont', '', dLO)
    
    for i in range(f):
        pdf.add_page()
        pdf.set_line_width(1)
        pdf.ellipse(10, høyde-dLO-10, dLO, dLO, "D") #Om man ønsker sirkel rundt tallet kan denne brukes. Da må rammen fjernes i cellen med tekst.
        pdf.set_font_size(dLO)
        pdf.set_xy(10, høyde-dLO-10)
        nummer = str(int(oppgavenummerIRekkefølge[i]))
        pdf.cell(dLO, dLO, nummer, 0,  0, "C")
        pdf.set_font_size(høyde/5)
        pdf.set_xy(10, høyde/5)
        oppgaveTekst = oppgaveListe [i]
        korreksjon = (i-1)
        if korreksjon < 0:
            korreksjon = korreksjon + f
        svarPåForrigeOppgave = svarListe [korreksjon]
        pdf.cell(bredde-20, 4*høyde/5, oppgaveTekst, 0, 0, "C")
        pdf.set_xy(10, 0)
        pdf.cell(bredde-20, høyde/5, svarPåForrigeOppgave, "B",  0, "C")
        pdf.set_line_width(0.2)

#Setter destinasjonen til en ny mappe på skrivebordet kalt "PDF-filer"
skrivebord = os.getcwd()
plassering = os.path.join(skrivebord, "PDF-filer")

#Om mappen ikke fungerer lager vi den:
if not os.path.exists(plassering):
    os.mkdir(plassering)

 #Testen
master = tk.Tk()
master.title("Loopgenerator")

spm1 = tk.Label(master, text="Hvor mange oppgaver vil du ha?").grid(row = 0)
e1 = tk.Entry(master)
e1.grid(row=1, column=0)

def oppgaveLin ():
    global a
    global b
    global tall
    global filnavn
    global filnavnIMappe
    global oppgavetype
    oppgavetype = "Lineære likninger"
    a = int(e1.get())
    lageOppgaver(a).lineæreLikninger()
    tall = a-1
    b = 1
    while b < a: #Lager listen med tall
        oppgavenummer.append(b + 1)
        b += 1
    tegnSirklerMedTall(a)
    tegnSirklerUtenTall (a)
    oppgavegenerator (a)
    filnavn = "Loop - " + oppgavetype + " - " + str(a) + " oppgaver" + ".pdf"
    filnavnIMappe = plassering + "\\" + "{}".format(filnavn)

    if a >= 6:
        pdf.output(filnavnIMappe, "F")
    master.destroy()
    os.startfile (plassering) #Åpner mappen med filen

def oppgaveAnd ():
    global a
    global b
    global tall
    global filnavn
    global filnavnIMappe
    global oppgavetype
    oppgavetype = "Andregradslikninger"
    a = int(e1.get())
    lageOppgaver(a).andregradslikninger()
    tall = a-1
    b = 1
    while b < a: #Lager listen med tall
        oppgavenummer.append(b + 1)
        b += 1
    tegnSirklerMedTall(a)
    tegnSirklerUtenTall (a)
    oppgavegenerator (a)
    filnavn = "Loop - " + oppgavetype + " - " + str(a) + " oppgaver" + ".pdf"
    filnavnIMappe = plassering + "\\" + "{}".format(filnavn)

    if a >= 6:
        pdf.output(filnavnIMappe, "F")
    master.destroy()
    os.startfile (plassering) #Åpner mappen med filen

def oppgaveRegn ():
    global a
    global b
    global tall
    global filnavn
    global filnavnIMappe
    global oppgavetype
    oppgavetype = "Regnerekkefølge"
    a = int(e1.get())
    lageOppgaver(a).regnerekkefølge()
    tall = a-1
    b = 1
    while b < a: #Lager listen med tall
        oppgavenummer.append(b + 1)
        b += 1
    tegnSirklerMedTall(a)
    tegnSirklerUtenTall (a)
    oppgavegenerator (a)
    filnavn = "Loop - " + oppgavetype + " - " + str(a) + " oppgaver" + ".pdf"
    filnavnIMappe = plassering + "\\" + "{}".format(filnavn)

    if a >= 6:
        pdf.output(filnavnIMappe, "F")
    master.destroy()
    os.startfile (plassering) #Åpner mappen med filen

oppgaveValg = tk.Label(master, text="Hvilken oppgavetype vil bruke?").grid(row = 5)

knapp1 = tk.Button(master, text='Lineære likninger', command=oppgaveLin).grid(row=6, column=0, pady=4)
knapp2 = tk.Button(master, text='Andregradslikninger', command=oppgaveAnd).grid(row=7, column=0, pady=4)
knapp3 = tk.Button(master, text='Regnerekkefølge', command=oppgaveRegn).grid(row=8, column=0, pady=4)
"""
knapp4 = tk.Button(master, 
          text='Prosentregning', command=oppgavePros).grid(row=9, 
                                                        column=0, 
                                                        pady=4)
"""
master.mainloop()