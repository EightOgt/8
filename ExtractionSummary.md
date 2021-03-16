## Extraction table List
|Table Name|Filter|Join (Parent) Table|Parent Columns|Child Columns|Join Filter
|----|----|----|----|----|----|
|BKPF|(	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|||||
|BSEC||BKPF|MANDT BUKRS BELNR GJAHR |MANDT BUKRS BELNR GJAHR | (	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|BSEG||BKPF|MANDT BUKRS BELNR GJAHR |MANDT BUKRS BELNR GJAHR |(	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|BSET||BKPF|MANDT BUKRS BELNR GJAHR |MANDT BUKRS BELNR GJAHR | (	CPUDT >= `<%=startDateDelta%>` AND  	CPUDT <= `<%=endDate%>` ) OR (     AEDAT >= `<%=startDateDelta%>` AND     AEDAT <= `<%=endDate%>` )|
|CDHDR| OBJECTCLAS = 'BELEG' AND (	   	UDATE >= `<%=startDateDelta%>` AND  	UDATE <= `<%=endDate%>` )|||||
|CDPOS||CDHDR|MANDANT OBJECTCLAS OBJECTID CHANGENR |MANDANT OBJECTCLAS OBJECTID CHANGENR | OBJECTCLAS = 'BELEG' AND (	   	UDATE >= `<%=startDateDelta%>` AND  	UDATE <= `<%=endDate%>` )|
|KNA1||||||
|LFA1||||||
|MARV||||||
|SKA1||||||
|SKB1||||||
|T001||||||
|T001B||||||
|T001W||||||
|T003T||||||
|T009B||||||
|T040T||||||
|TCURC||||||
|TCURX||||||
|TKA01||||||
|USR02||||||
|WITH_ITEM||||||
