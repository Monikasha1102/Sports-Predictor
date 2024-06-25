from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import csv

# Function to handle the first window
def first():
    global combo1, combo2, combo3, combo4, f, e, root, backimage

    root = Tk()
    root.geometry("900x550")
    root.resizable(0, 0)
    root.title("Sports Predictor")
    canvas = Canvas(root, height=550, width=900)
    canvas.pack()

    backimage = PhotoImage(file='C:\\Users\\msharma348\\OneDrive - DXC Production\\Desktop\\ipl match//pic1.png')
    imagelabel = Label(root, image=backimage)
    imagelabel.place(x=0, y=0, relwidth=1, relheight=1)

    label1 = Label(root, text="S P O R T S   P R E D I C T O R", font=('Antique Olive', 13, 'bold'), fg="black")
    label1.place(x=329, y=120)

    button1 = Button(root, font=('Antique Olive', 13, 'bold'), text="START", height=1, width=8, fg="blue", command=second)
    button1.place(x=780, y=450)

    root.mainloop()

# Function to handle the second window
def second():
    global combo1, combo2, combo3, combo4, combo5, combo6, txt, root1, backimage2

    root1 = Toplevel()
    root1.geometry("900x550")
    root1.resizable(0, 0)
    
    canvas1 = Canvas(root1, height=550, width=900)
    canvas1.pack()

    backimage2 = PhotoImage(file='C:\\Users\\msharma348\\OneDrive - DXC Production\\Desktop\\ipl match//pic2.png')
    imagelabel2 = Label(root1, image=backimage2)
    imagelabel2.place(x=0, y=0, relwidth=1, relheight=1)

    v1 = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Gujarat Lions',
          'Rising Pune Supergiant', 'Royal Challengers Bangalore',
          'Kolkata Knight Riders', 'Delhi Daredevils', 'Kings XI Punjab',
          'Chennai Super Kings', 'Rajasthan Royals', 'Deccan Chargers',
          'Kochi Tuskers Kerala', 'Pune Warriors', 'Rising Pune Supergiants']
    combo1 = Combobox(root1, values=v1, width=15, height=2, font=('CG Times', 12, 'bold'))
    combo1.place(x=140, y=150)
    combo1.set("")

    combo2 = Combobox(root1, values=v1, width=15, height=2, font=('CG Times', 12, 'bold'))
    combo2.place(x=600, y=150)
    combo2.set("")

    label2 = Label(root1, text="V E N U E", font=('Arial black', 13, 'bold'), fg="black", bg="white")
    label2.place(x=290, y=190)

    label3 = Label(root1, text="C I T Y", font=('Arial black', 13, 'bold'), fg="black", bg="white")
    label3.place(x=313, y=225)

    v3 = ["Rajiv Gandhi International Stadium, Uppal", "Maharashtra Cricket Association Stadium", "Saurashtra Cricket Association Stadium", "Holkar Cricket Stadium", "M Chinnaswamy Stadium","Wankhede Stadium", "Eden Gardens",
          "Feroz Shah Kotla","Punjab Cricket Association IS Bindra Stadium, Mohali","Green Park", "Punjab Cricket Association Stadium, Mohali","Sawai Mansingh Stadium", "MA Chidambaram Stadium, Chepauk","Dr DY Patil Sports Academy", "Newlands", "St George's Park","Kingsmead", "SuperSport Park", "Buffalo Park","New Wanderers Stadium", "De Beers Diamond Oval","OUTsurance Oval", "Brabourne Stadium","Sardar Patel Stadium, Motera", "Barabati Stadium",
          "Vidarbha Cricket Association Stadium, Jamtha",
          "Himachal Pradesh Cricket Association Stadium", "Nehru Stadium",
          "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
          "Subrata Roy Sahara Stadium",
          "Shaheed Veer Narayan Singh International Stadium",
          "JSCA International Stadium Complex", "Sheikh Zayed Stadium",
          "Sharjah Cricket Stadium", "Dubai International Cricket Stadium"]
    combo3 = Combobox(root1, values=v3, width=35, height=2, font=('CG Times', 12, 'bold'))
    combo3.place(x=430, y=190)
    combo3.set("")

    v4 = ['Hyderabad', 'Pune', 'Rajkot', 'Indore', 'Bangalore', 'Mumbai',
          'Kolkata', 'Delhi', 'Chandigarh', 'Kanpur', 'Jaipur', 'Chennai',
          'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
          'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
          'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Kochi',
          'Visakhapatnam', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah',
          'Dubai']
    combo4 = Combobox(root1, values=v4, width=15, height=2, font=('CG Times', 12, 'bold'))
    combo4.place(x=450, y=225)
    combo4.set("")

    label4 = Label(root1, text="Toss Winner", font=('Arial black', 13, 'bold'), fg="black", bg="white")
    label4.place(x=120, y=260)

    combo5 = Combobox(root1, values=v1, width=15, height=2, font=('CG Times', 12, 'bold'))
    combo5.place(x=120, y=300)
    combo5.set("")

    label5 = Label(root1, text="Toss Decision", font=('Arial black', 13, 'bold'), fg="black", bg="white")
    label5.place(x=620, y=260)

    v6 = ['field', 'bat']
    combo6 = Combobox(root1, values=v6, width=15, height=2, font=('CG Times', 12, 'bold'))
    combo6.place(x=610, y=300)
    combo6.set("")

    button2 = Button(root1, font=('Arial black', 13, 'bold'), text="PREDICT", height=1, width=8, fg="black", command=made)
    button2.place(x=650, y=360)

    label6 = Label(root1, text="OUTPUT", font=('Arial black', 13, 'bold'), fg="black", bg="white")
    label6.place(x=150, y=360)

    txt = Text(root1, width=15, height=1, font=("courier new", 25, "bold"), bg="white", fg="red", bd=20, wrap=WORD)
    txt.place(x=90, y=400)

    root1.mainloop()

# Function to handle the prediction
def made():
    a = combo1.get()
    b = combo2.get()
    c = combo4.get()
    d = combo3.get()
    e = combo5.get()
    f = combo6.get()

    team1 = [a]
    team2 = [b]
    city = [c]
    venue = [d]
    toss_winner = [e]
    toss_decision = [f]

    team1 = team1 + team2 + city + toss_decision + toss_winner + venue

    fields = ['team1', 'team2', 'city', 'toss_decision', 'toss_winner', 'venue']

    test = "IPLdemo.csv"

    with open(test, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(fields)
        csvwriter.writerow(team1)

    data = pd.read_csv("C:\\Users\\msharma348\\OneDrive - DXC Production\\Desktop\\ipl match/deliveries.csv")
    match = pd.read_csv("C:\\Users\\msharma348\\OneDrive - DXC Production\\Desktop\\ipl match/matches.csv")

    match = match.drop("umpire3", axis='columns')
    match['winner'] = match['winner'].fillna('Draw')
    match['player_of_match'] = match['player_of_match'].fillna('Match is Draw')
    match['city'] = match['city'].fillna('Dubai')
    match['winner'] = match['winner'].replace(['Rising Pune Supergiant'], 'Rising Pune Supergiants')

    matches = match[['team1', 'team2', 'city', 'toss_decision', 'toss_winner', 'venue', 'winner']]
    matches['team1'] = matches['team1'].replace(['Delhi Daredevils'], 'Delhi Capitals')
    matches['team2'] = matches['team2'].replace(['Delhi Daredevils'], 'Delhi Capitals')
    matches['toss_winner'] = matches['toss_winner'].replace(['Delhi Daredevils'], 'Delhi Capitals')
    matches['winner'] = matches['winner'].replace(['Delhi Daredevils'], 'Delhi Capitals')

    def findteams(venue):
        temp = matches[matches['venue'] == venue]
        a = temp['team1'].value_counts().index.tolist()
        b = temp['team2'].value_counts().index.tolist()
        return list(set(a + b))

    encode = {'team1': {}, 'team2': {}, 'toss_winner': {}, 'venue': {}, 'city': {}, 'winner': {}}

    def encoding(column):
        le = LabelEncoder()
        data = matches[column]._append(pd.Series([team1[0], team1[1], team1[2], team1[3], team1[4], team1[5]]))
        le.fit(data)
        encode[column] = dict(zip(le.classes_, le.transform(le.classes_)))
        return le.transform(matches[column])

    matches['team1'] = encoding('team1')
    matches['team2'] = encoding('team2')
    matches['toss_winner'] = encoding('toss_winner')
    matches['city'] = encoding('city')
    matches['venue'] = encoding('venue')
    matches['winner'] = encoding('winner')
    matches['toss_decision'] = encoding('toss_decision')

    team1 = [encode['team1'][team1[0]], encode['team2'][team1[1]], encode['city'][team1[2]], encode['toss_decision'][team1[3]], encode['toss_winner'][team1[4]], encode['venue'][team1[5]]]

    X = matches[['team1', 'team2', 'city', 'toss_decision', 'toss_winner', 'venue']]
    y = matches['winner']

    model = RandomForestClassifier(n_estimators=100, max_depth=5)
    model.fit(X, y)
    result = model.predict([team1])

    for key, value in encode['winner'].items():
        if value == result:
            output = key

    txt.delete('1.0', END)
    txt.insert(INSERT, output)

first()
