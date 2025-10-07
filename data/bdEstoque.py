import mysql.connector
from mysql.connector import Error

def get_conection():
      return mysql.connector.connect(
       host = 'localhost',
      user = 'root',
      passwd= '8433',
      database = 'estoque'
      )

con = get_conection()  
cursor = con.cursor()

query = "create table if not exists produtos(id int auto_increment primary key," \
" cod int not null, nome varchar(150) not null, qte int not null," \
" valorunidade float not null)"

cursor.execute(query)

def cadastrar_produto(codigo, nome, qte, valorUnitario):
   dados =(codigo, nome, qte, valorUnitario)
   try:
     con = get_conection()
     query = "INSERT INTO  produtos(cod , nome, qte, valorunidade) VALUES(%s, %s, %s, %s)"
     cursor = con.cursor()
     cursor.execute(query, dados)
     con.commit()
     print(cursor.rowcount, "Produto Cadastrado com sucesso!")
   except Error as e:
      print("Erro ao inserir dado: ", e)

   

def exibir_produtos():
   try: 
      con = get_conection()
      query = "SELECT * FROM produtos"
      cursor.execute(query)
      produtos = cursor.fetchall()
      for p in produtos:
         print("Produto: ", *p)
     
   except Error as e:
      print("Erro ao exibir dados: ", e)  
   if cursor: cursor.close()   
   if con: con.close()      


def atualizar_produto(id, cod, nome, qte, valorUnitario):
   dados = (cod, nome, qte, valorUnitario, id)
   try:
      con = get_conection()
      query ="UPDATE produtos Set cod = %s," \
            "nome = %s,qte = %s," \
            " valorunidade = %s WHERE id = %s"
      cursor = con.cursor()
      cursor.execute(query,dados)
      con.commit()
      print(f"Produto {dados} Atualizado com Sucesso!")
   except Error as e:
      print("Erro no comando Sql!", e)
   if cursor: cursor.close()   
   if con: con.close()     


def buscar_produto(nome):
   dados = [nome]
   try:
      con = get_conection()
      query = "SELECT * FROM produtos WHERE nome = %s"
      cursor = con.cursor()
      cursor.execute(query, dados)
      produto = cursor.fetchall()
      for p in produto:
         print(f"Produto : ",*p)
   except Error as e:
      print("Erro na busca sqlError!", e)
   if cursor: cursor.close()   
   if con: con.close()  

def deletar_produto(nome):
   dados = [nome]
   try:
      con = get_conection()
      query = "Delete from produtos WHERE nome = %s"
      cursor = con.cursor()
      cursor.execute(query,dados)
      con.commit()
      print(f"Produto {dados} Deletado Com Sucesso! ")
   except Error as e:
      print("Erro no comando Sql!", e)
   if cursor: cursor.close()   
   if con: con.close()  



exibir_produtos()


