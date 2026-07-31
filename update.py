import requests
import re


API = "https://ip.v2too.top/api/nodes"

CF_IP_URL = "https://raw.githubusercontent.com/yuanxiawan/cfipv4db/refs/heads/main/high_score_ips.txt"


def update_nodes():

    r = requests.get(
        API,
        timeout=10
    )

    r.raise_for_status()

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



def update_cf_ips():

    r = requests.get(
        CF_IP_URL,
        timeout=10
    )

    r.raise_for_status()


    lines = r.text.splitlines()


    result = []


    for line in lines:

        # 去掉 # 前面的空格
        line = re.sub(
            r"\s+#",
            "#",
            line
        )

        # 删除行尾空格
        line = line.rstrip()


        if line:
            result.append(line)


    with open(
        "ips.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "\n".join(result)
        )



def main():

    update_nodes()

    update_cf_ips()



if __name__ == "__main__":
    main()
