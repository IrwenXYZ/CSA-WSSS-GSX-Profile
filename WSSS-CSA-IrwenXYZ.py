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
def eastWestCargoOffset(aircraftData):
    offset = {
    300: 5,
    310: 5,
    318: 7.5,
    319: 7.5,
    320: 7.5,
    330: 3.5,
    737: 5.1,
    747: 3.5,
    777: 3.5,
    380: 3.4
    }
    
    offset787 = {
	8: 3.2,
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
def terminalOffset(aircraftData):
    offset = {
    300: 4.8,
    310: 4.8,
    318: 7.3,
    319: 7.3,
    320: 7.3,
    330: 3.3,
    737: 4.8,
    747: 3.3,
    777: 3.2,
    380: 3.2
    }
    
    offset787 = {
	8: 3,
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
        None : (acehub, terminalOffset),
    },
    GATE : {
        None : (CustomizedName("Terminal 4 G Gates | Gate G#", 4), terminalOffset)
    },
    GATE_A : {
        None : (terminal3Alpha, terminalOffset)
    },
    GATE_B : {
        None : (terminal3Bravo, terminalOffset)
    },
    GATE_C : {
        None : (terminal1Charlie, terminalOffset)
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
        None : (CustomizedName("Terminal 4 G Gates | Gate G#§", 4), terminalOffset)
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
        300 : (northRemote, terminalOffset),
        301 : (northRemote, terminalOffset),
        302 : (northRemote, terminalOffset),
        303 : (northRemote, terminalOffset),
        304 : (northRemote, terminalOffset),
        305 : (northRemote, terminalOffset),
        306 : (northRemote, terminalOffset),
        307 : (northRemote, terminalOffset),
        308 : (northRemote, terminalOffset),
        309 : (northRemote, terminalOffset),
        310 : (northRemote, terminalOffset),
        502 : (westCargo, eastWestCargoOffset),
        503 : (westCargo, eastWestCargoOffset),
        504 : (westCargo, eastWestCargoOffset),
        505 : (westCargo, eastWestCargoOffset),
        506 : (westCargo, eastWestCargoOffset),
        507 : (westCargo, eastWestCargoOffset),
        508 : (westCargo, eastWestCargoOffset),
        509 : (westCargo, eastWestCargoOffset),
        510 : (westCargo, eastWestCargoOffset),
        511 : (westCargo, eastWestCargoOffset),
        512 : (westCargo, eastWestCargoOffset),
        513 : (westCargo, eastWestCargoOffset),
        514 : (westCargo, eastWestCargoOffset),
        515 : (westCargo, eastWestCargoOffset),
        516 : (westCargo, eastWestCargoOffset),
        517 : (westCargo, eastWestCargoOffset),
        600 : (eastCargo, eastWestCargoOffset),
        601 : (eastCargo, eastWestCargoOffset),
        602 : (eastCargo, eastWestCargoOffset),
        603 : (eastCargo, eastWestCargoOffset),
        604 : (eastCargo, eastWestCargoOffset),
    },
    0 : {
        0 : (CustomizedName("Terminal 2 F Gates | Gate F36", 2), terminalOffset),
    },
}
