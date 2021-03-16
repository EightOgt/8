## Extraction table List
|Table Name|Filter|Join (Parent) Table|Parent Columns|Child Columns|Join Filter
|----|----|----|----|----|----|
|BKPF|BUKRS IN `<%=Company_Code%>`  AND AWTYP IN ('MKPF',  'RMRP', 'BKPF') AND (	   	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|||||
|BSEG||BKPF|Use Primary KeysMANDT BUKRS BELNR GJAHR |Use Primary KeysMANDT BUKRS BELNR GJAHR |BUKRS IN `<%=Company_Code%>`  AND AWTYP IN ('MKPF',  'RMRP', 'BKPF') AND (	   	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` ) |
|CDHDR|OBJECTCLAS IN ('EINKBELEG',  'BELEG',  'BANF',  'KRED') AND (	   	UDATE >= `<%=startDateDelta%>` AND  	UDATE <= `<%=endDate%>` )|||||
|CDPOS||CDHDR|Use Primary KeysMANDANT OBJECTCLAS OBJECTID CHANGENR |Use Primary KeysMANDANT OBJECTCLAS OBJECTID CHANGENR |OBJECTCLAS IN ('EINKBELEG',  'BELEG',  'BANF',  'KRED') AND (	   	UDATE >= `<%=startDateDelta%>` AND  	UDATE <= `<%=endDate%>`)|
|DD02T|TABNAME IN ('BKPF', 'BSEG', 'CDHDR', 'CDPOS', 'EBAN', 'EBKN', 'EKBE', 'EKES', 'EKET', 'EKKN', 'EKKO', 'EKPA', 'EKPO', 'KONV', 'LFA1', 'LFB1', 'LFM1', 'MAKT', 'MARA', 'MARC', 'NAST', 'RBKP', 'RSEG', 'USR02', 'QALS', 'QAVE', 'MSEG', 'T006B')|||||
|DD03M|TABNAME IN ('BKPF', 'BSEG', 'CDHDR', 'CDPOS', 'EBAN', 'EBKN', 'EKBE', 'EKES', 'EKET', 'EKKN', 'EKKO', 'EKPA', 'EKPO', 'KONV', 'LFA1', 'LFB1', 'LFM1', 'MAKT', 'MARA', 'MARC', 'NAST', 'RBKP', 'RSEG', 'USR02', 'QALS', 'QAVE', 'MSEG', 'T006B')|||||
|DD07T||||||
|EBAN||EKPO|MANDT BANFN BNFPO |MANDT BANFN BNFPO |AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>`|
|||EKKO|MANDT EBELN |MANDT EBELN |BUKRS IN `<%=Company_Code%>`    |
|EBKN||EBAN|MANDT BANFN BNFPO |MANDT BANFN BNFPO ||
|||EKPO|MANDT BANFN BNFPO |MANDT BANFN BNFPO |AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>`|
|||EKKO|MANDT EBELN |MANDT EBELN |BUKRS IN `<%=Company_Code%>`|
|EKBE|CPUDT >= `<%=startDateDelta%>` AND CPUDT <= `<%=endDate%>`|||||
|EKES|ERDAT >= `<%=startDateDelta%>` AND ERDAT <= `<%=endDate%>`|||||
|EKET||EKKO|Use Primary Keys|Use Primary Keys|BUKRS IN `<%=Company_Code%>`  |
|||EKPO|MANDT EBELN |MANDT EBELN |AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>`|
|EKKN||EKPO|MANDT EBELN EBELP |MANDT EBELN EBELP |AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>`|
|||EKKO|MANDT EBELN |MANDT EBELN |BUKRS IN `<%=Company_Code%>`|
|EKKO|AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>`|||||
|EKPA||EKPO|MANDT EBELN |MANDT EBELN |AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>`|
|||EKKO|MANDT EBELN |MANDT EBELN |BUKRS IN `<%=Company_Code%>`|
|EKPO|AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>`|EKKO|Use Primary Keys|Use Primary Keys|BUKRS IN `<%=Company_Code%>`   |
|KONV||EKKO|MANDT KNUMV |MANDT KNUMV |BUKRS IN `<%=Company_Code%>`|
|||EKPO|MANDT EBELN |MANDT EBELN |(     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|LFA1||||||
|LFB1||||||
|LFM1||||||
|LIKP|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|||||
|LIPS|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|LIKP|Use Primary Keys|Use Primary Keys||
|LTAK|BDATU >= `<%=startDateDelta%>` AND BDATU <= `<%=endDate%>`|||||
|LTAP|QDATU >= `<%=startDateDelta%>` AND QDATU <= `<%=endDate%>` |||||
|MAKT||||||
|MARA||||||
|MARC||MARA|Use Primary Keys|Use Primary Keys||
|MARV||||||
|MKPF|(	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|||||
|MSEG|BUKRS IN `<%=Company_Code%>` AND ( EBELN <> ''  --OR --VBELN_IM <> '' )  |MKPF|Use Primary Keys|Use Primary Keys|(	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` ) |
|NAST|(	DATVR >= `<%=startDateDelta%>` AND  	DATVR <= `<%=endDate%>` ) |||||
|PRCD_ELEMENTS||EKKO|MANDT KNUMV |CLIENT KNUMV |BUKRS IN `<%=Company_Code%>`|
|||EKPO|MANDT EBELN |MANDT EBELN |  (  AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>`    )|
|PRPS||EKPO|MANDT DISUB_PSPNR |MANDT POSID |	AEDAT >= `<%=startDateDelta%>` AND   	AEDAT <= `<%=endDate%>` |
|||EKKO|MANDT EBELN |MANDT EBELN ||
|QALS|(	ENSTEHDAT >= `<%=startDateDelta%>` AND  	ENSTEHDAT <= `<%=endDate%>` ) OR (     AENDERDAT >= `<%=startDateDelta%>` AND     AENDERDAT <= `<%=endDate%>` )|T001W|MANDT WERKS |MANDANT WERK ||
|||T001K|MANDT BWKEY |MANDT BWKEY |BUKRS IN `<%=Company_Code%>`|
|QAMR|(	ERSTELLDAT >= `<%=startDateDelta%>` AND  	ERSTELLDAT <= `<%=endDate%>` ) OR (     AENDERDAT >= `<%=startDateDelta%>` AND     AENDERDAT <= `<%=endDate%>` )|QALS|Use Primary Keys|Use Primary Keys||
|||T001W|MANDT WERKS |MANDANT WERK ||
|||T001K|MANDT BWKEY |MANDT BWKEY |BUKRS IN `<%=Company_Code%>`|
|QAVE|(	VDATUM >= `<%=startDateDelta%>` AND  	VDATUM <= `<%=endDate%>` ) OR (     VAEDATUM >= `<%=startDateDelta%>` AND     VAEDATUM <= `<%=endDate%>` )|T001W|MANDT WERKS |MANDANT VWERKS ||
|||T001K|MANDT BWKEY |MANDT BWKEY |BUKRS IN `<%=Company_Code%>`|
|RBKP|BUKRS IN `<%=Company_Code%>`     	  AND  (	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>`)|||||
|RSEG||RBKP|Use Primary Keys|Use Primary Keys|BUKRS IN `<%=Company_Code%>`     	  AND  (	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` )|
|T001||||||
|T001B||||||
|T001L||||||
|T001W||||||
|T006B||||||
|T009B||||||
|T023T||||||
|T024||||||
|T024E||||||
|T161S||||||
|T161T||||||
|T163I||||||
|T163Y||||||
|T16FB||||||
|T16FS||||||
|T179T||||||
|T685T||||||
|TCURC||||||
|TCURV||||||
|TCURX||||||
|TVKO||||||
|USR02||||||
