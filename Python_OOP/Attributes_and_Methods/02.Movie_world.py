import datetime
 
 
class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False
 
    def check_status(self):
        return self.is_rented
 
    def __repr__(self):
        if self.check_status():
            return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: not rented"
 
    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        (day, month_number, year) = date.split(".")
        datetime_object = datetime.datetime.strptime(month_number, "%m")
        full_month_name = datetime_object.strftime("%B")
        return cls(name, id, year, full_month_name, age_restriction)
 
 
class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []
 
    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join([x.name for x in self.rented_dvds])})"
 
 
 
class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []
 
    @staticmethod
    def dvd_capacity():
        return 15
 
    @staticmethod
    def customer_capacity():
        return 10
 
    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
 
    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
 
    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd_obj_list = [x for x in self.dvds if x.id == dvd_id]
        customer_obj_list = [x for x in self.customers if x.id == customer_id]
        if dvd_obj_list and customer_obj_list:
            dvd_obj = dvd_obj_list[0]
            customer_obj = customer_obj_list[0]
            if customer_obj.age < dvd_obj.age_restriction:
                return f"{customer_obj.name} should be at least {dvd_obj_list[0].age_restriction} to rent this movie"
            if dvd_obj in customer_obj.rented_dvds:
                return f"{customer_obj.name} has already rented {dvd_obj.name}"
            if dvd_obj.is_rented:
                return "DVD is already rented"
 
            customer_obj.rented_dvds.append(dvd_obj)
            dvd_obj.is_rented = True
            return f"{customer_obj.name} has successfully rented {dvd_obj.name}"
 
    def return_dvd(self, customer_id, dvd_id):
        dvd_obj_list = [x for x in self.dvds if x.id == int(dvd_id)]
        customer_obj_list = [x for x in self.customers if x.id == int(customer_id)]
        if dvd_obj_list and customer_obj_list:
            dvd_obj = dvd_obj_list[0]
            customer_obj = customer_obj_list[0]
            if dvd_obj and customer_obj:
                if dvd_obj not in customer_obj.rented_dvds:
                    return f"{customer_obj.name} does not have that DVD"
                dvd_obj.is_rented = False
                customer_obj.rented_dvds.remove(dvd_obj)
                return f"{customer_obj.name} has successfully returned {dvd_obj.name}"
 
    def __repr__(self):
        result = ""
        for x in range(len(self.customers)):
            result += f"{self.customers[x].__repr__()}" + "\n"
        for y in range(len(self.dvds)):
            result += f"{self.dvds[y].__repr__()}" + "\n"
        return result

