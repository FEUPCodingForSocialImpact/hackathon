# Hackathon Cidade + Inteligente  

### iPantry

Quantas vezes se perguntou o que tem na sua despensa? O objetivo deste software é resolver essa questão! Através da interface incluída,
você poderá adicionar e eliminar produtos da base de dados, controlar a sua quantidade e atribuir-lhes uma categoria. Através de apenas um
comando, você poderá ver todos os seus produtos, ver os que não tem e até vê-los por categorias. A cada produto pode ser atríbuido ainda o
estatuto de "produto prioritário" e ver apenas os produtos com este estatuto.
A partir de agora, terá a sua despensa na ponta dos dedos!

##### [Vídeo aqui](Demo/ipantry.mov?raw=true)  

#### Autores  

|Nome  |E-mail  |  
|---|---|    
|Eduardo Teixeira  |[Email](mailto:eduardo.r.teixeira@gmail.com)  |  
|João Lucas  |[Email](mailto:joaolucassilvamartins@gmail.com)  |  
|Rui Pinto  |[Email](mailto:ruipinto02@hotmail.com)  |  
|Tiago Silva  |[Email](mailto:tiagodusilva@gmail.com)  |  

#### Instruções

1. Caso o mySQL ainda não esteja instalado, siga as indicações no seguinte site (http://raspberrywebserver.com/sql-databases/using-mysql-on-a-raspberry-pi.html)
	NOTA: altere "temp" por "iPantry", "monitor" por "utilizador1", "password" por "1234";
	      substitua o comado "CREATE TABLE tempdat (tdate DATE, ttime TIME, zone TEXT, temperature NUMERIC);" por
	      "CREATE TABLE despensa (id INT PRIMARY KEY AUTO_INCREMENT, nome TEXT, quantidade INT, categoria TEXT, prioridade INT NOT NULL)"
2. Abrir o ficheiro DEMO.py
3. Correr DEMO.py, para saber os comandos disponíveis escreva na consola "HELP"

#### Hardware  

|Nome  |Link  |  
|---|---|  
|Raspberry Pi 3  |[Ver aqui](http://www.raspberrypi.org)  |  

#### Software  

|Nome  |Link  |  
|---|---|    
|MySql  |[Ver aqui](https://www.mysql.com/)  |  
|Tkinter  |[Ver aqui](http://www.tutorialspoint.com/python/python_gui_programming.htm)  |  

***  
[![Raspberry Pi Logo](https://upload.wikimedia.org/wikipedia/en/thumb/c/cb/Raspberry_Pi_Logo.svg/50px-Raspberry_Pi_Logo.svg.png)](http://raspberrypi.org)   
[**Coding for Social Impact**](http://codingforsocialimpact.fe.up.pt)  
Para mais informações [contacte-nos](mailto:hello@codingforsocialimpact.org.com).  
[![Creative Commons Attribution-ShareAlike 4.0 International License](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)  
This work is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License**.  
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.  
