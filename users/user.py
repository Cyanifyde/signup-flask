
class user():
    def __init__(self, id, email, name, password):
        self.id = id
        self.email = email
        self.name = name
        self.password = password
        g.append([self,id])
        
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(id):
        for x in g:
            try:
                if id==x[1]:
                    return x[0]
            except:pass


g=[]     
def get_id(id):
    for x in g:
        if id==x[1]:
            return x[0]

