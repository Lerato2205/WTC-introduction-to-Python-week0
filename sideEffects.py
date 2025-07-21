emoticon = "😊"

def main():
    global emoticon
    say("Im getting married")
    emoticon =  ":D"
    say("Congratulations!!!")

def say (phrase):
    print(phrase + "" + emoticon)

main()