
#!/usr/bin/env python3
import pyshark
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

import argparse
from datetime import datetime


"""
WebRTC 中的网络梯度延迟 OWDV(One Way Delay Variation)

abs_send_time_24 = (ntp_timestamp_64 >> 14) & 0x00ffffff ;
NTP timestamp is the number of seconds since the epoch, in 32.32 bit fixed point format.
It is 24 bit 6.18 fixed point,  yielding 64s wraparound and 3.8us resolution

int kAbsSendTimeFraction = 18;
int kAbsSendTimeInterArrivalUpshift = 8;
int kInterArrivalShift = RTPHeaderExtension::kAbsSendTimeFraction + kAbsSendTimeInterArrivalUpshift;
constexpr double kTimestampToMs = 1000.0 / static_cast<double>(1 << kInterArrivalShift);
uint32_t timestamp = send_time_24bits << kAbsSendTimeInterArrivalUpshift;
Timestamp send_time = Timestamp::Millis(static_cast<int64_t>(timestamp) * kTimestampToMs);

"""
# fraction part has 18 bits
kAbsSendTimeFraction = 18
kAbsSendTimeInterArrivalUpshift = 8
# after upshfit 8 bits, there are 26 bits for fraction
kInterArrivalShift = kAbsSendTimeFraction + kAbsSendTimeInterArrivalUpshift

kTimestampToMs = 1000.0 / (1 << kInterArrivalShift)


def send_time_to_ms(send_time_24bits):
    timestamp = send_time_24bits << kAbsSendTimeInterArrivalUpshift
    send_time = timestamp * kTimestampToMs
    return send_time


class RtpAnalyzer:

    def __init__(self, input_file, output_file):
        self._pcap_file = input_file
        self._csv_file = output_file

    def read_pcap(self, display_filter, count):

        dataList = []
        packets = pyshark.FileCapture(self._pcap_file, display_filter=display_filter)
        i = 0
        for packet in packets:
            dataItem = {}

            dataItem["arrival_time"] = datetime.fromtimestamp(float(packet.frame_info.time_epoch))
            dataItem["arrival_time_ms"] = float(packet.frame_info.time_epoch) * 1000
            dataItem["rtp_timestamp"] = int(packet.rtp.timestamp)
            dataItem["extseq"] = int(packet.rtp.extseq)
            dataItem["packet_size"] = int(packet.udp.length)

            if int(packet.rtp.ext_rfc5285_id) == 2:
                send_time_24bits = packet.rtp.ext_rfc5285_data.main_field.hex_value
                dataItem["abs_send_time"] = send_time_to_ms(send_time_24bits)

            dataList.append(dataItem)

            i += 1
            if i >= count:
                break

        dataFrame = pd.DataFrame(dataList)
        #print(dataFrame)
        return dataFrame

    def calculate_delta(self, df, row_interval=1):
        df["arrival_time_ms_diff"] = df["arrival_time_ms"].diff(periods=row_interval)
        df["send_time_diff"] = df["abs_send_time"].diff(periods=row_interval)
        df["OWDV"] = df["arrival_time_ms_diff"] - df["send_time_diff"]
        df["OWDV"] = df["OWDV"].abs()
        df = df[df['OWDV'] < 60]
        print(df)
        df.to_csv(self._csv_file)
        print(df["OWDV"].describe())

        print("* note: filter out OWDV if it > 60s because abs_send_time wrap around by 64s")
        return df

    def draw_chart(self, chart_file, df, x, y):
        plt.style.use('seaborn-v0_8-whitegrid')

        fig = plt.figure(figsize=(36, 18))
        font = {'size': 16}

        plt.plot(x, y, data=df)
        #plt.show()
        fig.savefig(chart_file)
        plt.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action='store', dest='input_file', help='specify input file')
    parser.add_argument('-o', action='store', dest='output_file', help='specify output file')
    parser.add_argument('-f', action='store', dest='filter', default="rtp", help='specify filter expression')
    parser.add_argument('-c', action='store', dest='count', default=10, help='specify packet count')
    args = parser.parse_args()

    if not args.input_file or not args.output_file or not args.output_file.endswith(".csv"):

        print("usage: ./rtp_analyze.py -i <pcap_file> -f <filter_expression>")
        print('such as: ./rtp_analyze.py -i /tmp/test_owdv.pcap -o "test_owdv.csv" -f "rtp.ssrc==0x8ab92fad" -c 100000')
        exit(0)

    rtpAnalyzer = RtpAnalyzer(args.input_file, args.output_file)

    df = rtpAnalyzer.read_pcap(args.filter, int(args.count))
    if not df.empty:
        df = rtpAnalyzer.calculate_delta(df)
        rtpAnalyzer.draw_chart("{}.png".format(args.output_file[:-4]), df, "arrival_time",  "OWDV")