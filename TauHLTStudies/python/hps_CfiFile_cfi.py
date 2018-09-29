import FWCore.ParameterSet.Config as cms

hpsTauHLTStudies = cms.EDAnalyzer("HPSTauHLTStudiesAnalyzer",
    hadronSrc = cms.InputTag("tauGenJetsSelectorAllHadrons"),
    tauElectronSrc = cms.InputTag("tauGenJetsSelectorElectrons"),
    tauMuonSrc = cms.InputTag("tauGenJetsSelectorMuons"),
    puSrc = cms.InputTag("slimmedAddPileupInfo"),

    slimmedTauSrc = cms.InputTag("slimmedTaus"),
    #hpsTauSrc = cms.InputTag("hltHpsPFTauProducerReg", "", "MYHLT"),
    hpsTauSrc = cms.InputTag("hltHpsPFTauProducer", "", "MYHLT"),
    hpsTauDM = cms.InputTag("hltHpsPFTauDiscriminationByDecayModeFindingNewDMsSingleTau","","MYHLT"),   
    #defaultTauSrc = cms.InputTag("hltPFTausSansRef", "", "MYHLT"),
    defaultTauSrc = cms.InputTag("hltPFTaus", "", "MYHLT"),
    #defaultTauSrc = cms.InputTag("hltPFTausReg", "", "MYHLT"),
    defaultTauDM = cms.InputTag("hltPFTauDiscriminationByDecayModeFindingNewDMsPFTaus","","MYHLT"),

    muonSrc = cms.InputTag("slimmedMuons"),
    electronSrc = cms.InputTag("slimmedElectrons"),
    jetSrc = cms.InputTag("slimmedJets"),
    metSrc = cms.InputTag("slimmedMETs"),
    pvSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    triggerSrc = cms.InputTag("TriggerResults","","MYHLT"),
    triggerObjectsSrc = cms.InputTag("slimmedPatTrigger","","LOCALHPS"),
    stage2TauSrc = cms.InputTag("caloStage2Digis","Tau","RECO"),
    genSrc = cms.InputTag("prunedGenParticles","","PAT"),
    eleMediumIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp90"),
    eleLooseIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring16-HZZ-V1-wpLoose"),
    #l2p5TauJet = cms.InputTag("hltL2TauJetsL1TauSeeded", "", "MYHLT"),
    #l2p5TauJet = cms.InputTag( "hltL2TausForPixelIsolation","","MYHLT" ),
    l2p5TauJet = cms.InputTag( "hltL2TausForPixelIsolationL1TauSeeded","","MYHLT" ),
    l2p5TauJetIso = cms.InputTag("hltL2TauPixelIsoTagProducerL1TauSeeded", "", "MYHLT"),
    #l2p5TauJetIso = cms.InputTag("hltL2TauPixelIsoTagProducer", "", "MYHLT"),
    l2p5Vertex = cms.InputTag("hltPixelVerticesRegL1TauSeeded", "", "MYHLT"),
    #l2p5Vertex = cms.InputTag( "hltPixelVerticesRegForTau","","MYHLT" ),
    l2p5Tracks = cms.InputTag("hltPixelTracksMergedRegL1TauSeeded", "", "MYHLT"),
    #l2p5Tracks = cms.InputTag("hltPixelTracksMergedRegForTau", "", "MYHLT"),
    beamSpot = cms.InputTag("hltOnlineBeamSpot", "", "MYHLT"),
    l2p5IsoOffline = cms.InputTag("hltL2TauPixelIsoTagProducer","","LOCALHPS"),
    l2p5IsoOfflineNew1 = cms.InputTag("newHltL2TauPixelIsoTagProducer","","LOCALHPS"),
    l2p5IsoOfflineNew2 = cms.InputTag("new2HltL2TauPixelIsoTagProducer","","LOCALHPS"),
)
