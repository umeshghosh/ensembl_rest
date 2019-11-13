from urllib.request import urlopen
import json

# read gene list
genes = open('ids.txt').read().split('\n')

# specify species: mouse or rat
species='mouse'

# output file
out = open(species+'_pct.txt','w')

# failed ids
fail=open(species+'_fail.txt','w')

# human to mouse
for gene in genes:
	try:
		# download data
		url='https://rest.ensembl.org/homology/id/'+gene+'?content-type=application/json;target_species='+species 
		d=urlopen(url).read()
		
		# read json
		d=json.loads(d)
	
		# extract pct_id
		target= d['data'][0]['homologies'][0]['target']
		target_id=target['id']
		pct=target['perc_id']
		
		print(gene, target_id, pct)
		#out.write(gene+','+target_id+','+pct+'\n')
	except:
		fail.write(gene+'\n')
