import tkinter
import random
import time
#################################################################################
#
#  Parametres du jeu

canvas = None   # zone de dessin

#Grille[0][0] désigne la case en haut à gauche
#Grille[2][0] désigne la case en haut à droite
#Grille[0][2] désigne la case en bas à gauche


Grille = [ [0,0,0,0,0,0], 
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0] ]  # attention les lignes représentent les colonnes de la grille
           
Scores = [0,0]   # score du joueur 1 (Humain) et 2 (IA)

#################################################################################
#
# gestion du joueur humain et de l'IA
# VOTRE CODE ICI
def restart():
    Grille[0] = [0,0,0,0,0,0]
    Grille[1] = [0,0,0,0,0,0]
    Grille[2] = [0,0,0,0,0,0]
    Grille[3] = [0,0,0,0,0,0]
    Grille[4] = [0,0,0,0,0,0]
    Grille[5] = [0,0,0,0,0,0]
    Grille[6] = [0,0,0,0,0,0]

def Is4AlignPlayer(numPlayer) :
    
    
    for x in range(len(Grille)) :
            for y in range(len(Grille[0])) :
                
                #diagonale haut droite
                for i in range(4) :
                    if ( (x+i<0) or (x+i>6) or (y-i<0) or (y-i>5) ) :
                        break
                    elif Grille[x+i][y-i] != numPlayer:
                        break
                    elif i == 3 :
                        return True
                
                #aligné de gauche vers la droite
                for i in range(4) :
                    if ( (x+i<0) or (x+i>6)) :
                        break
                    elif Grille[x+i][y] != numPlayer:
                        break
                    elif i ==  3:
                        return True
                        
                #diagonale haut gauche
                for i in range(4) :
                    if ( (x-i<0) or (x-i>6) or (y-i<0) or (y-i>5) ) :
                        break
                    elif Grille[x-i][y-i] != numPlayer:
                        break
                    elif i == 3 :
                        return True
              
                #aligné de haut vers le bas
                for i in range(4) :
                    if ( (y+i<0) or (y+i>5)) :
                        break
                    elif Grille[x][y+i] != numPlayer:
                        break
                    elif i == 3 :
                        return True
    
    return False
        
            
def EmptyCases():
    for line in Grille :
        for case in line :
            if case == 0 :
                return
    restart()
    
    
def availablePositions():
    liste = []
    
    for x in range(7) :
            for y in range(5,-1,-1) :
                
                if Grille[x][y] == 0:
                    liste.append((x,y))
                    break
               
                
    return liste 
    
    
def typeAlign(coup,typeAlignement, player):
    

    for x in range(len(Grille)) :
            for y in range(len(Grille[0])) :
                
                #diagonale haut droite
                cpt = 0
                cptEmpty = 0
                cptPlayer = 0 #compte le pion mis 
                for i in range(4) :
                    if ( (x+i<0) or (x+i>6) or (y-i<0) or (y-i>5) ) :
                        break
                    if Grille[x+i][y-i] == player:
                        cpt +=1
                    if Grille[x+i][y-i] == 0:
                        cptEmpty +=1
                    if x+i == coup[0] and y-i == coup[1]:
                        cptPlayer+=1
                    if i == 3 and cpt == 3 and cptPlayer == 1 and cptEmpty == 1 and typeAlignement == 2:
                        return True
                    if i == 3 and cpt == 2 and cptPlayer == 1 and cptEmpty == 2 and typeAlignement == 0:
                        return True
                    
                
                #aligné de gauche vers la droite
                cpt = 0
                cptPlayer = 0 #compte le pion mis
                cptEmpty = 0
                for i in range(4) :
                    if ( (x+i<0) or (x+i>6)) :
                        break
                    if Grille[x+i][y] == player:
                        cpt += 1
                    if Grille[x+i][y] == 0:
                        cptEmpty +=1
                    if x+i == coup[0] and y == coup[1]:
                        cptPlayer+=1
                    if i ==  3 and cpt == 3 and cptPlayer == 1 and cptEmpty == 1 and typeAlignement == 2:
                        return True
                    if i == 3 and cpt == 2 and cptPlayer == 1 and cptEmpty == 2 and typeAlignement == 0:
                        return True
                
                #diagonale haut gauche
                cpt = 0
                cptPlayer = 0 #compte le pion mis
                cptEmpty = 0
                for i in range(4) :
                    if ( (x-i<0) or (x-i>6) or (y-i<0) or (y-i>5) ) :
                        break
                    if Grille[x-i][y-i] == player:
                        cpt+=1
                    if Grille[x-i][y-i] == 0:
                        cptEmpty +=1
                    if x-i == coup[0] and y-i == coup[1]:
                        cptPlayer+=1
                    if i == 3 and cpt == 3 and cptPlayer == 1 and cptEmpty == 1 and typeAlignement == 2:
                        return True
                    if i == 3 and cpt == 2 and cptPlayer == 1 and cptEmpty == 2 and typeAlignement == 0:
                        return True
                    
            
                #aligné de bas vers le haut
                cpt = 0
                cptPlayer = 0 #compte le pion mis
                cptEmpty = 0
                for i in range(4) :
                    if ( (y-i<0) or (y-i>5)) :
                        break
                    if Grille[x][y-i] == player:
                        cpt+=1
                    if Grille[x][y-i] == 0:
                        cptEmpty +=1
                    if x == coup[0] and y-i == coup[1]:
                        cptPlayer+=1
                    if i == 3 and cpt == 3 and cptPlayer == 1 and cptEmpty == 1  and typeAlignement == 2:
                        return True
                    if i == 3 and cpt == 2 and cptPlayer == 1 and cptEmpty == 2 and typeAlignement == 0:
                        return True

    return False
    
def typeBlocAlign(coup,typeAlignement,player):
    
    playerToBloc = 0
    
    if player == 1 :
        playerToBloc = 2
        
    if player == 2 :
        playerToBloc = 1
    
    
        
    for x in range(len(Grille)) :
            for y in range(len(Grille[0])) :
                
                #diagonale haut droite
                cpt = 0
                cptEmpty = 0
                cptPlayer = 0 #compte le pion mis 
                for i in range(4) :
                    if ( (x+i<0) or (x+i>6) or (y-i<0) or (y-i>5) ) :
                        break
                    if Grille[x+i][y-i] == playerToBloc:
                        cpt +=1
                    if Grille[x+i][y-i] == 0:
                        cptEmpty +=1
                    if x+i == coup[0] and y-i == coup[1]:
                        cptPlayer+=1
                    if i == 3 and cpt == 3 and cptPlayer == 1 and cptEmpty == 0 and typeAlignement == 3:
                        return True
                    if i == 3 and cpt == 2 and cptPlayer == 1 and cptEmpty == 1 and typeAlignement == 1:
                        return True
                    
                
                #aligné de gauche vers la droite
                cpt = 0
                cptPlayer = 0 #compte le pion mis
                cptEmpty = 0
                for i in range(4) :
                    if ( (x+i<0) or (x+i>6)) :
                        break
                    if Grille[x+i][y] == playerToBloc:
                        cpt += 1
                    if Grille[x+i][y] == 0:
                        cptEmpty +=1
                    if x+i == coup[0] and y == coup[1]:
                        cptPlayer+=1
                    if i ==  3 and cpt == 3 and cptPlayer == 1 and cptEmpty == 0 and typeAlignement == 3:
                        return True
                    if i == 3 and cpt == 2 and cptPlayer == 1 and cptEmpty == 1 and typeAlignement == 1:
                        return True
                
                #diagonale haut gauche
                cpt = 0
                cptPlayer = 0 #compte le pion mis
                cptEmpty = 0
                for i in range(4) :
                    if ( (x-i<0) or (x-i>6) or (y-i<0) or (y-i>5) ) :
                        break
                    if Grille[x-i][y-i] == playerToBloc:
                        cpt+=1
                    if Grille[x-i][y-i] == 0:
                        cptEmpty +=1
                    if x-i == coup[0] and y-i == coup[1]:
                        cptPlayer+=1
                    if i == 3 and cpt == 3 and cptPlayer == 1 and cptEmpty == 0 and typeAlignement == 3:
                        return True
                    if i == 3 and cpt == 2 and cptPlayer == 1 and cptEmpty == 1 and typeAlignement == 1:
                        return True
                    
            
                #aligné de bas vers le haut
                cpt = 0
                cptPlayer = 0 #compte le pion mis
                cptEmpty = 0
                for i in range(4) :
                    if ( (y-i<0) or (y-i>5)) :
                        break
                    if Grille[x][y-i] == playerToBloc:
                        cpt+=1
                    if Grille[x][y-i] == 0:
                        cptEmpty +=1
                    if x == coup[0] and y-i == coup[1]:
                        cptPlayer+=1
                    if i == 3 and cpt == 3 and cptPlayer == 1 and cptEmpty == 0  and typeAlignement == 3:
                        return True
                    if i == 3 and cpt == 2 and cptPlayer == 1 and cptEmpty == 1 and typeAlignement == 1:
                        return True

    return False
        
    
def isTypeAlign(coup, typeAlignement, player) :
    
    #alignement de 2 sur 4
    if typeAlignement == 0 :
        Grille[coup[0]][coup[1]] = player
        if typeAlign(coup,typeAlignement,player) :
            Grille[coup[0]][coup[1]] = 0
            return True
        else :
            Grille[coup[0]][coup[1]] = 0
            return False
    
    #bloc alignement de 2 sur 4
    if typeAlignement == 1 :
        Grille[coup[0]][coup[1]] = player
        if typeBlocAlign(coup,typeAlignement,player) :
            Grille[coup[0]][coup[1]] = 0
            return True
        else :
            Grille[coup[0]][coup[1]] = 0
            return False
            
    #alignement de 3 sur 4
    if typeAlignement == 2 :
        Grille[coup[0]][coup[1]] = player
        if typeAlign(coup,typeAlignement,player) :
            Grille[coup[0]][coup[1]] = 0
            return True
        else :
            Grille[coup[0]][coup[1]] = 0
            return False
    
    #bloc un alignement de 3 sur 4
    if typeAlignement == 3 :
        Grille[coup[0]][coup[1]] = player
        if typeBlocAlign(coup,typeAlignement,player) :
            Grille[coup[0]][coup[1]] = 0
            return True
        else :
            Grille[coup[0]][coup[1]] = 0
            return False

    #alignement de 4
    if typeAlignement == 4 :
        Grille[coup[0]][coup[1]] = player
        if Is4AlignPlayer(player) :
            Grille[coup[0]][coup[1]] = 0
            return True
        else :
            Grille[coup[0]][coup[1]] = 0
            return False
        
def CalculScore(coup,player) :    
    score = 0
    #si alignement de 2 sur 4 :
    if isTypeAlign(coup,0,player):
        score = 10
    #si bloque alignement de 2 sur 4 : 
    if isTypeAlign(coup,1,player):
        score = 15
    #si alignement de 3 sur 4 :
    if isTypeAlign(coup,2,player):
        score = 30
    #si bloque alignement de 3 sur 4 :
    if isTypeAlign(coup,3,player):
        score = 50
    #si permet un alignement de 4
    if isTypeAlign(coup,4,player):
        score = 100
        
    return score
        
def PlacementJudicieux(player):
    L = availablePositions()
    scores = []
    
    #Calcul des scores
    for coup in L :
        
        scores.append(CalculScore(coup,player))
    
    print(scores)
    #détermination du meilleur score
    bestPos = 0 #case du tableau ayant le plus grand score
    for i in range(len(scores)) :
        if scores[i] > scores[bestPos] :
            bestPos = i
    
    return L[bestPos]    



def Note():
    
    if Is4AlignPlayer(2) :
        return 500
    if Is4AlignPlayer(1) :
        print("test")
        return -500
    
    LIA = []
    LH = []
    
    L = availablePositions()
    
    #Calcul des scores IA
    for coup in L :
        LIA.append(CalculScore(coup,2))
        LH.append(CalculScore(coup,1))
    
    #détermination du meilleur score IA
    bestScoreIA = 0
    for i in range(len(LIA)) :
        if LIA[i] > bestScoreIA :
            bestScoreIA = LIA[i]
    
    #détermination du meilleur score Humain
    bestScoreH = 0
    for i in range(len(LH)) :
        if LIA[i] > bestScoreH :
            bestScoreH = LH[i]
    
    return (bestScoreIA - bestScoreH)


def Minimax():
    L = availablePositions()
    L2 = None
    notes = []
    for coupIA in L :
        Grille[coupIA[0]][coupIA[1]] = 2
        
            
        L2 = availablePositions()
        noteIntermediaire = 0
        
        for coupHumain in L2 :
            
            Grille[coupHumain[0]][coupHumain[1]] = 1
            noteGrille = Note()
            if noteGrille < noteIntermediaire :
                noteIntermediaire = noteGrille
            Grille[coupHumain[0]][coupHumain[1]] = 0

        notes.append(noteIntermediaire)
        Grille[coupIA[0]][coupIA[1]] = 0
    print(notes)
    #détermination du meilleur score
    bestPos = 0 #case du tableau ayant le plus grand score
    for i in range(len(notes)) :
        if notes[i] > notes[bestPos] :
            bestPos = i
    
    return L[bestPos]  
    
    
 
def Play(x,y): 
    
    #IA placement judicieux
    '''
    #Au tour de L'IA placement judicieux
    CoupAJouer = PlacementJudicieux(1)

    Grille[CoupAJouer[0]][CoupAJouer[1]] = 1
    
    
    # liste = availablePositions()
    # directionRandom = random.randrange(len(liste))
    # for i in range(len(liste)) :
    #     if i == directionRandom :
    #         Grille[liste[i][0]][liste[i][1]] = 2
    
    if Is4AlignPlayer(1):
        Scores[0] += 1
        restart()
    EmptyCases()
    
    '''
    
    #joueur réel
    
    #vérification que le joueur 1 clique bien dans une case vide
    L = availablePositions()
    
    for posAvailable in L :
        if posAvailable[0] == x and posAvailable[1] >= y :
            Grille[x][posAvailable[1]] = 1
            if (Is4AlignPlayer(1)) :
                Scores[0] += 1
                restart()
            EmptyCases()
    
            
            Affiche()
            #temporisation
            time.sleep(0.5)
            
            #Au tour de L'IA Minimax
            CoupAJouer = PlacementJudicieux(2)
            #CoupAJouer = Minimax()
            Grille[CoupAJouer[0]][CoupAJouer[1]] = 2
            
            if Is4AlignPlayer(2):
                Scores[1] += 1
                restart()
            EmptyCases()
            
            Affiche()
            
        
            
        
        
          
    
    
################################################################################
#    
# Dessine la grille de jeu


def Affiche(PartieGagnee = False):
        ## DOC canvas : http://tkinter.fdex.eu/doc/caw.html
        canvas.delete("all")
        
        for i in range(8):
            canvas.create_line(i*50,0,i*50,300,fill="lightgray", width="4" )
            
        for i in range(7):
            canvas.create_line(0,i*50,350,i*50,fill="lightgray", width="4" )
            
        for x in range(7):
            for y in range(6):
                xc = x * 50 
                yc = y * 50
                
                if ( Grille[x][y] == 1):
                    canvas.create_oval(xc+10,yc+10,xc+40,yc+40,outline="yellow", width="4", fill = "yellow" )

                
                if ( Grille[x][y] == 2):
                    canvas.create_oval(xc+10,yc+10,xc+40,yc+40,outline="red", width="4", fill = "red" )
        
        msg = 'SCORES : ' + str(Scores[0]) + '-' + str(Scores[1])
        fillcoul = 'gray'
        if (PartieGagnee) : fillcoul = 'red'
        canvas.create_text(175,400, font=('Helvetica', 30), text = msg, fill=fillcoul)  
        
    
        canvas.update()   #force la mise a jour de la zone de dessin
        
  
####################################################################################
#
#  fnt appelée par un clic souris sur la zone de dessin

def MouseClick(event):
   
    window.focus_set()
    x = event.x // 50  # convertit une coordonée pixel écran en coord grille de jeu
    y = event.y // 50
    if ( (x<0) or (x>7) or (y<0) or (y>8) ) : return
     
    
    print("clicked at", x,y)
    
    Play(x,y)  # gestion du joueur humain et de l'IA
    

#####################################################################################
#
#  Mise en place de l'interface - ne pas toucher

# fenetre
window = tkinter.Tk()
window.geometry("350x500") 
window.title('Mon Super Jeu')
window.protocol("WM_DELETE_WINDOW", lambda : window.destroy())
window.bind("<Button-1>", MouseClick)

#zone de dessin
WIDTH = 350
HEIGHT = 500
canvas = tkinter.Canvas(window, width=WIDTH , height=HEIGHT, bg="#000000")
canvas.place(x=0,y=0)
Affiche()
 
# active la fenetre 
window.mainloop()


    
        

      
 

