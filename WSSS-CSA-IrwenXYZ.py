# -- coding: utf-8 --
msfs_mode = 1
icao = "wsss"

terminal3Alpha = CustomizedName("Terminal 3 A Gates | Gate A#§", 3)
terminal3Bravo = CustomizedName("Terminal 3 B Gates | Gate B#§", 3)
terminal1Charlie = CustomizedName("Terminal 1 C Gates | Gate C#§", 1)
terminal1Delta = CustomizedName("Terminal 1 D Gates | Gate D#§", 1)
terminal2Echo = CustomizedName("Terminal 2 E Gates | Gate E#§", 2)
terminal2Foxtrot = CustomizedName("Terminal 2 F Gates | Gate F#§", 2)
terminal4Golf = CustomizedName("Terminal 4 G Gates | Gate G#§", 4)
eastRemote = CustomizedName("East Remote Apron (200-203) | Stand #§", )
southEastRemote = CustomizedName("South East Remote Apron (205-209) | Stand #§", )
northRemote = CustomizedName("North Remote Apron (300-310) | Stand #§", )
# ^ stands 951-954 not in scenery
# northEastRemote = CustomizedName("North East Remote Apron | Stand #", )
# ^ stands 400-404 not in scenery
# southApron = CustomizedName("South Apron | Stand #", )
# ^ stands 461-487 not in scenery
westCargo = CustomizedName("West Cargo Apron (502-517) | Stand #", 5)
eastCargo = CustomizedName("East Cargo Apron (600-604) | Stand #", 6)
# eastService = CustomizedName("East Service Apron | Stand #", )
# ^ stands 606 & 609 not in scenery
acehub = CustomizedName("Acehub (611-612) | Stand #", 7)
parking = CustomizedName("Parking | Stand #", 0)

# A320 - 7.5m
@AlternativeStopPositions
def westCargoOffset(aircraftData):
    offset = {
        310: 5,
        318: 7.5,
        319: 7.5,
        320: 7.5,
        330: 3.5,
        747: 3.5,
    }
    
    offset787 = {
        9: 3.2,
        10: 3.5,
    }
    if aircraftData.idMajor == 787:
        return Distance.fromMeters(offset787.get(aircraftData.idMinor))
    else:
        try:
            return Distance.fromMeters(offset.get(aircraftData.idMajor))
        except:
            return Distance.fromMeters(0)

@AlternativeStopPositions
def eastCargoOffset(aircraftData):
    offset = {
        310: 5,
        318: 7.5,
        319: 7.5,
        320: 7.5,
        330: 3.5,
        747: 3.5,
    }
    
    offset787 = {
        9: 3.2,
        10: 3.5,
    }
    if aircraftData.idMajor == 787:
        return Distance.fromMeters(offset787.get(aircraftData.idMinor))
    else:
        try:
            return Distance.fromMeters(offset.get(aircraftData.idMajor))
        except:
            return Distance.fromMeters(0)

# A320 - 7.3m
@AlternativeStopPositions
def northRemoteOffset(aircraftData):
    offset = {
        310: 4.8,
        318: 7.3,
        319: 7.3,
        320: 7.3,
        330: 3.3,
        747: 3.3,
    }
    
    offset787 = {
        9: 3,
        10: 3.3,
    }
    if aircraftData.idMajor == 787:
        return Distance.fromMeters(offset787.get(aircraftData.idMinor))
    else:
        try:
            return Distance.fromMeters(offset.get(aircraftData.idMajor))
        except:
            return Distance.fromMeters(0)

@AlternativeStopPositions
def acehubOffset(aircraftData):
    offset = {
        310: 4.8,
        318: 7.3,
        319: 7.3,
        320: 7.3,
        330: 3.3,
        747: 3.3,
    }
    
    offset787 = {
        9: 3,
        10: 3.3,
    }
    if aircraftData.idMajor == 787:
        return Distance.fromMeters(offset787.get(aircraftData.idMinor))
    else:
        try:
            return Distance.fromMeters(offset.get(aircraftData.idMajor))
        except:
            return Distance.fromMeters(0)

@AlternativeStopPositions
def terminalOffset(aircraftData):
    offset = {
        310: 4.8,
        318: 7.3,
        319: 7.3,
        320: 7.3,
        330: 3.3,
        747: 3.3,
    }
    
    offset787 = {
        9: 3,
        10: 3.3,
    }
    if aircraftData.idMajor == 787:
        return Distance.fromMeters(offset787.get(aircraftData.idMinor))
    else:
        try:
            return Distance.fromMeters(offset.get(aircraftData.idMajor))
        except:
            return Distance.fromMeters(0)

parkings = {
    E_PARKING : {
        None : (acehub, acehubOffset),
    },
    GATE : {
        None : (CustomizedName("Terminal 4 G Gates| Gate G#", 4), )
    },
    GATE_A : {
        None : (terminal3Alpha, )
    },
    GATE_B : {
        None : (terminal3Bravo, )
    },
    GATE_C : {
        None : (terminal1Charlie, )
    },
    GATE_D : {
        None : (terminal1Delta, terminalOffset)
    },
    GATE_E : {
        None : (terminal2Echo, terminalOffset)
    },
    GATE_F : {
        None : (terminal2Foxtrot, terminalOffset)
    },
    GATE_G : {
        None : (terminal4Golf, )
    },
    PARKING : {
        200 : (eastRemote, terminalOffset),
        "200L" : (eastRemote, ),
        201 : (eastRemote, terminalOffset),
        202 : (eastRemote, terminalOffset),
        203 : (eastRemote, terminalOffset),
        205 : (southEastRemote, terminalOffset),
        206 : (southEastRemote, terminalOffset),
        207 : (southEastRemote, terminalOffset),
        208 : (southEastRemote, terminalOffset),
        209 : (southEastRemote, terminalOffset),
        300 : (northRemote, northRemoteOffset),
        301 : (northRemote, northRemoteOffset),
        302 : (northRemote, northRemoteOffset),
        303 : (northRemote, northRemoteOffset),
        304 : (northRemote, northRemoteOffset),
        305 : (northRemote, northRemoteOffset),
        306 : (northRemote, northRemoteOffset),
        307 : (northRemote, northRemoteOffset),
        308 : (northRemote, northRemoteOffset),
        309 : (northRemote, northRemoteOffset),
        310 : (northRemote, northRemoteOffset),
        502 : (westCargo, westCargoOffset),
        503 : (westCargo, westCargoOffset),
        504 : (westCargo, westCargoOffset),
        505 : (westCargo, westCargoOffset),
        506 : (westCargo, westCargoOffset),
        507 : (westCargo, westCargoOffset),
        508 : (westCargo, westCargoOffset),
        509 : (westCargo, westCargoOffset),
        510 : (westCargo, westCargoOffset),
        511 : (westCargo, westCargoOffset),
        512 : (westCargo, westCargoOffset),
        513 : (westCargo, westCargoOffset),
        514 : (westCargo, westCargoOffset),
        515 : (westCargo, westCargoOffset),
        516 : (westCargo, westCargoOffset),
        517 : (westCargo, westCargoOffset),
        600 : (eastCargo, eastCargoOffset),
        601 : (eastCargo, eastCargoOffset),
        602 : (eastCargo, eastCargoOffset),
        603 : (eastCargo, eastCargoOffset),
        604 : (eastCargo, eastCargoOffset),
    },
    0 : {
        0 : (CustomizedName("Terminal 2 F Gates | Gate F36", 2), terminalOffset),
    },
}
