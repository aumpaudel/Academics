class Animals():
    def type_(self, types):
        self.types = types 

class Pets(Animals):
    def name_(self, namee):
        self.namee = namee

class Dogs(Pets):
    def language_(self):
        self.language = "Bark"

d = Dogs() 
d.name_("Dog")
d.type_("Pet")
d.language_()
print(d.language, d.namee, d.types)