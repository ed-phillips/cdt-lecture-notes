# Multimodal AI for time series: literature review

Background reading for the "Multimodal and agentic AI for time series" lecture
(multimodal half, 30–40 min), part of the ML for Time Series module of the
EPSRC CDT in Healthcare Data Science. The next day's lab is ECG + EHR fusion.

The lecture runs **general first, then ECG + EHR as the working example**.
Sections 1–6 below are general; sections 7–9 are healthcare and ECG + EHR;
section 10 links to the neighbouring lectures (Xiao on foundation models and LLMs,
Yixuan on agentic AI).

**How this was checked (20 Oct 2026):** each entry's authors, venue and year were
checked against the publisher, proceedings or arXiv record. Paper summaries
are taken from abstracts and proceedings pages, not full read-throughs. Read
the paper before relying on any detail (numbers, method specifics) on a slide.
BibTeX keys refer to `lectures/references.bib`.

**Tags:** ★ = suggested for a slide; 📖 = suggested "further reading" pointer.

---

## 1. Surveys and taxonomies (general)

- ★📖 **Baltrušaitis, Ahuja & Morency (2019).** *Multimodal Machine Learning: A Survey and Taxonomy.* IEEE TPAMI 41(2). DOI 10.1109/TPAMI.2018.2798607 (online in 2018, print in 2019). `baltrusaitis2019multimodal`
  - It defines five core challenges: **representation, translation, alignment, fusion, co-learning**. It's the standard framing, and works well as one slide showing that fusion is only part of the picture.
- ★📖 **Liang, Zadeh & Morency (2024).** *Foundations & Trends in Multimodal Machine Learning: Principles, Challenges, and Open Questions.* ACM Computing Surveys. DOI 10.1145/3656580; arXiv 2209.03430. `liang2024foundations`
  - The updated taxonomy has six challenges: representation, alignment, reasoning, generation, transference, quantification. It also sets out principles of multimodal data such as heterogeneity and interconnections between modalities. This makes a good modern alternative to (or follow-on from) Baltrušaitis.
- ★📖 **Xu, Zhu & Clifton (2023).** *Multimodal Learning With Transformers: A Survey.* IEEE TPAMI 45(10), from p. 12113. DOI 10.1109/TPAMI.2023.3275156; arXiv 2206.06488. `xu2023multimodal`
  - Surveys Transformer-based multimodal learning: tokenisation of different modalities, fusion via attention (early, cross and hierarchical attention), multimodal pretraining, and open problems.
  - It's David Clifton's survey, and he also lectures on Friday. It's a natural citation for "attention as a general fusion mechanism".
- **Ngiam, Khosla, Kim, Nam, Lee & Ng (2011).** *Multimodal Deep Learning.* ICML 2011, 689–696. `ngiam2011multimodal`
  - The historical starting point for deep multimodal learning (audio-visual speech). It learned shared representations, and showed that one modality can improve features learned for another. Useful for one line of history.

## 2. Fusion mechanisms (general)

Ordered from simple to expressive. Concatenation needs no citation.

- **Arevalo, Solorio, Montes-y-Gómez & González (2017).** *Gated Multimodal Units for Information Fusion.* Listed under ICLR 2017; arXiv 1702.01992. I didn't confirm whether it was the main or workshop track. `arevalo2017gated`
  - Learned multiplicative gates that weight each modality's contribution per sample. It's the simplest "learned weighting" step beyond concatenation.
- **Zadeh, Chen, Poria, Cambria & Morency (2017).** *Tensor Fusion Network for Multimodal Sentiment Analysis.* EMNLP 2017, 1103–1114. `zadeh2017tensor`
  - Outer-product fusion that explicitly models interactions within each modality and across modalities. The classic example of "multiplicative" intermediate fusion.
- **Perez, Strub, de Vries, Dumoulin & Courville (2018).** *FiLM: Visual Reasoning with a General Conditioning Layer.* AAAI 2018. `perez2018film`
  - One modality produces a per-feature scale and shift for another modality's features. Good for "condition the ECG encoder on patient context from the EHR".
- ★ **Tsai, Bai, Liang, Kolter, Morency & Salakhutdinov (2019).** *Multimodal Transformer for Unaligned Multimodal Language Sequences.* ACL 2019, 6558–6569. `tsai2019multimodal`
  - Directional pairwise **cross-modal attention**, working **without explicit alignment** of sequences sampled at different rates. This is the paper most directly about *time-series* modalities with different sampling rates.
- **Jaegle, Gimeno, Brock, Vinyals, Zisserman & Carreira (2021).** *Perceiver: General Perception with Iterative Attention.* ICML 2021. `jaegle2021perceiver`
  - Cross-attends very large inputs into a small latent array, making few assumptions about the input modality. An example of a "modality-agnostic" architecture.
- **Nagrani, Yang, Arnab, Jansen, Schmid & Sun (2021).** *Attention Bottlenecks for Multimodal Fusion.* NeurIPS 2021. `nagrani2021attention`
  - Forces cross-modal exchange through a few bottleneck tokens. It matches or beats full cross-attention at lower cost, illustrating that "fuse a bit, in the middle" can beat "fuse everything".

## 3. Shared embedding spaces (general)

- ★ **Radford et al. (2021).** *Learning Transferable Visual Models From Natural Language Supervision* (CLIP). ICML 2021, PMLR 139:8748–8763. `radford2021learning`
  - Contrastive alignment of paired modalities into one space, which enables zero-shot transfer. This is the template that ECG–text work follows.
- **Girdhar et al. (2023).** *ImageBind: One Embedding Space To Bind Them All.* CVPR 2023, 15180–15190. `girdhar2023imagebind`
  - One space for six modalities, including IMU. The "hub" modality (images) is enough to bind the others without all modalities ever being paired together.
- ★ **Saporta, Puli, Goldstein & Ranganath (2024).** *Contrasting with Symile: Simple Model-Agnostic Representation Learning for Unlimited Modalities.* NeurIPS 2024. `saporta2024symile`
  - Pairwise CLIP misses information shared jointly across three or more modalities, so Symile uses a total-correlation objective instead. Its clinical experiment uses **chest X-rays, ECGs and lab measurements** (MIMIC), so it bridges straight into the ECG + EHR example.

## 4. LLMs as the fusion hub (general; sets up the agentic half)

- **Alayrac et al. (2022).** *Flamingo: a Visual Language Model for Few-Shot Learning.* NeurIPS 2022. `alayrac2022flamingo`
  - Feeds visual features into a frozen LLM through cross-attention layers.
- ★ **Liu, Li, Wu & Lee (2023).** *Visual Instruction Tuning* (LLaVA). NeurIPS 2023 (oral). `liu2023visual`
  - Frozen vision encoder, a projection into the LLM's token space, then instruction tuning. This "encoder + projector + LLM" recipe is copied widely, including for ECG.
- **Tu et al. (2024).** *Towards Generalist Biomedical AI* (Med-PaLM M). NEJM AI; arXiv 2307.14334. Records disagree on the first author, so check the NEJM AI byline. `tu2024towards`
  - One model for clinical text, imaging and genomics, evaluated on the MultiMedBench benchmark.
- ★ **Belyaeva et al. (2023).** *Multimodal LLMs for health grounded in individual-specific data* (HeLM). ICML 2023 workshop; arXiv 2307.09018. `belyaeva2023multimodal`
  - Complex modalities (spirograms, which are a *time series*) go through learned encoders into the LLM's embedding space; tabular data is serialised as text. On UK Biobank asthma prediction, adding spirograms raises AUROC from 0.49 to 0.75.
  - A clean, health-specific time-series example of the projector pattern.

## 5. When does fusion help, and why it's hard to train (general)

- ★ **Wang, Tran & Feiszli (2020).** *What Makes Training Multi-Modal Classification Networks Hard?* CVPR 2020, 12695–12705. `wang2020what`
  - The **multimodal model can underperform the best unimodal one**. Two causes: it overfits more, and different modalities overfit and generalise at different rates. Their fix is Gradient Blending.
  - The key "always check your unimodal baselines" paper.
- **Huang, Lin, Zhou, Yang & Huang (2022).** *Modality Competition: What Makes Joint Training of Multi-modal Network Fail in Deep Learning? (Provably).* ICML 2022, PMLR 162:9226–9259. `huang2022modality`
  - Theory: in jointly trained late fusion, modalities *compete*, and only a subset get learned well.
- **Peng, Wei, Deng, Wang & Hu (2022).** *Balanced Multimodal Learning via On-the-fly Gradient Modulation* (OGM-GE). CVPR 2022. `peng2022balanced`
  - A practical fix for a dominant modality starving the others: it scales each modality's gradients by its contribution.
- ★📖 **Liang et al. (2023).** *Quantifying & Modeling Multimodal Interactions: An Information Decomposition Framework.* NeurIPS 2023. `liang2023quantifying`
  - Splits the task-relevant information into **redundancy, uniqueness and synergy** across modalities (partial information decomposition).
  - The best conceptual lens for "should fusion help here?": fusion pays off when modalities are unique or synergistic, not when they are redundant.
- 📖 **Liang et al. (2021).** *MultiBench: Multiscale Benchmarks for Multimodal Representation Learning.* NeurIPS 2021 Datasets and Benchmarks. `liang2021multibench`
  - 15 datasets, 10 modalities and 6 areas (healthcare included), with standard implementations of 20 methods. It also measures robustness to missing modalities.

## 6. Missing modalities (general)

- ★ **Ma, Ren, Zhao, Testuggine & Peng (2022).** *Are Multimodal Transformers Robust to Missing Modality?* CVPR 2022, 18156–18165. `ma2022multimodal`
  - Transformers degrade badly when a modality is missing, and the best fusion strategy depends on the dataset.
- 📖 **Wu, Wang, Chen & Carneiro (2026).** *Deep Multimodal Learning with Missing Modality: A Survey.* TMLR; arXiv 2409.07825. `wu2026deep`
  - The reference survey for missing-modality methods. Point students here.

---

## 7. Healthcare reviews

- ★📖 **Huang, Pareek, Seyyedi, Banerjee & Lungren (2020).** *Fusion of medical imaging and electronic health records using deep learning: a systematic review and implementation guidelines.* npj Digital Medicine 3:136. DOI 10.1038/s41746-020-00341-z. `huang2020fusion`
  - The standard healthcare **early, joint and late fusion** taxonomy, with implementation guidelines. It's about imaging + EHR, but the taxonomy carries straight over to ECG + EHR.
- 📖 **Acosta, Falcone, Rajpurkar & Topol (2022).** *Multimodal biomedical AI.* Nature Medicine 28(9):1773–1784. DOI 10.1038/s41591-022-01981-2. `acosta2022multimodal`
  - A broad narrative review of the opportunities (biosensors, remote monitoring, digital twins) and the challenges (data, privacy). Good motivation for the "why multimodal in healthcare" slide.
- **Kline et al. (2022).** *Multimodal machine learning in precision health: A scoping review.* npj Digital Medicine 5:171. DOI 10.1038/s41746-022-00712-8. `kline2022multimodal`
  - 128 studies. **Early fusion was the most common strategy**. The few studies that compared against unimodal models report an average gain of about 6.4%. It flags missing deployment and fairness analysis.
- **Krones, Marikkar, Parsons, Szmul & Mahdi (2025).** *Review of multimodal machine learning approaches in healthcare.* Information Fusion 114:102690. DOI 10.1016/j.inffus.2024.102690. `krones2025review`
  - An Oxford review (Adam Mahdi's group): more than 50 studies, mostly imaging + tabular. **Effectiveness depends on the data and the task.**

## 8. Healthcare fusion case studies and benchmarks

- ★ **Soenksen et al. (2022).** *Integrated multimodal artificial intelligence framework for healthcare applications* (HAIM). npj Digital Medicine (2022). DOI 10.1038/s41746-022-00689-4. `soenksen2022integrated`
  - MIMIC-based: embeddings from tabular data, time series, notes and images are combined and fed to simple models, across 14,324 models.
  - Multimodal models beat single-source ones by 6–33%. Shapley values show which modality matters varies by task.
  - The closest published analogue to the lab's "embeddings from pretrained encoders, then fuse" set-up.
- ★ **Hayat, Geras & Shamout (2022).** *MedFuse: Multi-modal fusion with clinical time-series data and chest X-ray images.* MLHC 2022, PMLR 182:479–503. `hayat2022medfuse`
  - An LSTM-based fusion module that accepts unimodal or paired input, with clinical time series + chest X-ray on MIMIC-IV.
  - It beats more complex fusion on paired data and stays robust when X-rays are missing.
- **Elsharief et al. (2025).** *MedMod: Multimodal Benchmark for Medical Prediction Tasks with Electronic Health Records and Chest X-Ray Scans.* CHIL 2025, PMLR 287:781–803. `elsharief2025medmod`
  - Benchmarks early, joint and late fusion on EHR + chest X-ray (MIMIC-IV and MIMIC-CXR).
- ★ **Yin et al. (2026).** *When Does Multimodal Learning Help in Healthcare? A Benchmark on EHR and Chest X-Ray Fusion.* arXiv 2602.23614 (preprint). `yin2026when`
  - Fusion helps when **both modalities are present** and the task needs complementary information.
  - The temporal structure of the EHR causes **modality imbalance** that architectural complexity alone doesn't fix.
  - Gains **degrade quickly under realistic missingness**, and fusion **doesn't automatically improve fairness**.
  - A recent, sobering summary that's ideal for the "best practice" slide. It's still a preprint, so cite it as such.
- **Zhang, Li, Chen, Yan & Petzold (2023).** *Improving Medical Predictions by Irregular Multimodal Electronic Health Records Modeling.* ICML 2023, PMLR 202:41300–41313. `zhang2023improving`
  - ICU time series + clinical notes, **both irregularly sampled**. Each modality's irregularity is handled separately before an interleaved-attention fusion. Shows the problems specific to time series.

## 9. The ECG + EHR working example

Dataset and context:

- ★ **Gow, Pollard, et al. (2023).** *MIMIC-IV-ECG: Diagnostic Electrocardiogram Matched Subset* (v1.0). PhysioNet. DOI 10.13026/4nqg-sb35. `gow2023mimicivecg`
  - About 800k 10-second, 12-lead, 500 Hz ECGs from about 160k patients, **linked to the MIMIC-IV clinical database**. Cardiologist reports are included where available. Presumably the lab's data source; check this against the lab design.
- **Strodthoff, Lopez Alcaraz & Haverkamp (2024).** *Prospects for artificial intelligence-enhanced electrocardiogram as a unified screening tool for cardiac and non-cardiac conditions: an explorative study in emergency care.* European Heart Journal – Digital Health. DOI 10.1093/ehjdh/ztae039. `strodthoff2024prospects`
  - Introduces the MIMIC-IV-ECG-ICD benchmark. A single ECG model predicts 253 ICD codes, cardiac and non-cardiac, with AUROC above 0.8. A useful illustration of how much "EHR information" an ECG alone carries, which motivates the redundancy question from section 5.

The canonical clinical example of combining ECG and EHR:

- ★ **Khurshid et al. (2022).** *ECG-Based Deep Learning and Clinical Risk Factors to Predict Atrial Fibrillation.* Circulation 145:122–133. DOI 10.1161/CIRCULATIONAHA.121.057480. `khurshid2022ecg`
  - ECG-AI (a CNN on 12-lead ECGs), the CHARGE-AF clinical score, and their combination (CH-AI) for five-year AF risk.
  - The combination is best at all three sites (AUROC 0.838, 0.777 and 0.746, vs ECG-AI at 0.823, 0.747 and 0.705), so the two are **complementary**.
  - A simple **late-fusion** example from a top clinical journal, with external validation (including UK Biobank).

Per-modality encoders (connects to Thursday's FM practicals):

- **McKeen et al. (2025).** *ECG-FM: an open electrocardiogram foundation model.* JAMIA Open. DOI 10.1093/jamiaopen/ooaf122; arXiv 2408.05178. `mckeen2025ecgfm`
  - A transformer pretrained on about 1.5M ECGs, with masked reconstruction plus contrastive self-supervision. Strong linear-probe performance, and an open benchmark on MIMIC-IV-ECG.
- 📖 **Wornow et al. (2023).** *The shaky foundations of large language models and foundation models for electronic health records.* npj Digital Medicine 6:135. DOI 10.1038/s41746-023-00879-8. `wornow2023shaky`
  - Reviews 84 EHR foundation models and is critical of how they are evaluated. A useful caution when students fuse FM embeddings.
- **Wornow et al. (2023).** *EHRSHOT: An EHR Benchmark for Few-Shot Evaluation of Foundation Models.* arXiv 2307.02028. I believe it also appeared in NeurIPS 2023 Datasets and Benchmarks, but haven't confirmed it. `wornow2023ehrshot`
  - A longitudinal structured-EHR benchmark plus a released 141M-parameter EHR foundation model.

ECG + text (alignment rather than fusion):

- ★ **Liu, Wan, Ouyang, Shah, Bai & Arcucci (2024).** *Zero-Shot ECG Classification with Multimodal Learning and Test-time Clinical Knowledge Enhancement* (MERL). ICML 2024, PMLR 235:31949–31963. `liu2024zeroshot`
  - CLIP-style ECG–report pretraining, with zero-shot ECG classification from text prompts. Average zero-shot AUROC of 75.2% across six datasets, beating linear-probed self-supervised baselines trained on 10% of the labels.

Recent ECG + EHR fusion on MIMIC-IV-ECG (for awareness only; mostly 2025–26 and less established):
- CaMPNet (JMIR Formative Research, 2026): query-conditioned early fusion.
- LeMoF (arXiv 2601.10092): level-guided fusion for length-of-stay prediction.
- Lab-value abnormality prediction from ECG + metadata (Scientific Reports, 2025).
- MEETI (Scientific Data, 2026): MIMIC-IV-ECG extended with images, features and interpretation text.

Read these before citing any of them.

## 10. Time series + language, wearables, and ECG MLLMs (links to Xiao and Yixuan)

- 📖 **Zhang et al. (2024).** *Large Language Models for Time Series: A Survey.* IJCAI 2024; arXiv 2402.01801. `zhang2024large`
  - A taxonomy of approaches: prompting, quantisation, alignment, vision as a bridge, and tools. It probably overlaps with Xiao's lecture, so check with Xiao.
- 📖 **Liu et al. (2025).** *Towards Cross-Modality Modeling for Time Series Analytics: A Survey in the LLM Era.* IJCAI 2025; arXiv 2505.02583. `liu2025towards`
  - Time series + text: alignment and fusion strategies. The closest survey to the title of this lecture.
- **Liu et al. (2024).** *Time-MMD: Multi-Domain Multimodal Dataset for Time Series Analysis.* NeurIPS 2024 Datasets and Benchmarks. `liu2024timemmd`
  - Nine domains, with aligned text. Adding text cuts forecasting MSE by more than 15% on average. Outside healthcare, but a clear "text helps time series" result.
- **Kim, Xu, McDuff, Breazeal & Park (2024).** *Health-LLM: Large Language Models for Health Prediction via Wearable Sensor Data.* CHIL 2024, PMLR 248:522–539. `kim2024healthllm`
- **Belyaeva, Cosentino et al. (2025).** *A personal health large language model for sleep and fitness coaching* (PH-LLM). Nature Medicine. DOI 10.1038/s41591-025-03888-0. `belyaeva2025personal`
  - Gemini fine-tuned to reason over daily-aggregated wearable data.
  - Note: the arXiv preprint has a different title, "Towards a Personal Health Large Language Model" (2406.06474). The author order differs between records, so check it on the publisher's page.
- **Zhang et al. (2025).** *SensorLM: Learning the Language of Wearable Sensors.* NeurIPS 2025; arXiv 2506.09108. `zhang2025sensorlm`
  - Sensor–language pretraining on about 59.7M hours of wearable data, generalising CLIP and CoCa. Zero-shot, few-shot and retrieval results.
- **Lan et al. (2025).** *GEM: Empowering MLLM for Grounded ECG Understanding with Time Series and Images.* NeurIPS 2025; arXiv 2503.06073. `lan2025gem`
  - An ECG multimodal LLM whose two encoders take the raw signal and the ECG image, with "grounded" explanations tied to ECG features.
- **Liu, Bai, Yue & Zhang (2024).** *Teach Multimodal LLMs to Comprehend Electrocardiographic Images* (PULSE / ECGInstruct). arXiv 2410.19008. **Preprint only:** I found no peer-reviewed venue. `liu2024teach`

---

## Corrections to the first brainstorm

- **PH-LLM:** the Nature Medicine paper's title differs from the preprint's, and Belyaeva is listed first in the Google record.
- **Modality competition:** I had the paper by Huang, Lin, Zhou, Yang and Huang (ICML 2022) in mind; this is now the correct author list.
- **PULSE:** it's an arXiv preprint, not a conference paper.
- **Baltrušaitis et al.:** published online in 2018, print issue in 2019 (TPAMI 41(2)). Both years appear in citations.
- **Raghunath et al. (Nature Medicine 2020), ECG mortality:** dropped. I couldn't confirm that it combines the ECG model with clinical variables. Khurshid et al. (2022) is the cleaner fusion example.

## Possible lecture arc using this material

| Min | Section | Key references |
|---|---|---|
| 0–4 | What makes data multimodal; what's special about time-series modalities | Liang 2024; Acosta 2022 |
| 4–7 | Taxonomy of challenges (one slide) | Baltrušaitis 2019; Liang 2024; Xu 2023 |
| 7–17 | **Fusion, in general:** early, intermediate and late fusion; mechanisms from concatenation through gating, FiLM and cross-attention to bottlenecks | Huang 2020; Arevalo 2017; Perez 2018; Tsai 2019; Nagrani 2021 |
| 17–21 | Shared spaces and the LLM hub | CLIP; ImageBind; Symile; LLaVA; HeLM |
| 21–30 | **ECG + EHR worked example:** MIMIC-IV-ECG; complementarity (Khurshid 2022); FM encoders plus a fusion head (HAIM-style); ECG–text (MERL) | Gow 2023; Khurshid 2022; Soenksen 2022; McKeen 2025; Liu 2024 |
| 30–35 | **Does it help? Pitfalls:** unimodal baselines; imbalance; missing modalities; leakage and timing; fairness | Wang 2020; Liang 2023; Ma 2022; Yin 2026; Kline 2022 |
| 35 | Further-reading slide and lab preview | the 📖 items |

**A shortlist for the further-reading slide:**
- Baltrušaitis 2019 or Liang 2024 (taxonomy)
- Xu, Zhu & Clifton 2023 (transformers)
- Huang 2020 (healthcare fusion)
- Liang 2023 (when fusion helps)
- Wu 2026 (missing modalities)
- Liu 2025 (time series + language)
