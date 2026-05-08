# NLP Lab Matrix

## Purpose

nlplab is the Linux-native execution and evaluation workspace for Holmes language components.

Holmes owns the product surface and promotion contract. nlplab owns reproducible experiments, local adapters, fixtures, benchmark receipts, and cost/latency/quality measurements before anything graduates into `SocioProphet/prophet-platform`.

## Scope

The lab matrix covers these families:

| Family | Example adapters | Required proof |
| --- | --- | --- |
| Basic primitives | language ID, sentence segmentation, tokenization, lemmatization, POS, morphology | quality sample, latency, memory, span-offset correctness |
| Advanced primitives | dependency parsing, semantic role labeling, coreference | parse fidelity, span alignment, language coverage, failure modes |
| Rule techniques | regex, dictionaries, gazetteers, dependency patterns, table/header rules | deterministic fixtures, versioned rule pack, false-positive/false-negative cases |
| Classical ML | CRF, SVM/logistic/maxent, clustering, topic modeling, similarity baselines | train/eval split, quality metrics, calibration, CPU latency |
| Neural NLP | sequence/text models, embedding pipelines, ONNX exports | quality, footprint, CPU/GPU throughput, reproducibility |
| Transformers | token classification, text classification, relation extraction, embeddings, reranking, summarization, translation | task metrics, latency, GPU/CPU profile, model-card and license record |
| Retrieval bridge | Sherlock evidence packet writer | evidence refs, sensitivity ceiling, citation refs, freshness, no canonical-truth claims |
| Governance bridge | Holmes promotion receipt writer | corpus ref, pipeline/model ref, eval record, policy result, promotion record, rollback ref |

## Adapter layout

Adapters should live under `adapters/<family>/` and expose a small, deterministic command interface:

```text
adapter --input fixtures/text/sample.txt --output .artifacts/<adapter>/analysis.json
```

Every adapter should emit a `LanguageAnalysisRecord`-compatible JSON object containing:

- adapter name and version;
- algorithm family;
- task contract;
- corpus or fixture reference;
- pipeline or model reference;
- spans with byte/character offsets where applicable;
- confidence/calibration fields where applicable;
- latency and footprint observations;
- license and dependency metadata;
- policy and sensitivity tags;
- evidence refs.

## Fixture classes

The minimum fixture set is:

1. short English text;
2. long document text;
3. table-like text;
4. PII and sensitive-context text;
5. multilingual text;
6. domain/ontology-linked text;
7. adversarial or prompt-injection-like text;
8. contradiction and claim text.

## Benchmark receipts

Each benchmark run should produce:

- `LanguagePipelineReceipt`;
- per-task metric records;
- latency/footprint records;
- policy decision records;
- Sherlock-compatible evidence packets;
- rollback metadata;
- reproduction command.

## Promotion boundary

nlplab output is experimental until Holmes promotion criteria pass.

Sherlock may index nlplab outputs as pointer-backed evidence, but indexed records must not claim canonical truth. The Canon and Holmes promotion records decide whether a result becomes accepted evidence.
