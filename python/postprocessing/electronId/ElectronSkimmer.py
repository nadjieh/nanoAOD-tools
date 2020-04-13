import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class ElectronSkimmer(Module):
    def __init__(self , isSignal):
        self.isSignal = isSignal
        current_dir = os.path.dirname(os.path.abspath(__file__))       
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        
        all_electrons = Collection(event, "Electron")
        all_jets = Collection(event, "Jet")
        all_genPart = Collection(event, "GenPart")
        nFake = 0
        nPrompt = 0
        for electron in all_electrons:
            if electron.pt < 10 or abs(electron.eta) > 2.5: continue
            if electron.cutBased < 2: continue
            #to be checked for the ECAL gap
            if electron.genPartFlav == 1:
                nPrompt+=1
            else:
                nFake+=1
        return (nPrompt > 0 and self.isSignal) or (nFake > 0 and not self.isSignal)
        
        


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
ElectronSkimmerSignal = lambda : ElectronSkimmer(True)
ElectronSkimmerBackground = lambda : ElectronSkimmer(False)
