import pygame
import CONSTANTS
from main import *
from CONSTANTS import *
from core.movement_logic import *

pygame.init()

text_font = pygame.font.SysFont(None, 30)
text_font_big = pygame.font.SysFont(None, 40)

text_box_size = (10, 600, 500, 100)


# Location of problems, defined as invisible squares, that a player can interact if it approaches the coordinates
#Level1
problem1_level1 = pygame.Rect(303, 145, 30, 30)
problem2_level1 = pygame.Rect(535, 295, 30, 30)
problem3_level1 = pygame.Rect(800, 330, 30, 30)

#Level2
part1_problem1_level2 = pygame.Rect(505, 120, 30, 30)
part1_problem2_level2 = pygame.Rect(505, 280, 30, 30)
part1_problem3_level2 = pygame.Rect(505, 395, 30, 30)
part2_problem1_level2 = pygame.Rect(775, 120, 30, 30)
part2_problem2_level2 = pygame.Rect(775, 280, 30, 30)
part2_problem3_level2 = pygame.Rect(775, 395, 30, 30)

# Other levels





# In case you need to see those problem squares to visualize
def drawObject(color, level):

    if level == 1:
        pygame.draw.rect(WINDOW, color, problem1_level1)
        pygame.draw.rect(WINDOW, color, problem2_level1)
        pygame.draw.rect(WINDOW, color, problem3_level1)

    if level == 2:
        pygame.draw.rect(WINDOW, color, part1_problem1_level2)
        pygame.draw.rect(WINDOW, color, part1_problem2_level2)
        pygame.draw.rect(WINDOW, color, part1_problem3_level2)
        pygame.draw.rect(WINDOW, color, part2_problem1_level2)
        pygame.draw.rect(WINDOW, color, part2_problem2_level2)
        pygame.draw.rect(WINDOW, color, part2_problem3_level2)




def drawOptions(opt1, opt2, opt3, collide, level):

    opt1 = pygame.Rect(550, 600, 100, 100)
    opt2 = pygame.Rect(700, 600, 100, 100)
    opt3 = pygame.Rect(850, 600, 100, 100)

    #Draws answer options boxes
    pygame.draw.rect(WINDOW, WHITE, opt1)
    pygame.draw.rect(WINDOW, WHITE, opt2)
    pygame.draw.rect(WINDOW, WHITE, opt3)

    #Draw black borders
    pygame.draw.rect(WINDOW, BLACK, (549, 599, 100, 4))
    pygame.draw.rect(WINDOW, BLACK, (549, 699, 104, 4))
    pygame.draw.rect(WINDOW, BLACK, (549, 599, 4, 100))
    pygame.draw.rect(WINDOW, BLACK, (649, 599, 4, 100))

    pygame.draw.rect(WINDOW, BLACK, (699, 599, 100, 4))
    pygame.draw.rect(WINDOW, BLACK, (699, 699, 104, 4))
    pygame.draw.rect(WINDOW, BLACK, (699, 599, 4, 100))
    pygame.draw.rect(WINDOW, BLACK, (799, 599, 4, 100))

    pygame.draw.rect(WINDOW, BLACK, (849, 599, 100, 4))
    pygame.draw.rect(WINDOW, BLACK, (849, 699, 104, 4))
    pygame.draw.rect(WINDOW, BLACK, (849, 599, 4, 100))
    pygame.draw.rect(WINDOW, BLACK, (949, 599, 4, 100))



    #Detects which problems is currently approached and displays the possible answers (picutres/text) on the boxes, need to load the pictures in constant. There you can see dimensions aswell
    if level == 1:
        if collide == 1:
            WINDOW.blit(problem1_correct, (555, 605))
            WINDOW.blit(problem1_incorrect1, (705, 605))
            WINDOW.blit(problem1_incorrect2, (855, 605))
        if collide == 2:
            WINDOW.blit(problem2_incorrect2, (555, 605))
            WINDOW.blit(problem2_correct, (710, 605))
            WINDOW.blit(problem2_incorrect1, (855, 605))
        if collide == 3:
            WINDOW.blit(problem3_incorrect2, (555, 605))
            WINDOW.blit(problem3_incorrect1, (705, 605))
            WINDOW.blit(problem3_correct, (855, 605))

    # Other levels
    if level == 2:
        if collide == 1 or collide == 2 or collide == 3:
            WINDOW.blit(level2_part1_opt3, (555, 605))
            WINDOW.blit(level2_part1_opt1, (705, 605))
            WINDOW.blit(level2_part1_opt2, (855, 605))
        if collide == 4 or collide == 5 or collide == 6:
            WINDOW.blit(level2_part2_opt2, (555, 605))
            WINDOW.blit(level2_part2_opt3, (705, 605))
            WINDOW.blit(level2_part2_opt1, (855, 610))


def drawText(text):
    # drawing the  text box
    text_box = pygame.Rect(text_box_size)
    pygame.draw.rect(WINDOW, WHITE, text_box)
    pygame.draw.rect(WINDOW, BLACK, (5, 595, 510, 5)) # Top border
    pygame.draw.rect(WINDOW, BLACK, (5, 600, 5, 100)) # Left border
    pygame.draw.rect(WINDOW, BLACK, (510, 600, 5, 100)) # Right border
    pygame.draw.rect(WINDOW, BLACK, (5, 700, 510, 5)) # Bottom border


    #Displays text within the text box borders
    bkg = None
    y = text_box.top
    lineSpacing = -2
    while text:
        i = 1
        if y + 20 > text_box.bottom:
            break
        while text_font.size(text[:i])[0] < text_box.width and i < len(text):
            i += 1
        if i < len(text):
            i = text.rfind(' ', 0, i) + 1
        if bkg:
            comment = text_font.render(text[:i], True, BLACK, bkg)
            image.set_colorkey(bkg)
        else:
            comment = text_font.render(text[:i], False, BLACK)

        WINDOW.blit(comment, (text_box.left, y))
        y += 20 + lineSpacing

        text = text[i:]



def interact(character_rectangle, keys_pressed, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, level, mistakes):

    opt1 = pygame.Rect(550, 600, 100, 100)
    opt2 = pygame.Rect(700, 600, 100, 100)
    opt3 = pygame.Rect(850, 600, 100, 100)

    #Detects collison with the invisible squares
    point = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if level == 1:

         #Detects collison with the invisible squares
        collideProblem1 = character_rectangle.colliderect(problem1_level1)
        collideProblem2 = character_rectangle.colliderect(problem2_level1)
        collideProblem3 = character_rectangle.colliderect(problem3_level1)

        # While not near any problem
        if not collideProblem1 and not collideProblem2 and not collideProblem3:
            color = BLUE # When drawing the problem locations to visualize
            text = "Let's have a look! (Click and hold on 'TASK')"
        else:
            color = RED # When drawing the problem locations to visualize

        # Near problem 1
        if collideProblem1 and not fixed_1:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem1 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'Hmm, it seems the circuit is not fully connected. I wonder what fits in here'
                opt1 = pygame.Rect(550, 600, 100, 100)
                opt2 = pygame.Rect(700, 600, 100, 100)
                opt3 = pygame.Rect(850, 600, 100, 100)
                drawOptions(opt1, opt2, opt3, 1, level) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1 and not fixed_1:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'That seems to be right'
                        fixed_1 = True

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2 and not fixed_1:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_1 = False
                        mistakes += 1

                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3 and not fixed_1:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_1 = False
                        mistakes += 1

        # Once problem is fixed
        elif collideProblem1 and fixed_1:
            text = 'Simple enough!'

        # Problem 2
        if collideProblem2 and not fixed_2:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem2 and keys_pressed[pygame.K_RETURN]:
                text = 'This AND gate needs a name!'
                opt1 = pygame.Rect(550, 600, 100, 100)
                opt2 = pygame.Rect(700, 600, 100, 100)
                opt3 = pygame.Rect(850, 600, 100, 100)
                drawOptions(opt1, opt2, opt3, 2, level)

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1 and not fixed_2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_2 = False
                        mistakes += 1

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2 and not fixed_2:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_2 = True

                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3 and not fixed_3:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_2 = False
                        mistakes += 1

        # Once problem 2 is fixed
        elif collideProblem2 and fixed_2:
            text = 'BC, duh!'

        # Problem 3
        if collideProblem3 and not fixed_3:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem3 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'Looks like I need to name this OR gate'
                opt1 = pygame.Rect(550, 600, 100, 100)
                opt2 = pygame.Rect(700, 600, 100, 100)
                opt3 = pygame.Rect(850, 600, 100, 100)
                drawOptions(opt1, opt2, opt3, 3, level)

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1 and not fixed_3:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2 and not fixed_3:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3 and not fixed_3:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_3 = True

        # Once problem 3 is fixed
        elif collideProblem3 and fixed_3:
            text = "Of course! AB' + AC!"

        # Once all the problems are fixed
        if fixed_1 and fixed_2 and fixed_3:
            text = "Ha, I have done it!"

        # Other levels (I guess can copy the code and just change the level at top, text to whatever necessary, changing the location of the correct answer so it's not always option B

    if level == 2:

        #Detects collison with the invisible squares
        collideProblem1 = character_rectangle.colliderect(part1_problem1_level2)
        collideProblem2 = character_rectangle.colliderect(part1_problem2_level2)
        collideProblem3 = character_rectangle.colliderect(part1_problem3_level2)
        collideProblem4 = character_rectangle.colliderect(part2_problem1_level2)
        collideProblem5 = character_rectangle.colliderect(part2_problem2_level2)
        collideProblem6 = character_rectangle.colliderect(part2_problem3_level2)

            # While not near any problem
        if not collideProblem1 and not collideProblem2 and not collideProblem3:
            color = BLUE # When drawing the problem locations to visualize
            text = "Let's have a look! (Click and hold on 'TASK')"
        else:
            color = RED # When drawing the problem locations to visualize

        # Problem 1
        if collideProblem1 and not fixed_1:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem1 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'I need to name this part of a FPGA!'
                drawOptions(opt1, opt2, opt3, 1, level) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1 and not fixed_1:
                    text = 'Programmable I/O cells (blocks) interface between the FPGA and an external device'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_1 = False
                        mistakes += 1

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2 and not fixed_1:
                    text = 'Logic cells (blocks) can be configured to perform complex combinational functions, or act as simple logic gates like AND and XOR'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_1 = True


                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3 and not fixed_1:
                    text = 'Programmable interconnects (PI) known as a fabric directs signals between logic cells (blocks)'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_1 = False
                        mistakes += 1

        # Once problem 1 is fixed
        elif collideProblem1 and fixed_1:
            text = "Logic cells (blocks) give the FPGA it's computing power, hence they are located at the center of the FPGA and each one is connected to another with interconnects!"

        # Problem 2
        if collideProblem2 and not fixed_2:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem2 and keys_pressed[pygame.K_RETURN]:
                text = 'I need to name this part of a FPGA!'
                drawOptions(opt1, opt2, opt3, 2, level)

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1 and not fixed_2:
                    text = 'Programmable I/O cells (blocks) interface between the FPGA and an external device'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_2 = False
                        mistakes += 1

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2 and not fixed_2:
                    text = 'Logic cells (blocks) can be configured to perform complex combinational functions, or act as simple logic gates like AND and XOR'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_2 = False
                        mistakes +=1

                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3 and not fixed_2:
                    text = 'Programmable interconnects (PI) known as a fabric directs signals between logic cells (blocks)'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_2 = True

        # Once problem 2 is fixed
        elif collideProblem2 and fixed_2:
            text = 'Aha! Since programmable interconnects direct signals between logic cells (blocks), it only makes sense that they are located between the logic cells!'

        # Problem 3
        if collideProblem3 and not fixed_3:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem3 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'I need to name this part of a FPGA!'
                drawOptions(opt1, opt2, opt3, 3, level)

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1 and not fixed_3:
                    text = 'Programmable I/O cells (blocks) interface between the FPGA and an external device'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_3 = True

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2 and not fixed_3:
                    text = 'Logic cells (blocks) can be configured to perform complex combinational functions, or act as simple logic gates like AND and XOR'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3 and not fixed_3:
                    text = 'Programmable interconnects (PI) known as a fabric directs signals between logic cells (blocks)'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_3 = False
                        mistakes += 1

        # Once problem 3 is fixed
        elif collideProblem3 and fixed_3:
            text = 'Interface with external devices is very important, so there is no other possibilty, I/O cells (blocks) must be located on the outer side of the FPGA!'

        if collideProblem4 and not fixed_4:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem4 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'I need to insert the correct option!'
                drawOptions(opt1, opt2, opt3, 4, level) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1 and not fixed_4:
                    text = 'Looks like a bunch of straight lines connecting some blocks!'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_4 = False
                        mistakes += 1

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2 and not fixed_4:
                    text = "There's loads of logic gates that all lead to the same cell!"
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_4 = False
                        mistakes += 1


                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3 and not fixed_4:
                    text = 'Interesting! Looks like a complex system of arrays and logic gates!'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_4 = True

        # Once problem 4 is fixed
        elif collideProblem4 and fixed_4:
            text = 'Only possibility is that those are the the logic cells, where all the computing happens!'

        if collideProblem5 and not fixed_5:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem5 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'I need to insert the correct option!'
                drawOptions(opt1, opt2, opt3, 4, level) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1 and not fixed_5:
                    text = 'Looks like a bunch of straight lines connecting some blocks!'
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_5 = True

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2 and not fixed_5:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = "There's loads of logic gates that all lead to the same cell!"
                        fixed_5 = False
                        mistakes += 1


                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3 and not fixed_5:
                    text = 'Could this possibly fix it?'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_5 = False
                        mistakes += 1

        # Once problem is fixed
        elif collideProblem5 and fixed_5:
            text = 'Of course those are the programmable interconnects!'

        if collideProblem6 and not fixed_6:
            text = "Something's off! It's seems that there is a part missing!"

            if collideProblem6 and keys_pressed[pygame.K_RETURN]: # Pressing enter shows up possible fixes
                text = 'I need to insert the correct option!'
                drawOptions(opt1, opt2, opt3, 4, level) # Draws the answer options

                #Mouse over and click on answer
                collideAnswer1 = opt1.collidepoint(point)
                if collideAnswer1 and not fixed_6:
                    text = 'Looks like a bunch of straight lines connecting some blocks!'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_6 = False
                        mistakes += 1

                collideAnswer2 = opt2.collidepoint(point)
                if collideAnswer2 and not fixed_6:
                    text = "There's loads of logic gates that all lead to the same cell!"
                    if click[0]:
                        text = 'That seems to be right!'
                        fixed_6 = True


                collideAnswer3 = opt3.collidepoint(point)
                if collideAnswer3 and not fixed_6:
                    text = 'Interesting! Looks like a complex system of arrays and logic gates!'
                    if click[0]:
                        text = 'Nope, that does not seem right!'
                        fixed_6 = False
                        mistakes += 1

        # Once problem is fixed
        elif collideProblem6 and fixed_6:
            text = "It must be the I/O cell, where all the inputs and outputs come and go!"



        # Once all the problems are fixed
        if fixed_1 and fixed_2 and fixed_3 and fixed_4 and fixed_5 and fixed_6:
            text = "Eaz-peasy lemon squeezy ;)"


    return text, color, fixed_1, fixed_2, fixed_3, fixed_4, fixed_5, fixed_6, mistakes

def task(keys_pressed, level, mistakes):
    point = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(point)

    mistake_count = "Points lost: " + str(mistakes)
    global text_font


    # Task box and collision
    box_coordinates = pygame.Rect(1073, 65, 55, 20)
    collide_task = box_coordinates.collidepoint(point)

    #When clicked, it fills the blackboard with white page, so we can describe the goal of the level
    if collide_task and click[0]:
        pygame.draw.rect(WINDOW, WHITE, (59, 59, 1074, 426))

        if level == 1:
            WINDOW.blit(level1_task, (60, 60))
            task_description = text_font.render("Fix the circuit diagram such that it realizes the given diagram. ", True, BLACK,)
            hint1 = text_font.render('F1 = AB’C’ + ABC’ + ABC', True, BLACK)
            hint2 = text_font.render('F2 = A’BC + AB’C + ABC', True, BLACK)
            mistake_text = text_font_big.render(mistake_count, True, RED)
            WINDOW.blit(mistake_text, (830, 430)) # Currently there is a problem cause it keeps adding +1 to mistake counts if mouse button is pressed down, so often it will add more than one :/
            WINDOW.blit(task_description, (65, 370))
            WINDOW.blit(hint1, (65, 410))
            WINDOW.blit(hint2, (65, 450))
            #Could add a grade in the end, once the level is completed. Take the mistakes and calcuate the grade and assign it A B C D F and write it on the task white page

            # Other levels

        if level == 2:
            task_description = text_font.render("What you see on the blackboard is an FPGA which stands for Field Programmable Gate Array,", True, BLACK)
            task_description1 = text_font.render("which is an IC that can be programmed to perform a customized operation for a specific application. ", True, BLACK)
            task_description2 = text_font.render("Languages such as VHDL and Verilog are used to write the code for FPGA programming.""", True, BLACK)
            hint1 = text_font.render('FPGAs are reprogrammable. They are cost-efficient, however', True, BLACK)
            hint2 = text_font.render('They have high power consumption and programmers do not have any control over power optimization and', True, BLACK)
            hint3 = text_font.render("the programming of FPGA is not as simple as C programming.", True, BLACK)
            task_do = text_font.render("Choose the correct options to build a functional FPGA on the blackboard!", True, BLACK)
            mistake_text = text_font_big.render(mistake_count, True, RED)
            WINDOW.blit(mistake_text, (830, 430)) # Currently there is a problem cause it keeps adding +1 to mistake counts if mouse button is pressed down, so often it will add more than one :/
            WINDOW.blit(task_description, (65, 100))
            WINDOW.blit(task_description1, (65, 140))
            WINDOW.blit(task_description2, (65, 180))
            WINDOW.blit(hint1, (65, 220))
            WINDOW.blit(hint2, (65, 260))
            WINDOW.blit(hint3, (65, 300))
            WINDOW.blit(task_do, (65, 380))

        if level == 3:
            task_description = text_font.render("On this level you have couple calculations that are missing some of the values.", True, BLACK)
            task_description1 = text_font.render("In each of those you need to find a digit such that if we put it instead of the question mark, ", True, BLACK)
            task_description2 = text_font.render("it will give us the expected answer.", True, BLACK)
            hint1 = text_font.render('· Problem (1) is about sum of binary numbers. You can find more information about that in our video*', True, BLACK)
            hint12 = text_font.render('(timeslot [02:20-02:50])', True, BLACK)
            hint2 = text_font.render('· Problem (2) is about difference of binary numbers (timeslot [02:20-03:48])', True, BLACK)
            hint3 = text_font.render("· In problem (3) you need to transform a number from binary to hexadecimal representation", True, BLACK)
            hint32 = text_font.render("(timeslot [00:42-02:11])", True, BLACK)
            hint4 = text_font.render("Hint: it is easier to be done through decimal numbers system.", True, BLACK)
            task_do = text_font.render("*A video from group 37 about Digital Building Blocks is on the Brightspace", True, BLACK)
            mistake_text = text_font_big.render(mistake_count, True, RED)
            WINDOW.blit(mistake_text, (830, 430)) # Currently there is a problem cause it keeps adding +1 to mistake counts if mouse button is pressed down, so often it will add more than one :/
            WINDOW.blit(task_description, (65, 80))
            WINDOW.blit(task_description1, (65, 120))
            WINDOW.blit(task_description2, (65, 160))
            WINDOW.blit(hint1, (65, 200))
            WINDOW.blit(hint12, (65, 240))
            WINDOW.blit(hint2, (65, 280))
            WINDOW.blit(hint3, (65, 320))
            WINDOW.blit(hint32, (65, 360))
            WINDOW.blit(hint4, (65, 400))
            WINDOW.blit(task_do, (65, 460))

        if level == 4:
            k = 35
            text_font = pygame.font.SysFont(None, k)
            task_description = text_font.render("Unlike in the previous level, in this one you will have only two problems with missing", True, BLACK)
            task_description1 = text_font.render("digits. And again, you need to find them so that the calculations make sense. Although,", True, BLACK)
            task_description2 = text_font.render("don't feel relieved with the number of problems: there are still 3 questionmarks overall", True, BLACK)
            task_description3 = text_font.render("in the level, and moreover: second exercise is a bit harder as you may notice ;)", True, BLACK)
            hint1 = text_font.render('· So, problem (1) includes sum operation between two binary numbers,', True, BLACK)
            hint12 = text_font.render('but almost half of the result is lost (timeslot [02:20-02:50])', True, BLACK)
            hint2 = text_font.render('· In problem (2) you are asked to calculate number 124 (from decimal system)', True, BLACK)
            hint3 = text_font.render("to its representation with floating point (using IEEE standard 754 32-bit encoding format)", True, BLACK)
            hint32 = text_font.render("(timeslot[04:16-05:46])", True, BLACK)
            #hint4 = text_font.render("Hint: it is easier to be done through decimal numbers system.", True, BLACK)
            #task_do = text_font.render("*A video from group 37 about Digital Building Blocks is on the Brightspace", True, BLACK)
            mistake_text = text_font_big.render(mistake_count, True, RED)
            WINDOW.blit(mistake_text, (830, 430)) # Currently there is a problem cause it keeps adding +1 to mistake counts if mouse button is pressed down, so often it will add more than one :/
            WINDOW.blit(task_description, (65, 80+0*k))
            WINDOW.blit(task_description1, (65, 80+1*k))
            WINDOW.blit(task_description2, (65, 80+2*k))
            WINDOW.blit(task_description3, (65, 80+3*k))
            WINDOW.blit(hint1, (65, 80+4*k))
            WINDOW.blit(hint12, (65, 80+5*k))
            WINDOW.blit(hint2, (65, 80+6*k))
            WINDOW.blit(hint3, (65, 80+7*k))
            WINDOW.blit(hint32, (65, 80+8*k))
            #WINDOW.blit(hint4, (65, 80+8*k))
            #WINDOW.blit(task_do, (65, 80+9*k))

        if level == 5:
            k = 35
            text_font = pygame.font.SysFont(None, k)
            task_description = text_font.render("Only 2 levels to go meet the Boss! Great job!", True, BLACK)
            task_description1 = text_font.render("Anyway, here you are given a memory array, specifically DRAM (Dynamic Random", True, BLACK)
            task_description2 = text_font.render("Access Memory) array. You can learn more about it and also about other", True, BLACK)
            task_description3 = text_font.render("types of memory arrays in the video (that was already mentioned).", True, BLACK)
            task_description32 = text_font.render("Although, in that memory array some of the elements don't seem right,", True, BLACK)
            task_description4 = text_font.render('for example some of the capacitors are broken or their ground is missing.', True, BLACK)
            task_description5 = text_font.render('Besides all that trouble, some bat have bitten the wire that is being provided', True, BLACK)
            task_description52 = text_font.render("power and we kindly ask to fix all of that ^.^", True, BLACK)
            mistake_text = text_font_big.render(mistake_count, True, RED)
            WINDOW.blit(mistake_text, (830, 430)) # Currently there is a problem cause it keeps adding +1 to mistake counts if mouse button is pressed down, so often it will add more than one :/
            WINDOW.blit(task_description, (65, 80))
            WINDOW.blit(task_description1, (65, 160))
            WINDOW.blit(task_description2, (65, 200))
            WINDOW.blit(task_description3, (65, 240))
            WINDOW.blit(task_description32, (65, 280))
            WINDOW.blit(task_description4, (65, 320))
            WINDOW.blit(task_description5, (65, 360))
            WINDOW.blit(task_description52, (65, 400))

        if level == 6:
            k = 35
            text_font = pygame.font.SysFont(None, k)
            task_description = text_font.render("Wow, you did it, nice! Thank you!", True, BLACK)
            task_description1 = text_font.render("However, same happened to another one of our memory arrays, so can you please", True, BLACK)
            task_description2 = text_font.render("help us with that once again? To keep you focused and organized here is", True, BLACK)
            task_description3 = text_font.render("the task once again:", True, BLACK)
            task_description32 = text_font.render("Here you are given a memory array, specifically DRAM (Dynamic Random", True, BLACK)
            task_description4 = text_font.render('Access Memory) array. Info about it you may find in the video', True, BLACK)
            task_description5 = text_font.render("Although, in that memory array some of the elements don't seem right,", True, BLACK)
            task_description52 = text_font.render("for example some of the capacitors are broken or their ground is missing.", True, BLACK)
            task_description6 = text_font.render("Besides all that trouble, some mice have bitten the wire that is being", True, BLACK)
            task_description7 = text_font.render("provided power and we kindly ask to fix all of that ^.^", True, BLACK)
            mistake_text = text_font_big.render(mistake_count, True, RED)
            WINDOW.blit(mistake_text, (830, 430)) # Currently there is a problem cause it keeps adding +1 to mistake counts if mouse button is pressed down, so often it will add more than one :/
            WINDOW.blit(task_description, (65, 70))
            WINDOW.blit(task_description1, (65, 120))
            WINDOW.blit(task_description2, (65, 160))
            WINDOW.blit(task_description3, (65, 200))
            WINDOW.blit(task_description32, (65, 240))
            WINDOW.blit(task_description4, (65, 280))
            WINDOW.blit(task_description5, (65, 320))
            WINDOW.blit(task_description52, (65, 360))
            WINDOW.blit(task_description6, (65, 400))
            WINDOW.blit(task_description7, (65, 440))


    # Draws the task box on so that it is on top of the white page
    text_font = pygame.font.SysFont(None, 30)
    pygame.draw.rect(WINDOW, WHITE, box_coordinates)
    task_text = text_font.render('TASK', True, BLACK,)
    WINDOW.blit(task_text, (1075,66))
    pygame.draw.rect(WINDOW, BLACK, (1070, 62, 58, 3)) # Top border
    pygame.draw.rect(WINDOW, BLACK, (1070, 65, 3, 23)) # Left border
    pygame.draw.rect(WINDOW, BLACK, (1128, 62, 3, 26)) # Right border
    pygame.draw.rect(WINDOW, BLACK, (1073, 85, 55, 3)) # Bottom border


