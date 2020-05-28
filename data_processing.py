cd ..
cd TARAOcean_output/Ecoli_narG_5ecdb1640b546
unzip abun_enviro_data.zip
unzip homologSeq.zip

import pandas as pd
import numpy as np

env_par = pd.read_csv('environmental_parameters.csv', sep = '\t')
gene_ab = pd.read_csv('abundance_matrix.csv', sep = '\t', skiprows = [1])

# env_par.head()   
# gene_ab.head()    # make sure dataframe looks okay

#list(env_par.columns)   # check which environmental parameters are available

# calculating N:P ratio and N* (maybe unnecessary depending on what you're looking for)
env_par['NtoPratio'] = env_par['NO3_NO2 (µmol/l)']/env_par['PO4 (µmol/l)']
env_par['N*'] = env_par['NO3 (µmol/l)'] - 16*env_par['PO4 (µmol/l)'] + 2.9 

gene_ab.insert(0, 'ID', range(1, gene_ab.shape[0]+1))       # assign ID to each row 

taxonomy = gene_ab['Unnamed: 1'].str.split('; ',expand=True)
#gene_ab = pd.concat([taxonomy, gene_ab], axis=1)
#gene_ab = gene_ab.dropna(axis=0, subset=[1])  
m = taxonomy[1] != 'Bacteria'
gene_ab_euk, gene_ab_prok = taxonomy[m], taxonomy[~m]       # needed to split data to prokaryotes and non-prokaryotes due to different taxonomic levels

gene_ab_prok = gene_ab_prok[gene_ab_prok.columns[0:8]]
gene_ab_prok.columns = ['Biota', 'Superkingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genera', 'Species']
gene_ab_euk = gene_ab_euk.dropna(axis=0, subset=[0])
gene_ab_euk.columns = ['Biota', 'Superkingdom', 'Kingdom', 'Superphylum', 'Phylum', 'Subphylum', 'Class', 'Subclass', 'Infraclass',
           'Cohort', 'Order', 'Suborder', 'Infraorder', 'Superfamily', 'Family', 'Subfamily', 'Tribe', 'Genus']

gene_ab = pd.concat([gene_ab, pd.concat([gene_ab_prok, gene_ab_euk])], axis=1)

# calculating sum of abundance for each taxonomic level
gene_ab_melt = gene_ab.melt(id_vars = ['ID', 'Biota', 'Superkingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genera', 'Species', 'Kingdom', 'Superphylum', 'Subphylum', 'Subclass', 'Infraclass', 'Cohort', 'Suborder', 'Infraorder', 'Superfamily', 'Subfamily', 'Tribe', 'Genus'])
dummy = pd.get_dummies(gene_ab_melt, columns = ['Biota', 'Superkingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genera', 'Species', 'Kingdom', 'Superphylum', 'Subphylum', 'Subclass', 'Infraclass', 'Cohort', 'Suborder', 'Infraorder', 'Superfamily', 'Subfamily', 'Tribe', 'Genus'], dtype = 'int')
for col in dummy.columns.to_list():
    if col != ['value'] and dummy[col].dtype == 'int':
        dummy[col] = np.where(dummy[col] == 1, dummy['value'], dummy[col])
gene_ab_final = dummy.groupby('variable').sum().reset_index().rename({'variable' : 'rownames'}, axis=1).drop('value', axis=1)

# merged environmental parameters and gene abundance into one file
alldata = pd.merge(left=env_par, right=gene_ab_final, how='left', left_on='OGA_ID.1', right_on='rownames')