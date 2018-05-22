import pandas as pd 

location = r'./donor.tsv'
df = pd.read_csv(location, delimiter = '\t',encoding = 'utf-8')
df_dlbcl = df[(df.donor_diagnosis_icd10 == 'C83.3')]
df_dlbcl.to_csv('dlbcl.csv',encoding = 'utf-8',index = False)

loc = r'./dlbcl.csv'
new_df = pd.read_csv(loc, delimiter = ',', encoding = 'utf-8')
donor_ids = new_df['icgc_donor_id']
donor_ids.to_csv('donor_ids.csv', encoding = 'utf-8', index = False, header = 'icgc_donor_id')
#print(donor_ids)

loc1 = r'./mirna_seq.tsv'
mi_rna = pd.read_csv(loc1,delimiter= '\t', encoding = 'utf-8')
mi_rna.to_csv('mi_rna_csv.csv',encoding = 'utf-8',index = False)


mi_rna_csv = pd.read_csv(r'./mi_rna_csv.csv')
don_ids = pd.read_csv(r'./donor_ids.csv')
joined = pd.merge(mi_rna_csv,don_ids)
header = ['icgc_donor_id','mirna_id','normalized_read_count','raw_read_count']

joined.to_csv('mi_rna_dlbcl.csv',columns = header, encoding = 'utf-8',index = False)

#mi_rna_dlbcl = mi_rna_csv[(mi_rna_csv.icgc_donor_id == don_ids.icgc_donor_id)]
#mi_rna_dlbcl.to_csv('mi_rna_dlbcl.csv',encoding = 'utf-8',index = False)
#print(mi_rna_dlbcl)













 
    
    

    



















    

   

    
