import nacos
from nacos.listener import SubscribeListener

# Both HTTP/HTTPS protocols are supported, if not set protocol prefix default is HTTP, and HTTPS with no ssl check(verify=False)
# "192.168.3.4:8848" or "https://192.168.3.4:443" or "http://192.168.3.4:8848,192.168.3.5:8848" or "https://192.168.3.4:443,https://192.168.3.5:443"
SERVER_ADDRESSES = "10.4.0.210"
# SERVER_ADDRESSES = "127.0.0.1:8848"

# no auth mode
client = nacos.NacosClient(SERVER_ADDRESSES)
client.namespace = "bd0d4a55-cfe0-44bb-ad0e-1d50d1b57ada"

# auth mode
# client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, ak="{ak}", sk="{sk}")


print(client.add_naming_instance("ComfyUIPromptGen", "172.15.0.202", "8188", metadata={"route": "/prompt"}, healthy=False,
                                 ephemeral=False))

# print(client.add_naming_instance("TTSGen", "172.15.0.202", "5001", metadata={"route": "/"}, healthy=False,
#                                  ephemeral=False))
#
# print(client.add_naming_instance("TTSGen", "172.15.0.202", "5002", metadata={"route": "/"}, healthy=False,
#                                  ephemeral=False))
#
# print(client.add_naming_instance("TTSGen", "172.15.0.202", "5003", metadata={"route": "/"}, healthy=False,
#                                  ephemeral=False))
#
# print(client.add_naming_instance("TTSGen", "172.15.0.202", "5004", metadata={"route": "/"}, healthy=False,
#                                  ephemeral=False))
# print(client.remove_naming_instance("ComfyUIPromptGen", "172.15.0.202", "8188", None,False))
# data = client.list_naming_instance("tts")
# print(data["hosts"])

# def func(event, instance):
#     print(event, instance)
#     print("1111")
#
#
# fn1 = SubscribeListener(fn=func, listener_name="tts_listener")
#
# client.subscribe(fn1, 5, service_name="tts")
