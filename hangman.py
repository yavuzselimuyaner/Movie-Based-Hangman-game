def charlocation(string, characters):
    censored_string = ""
    for char in string:
        if char in characters:
            censored_string += char
        elif char == " ":
            censored_string += " "
        else:
            censored_string += "_"
    print(censored_string)

import random
win=False
lst=['The Shawshank Redemption', 'The Godfather', 'The Godfather: Part II', 'The Dark Knight', '12 Angry Men', "Schindler's List", 'The Lord of the Rings: The Return of the King', 'Pulp Fiction', 'The Good, the Bad and the Ugly', 'Fight Club', 'Forrest Gump', 'Inception', 'The Lord of the Rings: The Fellowship of the Ring', "One Flew Over the Cuckoo's Nest", 'Goodfellas', 'The Matrix', 'Seven Samurai', 'Star Wars: Episode V - The Empire Strikes Back', 'City of God', 'Se7en', 'The Silence of the Lambs', "It's a Wonderful Life", 'Leon: The Professional', 'Saving Private Ryan', 'The Departed', 'Whiplash', 'Gladiator', 'American History X', 'The Prestige', 'The Lion King', 'The Pianist', 'Psycho', 'City Lights', 'Once Upon a Time in the West', 'Alien', 'Rear Window', 'Modern Times', 'Memento', 'The Green Mile', 'Terminator 2: Judgment Day', 'Back to the Future', 'Casablanca', 'Amadeus', 'Apocalypse Now', 'Aliens', 'Oldboy', 'Once Upon a Time in America', 'Braveheart', 'Taxi Driver', 'Good Will Hunting', 'Amelie', 'Requiem for a Dream', 'The Lives of Others', 'A Clockwork Orange', 'The Elephant Man', 'Eternal Sunshine of the Spotless Mind', 'North by Northwest', "Singin' in the Rain", 'The Great Dictator', 'Double Indemnity', 'L.A. Confidential', 'Chinatown', 'Vertigo', 'Citizen Kane', 'The Shining', 'Paths of Glory', 'The Bridge on the River Kwai', 'All About Eve', 'Witness for the Prosecution', 'Dial M for Murder', 'The Third Man', 'A Separation', 'Come and See', 'Grave of the Fireflies', 'Downfall', 'The Secret in Their Eyes', 'Wild Strawberries', 'Metropolis', 'Yojimbo', 'Ran', 'The Seventh Seal', 'A Beautiful Mind', 'The Secret of Kells', 'The Secret of NIMH', 'The General', 'Amores perros', "Pan's Labyrinth", 'My Neighbor Totoro', 'The Wind Rises', 'Children of Heaven', 'Like Stars on Earth', 'My Father and My Son', 'The Act of Killing', 'The Look of Silence', 'Tokyo Story', 'There Will Be Blood', 'Therese Desqueyroux', 'Persona', 'Memories of Murder', 'Hacksaw Ridge']
flag=0
word = random.choice(lst).lower()
adam=[""" -------
|     |
|
|
|
|""", """ -------
|     |
|     O
|
|
|""", """ -------
|     |
|     O
|    /
|
|""",""" -------
|     |
|     O
|    /I
|
|""", """ -------
|     |
|     O
|    /I\ 
|
|""", """ -------
|     |
|     O
|    /I\ 
|
|""", """ -------
|     |
|     O
|    /|\ 
|    /\ 
|"""]

guessed_chars = []
while win == False:
    guessor = input("Guess a word or movie:\n")
    if len(guessor) == 1:
        if guessor in word:
            guessed_chars.append(guessor)
        else:
            print(f"Wrong guess ")
            print(adam[flag])
            flag += 1
            if flag >= 7:
                print(f"You lose {word} was the movie.")
                break
    else:
        if guessor == word:
            win = True
            print("You are right!")
        else:
            print(f"Wrong guess ")
            print(adam[flag])
            flag += 1
            if flag >= 7:
                print(f"You lose {word} was the movie.")
                break
    charlocation(word, guessed_chars)
    print()




