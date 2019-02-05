#!/bin/bash
#to run ./scripts/HELHC/RSG_ww/run_limits.sh helhc_v01/tagger sel0
myversion=$1
sel=$2
for ene in 2 4 6 8 10 12 14;
do
    ./myFit.exe h config_HELHC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config
    ./myFit.exe w config_HELHC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config
    ./myFit.exe f config_HELHC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config
    ./myFit.exe d config_HELHC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config
    ./myFit.exe p config_HELHC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config
    ./myFit.exe l config_HELHC/RSG_ww/"$myversion"/RSG_"$sel"_"$ene"TeV.config

done

