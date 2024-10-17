from constants import TOPIC_LIST

def topic_list_handle():
    i = 0
    if i < len(TOPIC_LIST):
        i += 1
        print(f"mudando topico para {TOPIC_LIST[i]}")
    elif i > len(TOPIC_LIST):
        i = 0
        print(f"mudando topico para {TOPIC_LIST[i]}")

    