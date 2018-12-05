def histogramD0(c,var1,var2):

    hl = ROOT.TH1F()
    hh = ROOT.TH1F()
    
    for event in t:

        m = len(event.electron_fracs1)

        for i in xrange(m):

            bar = event.electron_truthMatchedBarcode[i]
            found = False
            true_d0 = 0

            if bar >= 0:

                for j in xrange(len(event.truthleptonBarcode)):

                    if bar == event.truthleptonBarcode[j] and abs(event.truthleptonEta[j])<2.47:

                        found = True
                        true_d0 = event.truthleptond0[j]
                        break

            if not found: continue
            
            if true_d0 <= 0.2:
                
                hl.Fill(eval(var1))

            if true_d0 > 0.2:

                hh.Fill(eval(var1))
    
    c1 = ROOT.TCanvas(
    hl.SetLineColor(ROOT.kBlue)
    hh.SetLineColor(ROOT.kRed)



    hl.Draw("hist")
    hh.Draw("hist same")

    leg = ROOT.TLegend(.5,.6,.8,.87)
    leg.AddEntry(hl, "d0<=0.2", "l")
    leg.AddEntry(hh, "d0>0.2", "l")
    leg.Draw("same")
            
    m = max(hl.GetMaximum(),hh.GetMaximum())
    hl.SetMaximum(m*1.1)



import glob
import ROOT
import os
from array import array

ROOT.gROOT.LoadMacro("/afs/cern.ch/user/t/tholmes/FTK/scripts/python/atlasstyle/AtlasStyle.C")
ROOT.gROOT.LoadMacro("/afs/cern.ch/user/t/tholmes/FTK/scripts/python/atlasstyle/AtlasLabels.C");
ROOT.SetAtlasStyle()
ROOT.gROOT.SetBatch(0)

# Define grid
lifetimes = ["0p01", "0p1"]
masses = ["50", "100", "200", "300", "400", "500"]

# Define SRs
signal_regions = {"SR0": ""}

for sr in signal_regions:

    for lt in lifetimes:
        for m in masses:

            files = glob.glob("/afs/cern.ch/work/t/tholmes/LLP/user.lhoryn.mc16_13TeV.*.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_%s_0_%sns.062018_trees.root/*.root"%(m, lt))
            if len(files)==0:
                #print "Couldn't find files for mass %s, lifetime %s"%(m, lt)
                continue

            print "Using file with mass %s, lifetime %s"%(m, lt)
            t = ROOT.TChain("trees_SR_highd0_")
            for f in files: t.Add(f)
            
            histogramD0("c1 = ROOT.TCanvas()","event.electron_fracs1[i]","fracs1")


            raw_input("...")
