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

"""Types for constructing and optimizing variational quantum algorithms."""

from openfermioncirq.variational.ansatz import VariationalAnsatz

from openfermioncirq.variational.ansatzes import (
    LowRankTrotterAnsatz,
    SplitOperatorTrotterAnsatz,
    SwapNetworkTrotterAnsatz)

from openfermioncirq.variational.hamiltonian_objective import (
    HamiltonianObjective)

from openfermioncirq.variational.objective import VariationalObjective

from openfermioncirq.variational.study import VariationalStudy
