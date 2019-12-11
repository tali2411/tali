import time
import random
name = 0
stage = 1
combat = False
EXP = 0
EXP_needed = 10
def start ():
	global name
	print("Hola mortal, te encuentras en una cueva llena de peligros que deberás explorar a fondo \npara encontrar el botín y la gloria, o tu más temida muerte")
	name = input("\nMe llamo: ")
	print ("Guay, bienvenido %s" %name + ", si tienes cualquier duda, solo escribe help y los dioses te ayudaremos")
start()
class Entity:
	def __init__(self, name, hp, hpmáx, attack, stage, EXP_given):
		self.name = name
		self.hp = hp
		self.hpmáx = hpmáx
		self.attack = attack
		self.stage = stage
		self.EXP_given = EXP_given
	def introduce_self(self):
		print("You have found a " + self.name)
class Player:
	def __init__(self, name, hp, hpmáx, attack, lvl):
		self.name = name
		self.hp = hp
		self.hpmáx = hpmáx
		self.attack = attack
		self.lvl = lvl
#Enemigos clasificados en rareza y sus listas
jabalí = Entity('jabalí', 3, 3, 1, 1, 3)
kóbold = Entity('kóbold', 2, 2, 2, 1, 3)
bestia = Entity('bestia', 5, 5, 2, 1, 5)
mierda_de_vaca = Entity('mierda de vaca', 10, 10, 0, 1, 10)
elfo_parapléjico = Entity('elfo parapléjico', 3, 3, 1, 1, 3)
ogrón = Entity('ogrón', 50, 50, 7, 1, 10)
common_enemies_stage_1 = (jabalí, kóbold, bestia, mierda_de_vaca, elfo_parapléjico)
boss1 = (ogrón)
p = Player(name, 10, 10, 2, 1)
while p.hp > 0:
	line = input ("-> ")
	if line == 'help':
		print('usa el comando:\n','"explore" para explorar la estancia\n','"rest" para descansar y recuperar salud\n','"status" para ver tu salud, EXP...\n'' "attack" para atacar al enemigo\n','"flee" para huir del combate\n','"boss" para enfrentarte al jefe\n','"quit" para salir del juego')
		#Más relleno
	if line == 'status':
		print('HP -> %s'  %p.hp + ' / %d' %p.hpmáx )
		print('Attack -> %r' %p.attack)
		print('EXP -> %s' %EXP + ' / %d' %EXP_needed)
	if line == 'quit':
		p.hp = 0
		#Solo relleno
	if line == 'explore':
		if combat == True:
			print(' ehh que estás en combate')
		if combat == False:
			if stage == 1:
				sucesos_stage_1 = (0, 1, 2)
				happen = random.choice(sucesos_stage_1)
				if happen == 0:
					print(' caminas en la oscuridad y no sucede nada')
				if happen == 1:
					p.hp = p.hp - 1
					print(' te das un golpe con una piedra, que daño!')
				if happen == 2:
					enemy = random.choice(common_enemies_stage_1)
					print(' maldición!, un(a) %s' %enemy.name)
					line = 'otra cosa'
					combat = True
	if line == 'rest':
		if combat == True:
			print(' ehh que estás en combate')
		if combat == False:
			sucesos_rest = (1, 2, 3, 4, 5, 6)
			happenr = random.choice(sucesos_rest)
			if happenr == 1:
				enemy = random.choice(common_enemies_stage_1)
				print(' maldición!, un(a) %s' %enemy.name)
				line = 'otra cosa'
				combat = True
			else:
				p.hp = p.hp + 1
				print(' has dormido bien')
	if line == 'attack':
		if combat == False:
			print(' a quién pretendes atacar????')
		if combat == True:
			enemy.hp = enemy.hp - p.attack
			p.hp = p.hp - enemy.attack
			if enemy.hp <= 0:
				print(' has matado un(a) %s' %enemy.name)
				combat = False
				enemy.hp = enemy.hpmáx
				EXP = EXP + enemy.EXP_given
	if line == 'flee':
		if combat == False:
			print(' deja de correr como un tonto! no te persigue nadie')
		if combat == True:
			print(' huyes como una rata, pero al menos salvas tus nalgas')
			combat = False
	if line == 'boss':
		combat = True
		print('PREPARATÉ')
		print(' maldición!, el OGRÓN es mucho más tocho, poderoso y sensual de lo que pensabas')
		enemy = ogrón
	if line == 'chetos':
		p.hp = 1000
		p.attack = 20000
	if EXP >= EXP_needed:
		p.lvl = p.lvl + 1
		EXP = 0
		EXP_needed = EXP_needed * 2
		p.attack = p.attack + 0.5
		p.hp = p.hp + 2
		p.hpmáx = p.hpmáx + 2
		print(' subes de nivel, ahora estás más mamado, pero basto')
	if p.hp == 0:
		print(name + ' ha muerto, más suerte la próxima vez!')
		print('R.I.P.')
		time.sleep(1.5)