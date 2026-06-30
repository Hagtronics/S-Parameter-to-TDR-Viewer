#!/usr/bin/python3
"""
sparam_to_tdr_viewer

TDR Viewer

UI source file: sparam_to_tdr.ui
"""
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu


class sparam_to_tdrUI:
    def __init__(
        self,
        master=None,
        *,
        project_ui,
        resource_paths=None,
        translator=None,
        on_first_object_cb=None,
        data_pool=None,
    ):
        self.builder = pygubu.Builder(
            translator=translator,
            on_first_object=on_first_object_cb,
            data_pool=data_pool
        )
        self.builder.add_from_file(project_ui)
        if resource_paths is not None:
            self.builder.add_resource_paths(resource_paths)
        # Main widget
        self.mainwindow: tk.Toplevel = self.builder.get_object(
            "main_window", master)

        self.v_infile: tk.StringVar = None
        self.v_infile_props: tk.StringVar = None
        self.v_tdr_type: tk.StringVar = None
        self.v_tdr_window: tk.StringVar = None
        self.v_tdr_padding: tk.StringVar = None
        self.v_spar_response: tk.StringVar = None
        self.v_cbox_show_tdr: tk.StringVar = None
        self.v_tdr_gate_start: tk.StringVar = None
        self.v_tdr_gate_stop: tk.StringVar = None
        self.v_tdr_gating: tk.StringVar = None
        self.builder.import_variables(self)

    def center_window(self):
        if self.mainwindow.winfo_ismapped():
            min_w, min_h = self.mainwindow.wm_minsize()
            max_w, max_h = self.mainwindow.wm_maxsize()
            screen_w = self.mainwindow.winfo_screenwidth()
            screen_h = self.mainwindow.winfo_screenheight()
            final_w = min(
                screen_w,
                max_w,
                max(
                    min_w,
                    self.mainwindow.winfo_width(),
                    self.mainwindow.winfo_reqwidth(),
                ),
            )
            final_h = min(
                screen_h,
                max_h,
                max(
                    min_h,
                    self.mainwindow.winfo_height(),
                    self.mainwindow.winfo_reqheight(),
                ),
            )
            x = (screen_w // 2) - (final_w // 2)
            y = (screen_h // 2) - (final_h // 2)
            geometry = f"{final_w}x{final_h}+{x}+{y}"

            def set_geometry():
                self.mainwindow.geometry(geometry)

            self.mainwindow.after_idle(set_geometry)
        else:
            # Window is not mapped, wait and try again later.
            self.mainwindow.after(5, self.center_window)

    def run(self, center=False):
        if center:
            self.center_window()
        self.mainwindow.mainloop()

    def process_files(self):
        pass

    def rad_tdr_type_changed(self):
        pass

    def sb_tdr_padding_changed(self):
        pass

    def rad_spar_changed(self):
        pass

    def cb_show_gated_response_changed(self):
        pass

    def tdr_start_time_changed(self, scale_value):
        pass

    def tdr_stop_time_changed(self, scale_value):
        pass

    def cb_enable_gating_changed(self):
        pass
