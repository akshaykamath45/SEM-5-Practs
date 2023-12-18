import random

def generate_individual(length):
    """Generate a random binary string of a given length."""
    return ''.join(random.choice('01') for _ in range(length))

def fitness(individual):
    """Calculate the fitness of an individual (count of '1' in the binary string)."""
    return individual.count('1')

def crossover(parent1, parent2):
    """Perform crossover (single-point crossover in this case) between two parents."""
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual, mutation_rate):
    """Mutate an individual by flipping some bits based on the mutation rate."""
    mutated_individual = ''.join(
        bit if random.random() > mutation_rate else random.choice('01')
        for bit in individual
    )
    return mutated_individual

def genetic_algorithm(population_size, individual_length, generations, crossover_rate, mutation_rate):
    # Generate initial population
    population = [generate_individual(individual_length) for _ in range(population_size)]

    for generation in range(generations):
        # Evaluate fitness for each individual in the population
        fitness_scores = [fitness(individual) for individual in population]

        # Select parents based on fitness scores (roulette wheel selection)
        parents = random.choices(population, weights=fitness_scores, k=population_size)

        # Create next generation through crossover and mutation
        next_generation = []
        for i in range(0, population_size, 2):
            parent1, parent2 = parents[i], parents[i + 1]

            # Perform crossover
            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            # Perform mutation
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)

            next_generation.extend([child1, child2])

        # Replace the old population with the new generation
        population = next_generation

        # Print the best individual in the current generation
        best_individual = max(population, key=fitness)
        print(f"Generation {generation + 1}, Best Individual: {best_individual}, Fitness: {fitness(best_individual)}")

    # Return the best individual at the end of the evolution
    return max(population, key=fitness)

# Example usage
best_solution = genetic_algorithm(
    population_size=100,
    individual_length=20,
    generations=50,
    crossover_rate=0.8,
    mutation_rate=0.01
)

print("Best Solution:", best_solution)
print("Fitness:", fitness(best_solution))