import requests


API = "https://ip.v2too.top/api/nodes"


def main():

    r = requests.get(
        API,
        timeout=10
    )

    nodes = r.json()


    result = []

    for n in nodes:

        if (
            n.get("ip")
            and n.get("region")
            and n.get("latency") is not None
            and n.get("speed") is not None
            and n.get("time")
            and n.get("carrier")
        ):

            result.append(
                f"{n['ip']}#[{n['region']} {n['latency']} {n['speed']} {n['carrier']} {n['time']}]"
            )


    # 按速度降序
    result.sort(
        key=lambda x: float(x.split()[2]),
        reverse=True
    )


    with open(
        "nodes.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "\n".join(result)
        )


if __name__ == "__main__":
    main()
