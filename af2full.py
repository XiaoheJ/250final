import glob
import ROOT
import os

ROOT.gROOT.LoadMacro("/afs/cern.ch/user/t/tholmes/FTK/scripts/python/atlasstyle/AtlasStyle.C")
ROOT.gROOT.LoadMacro("/afs/cern.ch/user/t/tholmes/FTK/scripts/python/atlasstyle/AtlasLabels.C");
ROOT.SetAtlasStyle()
ROOT.gROOT.SetBatch(0)

signal_regions = {"SR0": ""}

for sr in signal_regions:

    files100_0 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399039.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_300_0_0p1ns.071918af2_trees.root/*.root")
    t100_0 = ROOT.TChain("trees_SR_highd0_")
    for f in files100_0: t100_0.Add(f)

    files100_1 = glob.glob("/eos/user/l/lhoryn/highd0/user.lhoryn.mc16_13TeV.399039.MGPy8EG_A14NNPDF23LO_SlepSlep_directLLP_300_0_0p1ns.071918full_trees.root/*.root")
    t100_1 = ROOT.TChain("trees_SR_highd0_")
    for f in files100_1: t100_1.Add(f)
   
    h100_0_el_d0 = ROOT.TH1F("100_0_mu_d0","100_0_mu_d0",15,0,30)
    h100_1_el_d0 = ROOT.TH1F("100_1_mu_d0","100_1_mu_d0",15,0,30)

    for event in t100_0:

        for i in xrange(len(event.muon_truthMatchedBarcode)):

            barcode = event.muon_truthMatchedBarcode[i]
            found_match = False
            true_d0 = 0
                    
            if barcode>=0:

                for j in xrange(len(event.truthLepton_barcode)):
                            
                    if barcode == event.truthLepton_barcode[j] and abs(event.truthLepton_eta[j])<2.47:
                                
                        found_match = True
                        true_d0 = event.truthLepton_d0[j]
                        break
                    
            if not found_match: continue
                
            h100_0_el_d0.Fill(true_d0)

    for event in t100_1:

        for i in xrange(len(event.muon_truthMatchedBarcode)):

            barcode = event.muon_truthMatchedBarcode[i]
            found_match = False
            true_d0 = 0
                    
            if barcode>=0:

                for j in xrange(len(event.truthLepton_barcode)):
                            
                    if barcode == event.truthLepton_barcode[j] and abs(event.truthLepton_eta[j])<2.47:
                                
                        found_match = True
                        true_d0 = event.truthLepton_d0[j]
                        break
                    
            if not found_match: continue
                
            h100_1_el_d0.Fill(true_d0)

    c = ROOT.TCanvas()
    r = ROOT.TRatioPlot(h100_0_el_d0, h100_1_el_d0, "pois")
    r.Draw()

    raw_input("...")
