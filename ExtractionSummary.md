## Extraction table List
|Table Name|Filter|Join (Parent) Table|Parent Columns|Child Columns|Join Filter
|----|----|----|----|----|----|
|ADRC||||||
|BKPF|BUKRS IN `<%=Company_Code%>`      	  AND (	   	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` ) AND AWTYP IN ('VBRK', 'MKPF', 'RMRP', 'BKPF')|||||
|BSEG||BKPF|Use Primary Keys|Use Primary Keys|BUKRS IN `<%=Company_Code%>`      	  AND (	   	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` ) AND AWTYP IN ('VBRK',  'MKPF',  'RMRP', 'BKPF')|
|CDHDR|OBJECTCLAS IN ('VERKBELEG', 'BELEG', 'KLIM', 'LIEFERUNG', 'TRANSPORT', 'BANF', 'KRED', 'EINKBELEG',  'DEBI',  'ADRESSE') AND (	   	UDATE >= `<%=startDateDelta%>` AND  	UDATE <= `<%=endDate%>` )|||||
|CDPOS||CDHDR|Use Primary Keys|Use Primary Keys|OBJECTCLAS IN ('VERKBELEG', 'BELEG', 'KLIM', 'LIEFERUNG', 'TRANSPORT', 'BANF', 'KRED', 'EINKBELEG',  'DEBI',  'ADRESSE') AND (	   	UDATE >= `<%=startDateDelta%>` AND  	UDATE <= `<%=endDate%>` )|
|DD02T|TABNAME IN ('BKPF', 'BSEG', 'CDHDR', 'CDPOS', 'EBAN', 'EBKN', 'EKBE', 'EKKN', 'EKES', 'EKET', 'EKKO', 'EKPA', 'EKPO', 'KNA1', 'KNB1', 'KNKK', 'KONV', 'LFA1', 'LFB1', 'LFM1', 'LIKP', 'LIPS', 'MAKT', 'MARA', 'MARC', 'MKPF', 'MSEG', 'NAST', 'PRPS', 'QALS', 'QAVE', 'RBKP', 'RSEG', 'T006B', 'TCURX', 'VBAK', 'VBAP', 'VBEP', 'VBFA', 'VBKD', 'VBPA', 'VBRK', 'VBRP', 'VEDA')|||||
|DD03M|TABNAME IN ('BKPF', 'BSEG', 'CDHDR', 'CDPOS', 'EBAN', 'EBKN', 'EKBE', 'EKKN', 'EKES', 'EKET', 'EKKO', 'EKPA', 'EKPO', 'KNA1', 'KNB1', 'KNKK', 'KONV', 'LFA1', 'LFB1', 'LFM1', 'LIKP', 'LIPS', 'MAKT', 'MARA', 'MARC', 'MKPF', 'MSEG', 'NAST', 'PRPS', 'QALS', 'QAVE', 'RBKP', 'RSEG', 'T006B', 'TCURX', 'VBAK', 'VBAP', 'VBEP', 'VBFA', 'VBKD', 'VBPA', 'VBRK', 'VBRP', 'VEDA')|||||
|DD07T||||||
|EBAN||EKPO|MANDT BANFN BNFPO |MANDT BANFN BNFPO |AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>` |
|||EKKO|Use Primary Keys|Use Primary Keys|BUKRS IN `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|EBKN||EBAN|Use Primary Keys|Use Primary Keys||
|||EKPO|MANDT BANFN BNFPO |MANDT BANFN BNFPO |AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>` |
|||EKKO|Use Primary Keys|Use Primary Keys|BUKRS IN `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|EKBE|CPUDT >= `<%=startDateDelta%>` AND CPUDT <= `<%=endDate%>` |EKKO|Use Primary Keys|Use Primary Keys|BUKRS IN `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|EKES|ERDAT >= `<%=startDateDelta%>` AND ERDAT <= `<%=endDate%>` |EKKO|Use Primary Keys|Use Primary Keys|BUKRS IN `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|EKET||EKPO|Use Primary Keys|Use Primary Keys|AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>` |
|||EKKO|Use Primary Keys|Use Primary Keys|BUKRS in `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|EKKN||EKPO|Use Primary Keys|Use Primary Keys|AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>` |
|||EKKO|Use Primary Keys|Use Primary Keys|BUKRS in `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|EKKO|BUKRS IN `<%=Company_Code%>`      	  AND  ( AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>` )|EKKN|MANDT EBELN |MANDT EBELN | |
|||VBAK|MANDT VBELN |MANDT VBELN ||
|EKPA||EKKO|MANDT EBELN |MANDT EBELN |BUKRS IN `<%=Company_Code%>`      	  AND  ( AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>`  )|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|EKPO|AEDAT >= `<%=startDateDelta%>` AND AEDAT <= `<%=endDate%>` |EKKO|Use Primary Keys|Use Primary Keys|BUKRS IN `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|FPLA||VBAP|MANDT VBELN |MANDT VBELN |(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|FPLT||FPLA|Use Primary Keys|Use Primary Keys||
|||VBAP|MANDT VBELN |MANDT VBELN |(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|JCDS|OBJNR LIKE 'VB%' AND (	UDATE >= `<%=startDateDelta%>` AND  	UDATE <= `<%=endDate%>` ) |||||
|KNA1||||||
|KNB1||||||
|KNKK||||||
|KNVV||||||
|KONV||VBAK|MANDT KNUMV |MANDT KNUMV ||
|||VBAP|MANDT VBELN |MANDT VBELN |(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|||VBAK|MANDT VBELN |MANDT VBELN ||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|LFA1||||||
|LFB1||||||
|LFM1||||||
|LIKP|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|LIPS|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|LIKP|Use Primary Keys|Use Primary Keys||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|LTAK|BDATU >= `<%=startDateDelta%>` AND BDATU <= `<%=endDate%>`|||||
|LTAP|QDATU >= `<%=startDateDelta%>` AND QDATU <= `<%=endDate%>`|||||
|MAKT||||||
|MARA||||||
|MARC||||||
|MARV||||||
|MKPF|(	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|||||
|MSEG|BUKRS IN `<%=Company_Code%>` AND ( EBELN <> '' OR VBELN_IM <> '' )|MKPF|Use Primary Keys|Use Primary Keys|(	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|NAST|(	DATVR >= `<%=startDateDelta%>` AND  	DATVR <= `<%=endDate%>` ) |||||
|PRCD_ELEMENTS||VBAK|MANDT KNUMV |CLIENT KNUMV ||
|||VBAP|MANDT VBELN |MANDT VBELN |(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|||VBAK|MANDT VBELN |MANDT VBELN ||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`	|
|PRPS||VBAP|MANDT PS_PSP_PNR |MANDT PSPNR |(	ERDAT >= `<%=startDateDelta%>` AND   	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|||VBAK|MANDT VBELN |MANDT VBELN ||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|QALS|(	ENSTEHDAT >= `<%=startDateDelta%>` AND  	ENSTEHDAT <= `<%=endDate%>` ) OR (     AENDERDAT >= `<%=startDateDelta%>` AND     AENDERDAT <= `<%=endDate%>` )|EKKO|MANDT EBELN |MANDANT EBELN |BUKRS IN `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|QAVE|(	VDATUM >= `<%=startDateDelta%>` AND  	VDATUM <= `<%=endDate%>` ) OR (     VAEDATUM >= `<%=startDateDelta%>` AND     VAEDATUM <= `<%=endDate%>` )|QALS|MANDANT PRUEFLOS |MANDANT PRUEFLOS |      |
|||EKKO|MANDT EBELN |MANDANT EBELN |BUKRS IN `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|RBKP|BUKRS IN `<%=Company_Code%>`   AND (	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` )|RSEG|MANDT BELNR GJAHR |MANDT BELNR GJAHR ||
|||EKKO|MANDT EBELN |MANDT EBELN ||
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|RSEG||RBKP|MANDT BELNR GJAHR |MANDT BELNR GJAHR |BUKRS IN `<%=Company_Code%>`   AND (	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` )|
|||RSEG|MANDT BELNR GJAHR |MANDT BELNR GJAHR ||
|||EKKO|MANDT EBELN |MANDT EBELN ||
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|T001||||||
|T001B||||||
|T001L||||||
|T001W||||||
|T006B||||||
|T009B||||||
|T014T||||||
|T023T||||||
|T024||||||
|T024B||||||
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
|TCURX||||||
|TJ02T||||||
|TSPAT||||||
|TSTCT||||||
|TVAGT||||||
|TVAK||||||
|TVAKT||||||
|TVAPT||||||
|TVAUT||||||
|TVFKT||||||
|TVFST||||||
|TVGRT||||||
|TVKBT||||||
|TVKMT||||||
|TVKO||||||
|TVKOT||||||
|TVLKT||||||
|TVLST||||||
|TVRO||||||
|TVSBT||||||
|TVSTT||||||
|TVTWT||||||
|USR02||||||
|VBAK|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|VBAP|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|VBAK|Use Primary Keys|Use Primary Keys||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|VBEP||VBAP|Use Primary Keys|Use Primary Keys|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|||VBAK|Use Primary Keys|Use Primary Keys||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|VBFA|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|VBAP|MANDT VBELN POSNR |MANDT VBELV POSNV ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|VBKD||VBAP|MANDT VBELN |MANDT VBELN |(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|||VBAK|Use Primary Keys|Use Primary Keys||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|VBPA||VBAP|MANDT VBELN |MANDT VBELN |(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|||VBAK|Use Primary Keys|Use Primary Keys||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|VBRK|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|VBRP|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` )|VBRK|Use Primary Keys|Use Primary Keys||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|VEDA||VBAK|Use Primary KeysMANDT VBELN |Use Primary Keys|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
|KONV (KONV_PO)||EKKO|MANDT KNUMV |MANDT KNUMV ||
|||EKPO|MANDT EBELN |MANDT EBELN |(     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|||EKKN|MANDT VBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|LIKP (LIKP_PO)|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|LIPS|MANDT VBELN |MANDT VBELN ||
|||EKKO|MANDT EBELN |MANDT VGBEL |BUKRS IN `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|LIPS (LIPS_PO)|(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|EKKO|MANDT EBELN |MANDT VGBEL |BUKRS IN `<%=Company_Code%>`|
|||EKKN|MANDT EBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|PRCD_ELEMENTS (PRCD_ELEMENTS_PO)||EKKO|MANDT KNUMV |CLIENT KNUMV |BUKRS IN `<%=Company_Code%>`|
|||EKPO|MANDT EBELN |MANDT EBELN |(     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|||EKKN|MANDT VBELN |MANDT EBELN ||
|||VBAK|MANDT VBELN |MANDT VBELN ||
|VBFA (VBFA_GI)|STUFE = 00|LIPS|MANDT VBELN POSNR |MANDT VBELV POSNV |(	ERDAT >= `<%=startDateDelta%>` AND  	ERDAT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|||LIKP|Use Primary Keys|Use Primary Keys||
|||TVKO|MANDT VKORG |MANDT VKORG |BUKRS IN `<%=Company_Code%>`|
