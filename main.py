import pygame
import sys
import random
#init
pygame.init()
screen=pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Jeu du pendu")
font=pygame.font.Font(None,35)
button_text= font.render("Jouer",True,(255,255,255))
button_rect= button_text.get_rect(center=(500,350))
button_rect.width += 50
button_rect.height += 20
word_text= font.render("Mot à ajouter...",True,(255,255,255))
word_rect= button_text.get_rect(center=(75,425))
easy_rect= button_text.get_rect(center=(535,150))
easy_text= font.render("easy",True,(255,255,255))
medium_rect= button_text.get_rect(center=(525,225))
medium_text= font.render("medium",True,(255,255,255))
hard_rect= button_text.get_rect(center=(535,300))
hard_text= font.render("hard",True,(255,255,255))
start_rect= button_text.get_rect(center=(535,300))
start_text= font.render("Commencer",True,(255,255,255))
text_rect=pygame.Rect(225, 400,600,50)
image1=pygame.image.load("picture/image1.png")
image2=pygame.image.load("picture/image2.png")
image3=pygame.image.load("picture/image3.png")
image4=pygame.image.load("picture/image4.png")
image5=pygame.image.load("picture/image5.png")
image6=pygame.image.load("picture/image6.png")
image7=pygame.image.load("picture/image7.png")
user_text= ''
score_win=0
score_lose=0
player=""
isgamefinish=True
input_active=False
tentatives = set()  # Pour stocker les lettres déjà essayées   
game=True
start_screen=True
gamemode=False
texte = True
pygame.display.flip()
#creation de listes pour y mettre les mots qui sont dans le fichier mots.txt, ca divise en mot faciles , moyen et difficile
easy_word=[] # listes de mots facile - de 6 lettres
with open("mots.txt","r")as file:
    for i in file:
        if len(i) <= 6:
            easy_word.append(i.rstrip("\n"))
medium_word=[]# listes de mots moyen entre 6 et 9 lettres
with open("mots.txt","r")as file:
    for i in file:
        if len(i) > 6 and len(i) <=9:
            medium_word.append(i.rstrip("\n"))
hard_word=[]#llistes de mots difficiles + de 9 lettres
with open("mots.txt","r")as file:
    for i in file:
        if len(i) >9 :
            hard_word.append(i.rstrip("\n"))                        
print(easy_word)
print(medium_word)
print(hard_word)
def message(message,message_rectangle,color):
    message = font.render(message,False,color)
    screen.blit(message,message_rectangle)

while game:   
    #ecran de debut pour choisir en jouer ou ajouter un mot 
    while start_screen == True:
        for event in pygame.event.get():
            screen.fill((0,130,255))
            screen.blit(button_text, (button_rect.centerx -29 , button_rect.centery -15))
            screen.blit(word_text, (word_rect.centerx -29 , word_rect.centery -15))
            pygame.draw.rect(screen, (0,0,0), button_rect, 2)    
            pygame.draw.rect(screen , (0, 172, 183),(20,20,350,300))   
            message("scores : ",(20,20,350,300),(0,0,0))
            message("comming soon...",(60,100,350,300),(0,0,0))
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    gamemode=True
                    #si l'utilisateur appuie sur jouer , un menu avec les 3 mode de difficultés s'ouvrira
                    while gamemode:                       
                        for event in pygame.event.get():
                            pygame.draw.rect(screen , (0,0,250),(350,90,350,300))
                            screen.blit(easy_text, (easy_rect.centerx -29 , easy_rect.centery -10))
                            screen.blit(medium_text, (medium_rect.centerx -29 , medium_rect.centery -10))
                            screen.blit(hard_text, (hard_rect.centerx -29 ,hard_rect.centery -10))
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if easy_rect.collidepoint(event.pos):
                                    lists= easy_word
                                    start_screen=False
                                    gamemode=False
                                elif medium_rect.collidepoint(event.pos):
                                    lists= medium_word
                                    start_screen=False
                                    gamemode=False
                                elif hard_rect.collidepoint(event.pos):
                                    lists= hard_word
                                    start_screen=False
                                    gamemode=False  
                                random_word= random_word=random.choice(lists)
                                hide_word="-"*len(random_word) 
                                lose =0                      
                            pygame.display.flip()        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si l'utilisateur clique dans la zone de texte, il pourra ecrire le mot qu'il souhaite ajouter
                if text_rect.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN: # lorsqu'il appuiras sur entrée le texte sera ecrit dans le fichier texte
                        with open("mots.txt","a") as file:
                            file.write(user_text+"\n")
                        print(user_text)  
                        user_text = ''  # Efface le texte après avoir appuyé sur Entrée
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]  # Supprime le dernier caractère
                    else:
                        user_text += event.unicode  # Ajoute le texte saisi par l'utilisateur
        pygame.draw.rect(screen, (0,0,0), text_rect, 2)
        #etape pour afficher le texte que l'utilisateur ecrit
        text_surface = font.render(user_text, True,(0,0,0))
        screen.blit(text_surface, (text_rect.x + 5, text_rect.y + 5))

        pygame.display.flip()
    #quand l'utilisateur aura choisi sa difficulté il tombera sur cet event (le jeu du pendu)
    for event in pygame.event.get():
        text_tentatives = font.render("Tentatives: " + ", ".join(sorted(tentatives)), True, (0, 0, 0))
        screen.blit(text_tentatives, (50, 50))
        screen.blit(start_text, (start_rect.centerx -29 , start_rect.centery -10))
        if event.type == pygame.QUIT:
            sys.exit()    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):   

                print(random_word) 
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                tentatives = set()  # Pour stocker les lettres déjà essayées
                random_word= random_word=random.choice(lists)
                hide_word="-"*len(random_word) 
                lose =0
                isgamefinish=True
        if isgamefinish:
            if event.type == pygame.KEYDOWN: 
                if event.unicode.isalpha() and event.unicode.upper() not in tentatives:
                    tentatives.add(event.unicode.upper())
                    if event.unicode.upper() in random_word.upper():
                        hide_word = "".join([i if i.upper() in tentatives else "-" for i in random_word])
                        print(hide_word)
                        print(random_word)                   
                    else:
                        lose +=1    
                        print(lose)
        screen.fill((255,255,255))
        #compte les nombre de fausse lettre de l'utilisateur et les associe aux differentes etapes du pendu (c'est des images)   
        if lose==0:
            screen.blit(image1,(350,200))
        if lose==1:
            screen.blit(image2,(350,200))
        if lose==2:
            screen.blit(image3,(350,200))  
        if lose==3:
            screen.blit(image4,(350,200))
        if lose==4:
            screen.blit(image5,(350,200))
        if lose==5:
            screen.blit(image6,(350,200))
        if lose>=6:
            screen.blit(image7,(350,200))                  
            message("Perdu ! :(",(500, 150,600,50),(255,0,0))    
            message("Appuyez sur échap pour (re)commencer une partie",(225, 50,600,50),(0,0,0)) 
            isgamefinish=False
        if hide_word==random_word:
            message("Gagné ! :D ",(500, 150,600,50),(255,0,0))
            message("Appuyez sur échap pour (re)commencer une partie",(225, 50,600,50),(0,0,0)) 
            score_win +=154
            isgamefinish=False
        message("Tentatives: " + ", ".join(sorted(tentatives)),(50, 115,600,50),(0,0,0))       
        message(hide_word,(450, 450,600,50),(0,0,0))
        pygame.display.flip()    
        
pygame.quit()
sys.exit()