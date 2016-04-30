#     Copyright 2016, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Python test originally created or extracted from other peoples work. The
#     parts from me are licensed as below. It is at least Free Software where
#     it's copied from other people. In these cases, that will normally be
#     indicated.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#

def f1():
    yield 1, 2, 3

def f2():
    yield 1, 2, 4


def comparer():
    g1 = f1()
    g2 = f2()

    # This enables tracing in a custom build of mine.
    a = 1
    o = oct
    o(a)

    for i in range(10000):
        # g1 == g2
        g1 == a

if __name__ == "__main__":
    comparer()