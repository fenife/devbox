from nicegui import ui
import shell
from engine import ShellResult

# log = ui.log(max_lines=100).classes('w-full h-300 w-300')

def to_label(r: ShellResult):
    ui.label(r.pwd)
    ui.label(r.cmd)
    output = r.output
    if isinstance(output, str):
        ui.label(output)
    if isinstance(output, (list, tuple)):
        for s in output:
            ui.label(s)

_log = None
def get_log_ui():
    global _log
    if not _log:
        _log = ui.log(max_lines=1000).classes('w-full h-500 w-500')
    return _log

def to_log(r: ShellResult):
    global _log
    _log.push(r.output)

# def to_code(r: ShellResult):
#     ui.code(r.output).classes('w-full')

def show(r: ShellResult):
    # to_code(r)
    to_log(r)

def ls_current_dir():
    result = shell.ls_current()
    show(result)


def net_entry():
    with ui.card().classes('w-full h-1000'):
        with ui.splitter().classes("w-full h-5000 w-200") as splitter:
            with splitter.before:
                ui.label('Card content')
                ui.button('Add label', on_click=ls_current_dir)

            with splitter.after:
                # log = ui.log(max_lines=100).classes('w-full h-100 w-100')
                log = get_log_ui()
            
        
        
# log = ui.log(max_lines=100).classes('w-full h-100 w-100')
