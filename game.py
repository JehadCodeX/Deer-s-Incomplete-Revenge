import random
import time

skip = input("Press X to skip cutscenes and start the game directly: ").lower()
play_cutscenes = skip != "x"

cutscenes = {
    1: ["*BANG!*", "Hector: Vamos, another Iberian red deer to pill his head out of his body!"],
    2: ["The sunset is coming. Hector is at his highest pleasure after having his 52nd head of Iberian red deer",
        "Hector saws an interesting Gun store on his way"],
    3: ["Hector decided to take a look at the store",
        "Hector: Hello 'Gun Man'. Do you have any great Gun-design that's fully fitting with the head that I've hunted today?",
        "Gun Man: Oh, hello hunter! Well, this gun will perfectly fit your hunting accomplishment!",
        "Hector's eyes start to shine, because the design of the gun perfectly resembles his personality (guns, deer, demonic style).",
        "Hector: ¡Ay, qué bonito! I will buy it! How much does it cost? I will pay anything… even my eyes!",
        "Gun Man: No, I don't need your eyes. I'm starving! Um do you have some nuts? If not, I will eat your FLESH.",
        "Luckily, Hector has one left nut bag in his pack.",
        "Hector: That's all?! Then take it.",
        "Hector hands the nut bag to the Gun Man.",
        "Gun Man: Nuts! Nuts! Nuts! AWESOME!",
        "Gun Man gives Hector the gun.",
        "Gun Man vanished, turning into dust flying in the wind.",
        "Hector enters the surprise state for seconds until his eyes had fallen at his new gun.",
        "Hector: Wow! Now this is the coolest gun I have in my collection. What a time to be alive!"],
    4: ["Hector was on his way back to his cabin.",
        "Hector's sense for the perfect target suddenly spikes!",
        "Hector: Oh my god! What a day! A Water Deer with horns!!!! How on earth is that possible?!",
        "Hector decided to use his new gun, which already had a couple of bullets loaded.",
        "Hector takes aim and fires at the Water Deer with horns with full passion.",
        "*BANG*",
        "Hector manages to take the Water Deer down.",
        "Anonymous: You will regret this, Hector.....",
        "Hector falls to the ground, before fully understands what's going on."],
    5: ["Hector is surrounded by four walls, without any source of light.",
        "*MMF*",
        "He tries to scream.",
        "Nothing comes out.",
        "His mouth is sealed.",
        "He starts to feel someone walking toward him.",
        "A deer in the shape of a demon slowly begins to emerge from the darkness.",
        "Deeruz: Every soul has its price...",
        "Deeruz: A human... humans are the most liar species in the universe.",
        "Deeruz: I will take your soul, but I must have fun taking it...",
        "*Demon's laugh*",
        "Hector is frozen in shock as his life line begins to appear, forcing him to regret every moment he has lived.",
        "Deeruz: Humans are the weakest species. They solve things and think they can stand against unnatural forces.",
        "Deeruz: Justice… a joke humans cling to, but they don’t even respect it among themselves.",
        "Deeruz: Let's play something both of us are good at... How about gambling a bit? Don't worry, it will be a fair game — only the worthy will win.",
        "Hector gains confidence, trembling but determined.",
        "Deeruz: You know what? I will bet myself, to show you that I am the one who is worthy. Humans only look out for themselves; their 'justice' is meaningless, it's my time now.",
        "Deeruz: Look at him, regretting every time humanity says the word 'fair'.",
        "Hector: (thinking) I can't let him win... I must show him how fair are we, at least lying at him.",
        "*Demon's laugh*",
        "Deeruz: You think that I couldn't read your mind! even before your death you still lie and believing on fairness!?",
        "A table forms from nowhere, containing Hector's new gun."],
    6: [
        "*DEMON'S LAUGH*"
    ],
    7: [
        "Deeruz: Take this!"
    ],
    8: [
        "Deeruz: Not enough to destroy me.",
        "Deeruz: stop tickling me Human!",
        "Deeruz: You won THIS TIME!",
        "Deeruz: still far to win...",
        "*Demon's deep breath*",
        "Deeruz: You've survived this time.",
        "Deeruz: Your last breath is soon...."
    ],
    9: [
        "DEMON'S SCREAM",
        "Deeruz: I hate humans!...... why I'm betting unfair creatures!!!",
        "Deeruz: You've won the battle not the war!",
        "Deeruz is suffering",
        "*DEMON'S FINAL SCREAM*"
    ],
    10: [
        "*DEMON'S VICTORY LAUGH*",
        "YOU 'HUMANS' COULD NEVER BEAT YOUR COACH!",
        "Deeruz: I hope that you've learned something, humans are too weak!!!"
    ]
}

if play_cutscenes:
    for scene in range(1, 6):
        print("\n" + "=" * 50)
        time.sleep(3)
        for line in cutscenes[scene]:
            print(line)
            time.sleep(4)

time.sleep(3)

print("\n" + "*" * 50)
print("In this game, you will play vs Deeruz using the gun you bought from Gun Man.")
print("Each round has 6 bullets with a maximum of 3 real bullets.")
print("You must shoot yourself 1 time per round.")
print("If a real bullet fires — death is instant.")
print("*" * 50 + "\n")

player_score = 0
deeruz_score = 0
MAX_WINS = 5
round_number = 1

time.sleep(30)

while player_score < MAX_WINS and deeruz_score < MAX_WINS:
    print("\n" + "=" * 50)
    print(f"ROUND {round_number}")
    print("=" * 50)
    time.sleep(2)

    shot_yourself = 1
    deeruz_selfshot = 1
    real_bullets = random.randint(1, 3)
    bullet_set = [1]*real_bullets + [0]*(6 - real_bullets)
    random.shuffle(bullet_set)
    round_over = False
    player_turn = True

    while not round_over and bullet_set:
        print("\n" * 2)
        print("-" * 40)
        print(f"Hector {player_score}  -  {deeruz_score} Deeruz")
        print(f"Bullets left: {len(bullet_set)}")
        print(f"Your self-shots left: {shot_yourself}")
        print(f"Deeruz self-shots left: {deeruz_selfshot}")
        time.sleep(2)

        if player_turn:
            print("\nYour turn...")
            time.sleep(1.5)

            if shot_yourself == 1 and len(bullet_set) == 2:
                print("You must shoot yourself")
                choice = "0"
            elif shot_yourself == 1:
                choice = input("0: shoot yourself (once) | 1: shoot Deeruz: ")
            else:
                choice = "1"

            if choice not in ["0", "1"]:
                print("Invalid input.")
                time.sleep(1)
                continue

            bullet = bullet_set.pop(0)

            if choice == "0":
                shot_yourself -= 1
                print("\nYou aim at yourself...")
                time.sleep(1.5)
                if bullet == 1:
                    print("*BANG!*")
                    print(cutscenes[6][0])
                    deeruz_score += 1
                    round_over = True
                else:
                    print("*CLICK*")
                    print(cutscenes[8][random.randint(3, 6)])
            else:
                print("\nYou shoot Deeruz...")
                time.sleep(1.5)
                if bullet == 1:
                    print("*BANG!*")
                    print(cutscenes[8][random.randint(0, 4)])
                    player_score += 1
                    round_over = True
                else:
                    print("*CLICK*")
                    print(cutscenes[6][0])

            player_turn = False

        else:
            if not bullet_set:
                break

            print("\nDeeruz's turn...")
            time.sleep(2)
            bullet = bullet_set.pop(0)
            if deeruz_selfshot == 1 and len(bullet_set) <= 1:
                deeruz_choice = "self"
                print("Deeruz: I must shoot at myself")
            elif deeruz_selfshot == 1 and random.randint(1, 3) == 3:
                deeruz_choice = "self"
            else:
                deeruz_choice = "you"

            if deeruz_choice == "self":
                deeruz_selfshot -= 1
                print("\nDeeruz shoots himself...")
                time.sleep(1.5)
                if bullet == 1:
                    print("*BANG!*")
                    print("Deeruz: Don't be so happy.")
                    player_score += 1
                    round_over = True
                else:
                    print("*CLICK*")
                    print(cutscenes[6][0])
            else:
                print("\nDeeruz shoots you...")
                time.sleep(1.5)
                if bullet == 1:
                    print("*BANG!*")
                    print(cutscenes[7][0])
                    deeruz_score += 1
                    round_over = True
                else:
                    print("*CLICK*")
                    print(cutscenes[8][random.randint(3, 6)])

            player_turn = True

        time.sleep(1.5)

    time.sleep(2)
    round_number += 1

print("\n" + "*" * 50)
if player_score >= MAX_WINS:
    for i in cutscenes[9]:
        print(i)
        time.sleep(1.5)
else:
    for x in cutscenes[10]:
        print(x)
        time.sleep(1.5)
print("*" * 50 + "\n")

JehadCode_text = """
************************************************** 
JehadCode's Final Words
************************************************** 
JehadCode: This game took me 8 hours and 35 minutes to make.
It's my first time creating a game focused on story rather than gameplay.
I hope that you've enjoyed playing the game...
You can find more projects on my GitHub Account: https://github.com/JehadCodeX
THANK YOU, GAMERS!
"""

easter_eggs_text = """
**************************************************
                 EASTER EGGS
**************************************************

Story Location: somewhere in Spain.

Why Spain: because 'Hector' is a popular name in Spain.

Iberian Red Deer: the most famous type of deer in Spain.

Water Deer: a type of deer living in China and Korea that doesn't grow horns but has long teeth.
I've chosen this type of deer because it's rare, and I've added horns to make it unnatural—just like a demon.

Hector: is a non-native English speaker living in a cabin near a deer hunting zone. He has a full collection of
guns with unique designs and a lot of deer heads.

Gun Man: Unknown

Deeruz: a demon-like creature upset about the unfairness of humans killing deer just to display their heads.

There are many theories in this game waiting to be discovered; it's all left to your imagination!
"""

credits_text = """
**************************************************
                 C R E D I T S
**************************************************

Game Design & Story: JehadCode
Lead Developer & Programmer: JehadCode
Debugger: JehadCode
Narrative & Dialogue: JehadCode
Cutscenes Direction: JehadCode
Credit, Easter Eggs, JehadCode's Final Words Writer: JehadCode
Credits, Easter Eggs and JehadCode's Final Words Display Programmer: ChatGPT


Powered By:
- Python

**************************************************
         “Humans could never beat their coach…”
**************************************************
"""


def display_word_by_word(text, delay=0.25):
    for line in text.splitlines():
        for word in line.split():
            print(word, end=' ', flush=True)
            time.sleep(delay)
        print()
    print("\n" + "*"*50 + "\n")


display_word_by_word(credits_text, delay=0.2)
display_word_by_word(easter_eggs_text, delay=0.1)
display_word_by_word(JehadCode_text, delay=0.2)
