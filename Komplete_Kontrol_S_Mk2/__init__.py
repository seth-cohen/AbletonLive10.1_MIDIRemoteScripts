# uncompyle6 version 3.4.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_S_Mk2/__init__.py
# Compiled at: 2019-05-08 17:06:57
from __future__ import absolute_import, print_function, unicode_literals
from .komplete_kontrol_s_mk2 import Komplete_Kontrol_S_Mk2
from ableton.v2.control_surface.capabilities import SUGGESTED_PORT_NAMES_KEY

def get_capabilities():
    return {SUGGESTED_PORT_NAMES_KEY: [
                                'Komplete Kontrol DAW - 1']}


def create_instance(c_instance):
    return Komplete_Kontrol_S_Mk2(c_instance=c_instance)