from config import API_ID, API_HASH, SESSIONS
from pyrogram import Client, idle


def load_plugins(plugin_name):
    path = Path(f"TheXSpam/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"TheXSpam{plugin_name}", path
    sys.TheXSpam["TheXSpam." + plugin_name] = load
    print("King X spam   has Imported " + plugin_name)


if __name__ == "__main__":

    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("SAIFHELPGC")
            CLIENT.join_chat("SAIFALLBOT")
            print(f"---> Client {i+1} has been Started...")
        except Exception as e:
            print(e)

    print("💞 YOUR SAIF USER-BOTDEPLOYED SUCCESSFULLY 💞")
    idle()
