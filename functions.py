import yfinance as yf
from scipy.optimize import minimize
#Creo una función con 4 terminos para descargar los tickers solicitados
def Descargar_Acciones_IPC(ticker, fecha_inicio, fecha_fin, Progress):
    df = yf.download(ticker, start=fecha_inicio, end=fecha_fin, progress = Progress)
    return df
## Funciones y datos necesarios para resolver el problema de selección de portafolios

# Varianza
def var(w, Sigma):
    return np.dot(w.T, np.dot(Sigma, w))

# -Ratio de Sharpe
def minus_RS(w, rf, er, Sigma):
    erp = np.dot(w.T, er)
    sp = var(w, Sigma)**0.5
    RS = (erp - rf) / sp
    return -RS
