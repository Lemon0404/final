import pyxel

class App:
    def __init__(self):
        pyxel.init(200,200)
        pyxel.sounds[0].set(notes='C3A3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sounds[1].set(notes='C3A2', tones='TT', volumes='33', effects='NN', speed=10)

        pyxel.mouse(True)
        self.bullets = []
        self.score=0
        self.speed=2
        self.n=[0]
        self.GameOver=False
        self.ball_count=0
        self.GetBall_count=0
        self.stage=1
        self.combo=False
        self.combo_ball=0
        self.balls=[]
        self.pad=Pad()
        self.balls.append(Ball())

        pyxel.run(self.update, self.draw)


    def update(self):

        self.pad.x = pyxel.mouse_x

        if self.GameOver:
            return 
        else:

            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.bullets.append(Bullet(pyxel.mouse_x))

            for bullet in self.bullets:
                bullet.move()
            
            for i in range(self.stage):
                self.balls[i].x += self.balls[i].vx*self.speed
                self.balls[i].y += self.balls[i].vy*self.speed
            
                if Pad.catch(self.pad,ball=self.balls[i]) and self.n[i]==0:
                    pyxel.play(0,0)
                    self.score += 10
                    self.n[i]+=1
                    self.combo=True
                    self.GetBall_count+=1
                    self.combo_ball+=1
                elif self.balls[i].y >=200 and self.n[i]==0:
                    self.ball_count+=1
                    self.combo=False
                    self.combo_ball=0

                if self.balls[i].y >= 200:
                    self.n[i]=0
                    self.speed+=0.2
                    self.balls[i].restart()

                self.balls[i].move()

            if self.GetBall_count>=10:
                self.stage+=1
                self.balls.append(Ball())
                self.GetBall_count=0
                self.speed=2
                self.n.append(0)
            if self.ball_count>=10:
                self.GameOver=True
                

    def draw(self):
        if self.GameOver:
            pyxel.text(90,90,"GameOver",0)
        else:
            pyxel.cls(7)
            for bullet in self.bullets:
                bullet.draw()
            for i in range(self.stage):
                pyxel.circ(self.balls[i].x,self.balls[i].y,10,6)
                pyxel.rect(self.pad.x-20, 195, 40, 5, 14)
                pyxel.text(8,8,"score: "+str(self.score),0)
            if self.combo:
                pyxel.text(8,18,str(self.combo_ball)+" Combo!",0)

class Ball:
    def __init__(self):
        Ball.restart(self)

    def restart(self):
        self.x = pyxel.rndi(0, 199)    #0から画面の横幅-1の間
        self.y = 0
        angle = pyxel.rndi(30, 150)    #30度から150度の間
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)

    def move(self):
        if self.x >190 or self.x<10:
                self.vx=-self.vx

    

class Pad:
    def __init__(self):
        self.x=100

    def catch(self,ball):
        if ball.y>=195 and self.x-19<ball.x<self.x+39:
            return True
        else:
            return False
        
class Bullet:
    def __init__(self, x):
        self.x=x
        self.y=200

    def move(self):
        self.y -= 5

    def draw(self):
        pyxel.circ(self.x, self.y, 2, 4)


App()