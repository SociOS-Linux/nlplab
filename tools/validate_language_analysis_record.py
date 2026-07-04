#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "language-analysis-record.example.json"
REQUIRED_TOP = {"apiVersion", "kind", "metadata", "spec"}
REQUIRED_SPEC = {
    "adapter",
    "algorithmFamily",
    "taskContract",
    "inputRef",
    "pipelineOrModelRef",
    "outputs",
    "metrics",
    "policy",
    "evidenceRefs",
}
ALGORITHM_FAMILIES = {
    "basic-primitives",
    "advanced-primitives",
    "rule-techniques",
    "classical-ml",
    "neural-nlp",
    "transformers",
    "foundation-language-services",
    "retrieval-bridge",
    "governance-bridge",
}


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def main() -> int:
    if not EXAMPLE.exists():
        return fail("missing examples/language-analysis-record.example.json")
    data = json.loads(EXAMPLE.read_text())
    missing_top = REQUIRED_TOP - set(data)
    if missing_top:
        return fail(f"missing top-level fields: {sorted(missing_top)}")
    if data["apiVersion"] != "nlplab.socios-linux.dev/v1":
        return fail("wrong apiVersion")
    if data["kind"] != "LanguageAnalysisRecord":
        return fail("wrong kind")
    spec = data["spec"]
    missing_spec = REQUIRED_SPEC - set(spec)
    if missing_spec:
        return fail(f"missing spec fields: {sorted(missing_spec)}")
    if spec["algorithmFamily"] not in ALGORITHM_FAMILIES:
        return fail(f"unknown algorithmFamily: {spec['algorithmFamily']}")
    adapter = spec["adapter"]
    for key in ["name", "version"]:
        if not adapter.get(key):
            return fail(f"missing adapter.{key}")
    if not spec["outputs"]:
        return fail("outputs must not be empty")
    if not spec["evidenceRefs"]:
        return fail("evidenceRefs must not be empty")
    metrics = spec["metrics"]
    for key in ["latencyMs", "memoryMb"]:
        if key not in metrics:
            return fail(f"missing metrics.{key}")
    policy = spec["policy"]
    for key in ["decision", "sensitivityCeiling"]:
        if not policy.get(key):
            return fail(f"missing policy.{key}")
    print("OK: nlplab language analysis record validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
