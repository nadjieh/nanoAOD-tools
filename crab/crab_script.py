#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis,outFileName
from PhysicsTools.NanoAODTools.postprocessing.electronId.ElectronSkimmer import ElectronSkimmerSignal, ElectronSkimmerBackground

II = inputFiles()
#II = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAODv6/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/270000/1FB6AF93-29B0-F34E-92EC-E9C859AED428.root']

if len(II)>0:
    if ('TTTo' in II[0]) or ('TTJets' in II[0]):
        modules_=[ElectronSkimmerBackground()]
    else:
        print('Signal')
        modules_=[ElectronSkimmerSignal()]
p = PostProcessor( "." , II , maxEntries = None, branchsel=None, cut=None, compression='LZMA:9',
                   outputbranchsel='{0}/python/PhysicsTools/NanoAODTools/postprocessing/electronId/keep_and_drop.txt'.format(os.environ['CMSSW_BASE']),
                   postfix=None, modules=modules_ , noOut=False, prefetch=False, justcount=False,
                   firstEntry=0, longTermCache=False, friend=False,
                   provenance=True,fwkJobReport=True,jsonInput=runsAndLumis() )
p.run()

print "DONE"

