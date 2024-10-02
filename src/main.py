import speedtest as st

def down_speed_test():
    test = st.Speedtest()

    down_speed = test.download()
    calculated_down_speed = round(down_speed / 10**6, 2)

    ping = test.results.ping

    result = {
        "downSpeed": calculated_down_speed,
        "ping": ping
    }

    return result

def up_speed_test():
    test = st.Speedtest()

    up_speed = test.upload()
    calculated_up_speed = round(up_speed / 10**6, 2)

    ping = test.results.ping

    result = {
        "upSpeed": calculated_up_speed,
        "ping": ping
    }

    return result

down_speed = down_speed_test()
up_speed = up_speed_test()

print("Download speed in Mbps: {0} - Pings: {1}".format(
    down_speed["downSpeed"],
    down_speed["ping"])
    )
print("Updownload speed in Mbps: {0} - Pings: {1}".format(
    up_speed["upSpeed"],
    up_speed["ping"])
    )
