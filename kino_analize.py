import json
from dataclasses import dataclass   
from typing import Optional
PATH = "imdb_top_999.json" # put the path to your file here

with open(PATH, "r") as f:
    data = json.load(f)

TO_DELETE = ["No_of_Votes", "Overview", "Meta_score"]

for kino in data.keys():
    for k in TO_DELETE:
        del data[kino][k]

    data[kino]["Name"] = kino
    
@dataclass
class Movie:
    Released_Year: Optional[str] = None
    Runtime: Optional[str] = None
    Genre: Optional[str] = None
    IMDB_Rating: Optional[str] = None
    Director: Optional[str] = None
    Star1: Optional[str] = None
    Star2: Optional[str] = None
    Star3: Optional[str] = None
    Star4: Optional[str] = None
    Gross: Optional[str] = None
    Name: Optional[str] = None


    @classmethod
    def WithName(cls,name):
        R_Y = data[name]["Released_Year"]
        RT = data[name]["Runtime"]
        G = data[name]['Genre']
        I_R = data[name]['IMDB_Rating']
        D = data[name]['Director']
        S1 = data[name]["Star1"]
        S2 = data[name]["Star2"]
        S3 = data[name]["Star3"]
        S4 = data[name]["Star4"]
        Gr = data[name]['Gross']
        N = name
        return cls(R_Y, RT, G, I_R, D, S1, S2, S3, S4, Gr, N)
    
    def ReturnAct(self):
        print(', '.join([self.Star1, self.Star2,self.Star3,self.Star4]))
    
    @classmethod
    def ReturnActors(cls,name):
        S1 = data[name]["Star1"]
        S2 = data[name]["Star2"]
        S3 = data[name]["Star3"]
        S4 = data[name]["Star4"]
        print(', '.join([S1, S2, S3, S4]))
    
    def DurationByHours(self):
        hours = int((self.Runtime.split())[0]) / 60
        print(round(hours,1))
    
    def AboutFilm(self):
        text = f"""«{self.Name}» ֆիլմում խաղացել են՝ {data[self.Name]['Star1']}, {data[self.Name]['Star2']} և ուրիշներ։ \
Ֆիլմի ռեժիսոր՝ {data[self.Name]['Director']}։ \nՏևում է {data[self.Name]['Runtime']} րոպե։ \
Ժանրը՝ {data[self.Name]['Genre']}։ Թողարկվել է {data[self.Name]['Released_Year']} թվականին։ \
Միջին ռեյտինգ՝ {data[self.Name]['IMDB_Rating']} IMDb-ում։ \
Բյուջեն՝ {data[self.Name]['Gross']} դոլար։  
        """

        print(text)

m = Movie.WithName("The Shawshank Redemption")
m.AboutFilm()