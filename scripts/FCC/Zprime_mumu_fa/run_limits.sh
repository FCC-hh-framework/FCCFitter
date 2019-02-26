#!/bin/bash
#to run ./scripts/FCC/Zprime_mumu_fa/run_limits.sh fcc_v02
myversion=$1

for ene in 4 6 8 10 12 14 15 16 18 20 25 30 35 40 45;
do
        ./myFit.exe h config_FCC/Zprime_mumu_ano/"$myversion"/Zprime_mumu_"$ene"TeV.config
        ./myFit.exe w config_FCC/Zprime_mumu_ano/"$myversion"/Zprime_mumu_"$ene"TeV.config
        ./myFit.exe f config_FCC/Zprime_mumu_ano/"$myversion"/Zprime_mumu_"$ene"TeV.config
        ./myFit.exe d config_FCC/Zprime_mumu_ano/"$myversion"/Zprime_mumu_"$ene"TeV.config
        ./myFit.exe p config_FCC/Zprime_mumu_ano/"$myversion"/Zprime_mumu_"$ene"TeV.config
        ./myFit.exe l config_FCC/Zprime_mumu_ano/"$myversion"/Zprime_mumu_"$ene"TeV.config
done

