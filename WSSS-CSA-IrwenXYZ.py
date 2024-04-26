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
        200 : (eastRemote, ),
        "200L" : (eastRemote, ),
        201 : (eastRemote, ),
        202 : (eastRemote, ),
        203 : (eastRemote, ),
        205 : (southEastRemote, ),
        206 : (southEastRemote, ),
        207 : (southEastRemote, ),
        208 : (southEastRemote, ),
        209 : (southEastRemote, ),
        300 : (northRemote, ),
        301 : (northRemote, ),
        302 : (northRemote, ),
        303 : (northRemote, ),
        304 : (northRemote, ),
        305 : (northRemote, ),
        306 : (northRemote, ),
        307 : (northRemote, ),
        308 : (northRemote, ),
        309 : (northRemote, ),
        310 : (northRemote, ),
        502 : (westCargo, ),
        503 : (westCargo, ),
        504 : (westCargo, ),
        505 : (westCargo, ),
        506 : (westCargo, ),
        507 : (westCargo, ),
        508 : (westCargo, ),
        509 : (westCargo, ),
        510 : (westCargo, ),
        511 : (westCargo, ),
        512 : (westCargo, ),
        513 : (westCargo, ),
        514 : (westCargo, ),
        515 : (westCargo, ),
        516 : (westCargo, ),
        517 : (westCargo, ),
        600 : (eastCargo, ),
        601 : (eastCargo, ),
        602 : (eastCargo, ),
        603 : (eastCargo, ),
        604 : (eastCargo, ),
    },
    0 : {
        0 : (CustomizedName("Terminal 2 F Gates | Gate F36", 2), ),
    },
}
