import dearpygui.dearpygui as dpg
from dearpygui.demo import show_demo

dpg.create_context()

def callback(sender, app_data):
    print("Sender: ", sender)
    print("App Data: ", app_data)

dpg.add_file_dialog(directory_selector=True, show=False, callback=callback, tag="file_dialog_id")

with dpg.window(label="Tutorial", width=800, height=300):
    dpg.add_button(label="Directory Selector", callback=lambda: dpg.show_item("file_dialog_id"))

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()