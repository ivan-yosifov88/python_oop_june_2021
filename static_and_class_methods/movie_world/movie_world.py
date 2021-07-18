class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        customers = '\n'.join(repr(customer) for customer in self.customers)
        dvds = '\n'.join(repr(dvd) for dvd in self.dvds)
        return customers + "\n" + dvds

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def filter_object(obj_id, list_of_obj):
        return [obj for obj in list_of_obj if obj.id == obj_id][0]

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)



    def rent_dvd(self, customer_id, dvd_id):
        # filtered_customers = [customer for customer in self.customers if customer.id == customer_id]
        # filtered_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id]
        current_customer = self.filter_object(customer_id, self.customers)
        current_dvd = self.filter_object(dvd_id, self.dvds)
        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd.is_rented:
            return "DVD is already rented"

        if not current_dvd.age_restriction <= current_customer.age:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = self.filter_object(customer_id, self.customers)
        current_dvd = self.filter_object(dvd_id, self.dvds)
        if current_dvd not in current_customer.rented_dvds:
            return f"{current_customer.name} does not have that DVD"

        current_customer.rented_dvds.remove(current_dvd)
        current_dvd.is_rented = False
        return f"{current_customer.name} has successfully returned {current_dvd.name}"

