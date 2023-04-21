import argparse
from obspy.clients.fdsn import Client
from obspy import UTCDateTime, read_inventory, read
from obspy import read
from subprocess import run
import os

parser = argparse.ArgumentParser()
parser.add_argument("--station",type=str)
parser.add_argument("--date",type=str)
parser.add_argument("--time",type=str)
parser.add_argument("--delta",type=str)
args=parser.parse_args()
print(args)
st = UTCDateTime(args.date+"T"+args.time)
sdt = st.datetime.strftime("%Y-%m-%dT%H:%M:%S")
if args.delta[-1].lower() == 'h':
    end=st+60*60*float(args.delta[:len(args.delta)-1])
elif args.delta[-1].lower() == 'm':
    end=st+60*float(args.delta[:len(args.delta)-1])
elif args.delta[-1].lower() == 's':
    end=st+float(args.delta[:len(args.delta)-1])
end = end.datetime.strftime("%Y-%m-%dT%H:%M:%S")
rs = f"'https://data.raspberryshake.org/fdsnws/dataselect/1/query?net=AM&sta={args.station}&loc=00&cha=*&start={st}&end={end}'"
try:
    run(["wget", rs,"-O", "data.mseed"],check=True)
except:
    run(["powershell","wget", rs,"-O", "data.mseed"],check=True)
stream = read("data.mseed")
stream.plot()
#inv = rs.get_stations(station=args.station, sttime=st, endtime=end)
#stream = rs.get_waveforms('AM', args.station, '00', '*', st, end)
#stream.plot()
