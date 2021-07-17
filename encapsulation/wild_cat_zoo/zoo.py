class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if not len(self.animals) < self.__animal_capacity:
            return "Not enough space for animal"

        needed_money = self.__budget - price
        if not 0 <= needed_money:
            return "Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not len(self.workers) < self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        filter_workers = [worker for worker in self.workers if worker.name == worker_name]
        if not filter_workers:
            return f"There is no {worker_name} in the zoo"
        worker_for_dismissal = filter_workers[0]
        self.workers.remove(worker_for_dismissal)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        needed_money_for_salaries = sum(worker.salary for worker in self.workers)
        if not needed_money_for_salaries <= self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_money_for_salaries
        left_budget = self.__budget
        return f"You payed your workers. They are happy. Budget left: {left_budget}"

    def tend_animals(self):
        needed_money_for_tending_animals = sum(animal.money_for_care for animal in self.animals)
        if not needed_money_for_tending_animals <= self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_money_for_tending_animals
        left_budget = self.__budget
        return f"You tended all the animals. They are happy. Budget left: {left_budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += '\n'.join(str(lion) for lion in lions) + '\n'

        result += f"----- {len(tigers)} Tigers:\n"
        result += '\n'.join(str(tiger) for tiger in tigers) + '\n'

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += '\n'.join(str(cheetah) for cheetah in cheetahs)

        return result

    def workers_status(self):
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += '\n'.join(str(keeper) for keeper in keepers) + '\n'

        result += f"----- {len(caretakers)} Caretakers:\n"
        result += '\n'.join(str(caretaker) for caretaker in caretakers) + '\n'

        result += f"----- {len(vets)} Vets:\n"
        result += '\n'.join(str(vet) for vet in vets)

        return result



