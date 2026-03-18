# This code is a Qiskit project.
#
# (C) Copyright IBM 2026.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Tests for the backwards-compatible interface for the `.models.` modules."""


def test_import_executor_version0_1():
    """Test that executor.version_0_1 is importable."""
    from ibm_quantum_schemas.models.executor.version_0_1.models import (
        ChunkPart,
        ChunkSpan,
        CircuitItemModel,
        MetadataModel,
        OptionsModel,
        ParamsModel,
        QuantumProgramModel,
        QuantumProgramResultItemModel,
        QuantumProgramResultModel,
        SamplexItemModel,
    )


def test_import_executor_version0_2():
    """Test that executor.version_0_2 is importable."""
    from ibm_quantum_schemas.models.executor.version_0_2.models import (
        ChunkPart,
        ChunkSpan,
        CircuitItemModel,
        ItemMetadataModel,
        MetadataModel,
        OptionsModel,
        ParamsModel,
        QuantumProgramModel,
        QuantumProgramResultItemModel,
        QuantumProgramResultModel,
        SamplexItemModel,
        SchedulerTimingModel,
        StretchValueModel,
    )


def test_import_noise_learner_v3_version_0_1():
    """Test that noise_learner_v3_version_0_1 is importable."""
    from ibm_quantum_schemas.models.noise_learner_v3.version_0_1.models import (
        LinbdbladResultMetadataModel,
        LinbdbladResultPostSelectionMetadataModel,
        NoiseLearnerV3ResultModel,
        NoiseLearnerV3ResultsModel,
        OptionsModel,
        ParamsModel,
        PostSelectionOptionsModel,
        TREXResultMetadataModel,
        TREXResultPostSelectionMetadataModel,
    )


def test_import_noise_learner_v3_version_0_2():
    """Test that noise_learner_v3_version_0_2 is importable."""
    from ibm_quantum_schemas.models.noise_learner_v3.version_0_2.models import (
        LinbdbladResultMetadataModel,
        LinbdbladResultPostSelectionMetadataModel,
        NoiseLearnerV3ResultModel,
        NoiseLearnerV3ResultsModel,
        OptionsModel,
        ParamsModel,
        PostSelectionOptionsModel,
        TREXResultMetadataModel,
        TREXResultPostSelectionMetadataModel,
    )


def test_import_common_models():
    """Test that the common models are importable."""
    from ibm_quantum_schemas.models.annotation_serializer import AnnotationSerializer
    from ibm_quantum_schemas.models.base_params_model import BaseParamsModel
    from ibm_quantum_schemas.models.ndarray_wrapper_model import NdarrayWrapperModel
    from ibm_quantum_schemas.models.pauli_lindblad_map_model import PauliLindbladMapModel
    from ibm_quantum_schemas.models.qpy_model import (
        QpyModel,
        QpyModelV13ToV16,
        QpyModelV13ToV17,
    )
    from ibm_quantum_schemas.models.samplex_model import (
        SamplexModel,
        SamplexModelSSV1,
        SamplexModelSSV1ToSSV2,
    )
    from ibm_quantum_schemas.models.tensor_model import F64TensorModel, TensorModel
    from ibm_quantum_schemas.models.typed_qpy_circuit_model import (
        TypedQpyCircuitModel,
        TypedQpyCircuitModelV13to17,
    )
