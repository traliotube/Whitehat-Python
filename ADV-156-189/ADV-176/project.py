import speedtest
import time
import matplotlib.pyplot as plt


listDownload = []
listUpload = []
listX = [1, 2, 3, 4, 5]

for i in range(0, 5):
    sp = speedtest.Speedtest()
    listDownload.append(round(sp.download()/1000000, 2))
    listUpload.append(round(sp.upload()/1000000, 2))
    print(f"Download: {listDownload}. Upload: {listUpload}")
    time.sleep(1)

plt.plot(listX, listDownload, label="Download Speed")
plt.plot(listX, listUpload, label="Upload Speed")
plt.title("Internet Speed Test")
plt.legend()
plt.show()
