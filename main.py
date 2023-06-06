from flask import Flask,render_template,request
from neo4j import GraphDatabase
import numpy as np
import pandas as pd
from py2neo import Node,Relationship,Graph,Path,Subgraph,NodeMatcher
from py2neo.matching import *
from pygments.lexers import templates

app= Flask(__name__,template_folder='template')

@app.route("/")
def Yönetici():
    return render_template('Login.html')

@app.route("/Yonetici",methods=["POST","GET"])
def giris():
    if request.method == "POST":
        email= request.form.get("Email")
        sifre= request.form.get("Sifre")
    if(email=="umut@gmail.com" and sifre=="1234"):

          return render_template("Yönetici.html")
    else:
          return render_template("Login.html")

@app.route("/",methods=["POST","GET"])
def ara():
    if request.method == "POST":
        arastirmaciAdi= request.form.get("arastırmacıAdı")
        yayinAdi= request.form.get("yayınAdı")
        graph = Graph("neo4j://localhost:7687", auth=("neo4j", "umut"))
        matcher = NodeMatcher(graph)
        query="MATCH (Arastırmacı {İsim:'Ahmet'}) RETURN Arastırmacı.ID,Arastırmacı.İsim,Arastırmacı.Soyisim AS İsim"
        result=graph.query(query)
        print(result)

        return render_template("Login.html")
    else:
        return render_template("Kullanıcı.html")
@app.route("/Kullanıcı",methods=["POST","GET"])
def kaydet():
    if request.method =="POST":
        arastirmaciID = request.form.get("araştırmacıID")
        arastirmaciAdi = request.form.get("araştırmacıAdı")
        arastirmaciSoyadi = request.form.get("araştırmacıSoyadı")
        yayinAdi = request.form.get("yayınAdı")
        yayinYili = request.form.get("yayınYılı")
        yayinTuru = request.form.get("yayınTuru")
        yayinYeri = request.form.get("yayınYeri")
        graph = Graph("neo4j://localhost:7687", auth=("neo4j", "umut"))
        node1=0
        node2=0
        node3=0
        node4=0
        node5=0
        node6=0
        print(node1)
        node1 = graph.nodes.match("Arastırmacılar", name="Arastırmacılar").first()
        node4 = graph.nodes.match("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi).first()
        node5 = graph.nodes.match("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili).first()
        node6 = graph.nodes.match("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri).first()
        temp1=0
        temp2=0
        temp3=0
        temp4=0
        temp5 = "x"
        temp6=0
        if node1 is None:
            temp4=0
        if node1 is not None:
            temp4=1

        if (temp4==0):
            node1 = Node("Arastırmacılar", name="Arastırmacılar")
            node2 = Node("Yayınlar", name="Yayınlar")
            node3 = Node("Yayıntürü", name="Yayıntürü")
            relation1 = Relationship(node1, "yayınyazarı", node2)
            relation2 = Relationship(node2, "yayınlanır", node3)
            node_ls = [node1, node2, node3, ]
            relation_ls = [relation1, relation2, ]
            subgraph = Subgraph(node_ls, relation_ls)
            tx = graph.begin()
            tx.create(subgraph)
            graph.commit(tx)
        if (temp4==1):
           print(" ")
        if node4 is None:
            temp1=0
        if node4 is not None:
            temp1=1
        if node5 is None:
            temp2= 0
        if node5 is not None:
            temp2= 1
        if node6 is None:
                temp3 = 0
        if node6 is not None:
                temp3 = 1
        if (temp1 == 0 and temp2 == 0 and temp3 == 0):
            node4 = Node("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi, Soyisim=arastirmaciSoyadi)
            node5 = Node("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili)
            node6 = Node("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri)
            relation4 = Relationship(node4, "yayınyazarı", node5)
            relation5 = Relationship(node5, "yayınlanır", node6)
            node_ls = [node4, node5, node6,]
            relation_ls = [relation4, relation5]
            subgraph = Subgraph(node_ls, relation_ls)
            tx = graph.begin()
            tx.create(subgraph)
            graph.commit(tx)
            node1 = graph.nodes.match("Arastırmacılar", name="Arastırmacılar").first()
            node2 = graph.nodes.match("Yayınlar", name="Yayınlar").first()
            node3 = graph.nodes.match("Yayıntürü", name="Yayıntürü").first()
            node4 = graph.nodes.match("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi).first()
            node5 = graph.nodes.match("Yayın",PK=yayinAdi+""+yayinYili,YayınAdı=yayinAdi, YayınYılı=yayinYili).first()
            node6 = graph.nodes.match("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri).first()
            relation1 = Relationship(node1, "araştırmacıbilgileri", node4)
            relation2 = Relationship(node2, "yayınbilgileri", node5)
            relation3 = Relationship(node3, "yayıntürübilgileri", node6)
            node_ls = [node1, node2, node3, node4, node5, node6, ]
            relation_ls = [relation1, relation2, relation3, ]
            subgraph = Subgraph(node_ls, relation_ls)
            tx = graph.begin()
            tx.create(subgraph)
            graph.commit(tx)
        if (temp1 == 1 and temp2 == 1 and temp3 == 1):

            node1 = graph.nodes.match("Arastırmacılar", name="Arastırmacılar").first()
            node2 = graph.nodes.match("Yayınlar", name="Yayınlar").first()
            node3 = graph.nodes.match("Yayıntürü", name="Yayıntürü").first()
            node4 = graph.nodes.match("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi).first()
            node5 = graph.nodes.match("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili).first()
            node6 = graph.nodes.match("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri).first()
            relation1 = Relationship(node1, "araştırmacıbilgileri", node4)
            relation2 = Relationship(node2, "yayınbilgileri", node5)
            relation3 = Relationship(node4, "yayınyazarı", node5)
            node_ls = [node1, node2, node3, node4, node5, node6, ]
            relation_ls = [relation1, relation2, relation3, ]
            subgraph = Subgraph(node_ls, relation_ls)
            tx = graph.begin()
            tx.create(subgraph)
            graph.commit(tx)
        if (temp1 == 0 and temp2 == 1 and temp3 == 1):

            node4 = Node("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi)
            graph.create(node4)
            node1 = graph.nodes.match("Arastırmacılar", name="Arastırmacılar").first()
            node2 = graph.nodes.match("Yayınlar", name="Yayınlar").first()
            node3 = graph.nodes.match("Yayıntürü", name="Yayıntürü").first()
            node4 = graph.nodes.match("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi).first()
            node5 = graph.nodes.match("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili).first()
            node6 = graph.nodes.match("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri).first()
            relation1 = Relationship(node1, "araştırmacıbilgileri", node4)
            relation2 = Relationship(node4,  "yayınyazarı", node5)
            node_ls = [node1,node2,node3, node4, node5, node6,]
            relation_ls = [relation1,relation2,]
            subgraph = Subgraph(node_ls, relation_ls)
            tx = graph.begin()
            tx.create(subgraph)
            graph.commit(tx)
        if (temp1 == 1 and temp2 == 1 and temp3 == 0):
            node6 = Node("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri)
            graph.create(node6)
            node1 = graph.nodes.match("Arastırmacılar", name="Arastırmacılar").first()
            node2 = graph.nodes.match("Yayınlar", name="Yayınlar").first()
            node3 = graph.nodes.match("Yayıntürü", name="Yayıntürü").first()
            node4 = graph.nodes.match("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi).first()
            node5 = graph.nodes.match("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili).first()
            node6 = graph.nodes.match("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri).first()
            relation1 = Relationship(node3, "araştırmacıbilgileri", node6)
            relation2 = Relationship(node5, "yayınlanır", node6)
            node_ls = [node1, node2, node3, node4, node5, node6, ]
            relation_ls = [relation1, relation2,]
            subgraph = Subgraph(node_ls, relation_ls)
            tx = graph.begin()
            tx.create(subgraph)
            graph.commit(tx)
        if (temp1 == 1 and temp2 == 0 and temp3 == 1):
            node5 = Node("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili)
            graph.create(node5)
            node1 = graph.nodes.match("Arastırmacılar", name="Arastırmacılar").first()
            node2 = graph.nodes.match("Yayınlar", name="Yayınlar").first()
            node3 = graph.nodes.match("Yayıntürü", name="Yayıntürü").first()
            node4 = graph.nodes.match("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi).first()
            node5 = graph.nodes.match("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili).first()
            node6 = graph.nodes.match("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri).first()
            relation1 = Relationship(node2, "yayınbilgileri", node5)
            relation2 = Relationship(node4, "yayınyazarı", node5)
            relation3 = Relationship(node5, "yayınlanır", node6)
            node_ls = [node1, node2, node3, node4, node5, node6, ]
            relation_ls = [relation1, relation2,relation3,]
            subgraph = Subgraph(node_ls, relation_ls)
            tx = graph.begin()
            tx.create(subgraph)
            graph.commit(tx)
        if (temp1 == 1 and temp2 == 0 and temp3 == 0):
            node5 = Node("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili)
            graph.create(node5)
            node6 = Node("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri)
            graph.create(node6)
            node1 = graph.nodes.match("Arastırmacılar", name="Arastırmacılar").first()
            node2 = graph.nodes.match("Yayınlar", name="Yayınlar").first()
            node3 = graph.nodes.match("Yayıntürü", name="Yayıntürü").first()
            node4 = graph.nodes.match("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi).first()
            node5 = graph.nodes.match("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili).first()
            node6 = graph.nodes.match("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri).first()
            relation1 = Relationship(node2, "yayınbilgileri", node5)
            relation2 = Relationship(node3, "yayıntürübilgileri", node6)
            relation3 = Relationship(node4, "yayınyazarı", node5)
            relation4 = Relationship(node5, "yayınlanır", node6)
            node_ls = [node1, node2, node3, node4, node5, node6, ]
            relation_ls = [relation1, relation2,relation3,relation4]
            subgraph = Subgraph(node_ls, relation_ls)
            tx = graph.begin()
            tx.create(subgraph)
            graph.commit(tx)
        if (temp1 == 0 and temp2 == 1 and temp3 == 0):
            node4 = Node("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi)
            graph.create(node4)
            node6 = Node("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri)
            graph.create(node6)
            node1 = graph.nodes.match("Arastırmacılar", name="Arastırmacılar").first()
            node2 = graph.nodes.match("Yayınlar", name="Yayınlar").first()
            node3 = graph.nodes.match("Yayıntürü", name="Yayıntürü").first()
            node4 = graph.nodes.match("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi).first()
            node5 = graph.nodes.match("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili).first()
            node6 = graph.nodes.match("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri).first()
            relation1 = Relationship(node1, "araştırmacıbilgileri", node4)
            relation2 = Relationship(node3, "yayıntürübilgileri", node6)
            relation3 = Relationship(node4, "yayınyazarı", node5)
            relation4 = Relationship(node5, "yayınlanır", node6)
            node_ls = [node1, node2, node3, node4, node5, node6, ]
            relation_ls = [relation1, relation2, relation3, relation4]
            subgraph = Subgraph(node_ls, relation_ls)
            tx = graph.begin()
            tx.create(subgraph)
            graph.commit(tx)
        if (temp1 == 0 and temp2 == 0 and temp3 == 1):
            node4 = Node("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi)
            graph.create(node4)
            node5 = Node("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili)
            graph.create(node5)
            node1 = graph.nodes.match("Arastırmacılar", name="Arastırmacılar").first()
            node2 = graph.nodes.match("Yayınlar", name="Yayınlar").first()
            node3 = graph.nodes.match("Yayıntürü", name="Yayıntürü").first()
            node4 = graph.nodes.match("Arastırmacı", ID=arastirmaciID, İsim=arastirmaciAdi,Soyisim=arastirmaciSoyadi).first()
            node5 = graph.nodes.match("Yayın",PK=yayinAdi+""+yayinYili, YayınAdı=yayinAdi, YayınYılı=yayinYili).first()
            node6 = graph.nodes.match("Tür",PK=yayinTuru+""+yayinYeri, YayınTürü=yayinTuru, YayınYeri=yayinYeri).first()
            relation1 = Relationship(node1, "araştırmacıbilgileri", node4)
            relation2 = Relationship(node2, "yayınbilgileri", node5)
            relation3 = Relationship(node4, "yayınsahibi", node5)
            relation4 = Relationship(node5, "yayınsahibi", node6)
            node_ls = [node1, node2, node3, node4, node5, node6, ]
            relation_ls = [relation1, relation2, relation3, relation4]
            subgraph = Subgraph(node_ls, relation_ls)
            tx = graph.begin()
            tx.create(subgraph)
            graph.commit(tx)
        return render_template('Kullanıcı.html')
    else:
         return render_template('Yönetici.html')

if __name__=='__main__':
  app.run(debug=True)


""""
        node1 = Node("Arastırmacılar", name="Arastırmacılar")
        node2 = Node("Yayınlar", name="Yayınlar")
        node3 = Node("Yayıntürü", name="Yayıntürü")
        relation1 = Relationship(node1, "yayınlar", node2)
        relation2 = Relationship(node1, "yayınlar", node3)
        node_ls = [node1, node2, node3,]
        relation_ls = [relation1, relation2,]
        subgraph = Subgraph(node_ls, relation_ls)
        tx = graph.begin()
        tx.create(subgraph)
        graph.commit(tx)
"""

