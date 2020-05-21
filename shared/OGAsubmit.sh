#!/bin/bash
requestName=$1
seq=$2
curl -s -X POST http://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas_dev/api/submit \
-H "Accept: application/json"  \
-H "Content-Type: application/json"  \
-d "{\"job_title\":\"$requestName\",\"option\":\"seq\",\"seq\": \"$seq\",\"tool\":\"blastp\",\"threshold\" : \"1e-80\",\"db\":\"OM-RGC_v1\",\"normalize\":\"pertotal\"}"