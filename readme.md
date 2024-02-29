`nokia_ont_pwgen.py` - Standalone version of password generator. It can be used in [Nokia G-010G-T](https://hack-gpon.org/ont-nokia-g-010g-t/) and probably other ONTs based on [CIG G-97CP](https://hack-gpon.org/ont-cig-g-97cp/) device.


### Change settings through Telnet instead of Uart

- Connect ONT with PC though Ethernet cable
- Disable ONT power
- Push and hold RESET button on ONT
- Enable ONT while holding RESET 
- Wait exactly 10s then leave RESET button
- Wait while ONT system boots
- Connect through telnet to address `10.89.89.163` with user `ONTUSER` and password generated
- If IP address is unreachable try also `10.89.39.124`
