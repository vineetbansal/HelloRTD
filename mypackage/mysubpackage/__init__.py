#  Copyright 2018 Vineet Bansal
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""My Sub Package
The implementations are based on the following publication:

.. [Bansal2005] "MSU at ImageCLEF: Cross language and interactive image retrieval",
   Vineet Bansal, Chen Zhang, Joyce Y. Chai, Rong Jin
   Lecture Notes in Computer Science (Vol. 3491, pp. 805-815)
   https://scholars.opb.msu.edu/en/publications/msu-at-imageclef-cross-language-and-interactive-image-retrieval-4
"""


def hello(recipient):
    """Return our awesome greeting message.

    Parameters
    ----------
    recipient : str
        The unsuspecting recipient of our greeting.


    Returns
    -------
    s : str
        The greeting!
    Note
    ----
        Additional notes go here.
    """
    return 'Hello ' + recipient
