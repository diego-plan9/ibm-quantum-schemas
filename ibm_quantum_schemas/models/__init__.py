# This code is a Qiskit project.
#
# (C) Copyright IBM 2025.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Models that provide common functionality."""

import warnings

warnings.warn(
    "Using ibm_quantum_schemas.models.* is deprecated and will be removed in an upcoming release."
    "Instead use ibm_quantum_schemas.program.version_x_y directly",
    category=DeprecationWarning,
    stacklevel=2,
)
