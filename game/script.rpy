# Vous pouvez placer le script de votre jeu dans ce fichier.

# How long the player has to make a choice in timeout seconds.
default timeout = 10.0

# The label the player is sent to if they fail to make a choice in the time
# allotted. If None, the timeout is disabled.
default timeout_label = None

# A preference that enables or disables timed choices.
default persistent.timed_choices = True

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    if (timeout_label is not None) and persistent.timed_choices:

        bar:
            xalign 0.5
            ypos 1
            xsize 1920
            ysize 30
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)
            left_bar "#cc3b32"

        timer timeout action Jump(timeout_label)

# Initialiser le score

define score = 0

screen score_screen():
    frame:
        align(1.0, 0.1)
        text "Score: [score]"

# Déclarez sous cette ligne les images, avec l'instruction 'image'
image mascotte = "mascotte.png"
image mascotte sad = "mascotte sad.png"
image fan = "fan base.png"
image fan angry = "fan angry.png"
image fan happy = "fan happy.png"
image basket = "basket base.png"
image basket angry = "basket angry.png"
image basket happy = "basket happy.png"
image tennis = "tennis base.png"
image tennis angry = "tennis angry.png"
image tennis happy = "tennis happy.png"
image archer = "archer base.png"
image archer angry = "archer angry.png"
image archer happy = "archer happy.png"
image paralympique = "paralympique base.png"
image paralympique angry = "paralympique angry.png"
image paralympique happy = "paralympique happy.png"
image winner = "winner base.png"
image winner angry = "winner angry.png"
image winner happy = "winner happy.png"
image kayak = "kayak base.png"
image kayak angry = "kayak angry.png"
image kayak happy = "kayak happy.png"
image cycliste = "cycliste base.png"
image cycliste angry = "cycliste angry.png"
image cycliste happy = "cycliste happy.png"

# Déclarez les personnages utilisés dans le jeu.
define m = Character('Mascotte', color="#cc3b32")
define f = Character('Fan', color="#6495d5")
define b = Character('Basketteur', color="#ef8d3a")
define t = Character('Tennis woman', color="#f9bdee")
define a = Character('Archère', color="#b07a6b")
define c = Character('Cycliste', color="#e44e25")
define p = Character('Paralympique', color="#0fb6f2")
define w = Character('Winner', color="#7e25e4")
define k = Character('Kayak', color="#be21ac")

# Le jeu commence ici
label start:

    scene bg jotoureiffel
    with fade
    play music "backgroundCrowdOutside.mp3"

    show mascotte

    m "Bienvenue à notre quizz, cher fan de JO !"

    m "Les Jeux Olympiques de Paris arrivent cette année et vous êtes en charge du déroulement de la cérémonie d'ouverture."

    m "Votre but est de répondre à toutes les questions. Il y en a 8 au total et vous avez 10 secondes pour répondre à chaque question. Si vous avez 6 bonnes réponses ou plus, les Jeux Olympiques pourront se dérouler !"

    m "Sinon, nous devrons les annuler..."
 
### QUESTION 1 (perso basket)###

    scene bg basket
    with fade
    play music "backgroundCrowdInside.mp3"

    show screen score_screen()

    $ timeout_label = "bad1"

    show basket
    b "Yo ! Es-tu prêt pour la première question ?"

    hide basket
    play music "backgroundQuestionTimer.mp3"
    menu: 
        
        "Quel pays a eu le plus de médailles d’or ?"
        
        "A) Allemagne":
            jump bad1

        "B) Etats-Unis":
            $ score = score + 1
            show basket happy
            play music "backgroundCrowdInside.mp3"
            play sound "correct.mp3"
            b "Bonne réponse ! En effet, Les Etats-Unis ont gagné au total 1175 médailles d'or depuis le début de l'ère moderne des JO."
            jump question2 

        "C) France":
            jump bad1

        "D) Chine":
            jump bad1


label bad1: 

    show basket angry
    play music "backgroundCrowdInside.mp3"
    play sound "wrong.mp3"
    b "Mince, c'était la réponse B. En effet, Les Etats-Unis ont gagné au total 1175 médailles d'or depuis le début de l'ère moderne des JO."
    jump question2

### QUESTION 2 (perso tennis)###

label question2: 

    scene bg tennis
    with fade

    $ timeout_label = "bad2"

    show tennis
    t "Deuxième question..."

    hide tennis
    play music "backgroundQuestionTimer.mp3"
    menu: 

        "Que représente la mascotte pour pour les JO de Paris 2024 ?" 

        "A) Une tour Eiffel":
            jump bad2

        "B) Un doudou":
            jump bad2

        "C) Un bonnet phrygien":
            $ score = score + 1
            show tennis happy
            play music "backgroundCrowdInside.mp3"
            play sound "correct.mp3"
            t "Bonne réponse ! En effet, le bonnet phrygien est la mascotte pour Paris 2024. Elle symbolise la République Française et la liberté."
            jump question3 

        "D) Une coccinelle":
            jump bad2


label bad2: 

    show tennis angry
    play music "backgroundCrowdInside.mp3"
    play sound "wrong.mp3"
    t "C'était la réponse C !!! En effet, le bonnet phrygien est la mascotte pour Paris 2024. Elle symbolise la République Française et la liberté."
    jump question3

### QUESTION 3 (perso fan)###

label question3: 

    scene bg piscine
    with fade

    $ timeout_label = "bad3"

    show fan
    f "Hey ! J'adore les JO et toi ? J'ai une question pour toi..."

    hide fan
    play music "backgroundQuestionTimer.mp3"
    menu: 

        "Le football est-il présent aux Jeux Olympiques ?"

        "A) Oui":
            $ score = score + 1
            show fan happy
            play music "backgroundCrowdInside.mp3"
            play sound "correct.mp3"
            f "Bonne réponse ! En effet, l'épreuve du football a été ajouté lors des Jeux Olympiques de Paris en 1900."
            jump question4

        "B) Non":
            jump bad3
    

label bad3: 

    show fan angry
    play music "backgroundCrowdInside.mp3"
    play sound "wrong.mp3"
    f "Mince, c'était la réponse A. L'épreuve du football a été ajouté lors des Jeux Olympiques de Paris en 1900."
    jump question4

### QUESTION 4 (perso tir à l'arc)###

label question4: 

    scene bg tiralarc
    with fade

    $ timeout_label = "bad4"

    show archer
    a "Quatrième question..."

    hide archer
    play music "backgroundQuestionTimer.mp3"
    menu: 

        "En quelle année a été intégrée l’épreuve de tir à l’arc ?"

        "A) En 1900":
            $ score = score + 1
            show archer happy
            play music "backgroundCrowdInside.mp3"
            play sound "correct.mp3"
            a "Bonne réponse ! En effet, l'épreuve de tir à l'arc apparait lors des JO de Paris en 1900. Elle a été présente jusqu'en 1920, puis a fait son retour en 1972."
            jump question5

        "B) En 1904":
            jump bad4
        
        "C) En 1920":
            jump bad4
        
        "D) En 1948":
            jump bad4
    

label bad4: 

    show archer angry
    play music "backgroundCrowdInside.mp3"
    play sound "wrong.mp3"
    a "Non, c'était la réponse A !!! L'épreuve de tir à l'arc apparait lors des JO de Paris en 1900. Elle a été présente jusqu'en 1920, puis a fait son retour en 1972."
    jump question5

### QUESTION 5 (perso paralympique)###

label question5: 

    scene bg course
    with fade

    $ timeout_label = "bad5"

    show paralympique
    p "Salut ! Me voilà pour te poser la cinquième question..."

    hide paralympique
    play music "backgroundQuestionTimer.mp3"
    menu: 

        "Est-ce que tous les sports présents aux JO sont déclinés pour les Paralympiques ?"

        "A) Oui":
            jump bad5
        
        "B) Non":
            $ score = score + 1
            show paralympique happy
            play music "backgroundCrowdInside.mp3"
            play sound "correct.mp3"
            p "Bonne réponse ! En effet, tous les sports sont déclinés pour les Paralympiques, sauf pour le golf."
            jump question6

    

label bad5: 

    show paralympique angry
    play music "backgroundCrowdInside.mp3"
    play sound "wrong.mp3"
    p "Mince, c'était la réponse B... Tous les sports sont déclinés pour les Paralympiques, sauf pour le golf."
    jump question6

### QUESTION 6 (winner)###

label question6: 

    scene bg stade
    with fade

    $ timeout_label = "bad6"

    show winner
    w "Sixième question..."

    hide winner
    play music "backgroundQuestionTimer.mp3"
    menu: 

        "Combien de médailles la France a-t-elle reçues ?"

        "A) 658":
            jump bad6

        "B) 1143":
            jump bad6
        
        "C) 556":
            jump bad6
        
        "D) 889":
            $ score = score + 1
            show winner happy
            play music "backgroundCrowdInside.mp3"
            play sound "correct.mp3"
            w "Bonne réponse ! En effet, La France a obtenu 889 médailles à la suite de la participation à 53 éditions des Jeux Olympiques."
            jump question7
    

label bad6: 

    show winner angry
    play music "backgroundCrowdInside.mp3"
    play sound "wrong.mp3"
    w "Aïe aïe aïe, c'était la réponse D. La France a obtenu 889 médailles à la suite de la participation à 53 éditions des Jeux Olympiques."
    jump question7

### QUESTION 7 (cycliste)###

label question7: 

    scene bg velodrome
    with fade

    $ timeout_label = "bad7"

    show cycliste
    c "Septième question..."

    hide cycliste
    play music "backgroundQuestionTimer.mp3"
    menu: 

        "En quelle année s'est déroulée la première édition des Jeux Olympiques modernes ?"

        "A) 1892":
            jump bad7

        "B) 1896":
            $ score = score + 1
            show cycliste happy
            play music "backgroundCrowdInside.mp3"
            play sound "correct.mp3"
            c "Bonne réponse ! En effet, la première édition des Jeux Olympiques telle qu'on la connait a eu lieu en 1896 à Athènes en Grèce."
            jump question8
        
        "C) 1904":
            jump bad7
        
        "D) 1900":
            jump bad7
    

label bad7: 

    show cycliste angry
    play music "backgroundCrowdInside.mp3"
    play sound "wrong.mp3"
    c "C'était la réponse B... La première édition des Jeux Olympiques telle qu'on la connait a eu lieu en 1896 à Athènes en Grèce."
    jump question8

### QUESTION 8 (kayak)###

label question8: 

    scene bg lac
    with fade

    $ timeout_label = "bad8"

    show kayak
    k "Voici la huitième et dernière question..."

    hide kayak
    play music "backgroundQuestionTimer.mp3"
    menu: 

        "Est-ce que les JO de la Jeunesse existent ?"

        "A) Oui":
            $ score = score + 1
            show kayak happy
            play music "backgroundCrowdInside.mp3"
            play sound "correct.mp3"
            k "Bonne réponse ! En effet, Les JO de la jeunesse existent depuis 2010 à Singapour et 2012 pour l'édition Hiver à Innsbruck en Autriche. Ce sont des jeunes athlètes de 15 à 18 ans qui participent à cet événement tous les 4 ans."
            jump end

        "B) Non":
            jump bad8
    

label bad8: 

    show kayak angry
    play music "backgroundCrowdInside.mp3"
    play sound "wrong.mp3"
    k "Mince, c'était la réponse A. Les JO de la jeunesse existent depuis 2010 à Singapour et 2012 pour l'édition Hiver à Innsbruck en Autriche. Ce sont des jeunes athlètes de 15 à 18 ans qui participent à cet événement tous les 4 ans."
    jump end


label end:

    if score>=6:
        scene bg goodend
        with fade

        play music "backgroundVictory.mp3"
        show mascotte
        m "Félicitations, vous avez gagné ! Grâce à vous, les cérémonies des JO de Paris 2024 vont bien se dérouler. Je vois que vous êtes un expert, vous méritez de gagner une médaille d'or !"

    else: 
        scene bg badend
        with fade

        play music "backgroundSad.mp3"
        show mascotte sad
        m "Vous avez un score de [score] points, ce qui est insuffisant pour le bon déroulement de l'évènement. Hélas, nous allons devoir annuler la cérémonie."