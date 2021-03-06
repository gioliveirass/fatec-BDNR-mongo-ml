import connectBD as connectDB
from pprint import pprint

def findSort():
    mydb = connectDB.connect()
    mycol = mydb.usuario
    print("\n===========================")
    print("==== TODOS OS USUARIOS ====") 
    print("===========================\n")
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        pprint(x)

def insert(name, cpf):
    mydb = connectDB.connect()
    mycol = mydb.usuario
    print("\n=========================")
    print("=== USUARIO INSERIDO ===") 
    print("=========================\n")
    mydict = { "nome": name, "cpf": cpf }
    x = mycol.insert_one(mydict)
    pprint(x.inserted_id)
    print("Usuario cadastrado com sucesso.")

def findQuery(name):
    mydb = connectDB.connect()
    mycol = mydb.usuario
    print("\n=========================")
    print("==== USUARIO BUSCADO ====") 
    print("=========================\n")
    myquery = { "nome": name }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        pprint(x)

def update(name, newName):
    mydb = connectDB.connect()
    mycol = mydb.usuario
    print("\n============================")
    print("==== USUARIO ATUALIZADO ====") 
    print("============================\n")
    myquery = { "nome": name }
    newvalues = { "$set":   { "nome": newName } }
    mycol.update_one(myquery, newvalues)
    pprint("Usuario atualizado com sucesso.")

def delete(name):
    mydb = connectDB.connect()
    mycol = mydb.usuario
    print("\n==========================")
    print("==== USUARIO DELETADO ====") 
    print("==========================\n")
    myquery = { "nome": name }
    mycol.delete_one(myquery)
    pprint("Usuario deletado com sucesso.")