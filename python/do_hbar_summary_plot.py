import ROOT as r

#result="Disco"
result="Limit"

#mode="27"
#mode="100"
mode="27_100"

##############################################
rsgww_disco      = ["G_{RS} #rightarrow W^{+}W^{-}",
                    [5.,7.,8.],  #  27 TeV ->   1, 15, 100 ab-1
                    [15.,22.,26.]] # 100 TeV -> 2.5, 30, 100 ab-1
qstar_disco      = ["Q* #rightarrow jj",
                    [10.,12.,14.],
                    [36.,40.,43.]]
zpttTC2_disco    = ["Z\'_{TC2} #rightarrow t#bar{t}",
                    [6.,8.,10.],
                    [16.,23.,27.]]
zpttSSM_disco    = ["Z\'_{SSM} #rightarrow t#bar{t}",
                    [4.,6.,8.],
                    [10.,18.,22.]]
zpll_disco       = ["Z\'_{SSM} #rightarrow l^{+}l^{-}",
                    [10.,13.,15.],
                    [33.,43.,47.]]
zptautau_disco   = ["Z\'_{SSM} #rightarrow #tau^{+}#tau^{-}",
                    [3.,6.,9.],
                    [12.,18.,23.]]
zpmumuflav_disco = ["Z\'_{f.a.} #rightarrow #mu^{+}#mu^{-}",
                    [0.1,2.,5.],
                    [10.,19.,23.]]

##############################################
rsgww_limit      = ["G_{RS} #rightarrow W^{+}W^{-}",
                    [6.2,8.,10.1],  #  27 TeV ->   1, 15, 100 ab-1
                    [20.5,28.,32.]] # 100 TeV -> 2.5, 30, 100 ab-1
qstar_limit      = ["Q* #rightarrow jj",
                    [11.5,14.,15.],
                    [40.5,43.,44.5]]
zpttTC2_limit    = ["Z\'_{TC2} #rightarrow t#bar{t}",
                    [7.2,10.,11.5],
                    [21.5,28.,31.]]
zpttSSM_limit    = ["Z\'_{SSM} #rightarrow t#bar{t}",
                    [5.3,8.4,10.3],
                    [16.,24.,27.5]]
zpll_limit       = ["Z\'_{SSM} #rightarrow l^{+}l^{-}",
                    [10.,13.,14.2],
                    [32.,40.,45.5]]
zptautau_limit   = ["Z\'_{SSM} #rightarrow #tau^{+}#tau^{-}",
                    [1.,6.,8.3],
                    [11.,14.,21.]]
zpmumuflav_limit = ["Z\'_{f.a.} #rightarrow #mu^{+}#mu^{-}",
                    [0.,4.5,0.],
                    [0.,26.,0.]]


##############################################
if result=="Disco" :
  rsgww      = rsgww_disco
  qstar      = qstar_disco
  zpttTC2    = zpttTC2_disco
  zpttSSM    = zpttSSM_disco
  zpll       = zpll_disco
  zptautau   = zptautau_disco
  zpmumuflav = zpmumuflav_disco
if result=="Limit" :
  rsgww      = rsgww_limit
  qstar      = qstar_limit
  zpttTC2    = zpttTC2_limit
  zpttSSM    = zpttSSM_limit
  zpll       = zpll_limit
  zptautau   = zptautau_limit
  # f.a. = 1710.06363
  zpmumuflav = zpmumuflav_limit

##############################################
database=[
zptautau,
#zpmumuflav,
zpll,
rsgww,
zpttSSM,
zpttTC2,
qstar,
]

nAna=6
nbins = (3*nAna)
if mode=="27" or mode=="100": nbins = (2*nAna)
h_27=[]
h_27.append( r.TH1D("h_27_1", "h_27_1", nbins,0.,nbins))
h_27.append( r.TH1D("h_27_2", "h_27_2", nbins,0.,nbins))
h_27.append( r.TH1D("h_27_3", "h_27_3", nbins,0.,nbins))
h_100=[]
h_100.append(r.TH1D("h_100_1","h_100_1",nbins,0.,nbins))
h_100.append(r.TH1D("h_100_2","h_100_2",nbins,0.,nbins))
h_100.append(r.TH1D("h_100_3","h_100_3",nbins,0.,nbins))

nMax=len(h_100)-1

color  = [[r.kYellow-7, r.kAzure-9], [r.kRed+1, r.kBlue+1], [r.kGray+3, r.kGray+2]]
legend = [["1 ab^{-1}", "2.5 ab^{-1}"], ["15 ab^{-1}", "30 ab^{-1}"], ["100 ab^{-1}", "100 ab^{-1}"]]

process = [database[0][0],database[1][0],database[2][0],database[3][0],database[4][0],database[5][0]]
val27   = [database[0][1],database[1][1],database[2][1],database[3][1],database[4][1],database[5][1]]
val100  = [database[0][2],database[1][2],database[2][2],database[3][2],database[4][2],database[5][2]]

count = 1
count_ana = 0
for i_bin in xrange( 1, nbins+1 ):
  if count==4 : count=1
  if count==1 :
    if mode=="27" :
      for i in xrange( 0, nMax+1 ) : h_27[i].SetBinContent(i_bin, val27[count_ana][i])
      count+=1
    elif mode=="100" :
      for i in xrange( 0, nMax+1 ) : h_100[i].SetBinContent(i_bin, val100[count_ana][i])
      count+=1
    else :
      for i in xrange( 0, nMax+1 ) : h_27[i].SetBinContent(i_bin, val27[count_ana][i])
  if count==2 :
    for i in xrange( 0, nMax+1 ) :
      h_100[i].SetBinContent(i_bin, val100[count_ana][i])
  #
  if mode=="27_100" :
    str_27   = '#scale[0.75]{#sqrt{s} = 27 TeV}'
    str_100  = '#scale[0.75]{#sqrt{s} = 100 TeV}'
    if count==1 : h_100[nMax].GetXaxis().SetBinLabel(i_bin,str_27)
    if count==2 : h_100[nMax].GetXaxis().SetBinLabel(i_bin,str_100)
    if count==3 :
      str_proc = '#scale[1.02]{#font[22]{'+process[count_ana]+'}}'
      h_100[nMax].GetXaxis().SetBinLabel(i_bin,str_proc)
      count_ana+=1
  else :
    if count==2 :
      str_proc = '#scale[1.02]{#font[22]{'+process[count_ana]+'}}'
      if mode=="27"  : h_27[nMax].GetXaxis().SetBinLabel(i_bin,str_proc)
      if mode=="100" : h_100[nMax].GetXaxis().SetBinLabel(i_bin,str_proc)
      count_ana+=1
  count+=1

for i in xrange( 0, nMax+1 ) :
  alpha=0.42
  if i==0: alpha=0.8
  if i==nMax: alpha=0.15
  #
  h_27[i].SetLineColorAlpha(color[i][0],0.)
  h_27[i].SetFillColorAlpha(color[i][0],alpha)
  h_27[i].SetMarkerColorAlpha(color[i][0],0.)
  h_100[i].SetLineColorAlpha(color[i][1],0.)
  h_100[i].SetFillColorAlpha(color[i][1],alpha)
  h_100[i].SetMarkerColorAlpha(color[i][0],0.)

canvas = r.TCanvas("test", "test", 600, 600)
canvas.SetTicks(1,1)
canvas.SetLeftMargin(0.21)
canvas.SetRightMargin(0.02)
r.gStyle.SetOptStat(0)
r.gPad.SetGridx()

leg = r.TLegend(0.73,0.52,0.98,0.70)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetLineColor(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.035)
leg.SetTextFont(42)

fact=1.1
if result=="Limit" and mode=="27": fact=1.15

if mode=="27" :
  #the_max=h_27[nMax].GetMaximum()
  the_max=0.
  for i in range(len(h_27)) : the_max = max(the_max, h_27[i].GetMaximum())
  if the_max==0. : the_max=1.
  h_27[nMax].SetMinimum(0.)
  h_27[nMax].SetMaximum(the_max*fact)
  h_27[nMax].SetTitle("")
  h_27[nMax].GetYaxis().SetTitleOffset(1.30)
  h_27[nMax].GetYaxis().SetTitle("Mass scale [TeV]")
  h_27[nMax].GetXaxis().SetLabelSize(0.05)
  h_27[nMax].GetXaxis().SetTickLength(0.)

  h_27[nMax].Draw("hbar")
  for i in xrange( nMax, -1, -1 ) :
    h_27[i].Draw("hbarsame")

  for i in xrange( 0, nMax+1 ) :
    leg.AddEntry(h_27[i],legend[i][0])
  leg.Draw("same")

else :
  #the_max=h_100[nMax].GetMaximum()
  the_max=0.
  for i in range(len(h_27))  : the_max = max(the_max, h_27[i].GetMaximum())
  for i in range(len(h_100)) : the_max = max(the_max, h_100[i].GetMaximum())
  if the_max==0. : the_max=1.
  h_100[nMax].SetMinimum(0.)
  h_100[nMax].SetMaximum(the_max*fact)
  h_100[nMax].SetTitle("")
  h_100[nMax].GetYaxis().SetTitleOffset(1.30)
  h_100[nMax].GetYaxis().SetTitle("Mass scale [TeV]")
  h_100[nMax].GetXaxis().SetLabelSize(0.05)
  h_100[nMax].GetXaxis().SetTickLength(0.)
  
  h_100[nMax].Draw("hbar")
  for i in xrange( nMax, -1, -1 ) :
    h_100[i].Draw("hbarsame")
    if mode=="27_100" : h_27[i].Draw("hbarsame")
  
  for i in xrange( 0, nMax+1 ) :
    if mode=="27_100" and i!=nMax : leg.AddEntry(h_27[i],legend[i][0])
    leg.AddEntry(h_100[i],legend[i][1])
  leg.Draw("same")

Text = r.TLatex()
Text.SetNDC()
Text.SetTextAlign(31)
Text.SetTextSize(0.033)
text = ''
if result=="Disco" : text = '5 #sigma Discovery'
if result=="Limit" : text = '95% CL Limit'
Text.DrawLatex(0.95, 0.72, text)

leftText27      = "HE-LHC Simulation (Delphes), #sqrt{s} = 27 TeV"
leftText100     = "FCC-hh Simulation (Delphes), #sqrt{s} = 100 TeV"
leftText27_100  = "FCC-hh / HE-LHC Simulation (Delphes)"
Text.SetTextAlign(31);
Text.SetTextSize(0.04)
if mode=="27"    : Text.DrawLatex(0.97, 0.92, '#it{' + leftText27     +'}')
elif mode=="100" : Text.DrawLatex(0.97, 0.92, '#it{' + leftText100    +'}')
else             : Text.DrawLatex(0.97, 0.92, '#it{' + leftText27_100 +'}')

canvas.RedrawAxis()
canvas.RedrawAxis("g");
canvas.GetFrame().SetBorderSize( 12 )
canvas.Modified()
canvas.Update()

extra=""
if mode=="27"  : extra="_onlyHELHC"
if mode=="100" : extra="_onlyFCChh"
canvas.Print("summary"+result+extra+".pdf")

