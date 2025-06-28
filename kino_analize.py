import json
PATH = "imdb_top_999.json" # put the path to your file here

with open(PATH, "r") as f:
    data = json.load(f)

TO_DELETE = ["No_of_Votes", "Overview", "Meta_score"]

for kino in data.keys():
    for k in TO_DELETE:
        del data[kino][k]

    data[kino]["Name"] = kino

class Movie:
    Released_Year = None
    Runtime = None
    Genre = None
    IMDB_Rating = None
    Director = None
    Star1 = None
    Star2 = None
    Star3 = None
    Star4 = None
    Gross = None
    Name = None

    def __init__(self, R_Y = None, RT = None, G = None, I_R = None, D = None, S1 = None, S2 = None, S3 = None, S4 = None, Gr = None, N = None): 
        self.Released_Year = R_Y
        self.Runtime = RT
        self.Genre = G
        self.IMDB_Rating = I_R
        self.Director = D
        self.Star1 = S1
        self.Star2 = S2
        self.Star3 = S3
        self.Star4 = S4
        self.Gross = Gr
        self.Name = N


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