import pandas as pd 

def find_tumor_icd():
    #filter donor data by tumor icd10. in new file will be only those patients who were diagnosed with dlbcl
    location = r'./donor.tsv'
    df = pd.read_csv(location, delimiter = '\t',encoding = 'utf-8')
    df_dlbcl = df[(df.donor_diagnosis_icd10 == 'C83.3')]
    df_dlbcl.to_csv('dlbcl.csv',encoding = 'utf-8',index = False)
def separate_dlbcl_ids():
    #separates patients with dlbcl into one column of ids to help filter further data
    loc = r'./dlbcl.csv'
    new_df = pd.read_csv(loc, delimiter = ',', encoding = 'utf-8')
    donor_ids = new_df['icgc_donor_id']
    donor_ids.to_csv('donor_ids.csv', encoding = 'utf-8', index = False, header = 'icgc_donor_id')

def retrieve_mi_rna():
    #retrieves mi_rna data into separate csv file which is ready to be filtered by patients ids and leave only dlbcl cases
    loc1 = r'./mirna_seq.tsv'
    mi_rna = pd.read_csv(loc1,delimiter= '\t', encoding = 'utf-8')
    mi_rna.to_csv('mi_rna_csv.csv',encoding = 'utf-8',index = False)

def mi_rna_dlbcl():
    #filter data by those patients diagnosed with dlbcl and merge mi_rna seq data with patients ids, stores this new merged data into new csv file ready to further work
    mi_rna_csv = pd.read_csv(r'./mi_rna_csv.csv')
    don_ids = pd.read_csv(r'./donor_ids.csv')
    joined = pd.merge(mi_rna_csv,don_ids)
    header = ['icgc_donor_id','mirna_id','normalized_read_count','raw_read_count']
    joined.to_csv('mi_rna_dlbcl.csv',columns = header, encoding = 'utf-8',index = False)
    
    
mi_rna_dlbcl = pd.read_csv(r'./mi_rna_dlbcl.csv')















 
    
    

    



















    

   

    
