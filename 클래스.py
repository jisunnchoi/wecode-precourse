class Database:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.dict = {}
    def insert(self, field, value):
        #클래스의 데이터 사이즈보다 클 경우 더이상 저장 x 
        if len(self.dict) >= self.size:
            return
        else:
            self.dict[field] = value 
    def select(self, field):
        #딕셔너리의 key 는 고유하기 때문에 아래와 같이 작성해도 중복 걱정x
        if field not in self.dict.keys():
            return None
        else:
            return self.dict[field]
    def update(self, field, value):
        if field not in self.dict.keys():
            return 
        else:
            self.dict[field] = value

    def delete(self, field):
        if field not in self.dict.keys():
            return 
        else:
            del self.dict[field]
    def __str__(self):
        return f'{self.name},{self.size},{self.dict}'

db = Database('sql',1) 
db.insert('name','정우성')
db.insert('gender','남자')
db.insert('singer','아이유')
print(db.select('name'))
print(db.select('gender'))
print(db.select('singer'))
print(db)