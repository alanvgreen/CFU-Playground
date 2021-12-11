# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nmigen import Signal
from nmigen_cfu import CfuBase

from .constants import Constants

class Cfu(CfuBase):
    """Gen2 accelerator CFU.
    
    Assumes working with a slimopt+cfu VexRiscV, which rsp_ready is always true.
    """
    def elab(self, m):
        # for now, everything completes in a single cycle, so can be always ready
        m.d.comb += self.cmd_ready.eq(1)

        m.d.comb += self.rsp_out.eq(0x12345678)
        m.d.comb += self.rsp_valid.eq(1)

        f = Signal()
        m.d.sync += f.eq(1)

        # # Separate funct3 and funct 7
        # funct3 = Signal(3)
        # funct7 = Signal(7)
        # m.d.comb += [
        #     funct3.eq(self.cmd_function_id[:3]),
        #     funct7.eq(self.cmd_function_id[-7:]),
        # ]

        # ping_result = Signal(32)
        
        # with m.If(self.cmd_valid):
        #     with m.If(funct3 == Constants.INS_PING):
        #         m.d.sync += ping_result.eq(self.cmd_in0 + self.cmd_in1)
        #         m.d.comb += self.rsp_out.eq(ping_result)

        #     m.d.comb += self.rsp_valid.eq(1)

def make_cfu():
    return Cfu()