import wave
def hide():
    song = wave.open("audio.wav", mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    with open("cipher.txt","r") as f:
        string=f.read()
    string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)
    with wave.open('output.wav', 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close() 
def extract():
    song = wave.open("output.wav", mode='rb')
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    decoded = string.split("###")[0]
    with open("after.txt","w") as f:
        f.write(decoded)
    song.close()
def menu():
    print("")
    print("")
    print("1. EMBED INTO AUDIO FILE")
    print("2. EXTRACT FROM THE AUDIO")
    print("")
    print("")
    n=int(input())
    if n==1:
        hide()
    elif n==2:
        extract()
menu()