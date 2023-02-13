import Data
#Tickers que se utilizaran para este 
Tickers_Mx = ["AMXL.MX", "WALMEX.MX", "GMEXICOB.MX", "FEMSAUBD.MX", "GFNORTEO.MX", "CEMEXCPO.MX"
            , "GAPB.MX", "ELEKTRA.MX", "TLEVISACPO.MX", "ASURB.MX", "BIMBOA.MX", "KIMBERA.MX"
            , "KOFUBL.MX", "GRUMAB.MX", "ORBIA.MX", "OMAB.MX", "AC.MX", "GFINBURO.MX"
            , "PE&OLES.MX", "ALFAA.MX", "PINFRA.MX", "CUERVO.MX", "GCARSOA1.MX", "MEGACPO.MX"
            , "BOLSAA.MX", "VESTA.MX", "GCC.MX", "Q.MX", "BBAJIOO.MX", "LIVEPOLC-1.MX", "ALSEA.MX"]
Mexico = Data.Descargar_Acciones_IPC(Tickers_Mx, "2021-01-31", "2023-01-25", False)["Adj Close"]