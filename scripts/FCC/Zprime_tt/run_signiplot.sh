python python/significance_plot.py -f "Data/Zprime_tt_fcc_v02_cut.json" -n "tt" -p tt_cut
python python/significance_plot.py -f "Data/Zprime_tt_fcc_v02_cut_TRFbtag.json" -n "tt" -p tt_cut_TRFbtag
python python/significance_plot.py -f "Data/Zprime_tt_fcc_v02_cut_TRFbtag.json" -n "TC2" -p tt_cut_TRFbtag
python python/significance_plot.py -f "Data/Zprime_tt_TC2_fcc_v02_tagger.json" -n "TC2" -p tt_TC2_tagger
python python/significance_plot.py -f "Data/Zprime_tt_TC2_fcc_v02_tagger_TRFbtag.json" -n "TC2" -p tt_TC2_tagger_TRFbtag
python python/significance_plot.py -f "Data/Zprime_tt_SSM_fcc_v02_tagger_TRFbtag.json" -n "SSM" -p tt_SSM_tagger_TRFbtag
python python/significance_plot.py -f "Data/Zprime_tt_SSM_fcc_v02_tagger_TRFbtag.json Data/Zprime_tt_TC2_fcc_v02_tagger_TRFbtag.json" -n "SSM TC2" -p tt_SSM_TC2_tagger_TRFbtag
python python/significance_plot.py -f "Data/Zprime_tt_TC2_helhc_v01_tagger_TRFbtag.json" -n "TC2" -p tt_TC2_tagger_TRFbtag --helhc
python python/significance_plot.py -f "Data/Zprime_tt_SSM_helhc_v01_tagger_TRFbtag.json" -n "SSM" -p tt_SSM_tagger_TRFbtag --helhc
python python/significance_plot.py -f "Data/Zprime_tt_SSM_helhc_v01_tagger_TRFbtag.json Data/Zprime_tt_TC2_helhc_v01_tagger_TRFbtag.json" -n "SSM TC2" -p tt_SSM_TC2_tagger_TRFbtag --helhc

python python/significance_plot.py -f "Data/Zprime_tt_TC2_fcc_v02_tagger_TRFbtag.json Data/Zprime_tt_TC2_fcc_v02_tagger_TRFbtag_degrade1.json Data/Zprime_tt_TC2_fcc_v02_tagger_TRFbtag_degrade2.json Data/Zprime_tt_TC2_fcc_v02_tagger_TRFbtag_degrade3.json" -n "nominal scenario1 scenario2 scenario3" -p tt_TC2_tagger_TRFbtag_degrade
