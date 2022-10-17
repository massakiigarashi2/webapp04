import streamlit as st
import matplotlib.pyplot as plt

from io import BytesIO
import requests
import pandas as pd

r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRV5baBORyvGtdK6PClZKGT_ZnnYwTvnqx5EaSENnJDCHt7ScASx9Ztsc96cBW10v3ftgBQB25LfUc2/pub?gid=513803270&single=true&output=csv')
data = r.content
df = pd.read_csv(BytesIO(data), index_col=0)

#O método columns permite mudar os rótulos das colunas de um DataFrame.
#O DATA FRAME é um objeto de duas dimensões, no qual cada coluna pode possuir um tipo de dado primário diferente. São utilizados para armazenar bases de dados. Este é talvez o formato de dados mais importante das linguagens de programação Python e R. 
#No data.frame cada coluna representa uma variável e cada linha um dado em si. Essa é a estrutura ideal para quando você tem várias variáveis de classes diferentes em um banco de dados.

df.columns = ['email', 'qtd', 'oficina']

st.markdown("""
                # *Oficinas Mack Week 2022* :bar_chart:
            """)	
st.subheader("Fig. 1 - Aferição de Púbico")
SUB_TITULO = '<p style="font-family:tahoma; color:Blue; font-size: 28px;">Desenvolvido pelo prof. Massaki de O. Igarashi</p>'
st.markdown(SUB_TITULO, unsafe_allow_html=True)

#O ideal, ao realizar quantificação de dados, é inicializar as variáveis ou arranjos de dados com valores 0, isto garante que não dê erro na exibição
qtd01 = 0
qtd02 = 0
qtd03 = 0
qtd04 = 0
qtd05 = 0
qtd06 = 0
qtd07 = 0
qtd08 = 0
qtd09 = 0
qtd10 = 0
qtd11 = 0
qtd12 = 0
qtd13 = 0
qtd14 = 0
qtd15 = 0
qtd16 = 0
qtd17 = 0
qtd18 = 0
qtd19 = 0
qtd20 = 0
qtd21 = 0

#A seguir faremos uma bisca por termos específicos contidos nas colunas do dataframe especificado por df['NOME_DA_COLUNA']

oficina01 = df['oficina']=='Oficina 01: LAB5/4º andar (19/set/22 às 9h) - Bootcamp Webapp Python (Prof. Massaki)'
oficina02 = df['oficina']=='Oficina 02: AUDITÓRIO (19/set/22 às 10h30) - Reconhecimento facial (Profa Erika)'
oficina03 = df['oficina']=='Oficina 03: 107/1º andar (19/set/22 às 14h) - Metodologias de estudo (Profas Karina e Maurita)'
oficina04 = df['oficina']=='Oficina 04: 108/1º andar (19/set/22 às 14h) - Inteligências múltiplas (Prof. Geraldo)'
oficina05 = df['oficina']=='Oficina 05: 109/1º andar (19/set/22 às 14h) - Desenv// ideias inovadoras e circulares (Profa Sânia)'
oficina06 = df['oficina']=='Oficina 06: AUDITÓRIO (20/set/22 às 08h) - Arte e Direito (Profa. Francesca)'
oficina07 = df['oficina']=='Oficina 07: Lab ENG sub -2 (20/set/22 às 14h) - Fabricação Tecido Plástico (Profas. Marlucy e Larissa)'
oficina08 = df['oficina']=='Oficina 08: 107/1º andar (20/set/22 às 14h) - Mapa mental para Gestão de Projetos (Prof. Geraldo)'
oficina09 = df['oficina']=='Oficina 09: AUDITÓRIO (20/set/22 às 14h) - Juri Simulado (Profa. Erika)'
#oficina10 = df['oficina']=='Oficina 10: AUDITÓRIO (21/set/22 às 9h) - Inclusão na universidade (Profa. Gisele)'
#oficina11 = df['oficina']=='Oficina 11: AUDITÓRIO (21/set/22 às 10h30) - Ética na Inovação (Prof. Massaki e Rev. Jabis)'
#oficina12 = df['oficina']=='Oficina 12: Lab Elétrica /sub -2 (21/set/22 às 13h30) - Elétrica sem mistérios (Prof. Marcos)'
#oficina13 = df['oficina']=='Oficina 13: 107/1º andar (21/set/22 às 14h) - Empreendedorismo Corporativo em MEMES (Prof. Geraldo)'
oficina14 = df['oficina']=='Oficina 14: LAB5/4º andar (21/set/22 às 14h) - Bootcamp Webapp Python (Prof. Massaki)'
oficina15 = df['oficina']=='Oficina 15: AUDITÓRIO (22/set/22 às 9h) - Marketing pessoal e carreiras (Profas. Marineide e Mariana)'
#oficina16 = df['oficina']=='Oficina 16: Sala 215 (22/set/22 às 14h) - Bem vindo à Bloomberg (Prof. Matias)'
#oficina17 = df['oficina']==''
#oficina18 = df['oficina']=='Oficina 18: Lab concreto/sub -2 (22/set/22 às 14h) - Concreto para construção civil (Prof. Pablo)'
#oficina19 = df['oficina']=='Oficina 19: 107/1º andar (23/set/22 às 14h) - Empregabilidade e Carreiras (Profa. Mariana)'
#oficina20 = df['oficina']=='Oficina 20: Lab Ind. 4.0 (23/set/22 às 14h) - Ind. 4.0 (Prof. Marcos)'
#oficina21 = df['oficina']=='Oficina 21: AUDITÓRIO SEMINÁRIO (23/set/22 às 14h) - Liberdade de expressão (Prof. Leopoldo)'

#O passo a seguir garante a consulta e retorno dos dados no dataframe que armazenará a consulta
df01 = df[oficina01]
df02 = df[oficina02]
df03 = df[oficina03]
df04 = df[oficina04]
df05 = df[oficina05]
df06 = df[oficina06]
df07 = df[oficina07]
df08 = df[oficina08]
df09 = df[oficina09]
#df10 = df[oficina10]
#df11 = df[oficina11]
#df12 = df[oficina12]
#df13 = df[oficina13]
df14 = df[oficina14]
df15 = df[oficina15]
#df16 = df[oficina16]
#df17 = df[oficina17]
#df18 = df[oficina18]
#df19 = df[oficina19]
#df20 = df[oficina20]
#df21 = df[oficina21]

#Como tem dados repetidos, optaremos por pegar apenas os maiores valores fazendo uso da função max()
qtd01 = max(df01['qtd'])
qtd02 = max(df02['qtd'])
qtd03 = max(df03['qtd'])
qtd04 = max(df04['qtd'])
qtd05 = max(df05['qtd'])
qtd06 = max(df06['qtd'])
qtd07 = max(df07['qtd'])
qtd08 = max(df08['qtd'])
qtd09 = max(df09['qtd'])
#qtd10 = max(df10['qtd'])
#qtd11 = max(df11['qtd'])
#qtd12 = max(df12['qtd'])
#qtd13 = max(df13['qtd'])
qtd14 = max(df14['qtd'])
qtd15 = max(df15['qtd'])
#qtd16 = max(df16['qtd'])
#qtd17 = max(df17['qtd'])
#qtd18 = max(df18['qtd'])
#qtd19 = max(df19['qtd'])
#qtd20 = max(df20['qtd'])
#qtd21 = max(df21['qtd'])

#Usaremos a função print e a função str() para converter um número para string e poder, assim, juntar um texto desejado com o valor da variável
print("Oficina 01 = " + str(qtd01))
print("Oficina 02 = " + str(qtd02))
print("Oficina 03 = " + str(qtd03))
print("Oficina 04 = " + str(qtd04))
print("Oficina 05 = " + str(qtd05))
print("Oficina 06 = " + str(qtd06))
print("Oficina 07 = " + str(qtd07))
print("Oficina 08 = " + str(qtd08))
print("Oficina 09 = " + str(qtd09))
#print("Oficina 10 = " + str(qtd10))
#print("Oficina 11 = " + str(qtd11))
#print("Oficina 12 = " + str(qtd12))
#print("Oficina 13 = " + str(qtd13))
print("Oficina 14 = " + str(qtd14))
print("Oficina 15 = " + str(qtd15))
#print("Oficina 16 = " + str(qtd16))
#print("Oficina 17 = " + str(qtd17))
#print("Oficina 18 = " + str(qtd18))
#print("Oficina 19 = " + str(qtd19))
#print("Oficina 20 = " + str(qtd20))
#print("Oficina 21 = " + str(qtd21))

#Criaremos uma lista de valores e rótulos
# Uma Lista em Python nada mais é que uma coleção ordenada de valores separados por vírgula e dentro de colchetes [] 

EsperadoOficinas = [0, 70, 70, 40, 40, 40, 133, 24, 24, 24, 90, 90, 30, 30, 46, 132, 23, 0, 23, 40, 32, 336, 70]
Oficinas = ['0','Oficina01','Oficina02','Oficina03','Oficina04','Oficina05','Oficina06','Oficina07','Oficina08','Oficina09','Oficina10','Oficina11', 'Oficina12','Oficina13','Oficina14','Oficina15','Oficina16','Oficina17','Oficina18','Oficina19','Oficina20',  'Oficina21']


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
#labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
labels = ['Oficina01','Oficina02','Oficina03','Oficina04','Oficina05','Oficina06','Oficina07','Oficina08','Oficina09','Oficina10','Oficina11', 'Oficina12','Oficina13','Oficina14','Oficina15','Oficina16','Oficina17','Oficina18','Oficina19','Oficina20',  'Oficina21']

#sizes = [15, 30, 45, 10]
sizes = [qtd01, qtd02, qtd03, qtd04, qtd05, qtd06, qtd07, qtd08, qtd09, qtd10, qtd11, qtd12, qtd13, qtd14, qtd15, qtd16, qtd17, qtd18, qtd19, qtd20, qtd21]
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
