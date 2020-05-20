#!/bin/bash


# ===========================================================================
#
# This code is for example purposes only.
#
# Please do not submit or retrieve more than one request every 30 seconds.
# A limit is set at 200 jobs per 24 hours
#and queries launched on the web interface have priority.



# ===========================================================================
######## request 1 ############ submit request
# ===========================================================================

#choose a name for the query
requestName="APItest"

#two options are possible: HMM_id and seq

#### with option : HMM_id 

#enter your Pfam_id
#Pfam_id="PF01228"

# build the request
#response1=`curl -s -X POST http://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas_dev/api/submit \
#-H "Accept: application/json"  \
#-H "Content-Type: application/json"  \
#-d "{\"job_title\":\"$requestName\",\"option\":\"HMM_id\",\"Pfam_id\": \"$Pfam_id\", \"threshold\" : \"1e-10\",\"db\":\"OM-RGC_v1\",\"normalize\":\"pertotal\"}"`


#### with option : seq

seq=">EAQ46983.1 Metallo-phosphoesterase [Roseobacter sp. MED193]\n\
MKYRTIFLSDIHLGTPGCQADLLLGFLNSHEADTYYLVGDIVDAWRIRRKGFLWPQAHNDVVQTLLAKAH\n\
DGARIFLIPGNHDEFLRSYYGTHFGGIEVVATADFVASDGKRYLVTHGDQFDAVVTNAKWLAHLGDQAYE\n\
FMLWLNTRINRLRHLWGGQYWSLSKWAKHQVKQAVNFISEYENVLTAEARRGGYDGVICGHIHSAAIRDL\n\
EGMTYVNTGDWVESCTAIVERDNGSLALIDWERSARRSRHRARRARQKDKVLENV"

# build the request
response1=`curl -s -X POST http://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas_dev/api/submit \
-H "Accept: application/json"  \
-H "Content-Type: application/json"  \
-d "{\"job_title\":\"$requestName\",\"option\":\"seq\",\"seq\": \"$seq\",\"tool\":\"blastp\",\"threshold\" : \"1e-80\",\"db\":\"OM-RGC_v1\",\"normalize\":\"pertotal\"}"`



#response1
#{"status":"200","titre":"test1","eta":461,"uniqid":"5c5816c267cee"}

echo $response1

status=`echo $response1 | sed -n 's/.*status\":\"\([0-9]*\)\",.*/\1/p'`

#if error, end of execution
if [ $status != "200" ]
then
    echo "error in response 1"
    exit 
fi

# parse out the estimated time to completion and the request id
eta=`echo $response1 | sed -n 's/.*eta\":\([0-9]*\),.*/\1/p'`
uniqid=`echo $response1 | sed -n 's/.*uniqid\":\"\([0-9a-zA-Z]*\)\".*/\1/p'`


# wait for search to complete
sleep $eta



# ===========================================================================
######## request 2 ########### check results
# ===========================================================================

response2=`curl -s -X POST http://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas_dev/api/checkResults \
-H "Accept: application/json"  \
-H "Content-Type: application/json"  \
-d "{\"uniqid\":\"$uniqid\"}"`

#response 2
#{"status":"200","url":"http:\/\/tara-oceans.mio.osupytheas.fr\/ocean-gene-atlas_devs\/\/results?id=5c543e0c9ccb5","resultfiles":["alignment result","homolog sequences","abundances & environmental data"]}

echo $response2

# parse out the URL of the result page
url=`echo $response2|sed -n 's/.*url\":\"\([-a-z:\\\/\.\_\?\=0-9]*\).*/\1/p'`
url2=`echo $url|tr -d '\\'`

echo "The answer page is accessible to : $url2"

status=`echo $response2 | sed -n 's/.*status\":\"\([0-9]*\)\",.*/\1/p'`

#if error, end of execution
if [ $status != "200" ]
then
    echo "error in response 2"
    exit 
fi


#create a directory ${requestName}"_"${uniqid}
dir=${requestName}"_"${uniqid}
mkdir $dir




# ===========================================================================
####### request 3 ######### download result file
# ===========================================================================


#alignment result
curl -s -X POST http://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas_dev/api/fetchResults \
-H "Accept: application/json"  \
-H "Content-Type: application/json"  \
-d "{\"uniqid\":\"$uniqid\",\"file\":\"alignment result\"}" > $dir/fileresult


#homolog sequences
curl -s -X POST http://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas_dev/api/fetchResults \
-H "Accept: application/json"  \
-H "Content-Type: application/json"  \
-d "{\"uniqid\":\"$uniqid\",\"file\":\"homolog sequences\"}" > $dir/homologSeq.zip


#abundances & environmental data
curl -s -X POST http://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas_dev/api/fetchResults \
-H "Accept: application/json"  \
-H "Content-Type: application/json"  \
-d "{\"uniqid\":\"$uniqid\",\"file\":\"abundances & environmental data\"}" > $dir/abun_enviro_data.zip

exit

