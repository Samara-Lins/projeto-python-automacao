#!/usr/bin/env python
# coding: utf-8

# In[56]:


#Passo 1:
# Pegar a cotação do dólar
# Pegar a cotação do euro
# Pegar a cotação do ouro
# Passo 2:
# Importar a base de dados e atualizá-la
# Passo 3:
# Recalcular os preços
# Passo 4:
# Exportar a base atualizada


# In[57]:


#Passo 1

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

navegador = wd.Firefox()
navegador.get('https://www.melhorcambio.com/dolar-hoje')
cotacao_dolar = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value').replace(',','.')
navegador.find_element('xpath','/html/body/form/div/section/div/div/div[10]/div/div/img').click()
cotacao_euro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value').replace(',','.')
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value').replace(',','.')







# In[58]:


#Passo 2

import pandas as pd

tabela = pd.read_excel('Produtos.xlsx')

# atualizar as cotações

e_dolar = tabela['Moeda'] == 'Dólar'
tabela.loc[e_dolar,'Cotação'] = float(cotacao_dolar)
e_euro = tabela['Moeda'] == 'Euro'
tabela.loc[e_euro,'Cotação'] = float(cotacao_euro)
e_ouro = tabela['Moeda'] == 'Ouro'
tabela.loc[e_ouro,'Cotação'] = float(cotacao_ouro)

# preço de compra = cotação x preço original

tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

# preço de venda = preço de compra x margem

tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

display(tabela)

tabela.to_excel("Produtos-Atualizado.xlsx")



# In[ ]:




