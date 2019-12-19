import application
from qgroundcontrol import QGroundControl
import toolbar
import main_menu
import analyze


def main():
    application.start()
    QGroundControl.set_window_size(950, 550)
    toolbar.open_main_menu()
    main_menu.open_analyze()
    analyze.AnalyzeMenu.open_mavlink_inspector()
    test.compare(
        analyze.MavLinkInspector.get_header(),
        "Inspect real time MAVLink messages.",
        'The header message should be "Inspect real time MAVLink messages"',
    )

    snooze(5)  # Are 5s enough? Missing indicator for loading all the menu items

    menu_width = analyze.MavLinkInspector.get_menu_witdh()

    for message in analyze.MavLinkInspector.get_message_buttons_texts():
        test.compare(
            analyze.MavLinkInspector.get_menu_elem_width(message),
            menu_width,
            f"{message} button width should be {menu_width}",
        )
        menu_elem_height = analyze.MavLinkInspector.get_menu_elem_height(message)
        analyze.MavLinkInspector.scroll_menu(menu_elem_height)
        print("Asad")
