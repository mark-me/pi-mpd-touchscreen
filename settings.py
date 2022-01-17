# This file is part of pi-jukebox.
#
# pi-jukebox is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pi-jukebox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pi-jukebox. If not, see < http://www.gnu.org/licenses/ >.
#
# (C) 2015- by Mark Zwart, <mark.zwart@pobox.com>

"""

================================================
**settings.py**: Contains project wide variables
================================================

"""
__author__ = 'Mark Zwart'

import os
import sys, pygame
from pygame.locals import *
import time

#: Switches between development/debugging on your desktop/laptop versus running on your Raspberry Pi
RUN_ON_RASPBERRY_PI = os.uname()[4][:3] == 'arm'

# Setting up touch screen, set if statement to true on Raspberry Pi
if RUN_ON_RASPBERRY_PI:
    os.environ['SDL_FBDEV'] = '/dev/fb1'
    os.environ['SDL_MOUSEDEV'] = '/dev/input/event5'
    os.environ['SDL_MOUSEDRV'] = 'TSLIB'

# Display settings
pygame.init() 	# Pygame initialization
#: The display dimensions, change this if you have a bigger touch screen.
DISPLAY_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 320, 240
PYGAME_EVENT_DELAY = 25

if RUN_ON_RASPBERRY_PI:  # If started on Raspberry Pi
    pygame.init()
    print(pygame.display.Info())
    display_flags = pygame.OPENGL | pygame.FULLSCREEN  # Turn on video acceleration
    SCREEN = pygame.display.set_mode(DISPLAY_SIZE, display_flags)
    pygame.mouse.set_visible(False)                                 # Hide mouse cursor
else:
    print(pygame.display.Info())
    SCREEN = pygame.display.set_mode(DISPLAY_SIZE)

#: The directory where resources like button icons or the font file is stored.
RESOURCES = os.path.dirname(__file__) + '/resources/'

#: Standard font type
FONT = pygame.font.Font(RESOURCES + 'DroidSans.ttf', 14)

""" Color definitions """
BLUE = 0, 148, 255
CREAM = 206, 206, 206
BLACK = 0, 0, 0
WHITE = 255, 255, 255
YELLOW = 255, 255, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
# Scheme aqua (currently not in use)
AQUA_TEAL = 18, 151, 147
AQUA_CHARCOAL = 80, 80, 80
AQUA_YELLOW = 255, 245, 195
AQUA_BLUE = 155, 215, 213
AQUA_PINK = 255, 114, 96
# Scheme FIFTIES
FIFTIES_CHARCOAL = 124, 120, 106
FIFTIES_TEAL = 66, 143, 128
FIFTIES_GREEN = 211, 227, 151
FIFTIES_YELLOW = 255, 245, 195
FIFTIES_ORANGE = 235, 110, 68

""" Mouse related variables """
GESTURE_MOVE_MIN = 50  # Minimum movement in pixels to call it a move
GESTURE_CLICK_MAX = 15  # Maximum movement in pixels to call it a click
GESTURE_PRESS_MIN = 500  # Minimum time to call a click a long press
# Gesture enumeration
GESTURE_NONE = -1
GESTURE_CLICK = 0
GESTURE_SWIPE_LEFT = 1
GESTURE_SWIPE_RIGHT = 2
GESTURE_SWIPE_UP = 3
GESTURE_SWIPE_DOWN = 4
GESTURE_LONG_PRESS = 5
GESTURE_DRAG_VERTICAL = 6
GESTURE_DRAG_HORIZONTAL = 7

""" Used icons """
# Switch icons
ICO_SWITCH_ON = RESOURCES + 'switch_on_48x32.png'
ICO_SWITCH_OFF = RESOURCES + 'switch_off_48x32.png'
ICO_MODAL_CANCEL = RESOURCES + 'back_22x18.png'

# General icons
ICO_PLAYER_FILE = RESOURCES + 'playing_file_48x32.png'
ICO_PLAYER_FILE_ACTIVE = RESOURCES + 'playing_file_active_48x32.png'
ICO_PLAYER_RADIO = RESOURCES + 'playing_radio_48x32.png'
ICO_PLAYER_RADIO_ACTIVE = RESOURCES + 'playing_radio_active_48x32.png'
ICO_PLAYLIST = RESOURCES + 'playlist_48x32.png'
ICO_PLAYLIST_ACTIVE = RESOURCES + 'playlist_active_48x32.png'
ICO_LIBRARY = RESOURCES + 'library_48x32.png'
ICO_LIBRARY_ACTIVE = RESOURCES + 'library_active_48x32.png'
ICO_DIRECTORY = RESOURCES + 'directory_48x32.png'
ICO_DIRECTORY_ACTIVE = RESOURCES + 'directory_active_48x32.png'
ICO_RADIO = RESOURCES + 'radio_48x32.png'
ICO_RADIO_ACTIVE = RESOURCES + 'radio_active_48x32.png'
ICO_SETTINGS = RESOURCES + 'settings_48x32.png'
ICO_SETTINGS_ACTIVE = RESOURCES + 'settings_active_48x32.png'
ICO_BACK = RESOURCES + 'back_48x32.png'

# Player icons
PIC_PLAY = RESOURCES + 'play.png'
ICO_MENU = RESOURCES + 'menu_80x50.png'
ICO_PLAY = RESOURCES + 'play_48x32.png'
ICO_PAUSE = RESOURCES + 'pause_48x32.png'
ICO_STOP = RESOURCES + 'stop_48x32.png'
ICO_NEXT = RESOURCES + 'next_48x32.png'
ICO_PREVIOUS = RESOURCES + 'prev_48x32.png'
ICO_VOLUME = RESOURCES + 'vol_48x32.png'
ICO_VOLUME_UP = RESOURCES + 'vol_up_48x32.png'
ICO_VOLUME_DOWN = RESOURCES + 'vol_down_48x32.png'
ICO_VOLUME_MUTE = RESOURCES + 'vol_mute_48x32.png'
ICO_VOLUME_MUTE_ACTIVE = RESOURCES + 'vol_mute_active_48x32.png'

# Library icons
ICO_SEARCH = RESOURCES + 'search_48x32.png'
ICO_SEARCH_ACTIVE = RESOURCES + 'search_active_48x32.png'
ICO_SEARCH_ARTIST = RESOURCES + 'artists_48x32.png'
ICO_SEARCH_ARTIST_ACTIVE = RESOURCES + 'artists_active_48x32.png'
ICO_SEARCH_ALBUM = RESOURCES + 'albums_48x32.png'
ICO_SEARCH_ALBUM_ACTIVE = RESOURCES + 'albums_active_48x32.png'
ICO_SEARCH_SONG = RESOURCES + 'songs_48x32.png'
ICO_SEARCH_SONG_ACTIVE = RESOURCES + 'songs_active_48x32.png'
ICO_PLAYLISTS = RESOURCES + 'playlists_48x32.png'
ICO_PLAYLISTS_ACTIVE = RESOURCES + 'playlists_active_48x32.png'

# Directory icons
ICO_FOLDER_ROOT = RESOURCES + 'folder_root_48x32.png'
ICO_FOLDER_UP = RESOURCES + 'folder_up_48x32.png'

# Radio icons
ICO_STATION_ADD = RESOURCES + 'station_add_48x32.png'
COVER_ART_RADIO = RESOURCES + 'radio_cover_art.png'
