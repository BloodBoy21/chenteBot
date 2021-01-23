import json, sqlite3, os
CWD = os.getcwd()
conexion = sqlite3.connect(fr'{CWD}\Data\dataLog.sqlite')
data = conexion.cursor()
command_key= []
dic = {}
json_file = r'%s\Data\%s'%(CWD,'data.json')

def add_data(user,date):
    data.execute("insert into data(user,date) values(?,?)", (user, date))
    conexion.commit()

def save_json(mode):
    global dic
    if mode == 0:
        try:
            with open(json_file)as data_file:
                dic = json.load(data_file)
            for n in dic.keys():
                command_key.append(n)
        except IOError as e:
            print(e)
    elif mode == 1:
        with open(json_file,'w') as f:
            json.dump(dic,f)


try:
    conexion.execute("create table data(id integer primary key autoincrement,user text,date text)")
    #conexion.execute("ALTER TABLE videos ADD COLUMN autor text")
except sqlite3.OperationalError:
    print("Database creada")