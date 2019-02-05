#!/bin/bash
# to run ./scripts/HELHC/Dijet/run_limits.sh helhc_v01 _sel1

myversion=$1
sel=$2

for ene in 2 4 6 8 10 12 14 16;
do
    ./myFit.exe h config_HELHC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe w config_HELHC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe f config_HELHC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe d config_HELHC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe p config_HELHC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config
    ./myFit.exe l config_HELHC/Dijet_Res/"$myversion"/dijet"$sel"_"$ene"TeV.config

done

