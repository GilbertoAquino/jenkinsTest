import argparse
from obspy.clients.fdsn import Client
from obspy import UTCDateTime, read_inventory, read
import os

parser = argparse.ArgumentParser()
parser.add_argument("--station",type=str)
parser.add_argument("--date",type=str)
parser.add_argument("--time",type=str)
parser.add_argument("--delta",type=str)
args=parser.parse_args()
print(args)
rs = Client('RASPISHAKE')
st= UTCDateTime(args.date+"T"+args.time)
if args.delta[3][len(args.delta[3])-1].lower() == 'h':
    end=st+60*60*float(args.delta[3][1:len(args.delta[3])-1])
elif args.delta[3][len(args.delta[3])-1].lower() == 'm':
    end=st+60*float(args.delta[3][1:len(args.delta[3])-1])
elif args.delta[3][len(args.delta[3])-1].lower() == 's':
    end=st+float(args.delta[3][1:len(args.delta[3])-1])
inv = rs.get_stations(station=args.station, sttime=st, endtime=end)
stream = rs.get_waveforms('AM', args.station, '00', '*', st, end)
stream.plot()