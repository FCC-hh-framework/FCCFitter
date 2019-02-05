python python/significance_plot.py -f "Data/Zprime_tt_TC2_helhc_v01_tagger_TRFbtag.json" -n "TC2" -p tt_TC2_tagger_TRFbtag --helhc
python python/significance_plot.py -f "Data/Zprime_tt_SSM_helhc_v01_tagger_TRFbtag.json" -n "SSM" -p tt_SSM_tagger_TRFbtag --helhc
python python/significance_plot.py -f "Data/Zprime_tt_SSM_helhc_v01_tagger_TRFbtag.json Data/Zprime_tt_TC2_helhc_v01_tagger_TRFbtag.json" -n "SSM TC2" -p tt_SSM_TC2_tagger_TRFbtag --helhc
#
python python/significance_plot.py -f "Data/Zprime_tt_helhc_v01.json" -n "tt" -p tt --helhc
python python/significance_plot.py -f "Data/Zprime_bb_helhc_v01.json" -n "bb" -p bb --helhc
python python/significance_plot.py -f "Data/Zprime_qq_helhc_v01.json" -n "qq" -p qq --helhc

