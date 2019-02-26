#!/bin/bash
#to run ./scripts/FCC/LQ_mumu/run_limits.sh fcc_v02
myversion=$1

for ene in 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40;
do
        ./myFit.exe h config_FCC/LQ_mumu/"$myversion"/LQ_mumu_"$ene"TeV.config
        ./myFit.exe w config_FCC/LQ_mumu/"$myversion"/LQ_mumu_"$ene"TeV.config
        ./myFit.exe f config_FCC/LQ_mumu/"$myversion"/LQ_mumu_"$ene"TeV.config
        ./myFit.exe d config_FCC/LQ_mumu/"$myversion"/LQ_mumu_"$ene"TeV.config
        ./myFit.exe p config_FCC/LQ_mumu/"$myversion"/LQ_mumu_"$ene"TeV.config
        ./myFit.exe l config_FCC/LQ_mumu/"$myversion"/LQ_mumu_"$ene"TeV.config
done

