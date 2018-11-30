def compare(a,b):
    if a == "Rock" and b =="Rock":
        print "Match Drawn"
    if a == "Rock" and b == "Paper":
        print "Player1 Won"
    elif a == "Rock" and b =="Scissors":
        print "Player2 Won"
    elif a =="Paper" and b =="Paper":
        print "Match Drawn"
    elif a == "Paper" and b =="Scissors":
        print "Player2 Won"
    elif a == "Paper" and b =="Rock":
        print "Player2 Won"
    elif a == "Scissors" and b =="Scissors":
        print "Match Drawn"
    elif a == "Scissors" and b =="Paper":
        print "Player1 Won"
    elif a == "Scissors" and b =="Rock":
        print "Player1 Won"

a = raw_input("Player1 choose Rock, Paper or Scissors?:")
b = raw_input("Player2 choose Rock, Paper or Scissors?:")
d = compare(a,b)
