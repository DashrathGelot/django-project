import pygame
import random
pygame.init()
clock=pygame.time.Clock()


def sn(window,black,snk_link,size_l,size):
    for x,y in snk_link:
            pygame.draw.rect(window,black,[x,y,size_l,size])

def dis_score(window,font,text,color,x,y):
    screen=font.render(text,True,color)
    window.blit(screen,[x,y])

def game():
    red=(255,0,0)
    white=(0,0,0)
    black=(255,0,0)
    height=376
    width=970

    window=pygame.display.set_mode((width,height))
    pygame.display.set_caption("snakes with me")
    pygame.display.update()
    with open("hiscore.txt","r") as f:
        hiscore=f.read()
    
    play=True
    game_over=False
    snake_x=10
    snake_y=10
    v_x=0
    v_y=0
    size=9
    size_l=9
    fps=19
    food_x=random.randint(10,width-220)
    food_y=random.randint(10,height-50)
    score=0
    snk_link=[]
    snk=1
    last_key_press=''
    las=''

    while play:
        if game_over:
            with open("C:\\Users\\gelot dashrath\\Desktop\\python program\\hiscore.txt","w") as f:
                f.write(str(hiscore))
            dis_score(window,font,"game over ! do you want play again? press enter",(0,0,255),100,10)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    play=False

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        game()
        else:

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    play=False

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT and last_key_press!=pygame.K_LEFT or event.key==pygame.K_d and las!=pygame.K_a:
                        last_key_press=pygame.K_RIGHT
                        las=pygame.K_d
                        v_x=5
                        v_y=0
                    if event.key==pygame.K_LEFT and last_key_press!=pygame.K_RIGHT or event.key==pygame.K_a and las!=pygame.K_d:
                        last_key_press=pygame.K_LEFT
                        las=pygame.K_a
                        v_x=-5
                        v_y=0
                    if event.key==pygame.K_UP and last_key_press!=pygame.K_DOWN or event.key==pygame.K_w and las!=pygame.K_s:
                        last_key_press=pygame.K_UP
                        las=pygame.K_w
                        v_y=-5
                        v_x=0
                    if event.key==pygame.K_DOWN and last_key_press!=pygame.K_UP or event.key==pygame.K_s and las!=pygame.K_w:
                        last_key_press=pygame.K_DOWN
                        las=pygame.K_s
                        v_y=5
                        v_x=0
                    
            snake_x+=v_x
            snake_y+=v_y 

            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                score+=10
                fs=10
                snk+=5
                food_x=random.randint(20,width/2)
                food_y=random.randint(20,height/2)
                if score>int(hiscore):
                    hiscore=score
                if score>fs*10:
                    fps+=3
                    fs+=10

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_link.append(head)

            if len(snk_link)>snk:
                del snk_link[0]

            if head in snk_link[:-1]:
                game_over=True

            if snake_x<9 or snake_x>width-200 or snake_y<9 or snake_y>height-20:
                game_over=True

            window.fill(white)
            sn(window,black,snk_link,size_l,size)
            font=pygame.font.SysFont(None,39)
            dis_score(window,font,"score : "+str(score),(0,0,255),800,1)
            dis_score(window,font,"hiscore : "+str(hiscore),(0,0,255),800,29)

            pygame.draw.rect(window,(0,255,0),[food_x,food_y,size,size])
            pygame.draw.line(window,red,(780,0),(780,380),9)
            pygame.draw.line(window,red,(0,0),(780,0),9)
            pygame.draw.line(window,red,(0,375),(780,375),9)
            pygame.draw.line(window,red,(0,0),(0,380),9)
            clock.tick(fps)
            pygame.display.update()
    pygame.quit()
    quit()
game()