import speedtest

def valuate_connection():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000
    upload_speed = st.upload() / 1000000

    return download_speed, upload_speed


