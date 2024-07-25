from speedtest import Speedtest  # pip install speedtest-cli

st = Speedtest()

print("Download Speed:", st.download())
print("Upload Speed:", st.upload())
