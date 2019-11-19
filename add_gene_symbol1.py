from urllib.request import urlopen
import json
import requests

# list of ensembl ids
genes=[]
for line in open('uniqueRPKM_606.tsv'):
	genes.append(line.split('\t')[0])
# skip header	
genes=genes[1:]

#iterate over 1k genes
n= int(len(genes)/1000) +1

for j in range(n):
	g=genes[1000*j:1000*(j+1)]
	
	headers={ "Content-Type" : "application/json", "Accept" : "application/json"}
	#data='{ "ids" : ["ENSG00000157764", "ENSG00000248378" ] }'
	data='{ "ids" : ' + json.dumps(g) +' }'
	ids = requests.post('https://rest.ensembl.org/lookup/id', headers=headers, data=data).json()
	
	for i in ids.keys():
		try:
			print(i, ids[i]['display_name'])
		except:
			pass
