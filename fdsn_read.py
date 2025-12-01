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
# inv.plot()  # opcional: mapa/estaciones (abre ventana)

# 2) Descargar formas de onda
st = client.get_waveforms(
    network="IU",
    station="ANMO",
    location="00",
    channel="BHZ",
    starttime=t0,
    endtime=t1
)

print(st)
st.detrend("linear")
st.filter("bandpass", freqmin=0.5, freqmax=5.0)

# 3) Guardar miniSEED
st.write("waveform.mseed", format="MSEED")

# 4) (Opcional) quitar respuesta y convertir a velocidad (m/s)
st_corr = st.copy()
st_corr.remove_response(inventory=inv, output="VEL", pre_filt=(0.1, 0.2, 10, 12))
st_corr.write("waveform_vel.mseed", format="MSEED")
