import glob
import ROOT
import os

ROOT.gROOT.LoadMacro("/afs/cern.ch/user/t/tholmes/FTK/scripts/python/atlasstyle/AtlasStyle.C")
ROOT.gROOT.LoadMacro("/afs/cern.ch/user/t/tholmes/FTK/scripts/python/atlasstyle/AtlasLabels.C");
ROOT.SetAtlasStyle()
ROOT.gROOT.SetBatch(0)

signal_regions = {"SR0": ""}

for sr in signal_regions:

    files100_0 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399030.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_100_0_0p01ns.071018_trees.root/*.root")
    t100_0 = ROOT.TChain("trees_SR_highd0_")
    for f in files100_0: t100_0.Add(f)

    files100_1 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399031.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_100_0_0p1ns.071018_trees.root/*.root")
    t100_1 = ROOT.TChain("trees_SR_highd0_")
    for f in files100_1: t100_1.Add(f)

    files300_1 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399039.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_300_0_0p1ns.071018_trees.root/*.root")
    t300_1 = ROOT.TChain("trees_SR_highd0_")
    for f in files300_1: t300_1.Add(f)

    files500_0 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399046.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_500_0_0p01ns.071018_trees.root/*.root")
    t500_0 = ROOT.TChain("trees_SR_highd0_")
    for f in files500_0: t500_0.Add(f)

    files500_1 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399047.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_500_0_0p1ns.071018_trees.root/*.root")
    t500_1 = ROOT.TChain("trees_SR_highd0_")
    for f in files500_1: t500_1.Add(f)

    files700_0 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399054.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_700_0_0p01ns.071018_trees.root/*.root")
    t700_0 = ROOT.TChain("trees_SR_highd0_")
    for f in files700_0: t700_0.Add(f)

    files700_1 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399055.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_700_0_0p1ns.071018_trees.root/*.root")
    t700_1 = ROOT.TChain("trees_SR_highd0_")
    for f in files700_1: t700_1.Add(f)
   
    h = ROOT.TH2F()
    p = ROOT.TProfile()
    h.GetXaxis().SetTitle("truth d0")
    h.GetYaxis().SetTitle("d0")
    h.SetBins(25,0,30,25,0,30)
    p.SetBins(25,0,30)

    for event in t700_1:

        for i in xrange(len(event.electron_truthMatchedBarcode)):

            barcode = event.electron_truthMatchedBarcode[i]
            found_match = False
            true_d0 = 0
                    
            if barcode>=0:

                for j in xrange(len(event.truthLepton_barcode)):
                            
                    if barcode == event.truthLepton_barcode[j] and abs(event.truthLepton_eta[j])<2.47:
                                
                        found_match = True
                        true_d0 = event.truthLepton_d0[j]
                        break
                    
            if not found_match: continue
            
            h.Fill(true_d0,abs(event.electron_IDtrack_d0[0]))
            p.Fill(true_d0,abs(event.electron_IDtrack_d0[0]))

    c = ROOT.TCanvas("c","c")
    
    h.Draw("COLZ")
    p.Draw("same")

    raw_input("...")
