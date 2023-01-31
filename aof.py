import time

def ex1():
	top_values = [0,0,0]

	lines = open("1.txt").readlines()
	value = 0
	for element in lines:
		if element == "\n":
			if value > top_values[0]:
				top_values.insert(0, value)
			elif value > top_values[1]:
				top_values.insert(1, value)
			elif value > top_values[2]:
				top_values.insert(2, value)

			value = 0
		else:
			value += int(element.replace("\n",""))


	print("top values: {}".format(top_values[0:3]))
	print("top 3: {}".format(sum(top_values[0:3])))


def ex2(part2 = False):
	lines = open("2.txt").readlines() 

	total_points = 0
	for line in lines:
		game_values = [0,0]

		#Convierto letras en números
		game_values[0] = ord(line.replace("\n","").split(" ")[0])-65	#ABC
		game_values[1] = ord(line.replace("\n","").split(" ")[1])-88	#XYZ

		if part2 == True:
			#Asigno el valor de mi jugada dependiendo de si pierdo (0), empato(1) o gano(2)
			game_values[1] = (game_values[1] + game_values[0] + 2) %3

		#Puntuación por la selección piedra(1), papel(2), tijeras(3)
		points = game_values[1] +1

		#Cambio las jugadas para hacerlas semejantes a que el oponente siempre saque papel op(piedra) - yo (papel) --> op(papel) - yo (tijera)
		if game_values[0] == 2:
			game_values[0] = (game_values[0] + 2)%3
			game_values[1] = (game_values[1] + 2)%3
		if game_values[0] == 0:
			game_values[0] = (game_values[0] + 1)%3
			game_values[1] = (game_values[1] + 1)%3

		#Comparaciones de resultados, ganar 6 ptos, empatar 3 ptos
		if (game_values[1]%3) > game_values[0]%3:
			points += 6
		elif game_values[1]%3 == game_values[0]%3:
			points += 3

		total_points += points

	print(total_points)
			

def ex3():
	lines = open("3.txt").readlines()
	groups = []

	group = []
	group_item = 0
	priority = 0
	for line in lines:
		line = line.replace("\n", "")
		sock1 = line[:int((len(line)/2))]
		sock2 = line[(int(len(line)/2)):]

		group.append(line)
		dupped_chars = []

		for char in sock1:
			if char in sock2 and char not in dupped_chars:
				dupped_chars.append(char)

		for dupped_char in dupped_chars:
			if dupped_char.islower():
				priority += ord(dupped_char)- 97 + 1
			else:
				priority += ord(dupped_char)- 65 + 27

		group_item += 1
		if group_item == 3:
			group_item = 0
			groups.append(group)
			group = []


	group_priority = 0
	for group in groups:
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		alphabet += alphabet.upper()
		for letter in alphabet:
			if letter in group[0] and letter in group[1] and letter in group[2]:
				if letter.islower():
					group_priority += ord(letter)- 97 + 1
				else:
					group_priority += ord(letter)- 65 + 27
	
	print("priority: " + str(priority))
	print("group priority: " + str(group_priority))



def ex4():
	lines = open("4.txt").readlines()

	sections_that_contains_another = 0
	sections_with_overlaps = 0

	for line in lines:
		line = line.replace("\n", "")

		section1 = [0,0]
		section2 = [0,0]

		section1[0] = int(line.split(",")[0].split("-")[0])
		section1[1] = int(line.split(",")[0].split("-")[1])

		section2[0] = int(line.split(",")[1].split("-")[0])
		section2[1] = int(line.split(",")[1].split("-")[1])

		#la seccion 1 siempre la más grande. Si no ocurre las intercambio para que sea así
		if (section1[1] - section1[0]) < (section2[1] - section2[0]):
			section2[0], section1[0] = section1[0], section2[0]
			section2[1], section1[1] = section1[1], section2[1]

		#seccion dentro de otra completamente
		if section1[0] <= section2[0] and section1[1] >= section2[1]:
			sections_that_contains_another += 1

		#Sección que tiene coincidencias con otra 
		if section1[1] >= section2[0] and section2[1] >= section1[0]:
			sections_with_overlaps += 1

	print(sections_that_contains_another)
	print(sections_with_overlaps)



def ex5(part2 = False):
	lists = {}
	#Creo diccionario con listas vacias
	for i in range(9):
		lists[str(i+1)] = []

	for line in open("5.txt").readlines():
		line = line.replace("\n", "")
		if line.startswith("move"):
			#####             Cuantas                 from                  a 
			action = [int(line.split(" ")[1]), line.split(" ")[3], line.split(" ")[5]]

			#Creo lista con las cajas a mover
			moves = []
			for i in range(action[0]):
				moves.append(lists[action[1]].pop())

			#Si es la parte dos las cajas no cambian el orden, por lo que el pop lo invierto
			if part2:
				moves = moves[::-1]

			#Concateno las listas
			lists[action[2]] += moves

		#Relleno automáticamente el diccionario con la entrada
		elif len(line) > 1:
			#print(line)
			for i in range(9):
				if line[1+4*i] != " " and line[1+4*i] not in "0123456789":
					lists[str(i+1)].insert(0, line[1+4*i])

	
	result = ""
	for key in lists.keys():
		if len(lists[key]) > 0:
			result += lists[key][-1]
	print(result)


def ex6():

	for line in open("6.txt").readlines():
		line = line.replace("\n", "")

		offset = []
		part1 = 0
		
		for char in line:
			offset.append(char)
			#A partir del 4 para la parte 1
			if len(offset) >= 4+1:
				offset = offset[1:]
				#Si la longitud de la lista es igual a la longitud del set es que todos los caracteres son distintos
				if(len(offset) == len(set(offset))) and part1 == 0:
					part1 = line.index(''.join(offset)) + 4
					break	#aunque ta feo es eficiente

		offset = []
		part2 = 0
		for char in line:
			offset.append(char)
			#A partir del 14 para la parte 2
			if len(offset) >= 14+1:
				offset = offset[1:]
				#Si la longitud de la lista es igual a la longitud del set es que todos los caracteres son distintos
				if(len(offset) == len(set(offset))) and part2 == 0:
					part2 = line.index(''.join(offset)) + 14
					break	#aunque ta feo es eficiente

		print("part1: {}".format(part1))
		print("part2: {}".format(part2))


def ex7():

	class Dir:
		name = ""
		children = []
		parent = None
		size = -1
		folder_size = 0

		def __init__(self, name = "root", children = [], parent = None, size = -1):
			self.name = name
			self.children = children
			self.parent = parent
			self.size = size
		def hasChild(self,child):
			my_childs_names = []
			for my_childs in self.children:
				my_childs_names.append(my_childs.name)
			return child.name in my_childs_names
		def repr(self, tabs = ""):
			if self.size == -1:
				print(tabs + "D>" + self.name + " " + str(self.folder_size))
			else:
				print(tabs + self.name + " " + str(self.size))

	
	def showTree(actual_dir, depth = 0):
		tabs = ""
		for i in range(depth):
			tabs += "\t"
		actual_dir.repr(tabs)
		
		for child in actual_dir.children:
			showTree(child, depth+1)

	def getFolderSizes(actual_dir):
		for child in actual_dir.children:
			if child.size > -1:
				child.parent.folder_size += child.size
			else:
				getFolderSizes(child)
				child.parent.folder_size += child.folder_size

	total_size = 0

	root = Dir("root", [], None, -1)
	actual_dir = root
	for line in open("7.txt").readlines():
		line = line.replace("\n","")

		if line.startswith("$ "):
			if line == "$ cd /":
				actual_dir = root
			elif line == "$ cd ..":
				actual_dir = actual_dir.parent
			elif line.startswith("$ cd "):
				for child in actual_dir.children:
					if child.name == line.replace("$ cd ", ""):
						actual_dir = child
		else:
			if line.startswith("dir "):
				child = Dir(line.replace("dir ", ""), [], actual_dir, -1)
				if not actual_dir.hasChild(child):
					actual_dir.children.append(child)
			else:
				child = Dir(line.split(" ")[1], [], actual_dir, int(line.split(" ")[0]))
				total_size += child.size
				if not actual_dir.hasChild(child):
					actual_dir.children.append(child)

	getFolderSizes(root)
	#showTree(root)
	

	def sumDirectoriesLessThan(actual_dir, total, size = 100000):
		if not actual_dir.size == -1:
			return 0
		else:
			#print(actual_dir.name + " " + str(total))
			if actual_dir.folder_size <= size:
				total += actual_dir.folder_size
			for child in actual_dir.children:
				aux = sumDirectoriesLessThan(child, total)
				if aux > 0:
					total = aux

			return total

	def showTreeWithMoreSizeThan(actual_dir, size, depth = 0):
		global all_size
		tabs = ""
		for i in range(depth):
			tabs += "\t"
			pass
		actual_dir.repr(tabs)
		
		for child in actual_dir.children:
			if child.folder_size <= size:
				#print("  " + child.name + " Sumado!")
				all_size += child.folder_size
				showTreeWithMoreSizeThan(child, size, depth+1)


	#showTreeWithMoreSizeThan(root, 100000)
	total = sumDirectoriesLessThan(root, 0)

	print("Total sum of directories less than 100000: " + str(total))

	total_space = 70000000
	used_space = root.folder_size
	required_space = 30000000 - (total_space - used_space)


	#print("required_space: " + str(required_space))


	all_dirs = []

	def getAllDirs(actual_dir, all_dirs):
		if actual_dir not in all_dirs:
			all_dirs.append(actual_dir)

		for child in actual_dir.children:
			getAllDirs(child, all_dirs)

	#print(len(all_dirs))
	getAllDirs(root, all_dirs)

	#print(len(all_dirs))


	def sortDirs(dirs):
		for i in range(len(dirs)-1, 0, -1):
			for j in range(i):
				if dirs[j].folder_size > dirs[j+1].folder_size:
					dirs[j], dirs[j+1] = dirs[j+1], dirs[j]
		return dirs

	sortDirs(all_dirs)

	i = 0
	while all_dirs[i].folder_size < required_space:
		i+=1

	print("Should delete folder: " + all_dirs[i].name + " with size of " + str(all_dirs[i].folder_size))


def ex8():
	trees = []
	for line in open("8.txt").readlines():
		line = line.replace("\n","")
		row = []
		for num in line:
			row.append(int(num))
		trees.append(row)

	#check if trees are lower from the right
	def checkHeigh(trees, x,y):
		####     	top left  right  bottom
		visible = [0,0,0,0]
		view_range = [0,0,0,0]

		tree_heigth = trees[x][y]

		x_length = len(trees)
		y_length = len(trees[0])

		#Check top
		if x == 0:
			visible[0] = 1
		else:
			xi = x-1
			visible[0] = 1
			#view_range[0] += 1
			while xi >= 0 and visible[0] == 1:
				view_range[0] += 1
				if trees[xi][y] >= tree_heigth:
					visible[0] = 0
				xi-=1

		#Check bottom
		if x == x_length-1:
			visible[3] = 1
		else:
			xi = x+1
			visible[3] = 1
			while xi < x_length and visible[3] == 1:
				view_range[3] += 1
				if trees[xi][y] >= tree_heigth:
					visible[3] = 0
				xi+=1

		#Check left
		if y == 0:
			visible[1] = 1
		else:
			yi = y-1
			visible[1] = 1
			while yi >= 0 and visible[1] == 1:
				view_range[1] += 1
				if trees[x][yi] >= tree_heigth:
					visible[1] = 0
				yi-=1

		#Check right
		if y == y_length-1:
			visible[2] = 1
		else:
			yi = y+1
			visible[2] = 1
			while yi < y_length and visible[2] == 1:
				view_range[2] += 1
				if trees[x][yi] >= tree_heigth:
					visible[2] = 0
				yi+=1

		return visible, view_range


	visible_trees = []
	visible_range = []
	for row in range(len(trees)):
		visible_trees.append([])
		visible_range.append([])
		for col in range(len(trees[row])):
			visible_trees[row].append(0)
			visible_range[row].append(0)

			checkHeightIs = checkHeigh(trees, row, col)
			for is_visible in checkHeightIs[0]:
				if is_visible == 1:
					visible_trees[row][col] = 1

			#El rango de visión de cada arbol se mide multiplicando los árboles que ve en cada dirección
			visible_range[row][col] = checkHeightIs[1][0]*checkHeightIs[1][1]*checkHeightIs[1][2]*checkHeightIs[1][3]


	total_visible = 0
	heigh_scenic = 0
	for row in range(len(trees)):
		if heigh_scenic < max(visible_range[row]):
			heigh_scenic = max(visible_range[row])

		for col in range(len(trees[row])):
			total_visible += visible_trees[row][col]



	print("Visible trees = " + str(total_visible))
	print("Highest scenic = " + str(heigh_scenic))


def ex9(part2):
	matrix = []
	matrix_size = 1000
	for i in range(matrix_size):
		matrix.append([])
		for j in range(matrix_size):
			matrix[i].append(0)

	start = [int(matrix_size/2), int(matrix_size/2)]

	rope = []

	if part2:
		knots = 10
	else:
		knots = 2

	for i in range(knots):
		rope.append([start[0],start[1]])

	def printMatrix(matrix, rope):
		matrix_to_print = []
		for i in range(len(matrix)):
			matrix_to_print.append([])
			for j in range(len(matrix)):
				matrix_to_print[i].append([])
				if matrix[i][j] == 0:
					matrix_to_print[i][j] = "· "
				elif matrix[i][j] >= 1:
					matrix_to_print[i][j] = "# "
				for k in reversed(range(len(rope))):
					if rope[k][0] == i and rope[k][1] == j:
						matrix_to_print[i][j] = "{} ".format(k)

		for row in matrix_to_print:
			print(''.join(row))
		time.sleep(1/4)

		return matrix_to_print
	
	def udpateTailKnot(rope, direction):
		prev_knot_pos = []
		for i in range(len(rope)):
			prev_knot_pos.append([])
			for j in range(len(rope[i])):
				prev_knot_pos[i].append(rope[i][j])

		#Muevo el head
		if direction == 'U':
			rope[0][0] -= 1
		elif direction == 'D':
			rope[0][0] += 1
		elif direction == 'R':
			rope[0][1] += 1
		elif direction == 'L':
			rope[0][1] -= 1
		print("rope {} {}".format(0, rope[0]))

		#Muevo el resto
		for knot in range(1, len(rope)):
			#Si estoy a dos de distancia del anterior actualizo por cualquier eje
			if abs(rope[knot-1][0] - rope[knot][0]) >= 2 or abs(rope[knot-1][1] - rope[knot][1]) >= 2:
				#Para la parte uno
				#En este caso el punto justo detrás de la cola siempre se mueve a la posición en la que estaba la cabeza la posición anterior
				if knot <= 1:
					rope[knot] = [prev_knot_pos[knot-1][0], prev_knot_pos[knot-1][1]]

				#Los siguientes nudos tienen un tratamiento distinto
				elif knot > 1:
					
					x_movement = 0
					y_movement = 0

					#Si la distancia entre un nudo y el anterior es 1 en cualquier eje, me muevo en esa dirección en 1 unidad
					if abs(rope[knot-1][0]-rope[knot][0]) == 1:
						x_movement = rope[knot-1][0]-rope[knot][0]
					if abs(rope[knot-1][1]-rope[knot][1]) == 1:
						y_movement = rope[knot-1][1]-rope[knot][1]

					#Para los movimientos raros en diagonal
					#Si la distancia entre un nudo y el anterior es dos, me muevo en esa dirección en una unidad también
					if abs(rope[knot-1][0]-rope[knot][0]) >= 2:
						x_movement = int((rope[knot-1][0]-rope[knot][0])/2)
					if abs(rope[knot-1][1]-rope[knot][1]) >= 2:
						y_movement = int((rope[knot-1][1]-rope[knot][1])/2)

					rope[knot][0] += x_movement
					rope[knot][1] += y_movement

					#Imprime la diferencia entre el nudo y el anterior y el movimiento relativo
					print("diff: [{},{}]".format((rope[knot-1][0]-rope[knot][0]),(rope[knot-1][1]-rope[knot][1])))
					print("move: [{},{}]".format(x_movement,y_movement))
			
			#La posición en la que queda el nudo
			print("rope {} {}".format(knot, rope[knot]))
			#printMatrix(matrix, rope)


		return rope


	for line in open("9.txt").readlines():
		line = line.replace("\n","")

		direction = line.split(" ")[0]
		distance = int(line.split(" ")[1])


		for step in range(distance):
			print(line)
			#printMatrix(matrix, rope)

			rope = udpateTailKnot(rope, direction)

			matrix[rope[-1][0]][rope[-1][1]] += 1
			


	final_matrix = printMatrix(matrix, rope)

	total_position_visited = 0
	for row in final_matrix:
		for element in row:
			if element in ['# ']:
				total_position_visited += 1
		
	#El valor 9 o 1 también cuenta. Esto es por como yo realizo la matriz "#" por donde visitó el último punto, y el último punto 1 o 9
	total_position_visited += 1

	print("Total position Visited = {}".format(total_position_visited))


def ex10():
	X = 1
	cycle_number = 0
	signal_strength = 0

	image = [0] * (40*6)
	image2 = []

	def setSprite(x):
		sprite = [0] * 40	#list de 40 ceros

		if x > 0 and x < 39:
			sprite[x-1] = 1
			sprite[x] = 1
			sprite[x+1] = 1
		if x+1 >= 39 or x-1 <= 0:
			#sprite[(x-1)%40] = 1
			sprite[x%40] = 1
			sprite[(x+1)%40] = 1

		return sprite

	def printValues(cycle_number, X):
		print("cycle number  : {}".format(cycle_number) )
		print("register value: {}".format(X) )
		print("Signal strength = {}".format(X*cycle_number))
		print()

	def convertImage(image):
		l = [str(x) for x in image]
		return ''.join(l).replace('0', '·').replace('1','#')

	def printImage(image):
		for i in range(int(len(image)/40)):
			l = image[i*40:(i+1)*40]
			print(''.join(l))

	for line in open("10.txt").readlines():
		line = line.replace("\n","")

		#image[cycle_number] = setSprite(X%(len(setSprite(1))-1))[cycle_number%len(setSprite(1))]
		printValues(cycle_number, X)
		print()
		
		sprite = convertImage(setSprite(X))
		image2.append(sprite[cycle_number%40])


		#print(sprite)
		#print(''.join(image2))



		cycle_number += 1
		
		if ((20+cycle_number)%40) == 0:
			signal_strength += X*cycle_number

		if line.startswith("addx"):
			sprite = convertImage(setSprite(X))
			image2.append(sprite[cycle_number%40])
			printValues(cycle_number, X)
			print(line)
			cycle_number += 1
			if ((20+cycle_number)%40) == 0:
				printValues(cycle_number, X)
				signal_strength += X*cycle_number
			X += int(line.split("addx ")[1])

	
	print("Total signal strength: {}".format(signal_strength))
	printImage(image2)

def ex11(part2):
	monkeys = []
	rounds = 20

	if part2:
		rounds = 10000

	class Monkey:
		name = ""
		item_list = []
		operation = ""
		cuantity = 0
		test = 0
		true_to_monkey = ""
		false_to_monkey = ""
		inspected_items = 0

		def __init__(self, name):
			self.name = name
		def __repr__(self):
			return "{}, {}, {}, {}, {}, {}, {}, {}".format(self.name, self.item_list, self.operation, self.cuantity, self.test, self.true_to_monkey, self.false_to_monkey, self.inspected_items)


	for line in open("11.txt").readlines():
		line = line.replace("\n","")

		if line.startswith("Monkey "):
			monkey = Monkey(line.replace(":", "").lower())

		if "Starting items: " in line:
			items = [int(item) for item in line.split("Starting items: ")[1].split(", ")]
			monkey.item_list = items
		
		if "Operation: new = " in line:
			operation = line.split("Operation: new = ")[1]
			if "*" in operation:
				if operation.count("old") == 2:
					monkey.operation = "^2"
				else:
					monkey.operation = "*"
			elif "+" in operation:
				monkey.operation = "+"

		if "Operation: new = " in line and monkey.operation != "^2":
			monkey.cuantity = int(line.split("Operation: new = ")[1].split(" ")[-1])

		if "  Test: divisible by " in line:
			monkey.test = int(line.split("  Test: divisible by ")[1])

		if "    If true: throw to " in line:
			monkey.true_to_monkey = line.split("    If true: throw to ")[1]
		if "    If false: throw to " in line:
			monkey.false_to_monkey = line.split("    If false: throw to ")[1]

		if line == "":
			monkeys.append(monkey)
			monkey = None

	monkeys.append(monkey)


	#Itero en rondas
	for roundx in range(rounds):
		if roundx % 1000 == 0:
			print()
			print("Round {}".format(roundx))
			for monkey in monkeys:
				print(repr(monkey))
			print()
		#time.sleep(1)
		#Itero en monos
		for monkey in monkeys:
			print("- " + monkey.name)
			
			#Itero en objetos en monos
			for item in monkey.item_list:
				monkey.inspected_items += 1
				worry_level = item
				new_worry_level = 0
				if monkey.operation == "^2":
					new_worry_level = worry_level**2
				elif monkey.operation == "*":
					new_worry_level = worry_level*monkey.cuantity
				elif monkey.operation == "+":
					new_worry_level = worry_level+monkey.cuantity
				
				#Reduzco el nivel de preocupación cuando el mono deja el item
				if part2:
					mod = 1
					for monkey_aux in monkeys:
						mod *= monkey_aux.test
					new_worry_level = new_worry_level % mod

				else:
					new_worry_level = int(new_worry_level/3)

				#itero en la lista de monos para tirarle el item a otro mono
				#print("new_worry_level:{} -> {}".format(worry_level, new_worry_level))
				for to_monkey in monkeys:
					#print("# " + monkey_name + " " + to_monkey.name)
					if (to_monkey.name == monkey.true_to_monkey and new_worry_level%monkey.test == 0) or (to_monkey.name == monkey.false_to_monkey and new_worry_level%monkey.test != 0):
						to_monkey.item_list.append(new_worry_level)
						print("  > {}, {}".format(to_monkey.name,to_monkey.item_list))


			monkey.item_list = []

	first_inspector = 0
	second_inspector = 0

	print("Round {}".format(rounds))
	for monkey in monkeys:
		if monkey.inspected_items > first_inspector:
			second_inspector = first_inspector
			first_inspector = monkey.inspected_items
		if monkey.inspected_items < first_inspector and monkey.inspected_items > second_inspector:
			second_inspector = monkey.inspected_items

		print(repr(monkey))
	print()

	print("first_inspector: {}".format(first_inspector))
	print("second_inspector: {}".format(second_inspector))
	print("product: {}".format(first_inspector*second_inspector))


def ex12():
	from rgbprint import rgbprint,Color

	def printMap(my_map, path = [], reachable_zone=[], banned_pos = []):
		heigthest = 0
		lowest = 0
		for row in my_map:
			if max(row) > heigthest:
				heigthest = max(row)
			if min(row) < lowest:
				lowest = min(row)
		print_map = []
		for row_i in range(len(my_map)):
			print_map.append([])
			for element in range(len(my_map[row_i])):
				if banned_pos != [] and [row_i,element] in banned_pos:
					print_map[row_i].append([ord('X')-97,Color(255,0,255)])
				elif reachable_zone != [] and [row_i,element] not in reachable_zone:
					print_map[row_i].append([my_map[row_i][element],Color(0,0,0)])
				else:
					if [row_i, element] in path:
						print_map[row_i].append([my_map[row_i][element],Color(0,255,255)])
					else:
						value = (my_map[row_i][element]-lowest)/(heigthest-lowest)	#normalizado
						color = int(value*255)
						x = color
						multiplicator = 255/max([x,255-x])
						print_map[row_i].append([my_map[row_i][element],Color(int(x*multiplicator),int((255-x)*multiplicator),0)])

		if path != []:
			print_map[path[-1][0]][path[-1][1]][1] = Color(255,255,255)
			print_map[path[0][0]][path[0][1]][1] = Color(255,255,255)

		for row in print_map:
			for element in row:
				rgbprint(chr(element[0]+97),end="",color=element[1])
			rgbprint("\n", end="")
		time.sleep(1)

	def canMove(heigthmap, position, destination = []):
		possible_moves = []
		#Es posible un movimiento a arriba
		if position[0] > 0 and position[0] <= len(heigthmap)-1:
			#print("arriba")
			#Si la altura de donde estoy está a menos de una unidad de alto de a donde voy
			if abs(heigthmap[position[0]][position[1]] - heigthmap[position[0]-1][position[1]]) <= 1:
				possible_moves.append([position[0]-1,position[1]])
		
		#Es posible un movimiento a abajo
		if position[0] >= 0 and position[0] < len(heigthmap)-1:
			#print("abajo")
			if abs(heigthmap[position[0]][position[1]] - heigthmap[position[0]+1][position[1]]) <= 1:
				possible_moves.append([position[0]+1,position[1]])
		
		#Es posible un movimiento a izquierdas
		if position[1] > 0 and position[1] <= len(heigthmap[0])-1:
			#print("izquierda")
			if abs(heigthmap[position[0]][position[1]] - heigthmap[position[0]][position[1]-1]) <= 1:
				possible_moves.append([position[0],position[1]-1])
		#Es posible un movimiento a derechas
		if position[1] >= 0 and position[1] < len(heigthmap[0])-1:
			#print("derecha")
			if abs(heigthmap[position[0]][position[1]] - heigthmap[position[0]][position[1]+1]) <= 1:
				possible_moves.append([position[0],position[1]+1])

		if destination != []:
			return sorted(possible_moves, key=lambda d: (d[0]-destination[0])**2+(d[1]-destination[1])**2)
		else:
			return possible_moves


	def getReachableZone(heigthmap, position,  banned_pos = [], heigth_level = 50):
		reachable_zone = [position]

		for node in reachable_zone:
			for move in canMove(heigthmap,node):
				if move not in reachable_zone and abs(heigthmap[move[0]][move[1]]-heigthmap[position[0]][position[1]]) < heigth_level and move not in banned_pos:
					reachable_zone.append(move)
		return reachable_zone


	def generateSphere(radius):
		#Pongo el centro de la esfera encima del punto de start_pos					#z,y,x
		sphere = []
		my_map = []
		for i in range((radius*2)-1):
			my_map.append([0] * ((radius*2)-1))

		for r in range(radius):
			my_map = []
			for i in range((radius*2)-1):
				my_map.append([0] * ((radius*2)-1))

			for i in range(0,r+1):
				my_map[radius+i-1][(radius-r-1)+i] = r #Fufa
				my_map[radius-i-1][(radius-r-1)+i] = r #Fufa
				my_map[radius+r-i-1][(radius-1)+i] = r #Fufa
				my_map[radius-r+i-1][(radius-1)+i] = r #Fufa

			sphere.append(my_map)

		return sphere

	def printStepsMap(steps_map, position = []):
		#time.sleep(0.5)
		for row in range(len(steps_map)):
			for col in range(len(steps_map[row])):
				if position != [] and row == position[0] and col == position[1]:
					rgbprint("X",end="",color=Color(0,255,255))
				else:
					element = steps_map[row][col]
					if element == 0:
						rgbprint("·",end="",color=Color(127,127,127))
					else:
						color = element%255
						multiplicator = 255/max([color,255-color])
						rgbprint(element%10,end="",color=Color(int(color*multiplicator),int((255-color)*multiplicator),0))
			print()
		print()

	
	start_pos = [0,0]
	final_pos = [0,0]
	heigthmap = []
	row_num = 0

	
	banned_pos = []
	#Rellena el heigthmap
	for line in open("12e.txt").readlines():
		line = line.replace("\n","")
		row = []
		for char_pos in range(len(line)):
			if line[char_pos] == 'S':
				row.append(ord('a')-97)
				start_pos = [row_num, char_pos]
			elif line[char_pos] == 'E':
				row.append(ord('z')-97)
				final_pos = [row_num, char_pos]
			elif line[char_pos] == "X":
				row.append(-1)
				banned_pos.append([row_num, char_pos])
			else:
				row.append(ord(line[char_pos])-97)
		heigthmap.append(row)
		row_num += 1



	print("heigthmap size: {}x{}".format(len(heigthmap), len(heigthmap[0])))
	
	#printMap(heigthmap)

	#start_pos, final_pos = final_pos, start_pos

	print("start post: {}".format(start_pos))
	print("final post: {}".format(final_pos))
	
	reachable_zone = getReachableZone(heigthmap,start_pos,banned_pos)
	printMap(heigthmap, reachable_zone=reachable_zone, banned_pos=banned_pos)

	unreachable_points = (len(heigthmap)*len(heigthmap[0]))-len(reachable_zone)

	if final_pos not in reachable_zone:
		print("Final pos is unreachable from start pos")

	paths = []

	sphere_radius = 2
	sphere = generateSphere(sphere_radius)

	#Creo el mapa de pasos
	steps_map = []
	for row in heigthmap:
		steps_map.append([0]*len(row))
	steps_map[start_pos[0]][start_pos[1]] = 1

	#reachable_zone_by_heigth = getReachableZone(heigthmap, start_pos, 2)

	position = [start_pos[0],start_pos[1]]

	printStepsMap(steps_map, [0,0])
	
	steps_made = [position]

	start_time = time.time()
	for step in steps_made:
		if steps_map[step[0]][step[1]] > 0:
			position = [step[0], step[1]]
			reachable_zone_by_heigth = getReachableZone(heigthmap, position, banned_pos, 2)
			for sphere_layer in range(len(sphere)):
				for sphere_row in range(len(sphere[sphere_layer])):
					for sphere_point in range(len(sphere[sphere_layer][sphere_row])):
						if sphere[sphere_layer][sphere_row][sphere_point] > 0:
							if [sphere_row-(sphere_radius-1)+position[0],sphere_point-(sphere_radius-1)+position[1]] in reachable_zone_by_heigth:
								new_distance = steps_map[position[0]][position[1]] + sphere[sphere_layer][sphere_row][sphere_point]
								if steps_map[sphere_row-(sphere_radius-1)+position[0]][sphere_point-(sphere_radius-1)+position[1]] == 0 or new_distance < steps_map[sphere_row-(sphere_radius-1)+position[0]][sphere_point-(sphere_radius-1)+position[1]]:
									steps_map[sphere_row-(sphere_radius-1)+position[0]][sphere_point-(sphere_radius-1)+position[1]] = new_distance
									steps_made.append([sphere_row-(sphere_radius-1)+position[0],sphere_point-(sphere_radius-1)+position[1]])
									if len(steps_made)%20 == 0:
										printStepsMap(steps_map, position)
									else:
										print("{:.2f}% {}steps_made {}seconds".format((100*len(steps_made))/((len(steps_map)*len(steps_map[0]))-unreachable_points),len(steps_made),int(time.time()-start_time)))

	print()
	printStepsMap(steps_map)

	lower_points = []
	for point in reachable_zone:
		if heigthmap[point[0]][point[1]] == 0:
			lower_points.append(point)

	sorted(lower_points, key=lambda l: steps_map[l[0]][l[1]])
	
	heigther_points = []
	for point in reachable_zone:
		if heigthmap[point[0]][point[1]] == 25:
			heigther_points.append(point)

	sorted(heigther_points, key=lambda l: steps_map[l[0]][l[1]])

	if len(lower_points) > 0:
		print("distance to near lowest point: {}".format(steps_map[lower_points[0][0]][lower_points[0][1]]))
	if len(heigther_points) > 0:
		print("distance to near heigthest point: {}".format(steps_map[heigther_points[0][0]][heigther_points[0][1]]))

	x = input("Input coords of final point. Input Q to exit: ")
	while x != "Q":
		if "," in x:
			final_pos = [int(x.replace("[", "").replace("]", "").split(",")[0]),int(x.replace("[", "").replace("]", "").split(",")[1])]
		if final_pos[0] >= 0 and final_pos[0] < len(heigthmap) and final_pos[1] >= 0 and final_pos[1] < len(heigthmap[0]):
			if final_pos not in reachable_zone:
				print("Final pos is unreachable from start pos")

			else:
				path = [final_pos]
				for step in range(steps_map[final_pos[0]][final_pos[1]],0,-1):
					moves = canMove(heigthmap,path[-1])
					for move in moves:
						if steps_map[move[0]][move[1]] == step:
							path.append(move)
							break

				printMap(heigthmap, path, reachable_zone=reachable_zone, banned_pos=banned_pos)

				print("Path has {} steps".format(len(path)))
		else:
			print("Final pos is not in heigthmap")
			print("heigthmap size: {}x{}".format(len(heigthmap), len(heigthmap[0])))

		x = input("Input coords of final point. Input Q to exit: ")




ex12()


