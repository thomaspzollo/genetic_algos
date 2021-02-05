import matplotlib.pyplot as plt
import copy
import random

def populate():

	global population
	pop = []
	for i in range(0,10):

		pop.append([])
	
		for j in range(0,11):

			pop[i].append(random.randint(smallest,biggest+1))

	population = pop

def evolve():

	global env

	for i in range(generations):

		env = environmental_change()
		envs.append(env)

		selected = select(population)
		print(env)
		print(selected)
		averages.append(sum(selected) / len(selected))

		reproduction(selected)

def environmental_change():
	global env

	temp_env = env + random.randint(-1,1)
	return temp_env

def select(pop):

	balances = []
	for adult in pop:

		average = sum(adult) / len(adult)
		diff = abs(env - average)
		balances.append(diff)

	selected_pos = balances.index(min(balances))
	selected = copy.copy(pop[selected_pos])
	return selected

def reproduction(selected):

	for n in range(len(population)):
		population[n] = reproduce(selected)

def reproduce(adult):

	new_adult = []
	for n in range(len(adult)):

		new_adult.append(mutate(adult[n]))

	return new_adult

def mutate(trait):

	if (random.randint(0,10) > 2):
		mutation = random.randint(-1,1)
		if ((mutation == -1) and (trait == smallest)) or ((mutation == 1) and (trait == biggest)):
			return trait
		trait = trait + mutation
	return trait

def print_pop():
	print()
	print('pop')
	for j in population:
		print(j)
	print()

if __name__ == '__main__':

	global env, generations, envs, averages, biggest, smallest
	env = 20
	generations = 200
	envs = []
	averages = []
	biggest = 100
	smallest = 1

	populate()
	evolve()

	print_pop()

	plt.plot(averages)
	plt.plot(envs)
	plt.show()
	




