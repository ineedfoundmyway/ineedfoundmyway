from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
OUT=Path(__file__).resolve().parents[1]/'assets'/'terminal'
OUT.mkdir(parents=True,exist_ok=True)
BG='#080A0B'; GREEN='#B9FF35'; FG='#ECF4E4'; DIM='#8D9E89'; LINE='#273327'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
def f(n,b=False):return ImageFont.truetype(BOLD if b else FONT,n)
def render(kind,i):
 h=360 if kind=='identity' else 270
 im=Image.new('RGB',(1200,h),BG);d=ImageDraw.Draw(im)
 d.rectangle((1,1,1198,h-2),outline=LINE)
 for x in range(30,1200,48): d.line((x,46,x,h-38),fill='#0F1510')
 for y in range(46,h-38,24):d.line((30,y,1170,y),fill='#0F1510')
 d.rectangle((0,0,1200,45),fill='#101610')
 for x,c in [(24,GREEN),(46,'#56694B'),(68,'#30402B')]:d.ellipse((x,17,x+9,26),fill=c)
 d.text((100,13),'nyctophile@lab:~ / '+kind,font=f(16),fill=DIM)
 d.text((976,13),'VISUAL STUDY',font=f(14),fill=DIM)
 if kind=='identity':
  d.text((48,72),'N Y C T O P H I L E',font=f(46,True),fill=FG)
  d.text((50,140),'ineedfoundmyway // fullstack & cybersecurity',font=f(21),fill=GREEN)
  lines=['> C + JAVA / THE FOUNDATION','> OFFENSIVE RESEARCH / DEFENSIVE THINKING','> TRACE THE SYSTEM. QUESTION THE ASSUMPTION.']
  for j,s in enumerate(lines):
   d.text((50,199+j*32),s,font=f(18),fill=DIM if j<2 else FG)
  # Abstract flowing hexadecimal columns; decorative, not telemetry.
  for col in range(7):
   for row in range(7):
    k=(row+col*3+i//3)%16
    d.text((900+col*34,73+row*30),format(k,'X'),font=f(19),fill=GREEN if row==(i//4+col)%7 else '#30402B')
 elif kind=='partner':
  d.text((48,68),'OFFICIAL CODE PARTNER',font=f(17),fill=GREEN)
  d.text((45,99),'brunnojob',font=f(46,True),fill=FG)
  d.text((48,165),'ineedfoundmyway + brunnojob',font=f(20),fill=DIM)
  d.text((48,198),'SHARED CODE. SHARED REVIEW. STRONGER SYSTEMS.',font=f(16),fill=FG)
  for y in (91,185):
   d.line((865,y,945,y,1005,138,1135,138),fill='#405832',width=2)
   t=(i/40+(0.5 if y==185 else 0))%1; pts=[(865,y),(945,y),(1005,138),(1135,138)]
   ls=[80,math.hypot(60,138-y),130];dist=t*sum(ls)
   for a,b,l in zip(pts,pts[1:],ls):
    if dist<=l:
     x=a[0]+(b[0]-a[0])*dist/l; yy=a[1]+(b[1]-a[1])*dist/l;break
    dist-=l
   d.ellipse((x-4,yy-4,x+4,yy+4),fill=GREEN)
  d.ellipse((998,131,1012,145),fill=FG)
 elif kind=='toolkit':
  d.text((48,66),'THE TOOLKIT / BELOW THE FRAMEWORK',font=f(24,True),fill=FG)
  labels=['C + JAVA','FULLSTACK','AUTOMATION','BINARIES']
  subs=['logic / data','UI / API / SQL','Python / shell','memory / RE']
  for j,(label,sub) in enumerate(zip(labels,subs)):
   x=48+j*285; active=(i//10)%4==j
   d.rectangle((x,116,x+255,202),outline=GREEN if active else LINE,width=2)
   d.text((x+16,132),label,font=f(20,True),fill=GREEN if active else FG)
   d.text((x+16,167),sub,font=f(15),fill=DIM)
 else:
  d.text((48,66),'ATTACK PATH / DEFENSIVE OUTCOME',font=f(25,True),fill=FG)
  labels=['RECON','ANALYZE','REPRODUCE','HARDEN']
  for j,label in enumerate(labels):
   x=48+j*285
   d.text((x,122),'0'+str(j+1)+' / '+label,font=f(20,True),fill=GREEN if i//10==j else FG)
   d.line((x,165,x+244,165),fill=LINE,width=3)
   if i//10==j:d.line((x,165,x+int(244*((i%10)+1)/10),165),fill=GREEN,width=3)
  d.text((48,198),'CONTROLLED LABS / THREAT RESEARCH / DETECTION & REMEDIATION',font=f(17),fill=DIM)
 d.line((30,h-35,1170,h-35),fill=LINE)
 d.line((30,h-35,30+int(1140*(i+1)/40),h-35),fill=GREEN)
 d.text((30,h-25),'READ THE SOURCE. FOLLOW THE SIGNAL.',font=f(13),fill=DIM)
 d.text((972,h-25),'NYCTOPHILE //',font=f(13),fill=GREEN)
 return im
for kind in ['identity','partner','toolkit','security']:
 frames=[render(kind,i) for i in range(40)]
 frames[0].save(OUT/(kind+'.png'))
 frames[0].save(OUT/(kind+'.gif'),save_all=True,append_images=frames[1:],loop=0,duration=100,optimize=True)
 print(kind,(OUT/(kind+'.gif')).stat().st_size,'bytes')
