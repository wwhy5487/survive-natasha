#GameJam 14-15/11/2026 Haven Penang
#Group member: Ryan Trinice Joycelyn
#ezzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

#Project 1.0 I DONT WANT TO GO SCHOOL
#Project 2.0 Choose a pet to go school

#ezzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

#DEFINES ---------------------------------------------------------------------------------------------------------------------------

define naijiao = Character("Nai Jiao", image="naijiao.png")
define naigou = Character("Nai Gou", image="naigou.png")
define alarm = Character("Alarm")
define natasha = Character("Natasha")
define jumpscare = "jumpscare.mpeg"
define horrorbackgroundmusic = "horrorbackgroundmusic.mpeg"
define naijiaofall = "naijiaofall.jpg"

label survive:
    scene survive
    "You survived!"
    jump endsurvive

#START GAME -------------------------------------------------------------------------------------------------------------------------
label start:
    scene startbackground
    stop audio
    play music horrorbackgroundmusic
    narrator "Wake up."
    narrator "You wake up, take a shower and prepare for school."
    narrator "When you arrive, you notice something strange."
    narrator "Nobody is there. The school gates are open, but the entire building is silent."

    scene alarm
    play music alarmsound                                    #DISABLE FIRST ******************

    narrator "Suddenly, you hear your alarm ringing again."
    narrator "Your phone shows 7:00 AM."
    narrator "What will you do?"
    scene startbackground

    menu:
        "A. Enter the school and investigate.":
            jump enter_school

        "B. Call your mother.":
            jump call_mother

        "C. Run towards the school exit.":
            jump run_exit
        "D. Sleep":
            jump sleep

   
label enter_school:
    hide alarm
    stop music
    play music horrorbackgroundmusic
    narrator "A"
    narrator "You enter the building. All the classroom doors are open."
    scene yellowcreature
    narrator "Suddenly, you see a yellow creature standing at the end of the corridor."
    narrator "It disappears when you blink."
    narrator "You hear a voice behind you:"
    narrator "Don't follow it..."
    narrator "What will you do?"
    
    menu:
        "A. Follow the yellow creature.":
            jump follow_creature
        "B. Hide inside the classroom.":
            jump hide_classroom
        "C. Run towards the school exit.":
            jump run_exit

label follow_creature:
    "You decide to follow the creature."
    "The creature leads you into a forest..."
    jump story3
    
label call_mother:
    hide alarm
    stop music
    play music horrorbackgroundmusic
    scene callmom
    narrator "B"
    narrator "You call your mother."
    narrator "She answers, but her voice sounds strange."
    narrator "Listen carefully. If you see two yellow creatures, don't trust either of them."
    narrator "Suddenly, the call disconnects."
    narrator "You turn around and see a dark forest behind the school."
    narrator "What will you do?"
    
    menu:
        "A. Walk into the forest.":
            jump story3
        "B. Try calling your mother again.":
            jump call_mother_again
        "C. Hide inside the school.":
            jump hide_classroom
            
label run_exit:
    hide alarm
    stop music
    narrator "C"
    narrator "You run away from the school."
    narrator "But no matter how far you run, you keep returning to the same school entrance."
    scene forest
    narrator "You suddenly notice a forest behind the school gates."
    narrator "You decide to enter it."
    jump story3

label call_mother_again:
    scene callmom2
    narrator "..."
    narrator "... ... ..."
    narrator "The phone doesn't pick up."
    #play music
    narrator "Buzz, buzz."
    narrator "The sound from your phone seems to have attracted something."
    stop music
    show natashakill
    play music jumpscare
    natasha "..."
    narrator "..."
    jump start

label hide_classroom:
    scene classroom
    narrator "You hide under a dusty desk in the classroom."
    scene underdesk
    narrator "You observe and listen to your surroundings. Footsteps are approaching."
    narrator "Your heart races, and suddenly..."
    narrator "The creatures are behind you"
    #play audio
    show naigou:
        xalign 0.25
        yalign 0.5
    show naijiao:
        xalign 0.75
        yalign 0.5
    narrator "The yellow creatures are watching you."
    narrator "They stare into your eyes and your soul."
    naijiao "Zesxdrctfgvbhunjkmljihfds."
    narrator "Nai Jiao asks if you need any help."
    naigou "Esdrtfgyhuijkmo,hgjjhgfdrstythjhhgj.khyt"
    narrator "Nai Gou says they can help you."
    narrator "What will you do?"

    menu:
        "I need help.":
            jump accepthelp
        "I don't need help.":
            jump rejecthelp

label accepthelp:
    "You accept their help."
    "They take you out of the school into the forest."
    jump story3                                      #story 3 (tiktok)-----------------------------------------------------------------


label rejecthelp:
    naigou "..."
    naijiao "..."
    hide naijiao
    hide naigou
    narrator "Nai Jiao and Nai Gou crawl away."
    narrator "But the footsteps don't fade."
    narrator "It's coming."
    show natashakill
    play music jumpscare
    natasha "..."
    narrator "..."
    jump start






#SCENE 2 ------------------------------------------------------------------------------------------------------------------------------------
label sleep:
    hide clock
    stop music
    play music horrorbackgroundmusic
    scene bedroom
    narrator "D. You choose to head back to bed and sleep."
    narrator "You turn off your alarm and close your eyes."
    narrator "Suddenly, you hear strange birds screaming."
    scene forest
    narrator "You open your eyes again, but you are no longer in your bedroom."
    narrator "You find yourself lying in the middle of a dark forest. Your phone has no signal, and your school bag is beside you."
    narrator "Welcome back. We have been waiting for you."
    #show sign
    narrator "You hear strange footsteps coming from behind the trees."
    narrator "What will you do?"

    menu:
        "Follow the mysterious footsteps.":
            narrator "You choose to follow the footsteps."
            jump followfootsteps
        "Walk towards the sound of running water.":
            narrator "You choose to follow the sound of the river."
            jump followriver
        "Explore the dark forest":
            narrator "You are curious about the mysterious dark forest."
            narrator "You slowly walk inside."
            jump story3

label followfootsteps:
    narrator "You follow the footprints deeper into the forest."
    narrator "After a few minutes, you see a small yellow creature standing beside a tree."
    show naigou:
        xalign 0.25
        yalign 0.5
    narrator "It looks at you and waves."
    narrator "Hello! Are you lost? My name is Nai Gou. I can help you find your way home."
    narrator "What will you do?"
    menu:
        "Trust Nai Gou and follow him.":
            narrator "You choose to trust Nai Gou and follow him."
            jump naigoustory3
        "Ask him why he is alone in the forest.":
            naigou "..."
            naigou "... ... ..."
            naigou "I've been here for a very long time."
            naigou "Let me guide you."
            narrator "You don't know how to get out of this place, so you follow Nai Gou..."
            jump naigoustory3
        "Run away from him.":
            narrator "You are too scared, so you run away."
            narrator "You don't see the hole beneath you and fall into it."
            jump hiddenhole

label followriver:
    scene riverblack
    narrator "You hear water flowing nearby."
    narrator "You follow the sound until you reach a river."
    "Suddenly, you notice a small wooden boat on the riverbank."
    "There is a black creature sitting inside it."
    "It waves at you."
    "Do you want a ride? I know a shortcut!"
    menu:
        "Yes":
            "You decide to follow the shortcut."
            "Halfway there, the creature stops."
            natasha "..."
            show natashakill
            play music jumpscare
            "..."
            jump start
        "No":
            "You reject the offer and run away from the black creature."
            "You don't see the hole beneath you and fall into it."
            jump hiddenhole

    

label hiddenhole:
    "..."
    "Where am I?"
    natasha "..."
    show natashakill
    play music jumpscare
    "..."
    jump start

#story 3 (tiktok)-----------------------------------------------------------------------------------------

label story3:
    scene forest
    show naigou:
        xalign 0.25
        yalign 0.5
    show naijiao:
        xalign 0.75
        yalign 0.5
    "You have to choose one to lead you out of this forest."
    menu:
        "Choose Nai Gou":
            "You decide to choose Nai Gou."
            jump naigoustory3
        "Choose Nai Jiao":
            "You decide to choose Nai Jiao."
            jump naijiaostory3

label naigoustory3:
    hide naijiao
    hide naigou
    show naigouflash:
        xalign 0.5
        yalign 0.5
    scene gasstation

    "Nai Gou takes out a flashlight and leads you through the dark forest to an abandoned gas station."
    show naigouflash:
        xalign -0.5
        yalign 0.5
    "There is a broken car parked outside. You realise that you need to find something to repair its flat tyre."
    "You both enter the storage room to search for useful tools."
    hide naigouflash
    "Nai Gou seems to know everything about this place. He moves around the storage room suspiciously quickly, as if he already knows exactly where everything is."
    "He shines his flashlight towards two rusty metal boxes in front of you."
    "Which one do you choose?"
    scene redboxnbluebox
    menu:
        "The red box":
            "You choose the red box."
            jump redbox
        "The blue box":
            "You choose the blue box."
            jump bluebox

label redbox:
    hide naigouflash
    scene redbox
    "You open the red box, but there is nothing inside."
    "You become frustrated and accidentally knock the entire box onto the floor."
    scene redboxfall
    "CLANG!"
    "The loud noise echoes throughout the gas station."
    "Suddenly, you hear something approaching."

    "It’s Natasha!"
    show natashakill
    play music jumpscare
    natasha "..."
    jump start

label bluebox:
    hide naigouflash
    scene bluebox
    "You open the blue box and discover a collection of useful tools."
    "You quickly take them and use them to repair the car’s flat tyre."
    "After successfully fixing the car, you and Nai Gou prepare to leave."
    "However, just as you are about to get outside, you hear a terrifying noise."
    "Natasha is coming!"
    jump hidenseek

label hidenseek:
    scene gasstation
    "You hear loud footsteps approaching the gas station."
    "Nai Gou quickly looks around and whispers:"
    "Quick! We need to hide! There’s no time!"
    "He points towards two possible hiding places."
    "Where will you hide?"
    menu:
        "Hide behind the shelves.":
            "You decide to hide behind the shelves."
            jump hideshelves
        "Hide under the car.":
            "You decide to hide under the car."
            jump hidecar

label hidecar:
    scene naigoucar
    "You quickly crawl underneath the car."
    "You tightly grip the metal underneath the vehicle and hold your breath."
    "You hear footsteps getting closer."
    "Suddenly, a pair of barefoot feet slowly walks past you."
    "You stay completely still, hoping Natasha won’t notice you."
    "After a few terrifying seconds, the footsteps finally disappear."
    jump survive


label hideshelves:
    scene naigoushelf
    "You quickly squeeze yourself behind the shelves and curl up into a ball."
    "You try your best not to make a sound."
    "Suddenly, a bright flashlight shines directly towards you."
    "You freeze."
    "Natasha has found you!"
    "Before you can escape, Natasha grabs you."
    show natashakill
    play music jumpscare
    natasha "..."
    jump start



label naijiaostory3:
    hide naigou
    hide naijiao
    show naijiao:
        xalign 0.5
        yalign 0.0
    scene naijiaopath
    "You and Nai Jiao come to a crossroads."
    "You see two paths: a regular road and a path with footprints."
    "Which do you choose?"
    menu:
        "Take the regular road.":
            "You choose to follow the regular road."
            jump regularroad
        "Follow the path with footprints.":
            "You choose to follow the path with footprints."
            jump pathwithfootsteps

label regularroad:
    scene naijiaoriver
    "You follow the regular road and find a river."
    "Nai Jiao wants to cross the river."
    "But it sinks into the mud when it takes its first step."
    scene naijiaosink
    "Nai Jiao can't get out..."
    "You and Nai Jiao slowly sink into the mud."
    "..."
    jump start

label pathwithfootsteps:
    scene abandonedhouse
    "You and Nai Jiao follow the path, and nothing strange happens."
    "You and Nai Jiao find an abandoned house."
    "Nai Jiao says he is tired and wants to rest."
    "What will you do?"
    menu:
        "Rest at the abandoned house.":
            "You decide to rest."
            jump restabandonedhouse
        "Keep escaping the forest.":
            "You decide to keep going."
            jump keepescaping


label restabandonedhouse:
    scene black
    hide naijiao
    "You and Nai Jiao rest at the abandoned house."
    "Nai Jiao seems aggressive right now."
    "Nai Jiao keeps stomping on the floor."
    "As Nai Jiao keeps stomping, the floor cracks."
    "You and Nai Jiao fall through the floor..."
    show naijiaofall
    "..."
    jump start

label keepescaping:
    scene naijiaochoose
    "You and Nai Jiao don't stop to rest and keep going."
    "There's an unpleasant sound behind you."
    "You have two choices."
    menu:
        "Hide inside the car beside you.":
            "You decide to hide inside the car."
            jump endscenenaijiaodie
        "Run straight ahead.":
            "You decide to run away with Nai Jiao."
            jump endscenenaijiaosurvive


label endscenenaijiaodie:
    scene naijiaocar 
    "Nai Jiao seems quiet for now."
    "*Bump*"
    "There is a strange noise coming from the roof of the car."
    scene naijiaocar2
    "Suddenly, the roof breaks!"
    show natashakill
    play music jumpscare
    "..."
    jump start

label endscenenaijiaosurvive:
    "You and Nai Jiao run for your lives."
    "The creature stops chasing you."
    "You survived."
    jump survive 


label endsurvive:
    scene black
    "Thank you for playing!"
    "End credits:"
    scene endscreencc
    "Project title: Survive Natasha"
    "Project members: Ryan Trinice Joycelyn"
    "Goodbye!"


