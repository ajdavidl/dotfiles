from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from os import listdir
from random import sample

import colors

mbfs = colors.mbfs()
doomOne = colors.doomOne()
dracula = colors.dracula()
everforest = colors.everforest()
nord = colors.nord()
gruvbox = colors.gruvbox()


#Choose colorscheme
colorscheme = doomOne

#Colorschme funcstion
colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo = colorscheme


image_path = "/home/usuario/Imagens/dark_wallpapers/"
lista_wallpapers = listdir(image_path)
wallpaper_path1 = image_path+sample(lista_wallpapers, k = 1)[0]
wallpaper_path2 = image_path+sample(lista_wallpapers, k = 1)[0]


#import subprocess
#subprocess.call(['display', '-window', 'root', '/home/usuario/Imagens/dark-wallpaper-23.jpg'])

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod],"comma", lazy.to_screen(0), desc = "Focus to monitor 0"),
    Key([mod],"period", lazy.to_screen(1), desc = "Focus to monitor 1"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "F11", lazy.spawn("alacritty -e xrandr --output eDP1 --brightness 0.5")),
    Key([mod], "F12", lazy.spawn("alacritty -e xrandr --output eDP1 --brightness 1")),
    
    # Start apps
    Key([mod], "q", lazy.spawn("alacritty -e vim .config/qtile/config.py")),
    Key([mod], "w", lazy.spawn('alacritty -e curl wttr.in ; sleep 1200')),
    Key([mod], "e", lazy.spawn("dolphin")),
	Key([mod, "shift"], "e", lazy.spawn("alacritty -e ranger")),
    Key([mod], "r", lazy.spawn("rstudio-bin")),
	Key([mod, "shift"], "r", lazy.spawn("alacritty -e R")),
	Key([mod], "t", lazy.spawn("alacritty -e /home/usuario/Documentos/tor-browser_en-US/Browser/start-tor-browser")),
    #Key([mod], "y", lazy.spawn("")),
    Key([mod], "u", lazy.spawn("alacritty -e sudo pacman -Syu")),
    Key([mod], "i", lazy.spawn("alacritty -e system-config-printer")),
    Key([mod], "o", lazy.spawn("libreoffice")),
    Key([mod], "p", lazy.spawn("alacritty -e ipython")),
    Key([mod, "shift"], "p", lazy.spawn("alacritty -e python")),
    Key([mod], "a", lazy.spawn("emacs")),
    Key([mod], "s", lazy.spawn("alacritty -e setxkbmap -model abnt -layout us -variant intl")),
    Key([mod, "shift"], "s", lazy.spawn("alacritty -e setxkbmap -model abnt -layout brmine -variant hall2")),
    Key([mod], "d", lazy.spawn("alacritty -e setxkbmap -model abnt -layout br -variant dvorak")),
    Key([mod, "shift"], "d", lazy.spawn("alacritty -e setxkbmap -model abnt -layout us -variant dvorak")),
    Key([mod], "f", lazy.spawn("firefox")),
	Key([mod], "g", lazy.spawn("chromium")),
	Key([mod], "h", lazy.spawn("alacritty -e htop")),
	Key([mod], "j", lazy.spawn("alacritty -e jupyter lab")),
	Key([mod, "shift"], "j", lazy.spawn("alacritty -e julia")),
	Key([mod], "k", lazy.spawn("alacritty -e keepass")),
	Key([mod], "l", lazy.spawn("xscreensaver-command -lock")),
	Key([mod,"shift"], "l", lazy.spawn("xscreensaver -no-splash")),
	#Key([mod, "shift"], "x", lazy.spawn("alacritty -e sudo xmrig")),
	Key([mod], "x", lazy.spawn("xterm")),
    Key([mod], "c", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #Key([mod, "shift"], "c", lazy.spawn("alacritty -e cal -y ; sleep 1200")),
	Key([mod, "shift"], "c", lazy.spawn("alacritty -e calibre")),
    Key([mod], "v", lazy.spawn("vscodium")),
	Key([mod], "b", lazy.spawn("brave")),
	Key([mod], "n", lazy.spawn("notepadqq")),
	Key([mod, "shift"], "n", lazy.spawn("kwrite")),
	Key([mod], "m", lazy.spawn("alacritty -e xrandr --output eDP1 --auto --output HDMI-1-0 --auto --right-of eDP1")),
    Key([mod], "z", lazy.spawn("vlc")),

# Change the volume if your keyboard has special volume keys.
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5dB")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5dB")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    
    #Rofi
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show run"), desc = "Launch primary launcher"),

]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('terminal', "alacritty", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('text_editor', "alacritty -e vim", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('file_manager', "alacritty -e ranger", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('process_viewer', "alacritty -e htop", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key([mod, "control"], "Return", lazy.group['scratchpad'].dropdown_toggle('terminal')),
    Key([mod, "control"], "v", lazy.group['scratchpad'].dropdown_toggle('text_editor')),
    Key([mod, "control"], "e", lazy.group['scratchpad'].dropdown_toggle('file_manager')),
    Key([mod, "control"], "h", lazy.group['scratchpad'].dropdown_toggle('process_viewer')),
])  


layouts = [
    layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", foregroundColor),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayout(
                       foreground = foregroundColor,
                       background = backgroundColor,
                       padding = 5),
                widget.TextBox(text = '',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37),
                widget.TextBox("Comandos: &lt;M-c&gt;", foreground=foregroundColor),
                widget.Systray(),
                widget.TextBox(
                       text = '',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37),
				widget.Net(interface = "enp59s0",
                    format = '{down} ↓↑ {up}',
                    foreground = foregroundColor,
                    background = backgroundColor,
                    padding = 5),
				widget.TextBox(
                       text='',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " ⟳",
                       padding = 2,
                       foreground = foregroundColor,
                       background = backgroundColor,
                       fontsize = 14
                       ),
              widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "{updates} Updates",
                       foreground = foregroundColor,
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e sudo pacman -Syu')},
                       background = backgroundColor
                       ),
              widget.TextBox(
                       text = '',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = foregroundColor,
                       background = backgroundColor,
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = foregroundColor,
                       background = backgroundColor,
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CPU(
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 0",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 1",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 2",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 3",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 4",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 5",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ), 
              widget.TextBox(
                       text = '',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Battery(
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.TextBox(
                       text='',
                       foreground = foregroundColor,
                       background = backgroundColor,
                       padding = 0,
                       fontsize = 37
                       ),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
        ),
        wallpaper = wallpaper_path1,
		wallpaper_mode = "fill",

    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", foregroundColor),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayout(
                       foreground = foregroundColor,
                       background = backgroundColor,
                       padding = 5),
                widget.TextBox(text = '',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37),
                widget.TextBox("Comandos: &lt;M-c&gt;", foreground=foregroundColor),
                widget.TextBox(
                       text = '',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37),
				widget.Net(interface = "enp59s0",
                    format = '{down} ↓↑ {up}',
                    foreground = foregroundColor,
                    background = backgroundColor,
                    padding = 5),
				widget.TextBox(
                       text='',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = foregroundColor,
                       background = backgroundColor,
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = foregroundColor,
                       background = backgroundColor,
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e htop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CPU(
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 0",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 1",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 2",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 3",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 4",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.ThermalSensor(
                       tag_sensor = "Core 5",
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ), 
              widget.TextBox(
                       text = '',
                       background = foregroundColor,
                       foreground = backgroundColor,
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Battery(
                       foreground = foregroundColor,
                       background = backgroundColor 
                      ),
              widget.TextBox(
                       text='',
                       foreground = foregroundColor,
                       background = backgroundColor,
                       padding = 0,
                       fontsize = 37
                       ),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
         ),
       wallpaper = wallpaper_path2,
	   wallpaper_mode = "fill",
     ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
