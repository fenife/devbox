from nicegui import ui
from net import net_entry

net_entry()

ui.run(host="0.0.0.0", port=8010)
