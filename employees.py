# 1. Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

# 2. Consider the concept of aggregation, and modify the Company class so that you assign employees to a company.

# 3. Create a company, and three employees, and then assign the employees to the company.

class Employee(object):
    """This represents an employee"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def __str__(self):
        return f"{self.employee_name}"


class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self._employees = list()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    @property
    def employees(self):
        """Lists all employees in the company
        Method arguments:
        n/a
        Builds dictionary with company (key) and list of employees (value)
        Example:
        {
            "Apple": ["Steve Jobs", "Other person", "Another person"]
        }
        """

        # create empty dictionary
        companies_and_emps = dict()
        # get name of company
        company = self.get_company_name()
        # loop over employees list
        for emp in self._employees:
            try:
                # add employee as value for company key
                companies_and_emps[company].append(emp.employee_name)
            except KeyError:
                # create new key value pair with company as key and an empty list as value
                companies_and_emps[company] = list()
                # add employee as value for company key
                companies_and_emps[company].append(emp.employee_name)

        # print(companies_and_emps)

        return companies_and_emps

    @employees.setter
    def employees(self, emp):
        """This method adds an employee to list of employees
        
        Arguments:
            emp {Employee} -- Employee obj
        """
        
        self._employees.append(emp)

    def __str__(self):
        return f"{self.company_name}"


class Industry(object):
    """This represents an industry"""

    def __init__(self, name):
        self.name = name
        self.companies = dict()
    
    def add_company_to_industry(self, company_obj):
        """Adds company object to industry
        
        Arguments:
            company_obj {Company} -- Represents a company and includes a list of its employees
        """

        # industry = self.name
        # comp = company_obj.company_name

        try:
            # try to add company (value) to industry (key)
            self.companies[company_obj.company_name].append(company_obj)
        except KeyError:
            # if key doesn't exist, create new key value pair
            self.companies[company_obj.company_name] = list()
            # add company (value) to industry (key)
            self.companies[company_obj.company_name].append(company_obj)
        
        # print(f'{comp} has been added to the {industry} industry.')

    def list_industries(self):
        """Method to list industries and related companies
        Method Arguments:
        n/a
        """

        # create empty dictionary
        ind = dict()
        # loop over companies in industry
        for c in self.companies:
            try:
                # add company to industry (key) 
                ind[self.name].append(c)
            except KeyError:
                # create new key value pair with industry as key and an empty list as value
                ind[self.name] = list()
                # add company to industry (key) 
                ind[self.name].append(c)
        print(ind)

    def __str__(self):
        return f'{self.name}'


# Create a company
NSS = Company('Nashville Software School', '2013')
Academy = Company('Academy Sports & Outdoors', '1986')

# create three employees
kimmy = Employee('Kimmy')
joe = Employee('Joe')
brenda = Employee('Brenda')

justin = Employee('Justin')
matt = Employee('Matt')
chris = Employee('Chris')

# assign the employees to the company
NSS.employees = kimmy
NSS.employees = joe
NSS.employees = brenda

Academy.employees = justin
Academy.employees = matt
Academy.employees = chris

# this was the problem area
# print("company: ", NSS.company_name, "employees: ", NSS.employees)

print(NSS.employees)
print(Academy.employees)

# create an industry instance
education = Industry('Education')
retail = Industry('Retail')
# add company to industry
education.add_company_to_industry(NSS)
retail.add_company_to_industry(Academy)

education.list_industries()
retail.list_industries()
