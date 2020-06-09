class  _Employee:    
    # class variables
    domains = set()
    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    # @property
    # def domains(self):
    # #     #print(f'@property domains: type of domains: {type(self.domains)}')
    # #     print(f'@property domains: value of domains: {_Employee.domains}')
    #     return _Employee.domains

    # @domains.setter
    # def domains(self, domain):
    #     #print(f'@domains.setter: - type of domain: {type(self.domains)}')
    #     print(f'@domains.setter - domains property val: {_Employee.domains}')
    #     #self.domains.append(domain)
    #     #self.domains += domain
    #     #print(f'@domains.setter - domains property after append: {self.domains}')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        reducedDomain = self.extractDomain(new_email)
        myallowed_domain = self.allowed_domain(reducedDomain)
        if myallowed_domain == True:
            _Employee.domains.add(reducedDomain)
            # print(f'domains: {_Employee.domains}')
            self._email = new_email
        elif myallowed_domain == False:
            raise RuntimeError(f'Sorry {self.name}, * {reducedDomain} * is not on the allowed domains list.')
   

    def __init__(self, name, email):
        self.name = name
        self.email = email
        #self._email = self.email

        #print(self.extractDomain(self._email))

        #_Employee.domains.append(extractDomain(email))
        #domainname = self.extractDomain(email)
        #_Employee.domains.append(self.extractDomain(email))
        #print(f'domains class var before append: {_Employee.domains}')
        #_Employee.domains = self.extractDomain(email)
        #_Employee.domains += self.extractDomain(email)
        #print(f'domains class var after append: {_Employee.domains}'
        # print(f'Class __init__: - type of domains: {type(_Employee.domains)}')
        # print(f'Class __init__: - value of domains: {_Employee.domains}')


    def display(self):
        print(self.name, self.email)

    @staticmethod
    def extractDomain(empEmail):
        # splitdomain = empEmail.split("@")[1]
        # print(f'splitdomain = {splitdomain}')
        domainName = empEmail.split("@")[1]
        ### domain = new_email[new_email.index('@')+1 : ]
        print(f'domain: {domainName}')
        return domainName
        #return domainName[1]

    @staticmethod
    def allowed_domain(mydomain):
        if mydomain not in _Employee.allowed_domains:
            return False
        return True
        

    # Add a class variable named domains to the following Employee class. 
    # Make this class variable a set and it should store all domain names used by employees.       
      
e1 = _Employee('John','john@gmail.com')
e2 = _Employee('Jack','jack@yahoo.com')
e3 = _Employee('Jill','jill@outlook.com')
e4 = _Employee('Ted','ted@yahoo.com')
e5 = _Employee('Tim','tim@gmail.com')
e6 = _Employee('Mike','mike@yahoo.com')
#e7 = _Employee('Phil','phil@test.com')
e6.display()
print(f'Full content of domains class var: {_Employee.domains}')