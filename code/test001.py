def hello_world():
    print("""
    序列号与字体的对应关系：
    1：Big-Money-ne
    2:Big
    3:Cards
    4:Doom
    5:Ogre
    """)
    msg = int(input('请输入序列号:\n'))
    if msg == 1:
        print("""
         /$$   /$$           /$$ /$$                                                   /$$       /$$ /$$
        | $$  | $$          | $$| $$                                                  | $$      | $$| $$
        | $$  | $$  /$$$$$$ | $$| $$  /$$$$$$        /$$  /$$  /$$  /$$$$$$   /$$$$$$ | $$  /$$$$$$$| $$
        | $$$$$$$$ /$$__  $$| $$| $$ /$$__  $$      | $$ | $$ | $$ /$$__  $$ /$$__  $$| $$ /$$__  $$| $$
        | $$__  $$| $$$$$$$$| $$| $$| $$  \ $$      | $$ | $$ | $$| $$  \ $$| $$  \__/| $$| $$  | $$|__/
        | $$  | $$| $$_____/| $$| $$| $$  | $$      | $$ | $$ | $$| $$  | $$| $$      | $$| $$  | $$    
        | $$  | $$|  $$$$$$$| $$| $$|  $$$$$$/      |  $$$$$/$$$$/|  $$$$$$/| $$      | $$|  $$$$$$$ /$$
        |__/  |__/ \_______/|__/|__/ \______/        \_____/\___/  \______/ |__/      |__/ \_______/|__/
        """)
    if msg == 2:
        print("""
          _    _      _ _                            _     _ _ 
         | |  | |    | | |                          | |   | | |
         | |__| | ___| | | ___   __      _____  _ __| | __| | |
         |  __  |/ _ \ | |/ _ \  \ \ /\ / / _ \| '__| |/ _` | |
         | |  | |  __/ | | (_) |  \ V  V / (_) | |  | | (_| |_|
         |_|  |_|\___|_|_|\___/    \_/\_/ \___/|_|  |_|\__,_(_)
        """)
    if msg == 3:
        print("""
        .------..------..------..------..------.     .------..------..------..------..------..------.
        |H.--. ||E.--. ||L.--. ||L.--. ||O.--. |.-.  |W.--. ||O.--. ||R.--. ||L.--. ||D.--. ||!.--. |
        | :/\: || (\/) || :/\: || :/\: || :/\: ((5)) | :/\: || :/\: || :(): || :/\: || :/\: || (\/) |
        | (__) || :\/: || (__) || (__) || :\/: |'-.-.| :\/: || :\/: || ()() || (__) || (__) || :\/: |
        | '--'H|| '--'E|| '--'L|| '--'L|| '--'O| ((1)) '--'W|| '--'O|| '--'R|| '--'L|| '--'D|| '--'!|
        `------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'`------'`------'
        """)
    if msg == 4:
        print("""
         _   _      _ _                            _     _ _ 
        | | | |    | | |                          | |   | | |
        | |_| | ___| | | ___   __      _____  _ __| | __| | |
        |  _  |/ _ \ | |/ _ \  \ \ /\ / / _ \| '__| |/ _` | |
        | | | |  __/ | | (_) |  \ V  V / (_) | |  | | (_| |_|
        \_| |_/\___|_|_|\___/    \_/\_/ \___/|_|  |_|\__,_(_)                                         
        """)
    if msg == 5:
        print("""
                    _ _                            _     _   _ 
          /\  /\___| | | ___   __      _____  _ __| | __| | / \
         / /_/ / _ \ | |/ _ \  \ \ /\ / / _ \| '__| |/ _` |/  /
        / __  /  __/ | | (_) |  \ V  V / (_) | |  | | (_| /\_/ 
        \/ /_/ \___|_|_|\___/    \_/\_/ \___/|_|  |_|\__,_\/   
        """)
    else:
        print("请输入1~5的序列号！")
hello_world()