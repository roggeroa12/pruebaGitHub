from obspy.clients.fdsn import Client
from obspy import UTCDateTime

# Puedes usar "IRIS", "USGS", "EMSC", "RESIF", etc. (depende qué tengas disponible)
client = Client("IRIS")

# Ventana de tiempo
t0 = UTCDateTime("2020-01-01T00:00:00")
t1 = t0 + 60  # 60 segundos

# 1) Descubrir estaciones/canales (metadata)
inv = client.get_stations(
    network="IU",
    station="ANMO",
    location="00",
    channel="BH?",
    starttime=t0,
    endtime=t1,
    level="response"   # incluye respuesta instrumental
)

print(inv)  # resumen