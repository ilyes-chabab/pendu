import pygame
import sys
import random

pygame.init()
screen=pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Jeu du pendu")
font=pygame.font.Font(None,35)
button_text= font.render("Jouer",True,(255,255,255))
button_rect= button_text.get_rect(center=(500,350))
button_rect.width += 50
button_rect.height += 20
text_rect=pygame.Rect(225, 400,600,50)

user_text= ''
input_active=False


pygame.display.flip()
mot=[]

with open("mots.txt","r")as file:
    for i in file:
        mot.append(i.rstrip("\n"))

def message(message,message_rectangle,color):
    message = font.render(message,False,color)
    screen.blit(message,message_rectangle)    

image1=pygame.image.load("picture/image1.png")
image2=pygame.image.load("picture/image2.png")
image3=pygame.image.load("picture/image3.png")
image4=pygame.image.load("picture/image4.png")
image5=pygame.image.load("picture/image5.png")
image6=pygame.image.load("picture/image6.png")
image7=pygame.image.load("picture/image7.png")

tentatives = set()  # Pour stocker les lettres déjà essayées
random_word= random_word=random.choice(mot)
hide_word="-"*len(random_word)
lose=0
win=0
game=True
start_screen=True
while game:   
    while start_screen == True:
        for event in pygame.event.get():
            text_jouer=pygame.Rect(225,300,600,50)
            screen.fill((0,0,255))
            screen.blit(button_text, (button_rect.centerx -29 , button_rect.centery -10))
            pygame.draw.rect(screen, (0,0,0), button_rect, 2)
                        
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    start_screen=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si l'utilisateur clique dans la zone de texte, activez l'entrée de texte
                if text_rect.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        with open("mots.txt","a") as file:
                            file.write(user_text+"\n")
                        print(user_text)  # Affiche le texte lorsque l'utilisateur appuie sur Entrée
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

    for event in pygame.event.get():
        text_tentatives = font.render("Tentatives: " + ", ".join(sorted(tentatives)), True, (0, 0, 0))
        screen.blit(text_tentatives, (50, 50))
        
        if event.type == pygame.QUIT:
            sys.exit()    
        print(random_word) 
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                tentatives = set()  # Pour stocker les lettres déjà essayées
                random_word= random_word=random.choice(mot)
                hide_word="-"*len(random_word) 
                lose =0 
                win=0
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha() and event.unicode.upper() not in tentatives:
                tentatives.add(event.unicode.upper())

                if event.unicode.upper() in random_word.upper():
                    hide_word = "".join([i if i.upper() in tentatives else "-" for i in random_word])
                else:
                    lose +=1    
                    print(lose)
        

        screen.fill((0,255,255))   
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
        message("Tentatives: " + ", ".join(sorted(tentatives)),(50, 115,600,50),(0,0,0))       
        message(hide_word,(450, 450,600,50),(0,0,0))
        pygame.display.flip()    
        

pygame.quit()
sys.exit()