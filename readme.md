## Enso Portable

A fork of [GChristensen's portable distribution](https://github.com/GChristensen/enso-portable) of the *community* version of Humanized Enso Launcher for Windows (with additional commands and functionality).

---

<img src="https://raw.githubusercontent.com/thdoan/enso-portable/master/screen.jpg">

#### Description

Enso is a GUI-less application launcher that is both influenced by and dedicated in memory of [Jef Raskin](http://en.wikipedia.org/wiki/Jef_Raskin), the father of the Apple Macintosh project. It incorporates many ideas about human-computer interfaces from Jef's book, [The Humane Interface](http://en.wikipedia.org/wiki/The_Humane_Interface). In fact, Enso's original developer, Humanized, was led by Jef's son [Aza Raskin](http://www.azarask.in/blog/post/enso_beta_hints_1/).

Enso allows you to launch programs found in the Windows Start Menu (or picked manually using the `learn as open` command), and perform many other operations from the command line triggered by pressing the Caps Lock key. It's possible to extend Enso and easily create your own commands using the Python (version 2.5) programming language.

#### Installation

1. Click 'Clone in Desktop' button or type `git clone https://github.com/thdoan/enso-portable.git` from the command line. If you don't have Git installed, then click the 'Download ZIP' button, extract the 'enso-portable-master' folder to anywhere on your hard drive (it's portable after all), and rename it to 'enso-portable'.
2. Download [python.7z](http://thdoan.github.io/enso-portable/downloads/python.7z) and extract the contents to the 'enso-portable\enso\python' folder (you'll need to install [7-Zip](http://www.7-zip.org/7z.html) first).
3. Double-click on 'enso-portable\enso\run-enso.exe' to launch Enso.

#### Notes

- There is no need to hold down the Caps Lock key as in the original version (you only need to hit it once; this setting can be adjusted in the 'enso-portable\enso\enso\config.py' file).
- Use the `help` command to get the list of available commands.
- To add a new command, you need to create a Python file (*.py) with its source code in the 'enso-portable\enso\commands' folder (you can use [text_tools.py](https://github.com/thdoan/enso-portable/blob/master/enso/commands/text_tools.py) as a template; see the [docs](https://github.com/thdoan/enso-portable/blob/master/enso/docs/enso-docs.txt) for more info).
- If you have no need for a command, you can turn it off by moving it to the 'enso-portable\enso\commands_OFF' folder. This way you do not pollute the suggestions list with commands that you will never use.

#### Background

GChristensen: I haven't found any Enso command package suitable for my needs, so I decided to make my own one. If you like Enso, you can use the source code freely as you wish.

#### Additional Functionality (not found in the original Enso)

- Ability to restart using a tray menu item or the `enso restart` command (GChristensen)
- Ability to enter all standard symbols in quasimode (thdoan)
- Ability to enter numbers and symbols using the keypad (thdoan)

#### Additional Commands

- **session.py** - Session/Power management commands (self-explanatory):

	* `log off`
	* `shut down`
	* `reboot`
	* `suspend`
	* `hibernate`

- **system.py** - System commands:

	* `kill [process name or ID]` - kill a process using its executable name (without extension) or ID

- **dial.py** - Dial-up network related commands:

	* `dial [connection name]` - connect to the Internet using a dial-up connection
	* `hangup [connection name]` - close an Internet connection

- **idgen.py** - Commands to generate ID strings:

	* `guid [format]` - generate a UUID in several formats (upper/lower case, numeric)
	* `random [from num to num]` - generate a random number in the Int32 positive range [0-2147483646]

- **lingvo.py** - Control ABBYY Lingvo dictionary software. It's possible to specify translation direction (see command help for details).

	* `lingvo [word from lang to lang]` - translate a word
	* `quit lingvo` - close Lingvo

- **mount.py** - A set of shortcuts to [un]mount TrueCrypt volumes. WARNING: Does not work out of the box (hacking required).

	* `truecrypt mount [letter]` - mount a TrueCrypt volume assigned to the specified letter
	* `truecrypt umount` - unmount all mounted volumes

- **dd_wrt.py** - A set of dd-wrt shortcut commands (requires terminal access to a [dd-wrt](http://www.dd-wrt.com) router). WARNING: Does not work out of the box (hacking required).

	* `wake slave` - send a magic packet to a workstation with MAC address hard-coded in the command file
	* `switch wireless` - turn wireless radio on/off
	* `wan reconnect` - reconnect the PPPoE daemon (may be useful to get a new IP from a dynamic pool)

#### Dependencies

- Python 2.5 (download the 7z archive from the link in the Installation section)
- ABBYY Lingvo dictionary software (optional)

#### Known Issues

- The trigger key will not show the command line if Windows Taskbar is under the focus.

#### Contributors

- [Brian Peiris](https://github.com/brianpeiris)

#### Resources

- [Enso Google Project](https://code.google.com/p/enso/) (no longer maintained)
- [Enso Project in Launchpad](https://launchpad.net/enso) (no longer maintained)
- [Enso 2.0 Design Thoughts](http://www.azarask.in/blog/post/enso-20-design-thoughts/)
- [More Enso Commands](http://www.azarask.in/blog/post/more-enso-commands-for-free/)