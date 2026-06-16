# Detailed Research Paper PDF Analysis
This document contains a deep extraction and analysis of the methodology, experiments, and results of downloaded PDFs.

---

## Detailed Analysis: OpenHalDet: A Unified Benchmark for Hallucination Detection across Diverse Generation Scenarios
*(Extracted offline using regex heuristics)*

### 1. Methodology & Architecture
method requires no
additional training, calibration or fitting, or supervised adaptation. See Table 8 for more details.
2.4 Evaluation Metrics
Following [3, 39], we useAUROCas the primary metric. Each detector assigns a scalar hallucination
score to each response, where higher scores indicate higher hallucination risk. AUROC evaluates
whether hallucinated responses receive higher scores than correct responses across decision thresholds.
In addition to the main benchmark tables, we provide a separate supplementary cost analysis to
characterize detector efficiency rather than to define the primary ranking. We reportCost@N, the
wall-clock time for applying a detector to N samples under a fixed hardware and evaluation protocol,
decomposed into feature preparation, training, and inference time.See more details in Appendix G.
3 Supported Detection Methods and Evaluation Protocol
This section provides a concise overview of the 16 hallucination detection methods shown in Figure 1.
We focus on representative methods with publicly available implementations or sufficiently clear
algorithmic descriptions for reproducible implementation,see more details in Appendix E.
3.1 Black-box Detectors
Bl...

### 2. Experiments & Evaluation
experiment configuration that specifies the dataset,
split, target model, system prompt, number of shots, maximum generation length, model-loading
arguments, generation arguments, chat-template arguments, layer-selection rule, token-selection
rule, and output directory. Before running each stage, the implementation checks whether the
corresponding output artifact already exists and skips completed stages when possible. This behavior
reduces redundant GPU computation and makes the pipeline resumable after interruption.
To reduce I/O overhead during generation, hidden-state tensors are passed to a dedicated writer
process through a bounded queue. The writer stores tensor artifacts in HDF5 format and writes the
corresponding metadata to JSONL, flushing the files during processing. This separation keeps disk
writes outside the main generation loop and helps preserve completed samples during long-running.
D Annotation
OpenHalDet uses an automatic annotation stage to convert generated model responses into stan-
dardized correctness labels for detector evaluation. Given a generated response, the annotation
module provides the judge model with the original question, optional context, accep...

### 3. Results & Findings
result, white-box detectors are typically more
applicable to open-source or fully accessible models than to closed-source API-only systems.
These methods use internal representations extracted from the target LLM to detect hallucination.
We organize them according to how internal signals are used:representation-consistency scores,con-
trastive or subspace-based objectives,hidden-state probes, andprompt- or dynamics-guided internal
features. Forrepresentation-consistencymethods, EIGENSCORE[ 26] measures representation-level
consistency across stochastic generations by analyzing the spectral geometry of hidden-state represen-
tations. Forcontrastive or subspace-basedmethods, CCS [ 27] learns a contrast-consistent direction
from paired hidden states, while HALOSCOPE[ 39] estimates hallucination-related membership in a
latent representation subspace and trains a truthfulness classifier from the estimated memberships.
Forhidden-state probemethods, SAPLMA [ 28] trains a supervised classifier on input-output hid-
den states to predict statement truthfulness. MIND [ 60] uses generation-time hidden states in an
unsupervised training framework for real-time hallucination detection, and SEP [...

---

