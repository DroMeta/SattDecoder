#  Copyright (c) 2024. Alexander Baskikh
#
#  MIT License (MIT), http://opensource.org/licenses/MIT
#  Full license can be found in the LICENSE-MIT file
#
#  SPDX-License-Identifier: MIT

import sys

from SatsDecoder.systems.ax25 import *
from SatsDecoder.systems.geoscan import *
from SatsDecoder.systems.sonate2 import *
from SatsDecoder.systems.usp import *

PROTOCOLS = {}
for i in (
        'geoscan',
        'usp',
        'sonate2',
        'ax25',
        ):
    m = getattr(sys.modules['SatsDecoder.systems'], i)
    for n in dir(m):
        if n.endswith('Protocol'):
            PROTOCOLS[m.proto_name] = getattr(m, n)
            break
