## TITLE & INTRO ##

print("-- AP WORLD HISTORY --")
print("UNIT 1 PRACTICE TEST\n")
print("This practice test has 5 questions\nand the answers will be shown\nthroughout the quiz.")
print('Before you begin, answer the questions as A/a, B/b, C/c, D/c.\n EX. "A"')

print("\nYour score will be calculated as well.")

## QUIZ QUESTIONS ##

score = 0

def questiononePrompt():
    global score
    print("\n1. What was the main reason for the\nSong Dynasty’s population growth?\n")

    questiononeUser = input("\nA. Expansion of territory\nB. Champa rice\nC. Industrialization\nD. Religious reforms\n").lower()

    if questiononeUser == "b":
        print("\nCorrect. Champa rice was used since it was drought free,\nharvested many times a year, and even caused a population\nspike.")
        score += 1
    else:
        print("\nIncorrect. The correct answer is Champa rice as it was\ndrought free, could be harvested many times a year and\ncaused a population spike in growth.")
    
def questiontwoPrompt():
    global score
    print("\n2. Which system best describes political organization in medieval Europe?")

    questiontwoUser = input("\nA. Bureaucracy\nB. Democracy\nC. Feudalism\nD. Theocracy\n").lower()

    if questiontwoUser == "c":
        print("\nCorrect. Europe used a decenteralized feudal system.")
        score += 1
    else:
        print("\nIncorrect. Europe used a decenteralized feudal\nsystem in which it was hierarchical.")

def questionthreePrompt():
    global score
    print("\n3. The Seljuk Empire maintained power primarily through:")

    questionthreeUser = input("\nA. Civil service exams\nB. Trade monopolies\nC. Military strength\nD. Democratic elections\n")

    if questionthreeUser == "c":
        print("\nCorrect. They expanded by using mobile and calvary-heavy forces.")
        score += 1
    else:
        print("\nIncorrect. The Seljuk Empire used military strength\nto maintain power.")

def questionfourPrompt():
    global score
    print("\n4. What was a key effect of the House of Wisdom?")

    questionfourUser = input("\nA. Spread of feudalism\nB. Preservation and translation of knowledge\nC. Creation of civil service exams\nD. Expansion of Christianity\n").lower()

    if questionfourUser == "b":
        print("\nCorrect. They trasnlated Greek texts into Arabic.")
        score += 1
    else:
        print("\nIncorrect. The answer is perservation and translation of knowledge\n as scholars at the House of Wisdom tranlated texts\nfrom Greek to Arabic.")

def questionfivePrompt():
    global score
    print("\n5. Which region had the MOST centralized government?")

    questionfiveUser = input("\nA. Europe\nB. China\nC. South Asia\nD. Americas\n").lower()

    if questionfiveUser == "b":
        print("\nCorrect. China has the most centeralized government as\nthey used confucanism.")
        score += 1
    else:
        print("\nIncorrect. China has the most centeralized government as\nthey used confucanism.")

quizOrder = [questiononePrompt, questiontwoPrompt, questionthreePrompt, questionfourPrompt, questionfivePrompt]

## QUIZ TIME ##
while True: #need loop incase they wanna restart you know?
    begin = input("Start? Y/N ").lower()
    score = 0

    if begin == "y":
        for order in quizOrder:
            order()
        print(f"\nYour score was a total of: {score}/5.")

        restart = input("\nWould you like to try again? ").lower()

        if restart != "y":
            break

    else:
        break
