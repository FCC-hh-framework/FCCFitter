#!/bin/bash
#to run ./scripts/HELHC/Zprime_tt/run_limits.sh helhc_v01/tagger_TC2_TRFbtag sel0
myversion=$1
sel=$2
for ene in 2 4 6 8 10 12 14;
do

    ./myFit.exe h config_HELHC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config
    ./myFit.exe w config_HELHC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config
    ./myFit.exe f config_HELHC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config
    ./myFit.exe d config_HELHC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config
    ./myFit.exe p config_HELHC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config
    ./myFit.exe l config_HELHC/Zprime_tt/"$myversion"/Zprime_"$sel"_"$ene"TeV.config

done

