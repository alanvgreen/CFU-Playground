/*
 * Copyright 2021 The CFU-Playground Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <stdint.h>

uint32_t Cfu(uint32_t functionid, uint32_t rs1, uint32_t rs2)
{
  uint32_t s1=1, s2=1;

  for (uint32_t count = rs1; count > 0; --count) {
      uint32_t sum = s1 + s2;
      s1 = s2;
      s2 = sum;
  }

  return s2;
}



