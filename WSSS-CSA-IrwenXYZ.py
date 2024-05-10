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


@AlternativeStopPositions
def ChangiOffsets(aircraftData):
    offset = {
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

parkings = {
    E_PARKING : {
        None : (acehub, ),
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
        None : (terminal1Delta, )
    },
    GATE_E : {
        None : (terminal2Echo, )
    },
    GATE_F : {
        None : (terminal2Foxtrot, )
    },
    GATE_G : {
        None : (terminal4Golf, )
    },
    PARKING : {
        200 : (eastRemote, ChangiOffsets),
        "200L" : (eastRemote, ChangiOffsets),
        201 : (eastRemote, ChangiOffsets),
        202 : (eastRemote, ChangiOffsets),
        203 : (eastRemote, ChangiOffsets),
        205 : (southEastRemote, ChangiOffsets),
        206 : (southEastRemote, ChangiOffsets),
        207 : (southEastRemote, ChangiOffsets),
        208 : (southEastRemote, ChangiOffsets),
        209 : (southEastRemote, ChangiOffsets),
        300 : (northRemote, ChangiOffsets),
        301 : (northRemote, ChangiOffsets),
        302 : (northRemote, ChangiOffsets),
        303 : (northRemote, ChangiOffsets),
        304 : (northRemote, ChangiOffsets),
        305 : (northRemote, ChangiOffsets),
        306 : (northRemote, ChangiOffsets),
        307 : (northRemote, ChangiOffsets),
        308 : (northRemote, ChangiOffsets),
        309 : (northRemote, ChangiOffsets),
        310 : (northRemote, ChangiOffsets),
        502 : (westCargo, ChangiOffsets),
        503 : (westCargo, ChangiOffsets),
        504 : (westCargo, ChangiOffsets),
        505 : (westCargo, ChangiOffsets),
        506 : (westCargo, ChangiOffsets),
        507 : (westCargo, ChangiOffsets),
        508 : (westCargo, ChangiOffsets),
        509 : (westCargo, ChangiOffsets),
        510 : (westCargo, ChangiOffsets),
        511 : (westCargo, ChangiOffsets),
        512 : (westCargo, ChangiOffsets),
        513 : (westCargo, ChangiOffsets),
        514 : (westCargo, ChangiOffsets),
        515 : (westCargo, ChangiOffsets),
        516 : (westCargo, ChangiOffsets),
        517 : (westCargo, ChangiOffsets),
        600 : (eastCargo, ChangiOffsets),
        601 : (eastCargo, ChangiOffsets),
        602 : (eastCargo, ChangiOffsets),
        603 : (eastCargo, ChangiOffsets),
        604 : (eastCargo, ChangiOffsets),
    },
    0 : {
        0 : (CustomizedName("Terminal 2 F Gates | Gate F36", 2), ChangiOffsets),
    },
}
