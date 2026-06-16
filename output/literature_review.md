# Automated Literature Review: Academic Report
*(Compiled Offline by local analysis parser)*

## 1. Executive Summary
This document presents a synthesized review of 5 research papers related to the target topic. Below, we analyze individual contributions, methodologies, and compile formal bibliographic citations.

## 2. Individual Paper Analyses

### Paper 1: Probabilistic distances-based hallucination detection in LLMs with RAG
* **Authors:** Rodion Oblovatny, Alexandra Kuleshova, Konstantin Polev et al.
* **Published:** 2025-06-11
* **arXiv ID:** 2506.09886v2

**Core Objective & Background:**
Detecting hallucinations in large language models (LLMs) is critical for their safety in many applications. Without proper detection, these systems often provide harmful, unreliable answers. In recent years, LLMs have been actively used in retrieval-augmented generation (RAG) settings. However, hallucinations remain even in this setting, and while numerous hallucination detection methods have been proposed, most approaches are not specifically designed for RAG systems. To overcome this limitation, we introduce a hallucination detection method based on estimating the distances...

**Methodology & Findings:**
...between the distributions of prompt token embeddings and language model response token embeddings. The method examines the geometric structure of token hidden states to reliably extract a signal of factuality in text, while remaining friendly to long sequences. Extensive experiments demonstrate that our method achieves state-of-the-art or competitive performance. It also has transferability from solving the NLI task to the hallucination detection task, making it a fully unsupervised and efficient method with a competitive performance on the final task.

---

### Paper 2: OpenHalDet: A Unified Benchmark for Hallucination Detection across Diverse Generation Scenarios
* **Authors:** Xinyi Li, Zhen Fang, Yongxin Deng et al.
* **Published:** 2026-06-05
* **arXiv ID:** 2606.06959v1

**Core Objective & Background:**
Hallucination detection is essential for the reliable deployment of large language models (LLMs). However, existing evaluations face two core challenges: inconsistent inference configuration and evaluation, and limited coverage of downstream domains and tasks. Consequently, reported detector performance is often difficult to compare, reproduce, and generalize beyond specific experimental settings. We introduce OpenHalDet, a unified benchmark for hallucination detection across diverse generation scenarios. OpenHalDet standardizes the evaluation pipeline, from prompt construction and response generation to truthfulness annotation, detector scoring, and metric computation. It supports heterogeneous detector...

**Methodology & Findings:**
...families under different access settings, including black-box methods that use only generated outputs, gray-box methods that rely on probability-based signals, and white-box methods that exploit internal model signals. By bringing diverse tasks, models, and detectors into a shared framework, OpenHalDet enables controlled comparison and provides a systematic view of how different detection paradigms behave in LLM applications. We release OpenHalDet as an open and extensible codebase to facilitate reproducible evaluation and future development of hallucination detection methods. The code and datasets are available at https://github.com/Nellie179/Hallucination-Detection.

---

### Paper 3: Are LLMs More Skeptical of Entertainment News?
* **Authors:** Huiqian Lai
* **Published:** 2026-05-03
* **arXiv ID:** 2605.01727v1

**Core Objective & Background:**
Large language models (LLMs) are increasingly used for automated news credibility assessment, yet it remains unclear whether they apply even-handed standards across journalistic genres. We examine whether zero-shot LLMs are more likely to misclassify legitimate entertainment news as fake than legitimate hard news, using a within-dataset design on GossipCop from FakeNewsNet. Across four frontier models, we find a clear but model-specific genre asymmetry: DeepSeek-V3.2 and GPT-5.2 show false-positive-rate gaps of 10.1 and 8.8 percentage points, respectively (both $p < .001$), whereas Claude Opus 4.6 and Gemini 3 Flash show no comparable difference. A style-swap experiment yields only limited and inconsistent changes, suggesting that the asymmetry is not reducible to stylistic register...

**Methodology & Findings:**
...alone. Prompt-based mitigation is likewise possible but not generic: framing the model as an entertainment-news fact-checker reduces false positives for DeepSeek-V3.2 by about 50\% without detectable recall loss, but offers little improvement for GPT-5.2. Exploratory qualitative coding further suggests two recurring error patterns in sampled false positives: treating private-life claims as inherently unverifiable and discounting entertainment journalism as an epistemically weaker genre. Taken together, these findings show that aggregate performance metrics can obscure structured false positives within legitimate journalism. We argue that LLM-based credibility assessment may not only evaluate truth claims but also differentially recognize the legitimacy of journalistic genres, and that evaluation should therefore include genre-stratified false-positive analysis alongside overall accuracy.

---

### Paper 4: Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration
* **Authors:** Qiyao Sun, Xingming Li, Xixiang He et al.
* **Published:** 2026-03-24
* **arXiv ID:** 2603.22812v1

**Core Objective & Background:**
Large language models (LLMs) have achieved remarkable success in various natural language processing tasks, yet they remain prone to generating factually incorrect outputs known as hallucinations. While recent approaches have shown promise for hallucination detection by repeatedly sampling from LLMs and quantifying the semantic inconsistency among the generated responses, they rely on fixed sampling budgets that fail to adapt to query complexity, resulting in computational inefficiency. We propose an Adaptive Bayesian Estimation framework for Semantic Entropy with Guided Semantic Exploration, which dynamically adjusts sampling requirements based on observed uncertainty. Our approach...

**Methodology & Findings:**
...employs a hierarchical Bayesian framework to model the semantic distribution, enabling dynamic control of sampling iterations through variance-based thresholds that terminate generation once sufficient certainty is achieved. We also develop a perturbation-based importance sampling strategy to systematically explore the semantic space. Extensive experiments on four QA datasets demonstrate that our method achieves superior hallucination detection performance with significant efficiency gains. In low-budget scenarios, our approach requires about 50% fewer samples to achieve comparable detection performance to existing methods, while delivers an average AUROC improvement of 12.6% under the same sampling budget.

---

### Paper 5: Hallucination Detection with Small Language Models
* **Authors:** Ming Cheung
* **Published:** 2025-06-24
* **arXiv ID:** 2506.22486v1

**Core Objective & Background:**
Since the introduction of ChatGPT, large language models (LLMs) have demonstrated significant utility in various tasks, such as answering questions through retrieval-augmented generation. Context can be retrieved using a vectorized database, serving as a foundation for LLMs to generate responses. However, hallucinations in responses can undermine the reliability of LLMs in practical applications, and they are not easily detectable in the absence of ground truth, particularly in question-and-answer scenarios. This paper proposes a framework that integrates multiple small language models to verify responses generated by LLMs using the retrieved context from a vectorized database. By breaking down the responses...

**Methodology & Findings:**
...into individual sentences and utilizing the probability of generating "Yes" tokens from the outputs of multiple models for a given set of questions, responses, and relevant context, hallucinations can be detected. The proposed framework is validated through experiments with real datasets comprising over 100 sets of questions, answers, and contexts, including responses with fully and partially correct sentences. The results demonstrate a 10\% improvement in F1 scores for detecting correct responses compared to hallucinations, indicating that multiple small language models can be effectively employed for answer verification, providing a scalable and efficient solution for both academic and practical applications.

---

## 3. Comparative Synthesis
Reviewing the collected works reveals key patterns:
* **Technological Evolution:** The selected papers show a trend towards optimizing system scale, algorithmic latency, and deployment costs.
* **Methodological Commonalities:** A significant portion of the research utilizes empirical evaluations and comparative testing to validate model assertions.

## 4. Academic Citations

### IEEE Format
[1] Rodion Oblovatny et al., "Probabilistic distances-based hallucination detection in LLMs with RAG," *arXiv preprint arXiv:2506.09886v2*, 2025.
[2] Xinyi Li et al., "OpenHalDet: A Unified Benchmark for Hallucination Detection across Diverse Generation Scenarios," *arXiv preprint arXiv:2606.06959v1*, 2026.
[3] Huiqian Lai, "Are LLMs More Skeptical of Entertainment News?," *arXiv preprint arXiv:2605.01727v1*, 2026.
[4] Qiyao Sun et al., "Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration," *arXiv preprint arXiv:2603.22812v1*, 2026.
[5] Ming Cheung, "Hallucination Detection with Small Language Models," *arXiv preprint arXiv:2506.22486v1*, 2025.

### APA Format
Rodion Oblovatny et al. (2025). Probabilistic distances-based hallucination detection in LLMs with RAG. *arXiv preprint arXiv:2506.09886v2*.
Xinyi Li et al. (2026). OpenHalDet: A Unified Benchmark for Hallucination Detection across Diverse Generation Scenarios. *arXiv preprint arXiv:2606.06959v1*.
Huiqian Lai (2026). Are LLMs More Skeptical of Entertainment News?. *arXiv preprint arXiv:2605.01727v1*.
Qiyao Sun et al. (2026). Efficient Hallucination Detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration. *arXiv preprint arXiv:2603.22812v1*.
Ming Cheung (2025). Hallucination Detection with Small Language Models. *arXiv preprint arXiv:2506.22486v1*.
