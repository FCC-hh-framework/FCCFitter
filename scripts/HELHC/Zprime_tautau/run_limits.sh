#!/bin/bash
# configs are default _mt
#to run ./scripts/HELHC/Zprime_tautau/run_limits.sh helhc_v01
myversion=$1
sel=$2
for ene in 2 4 6 8 10 12 14;
do

    ./myFit.exe h config_HELHC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config
    ./myFit.exe w config_HELHC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config
    ./myFit.exe f config_HELHC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config
    ./myFit.exe d config_HELHC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config
    ./myFit.exe p config_HELHC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config
    ./myFit.exe l config_HELHC/Zprime_tautau/"$myversion"/Zprime_"$ene"TeV"$sel".config

done
