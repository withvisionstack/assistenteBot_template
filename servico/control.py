import speedtest

def valuate_connection():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000
    upload_speed = st.upload() / 1000000

    return download_speed, upload_speed


if __name__ == "__main__":
    download_speed, upload_speed = valuate_connection()

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
