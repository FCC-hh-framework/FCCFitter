#!/bin/bash
#to run ./scripts/FCC/Dijet/run_limits.sh fcc_v02 _sel1/_sel1_5p/_sel1_10p/_sel1_15p/_sel1_20p

myversion=$1
sel=$2

for ene in 15 20 25 30 35 40 45 50;
do
    ./myFit.exe h config_FCC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe w config_FCC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe f config_FCC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe d config_FCC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe p config_FCC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe l config_FCC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config

done

