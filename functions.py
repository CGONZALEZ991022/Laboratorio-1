import yfinance as yf
#Creo una función con 4 terminos para descargar los tickers solicitados
def Descargar_Acciones_IPC(ticker, fecha_inicio, fecha_fin, Progress):
    df = yf.download(ticker, start=fecha_inicio, end=fecha_fin, progress = Progress)
    return df