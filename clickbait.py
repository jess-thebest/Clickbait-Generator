#jessica
#7/16/24
#clickbait


#init
#functions
def easy_headline():
    verb = input("Enter a Verb:")
    return ("You Won't Believe How Easy It Is To " + verb + " Click Here To See Now!!")

def vacay_headline():
    place = input("Enter a Place:")
    return (place + " Is The Cheapest and Best Place To Go On Vacation!!")

def activites_headline():
    number = input("Enter a Number:")
    city = input("Enter a City:")
    return (number + " Fun Activies To Do In " + city + "!!!")

def celeb_headline():
    celeb = input("Enter a Celeb:")
    return ("Crazy Rumor that " + celeb + " Has The Same Birthday As You!!!!" )

def company_headline():
    company = input("Enter a Company:" )
    return (company + " Doesn't Want You To Know That Their Products Are Harmful!!!")


def clickbait_headline():
    print(easy_headline())
    print(vacay_headline())
    print(activites_headline())
    print(celeb_headline())
    print(company_headline())

#main
while True:
    print("Welcome to Clickbait Headlines.")
    clickbait_headline()
    ans = input("Do you want to read more headlines? Yes or No")
    if ans == "No": 
        break

