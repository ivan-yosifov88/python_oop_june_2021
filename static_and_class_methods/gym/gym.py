class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def is_object_in_list_of_objects(obj, list_of_obj):
        return obj in list_of_obj

    @staticmethod
    def get_obj(obj_id, list_of_obj):
        return [obj for obj in list_of_obj if obj.id == obj_id][0]

    def add_customer(self, customer):
        if not self.is_object_in_list_of_objects(customer, self.customers):
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if not self.is_object_in_list_of_objects(trainer, self.trainers):
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if not self.is_object_in_list_of_objects(equipment, self.equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not self.is_object_in_list_of_objects(plan, self.plans):
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not self.is_object_in_list_of_objects(subscription, self.subscriptions):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        current_subscription = self.get_obj(subscription_id, self.subscriptions)
        current_customer = self.get_obj(current_subscription.id, self.customers)
        current_trainer = self.get_obj(current_subscription.id, self.trainers)
        current_plan = self.get_obj(current_subscription.id, self.plans)
        current_equipment = self.get_obj(current_plan.id, self.equipment)

        return f"{current_subscription}\n{current_customer}\n{current_trainer}\n{current_equipment}\n{current_plan}"
