# Euclid 2D

### Table of Contents

| Section                                   | Description                                                               |
|-------------------------------------------|---------------------------------------------------------------------------|
| [Introduction](#introduction)             | What is this repository about?                                            |
| [Geometry Syntax](#syntax) | How to formulate a geometry problem or proof.                              |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Object Types](#syntax-object-types)    | What are the different types of objects that can appear in a problem statement or proof. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Constructions](#syntax-constructions)  | How to use geometric objects to describe more geometric objects. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Predicates](#syntax-predicates)        | How to use geometric objects to describe predicates. |
| [Geometry Configuration Rules](#configuration) | What are the rules that geometric objects abide to? |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Constructions](#configuration-constructions)   | How constructions are defined. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Predicates](#configuration-predicates)         | How predicates are defined. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Theorems](#configuration-theorems)             | How theorems are defined. |
| [Geometry Document](#syntax-structure) | All about the file format in which we save geometry problem statements and proofs. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Assumptions](#syntax-assumptions)      | The section containing the given predicates in the problem. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Embedding](#syntax-embedding)          | The section containing a coordinate embedding of geometry objects. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Need to prove](#syntax-need-to-prove)  | The section containing the predicates that need to be proved. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Proof](#syntax-proof)                  | The section containing the proof. |
| [Generating Problems](#problem-generator) | How to generate geometry problems (just their statements, without proof).  |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Introduction](#problem-generator-introduction)         | What is this module about? |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Capabilities](#problem-generator-capabilities)         | What can we do with it? |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Usage](#problem-generator-introduction)                | How do we use it? |
| [Solving Problems](#solver) | How to solve geometry problems |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Embedding a question](#solver-embedding)               | How to take a geometry problem and embed it in 2D space. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Generating a proof](#solver-proof-generation)          | How to take a geometry problem and generate a proof. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Trimming proofs](#solver-trimming)                     | How to shorten a proof until its length is locally optimal. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Checking + Validating a proof](#solver-checking)       | How to make sure a written proof is correct. |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Running an interactive terminal](#solver-interacting)  | How to evaluate expressions and predicates in a geometry problem (possibly with a partially-written proof). |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Prettifying](#solver-prettifying)                      | How to make a proof easier to read by humans. |

## <span id="introduction"> Introduction </span>

This is an open-source research project focused on using AI to solve, invent, and analyze problems in 2D Euclidean geometry.

The subject has a rich history, including Tarski's work on the decidability of Euclidean geometry in the 1920s and the practical contributions of Chou, Gao, and Zhang in the 1990s, which came close to achieving IMO-level problem-solving. Recent interest in the field was reignited by Google DeepMind's press release in July 2024, suggesting that Alpha Geometry 2 has mastered IMO-level geometry questions. However, as of January 2025, Google has not disclosed Alpha Geometry 2. We believe that open-source projects like this can increase the likelihood of AI becoming a useful tool for advancing mathematics and benefiting the mathematical community.

We focus on Large Language Models (LLMs), hoping to integrate an LLM proficient in geometry with those knowledgeable in other domains. We hope this integration will create a synergistic effect, enhancing the capabilities of LLMs across a broad spectrum of logical and geometrical applications.

We are testing the following hypotheses.

Hypothesis 1: LLMs of moderate size (< 70B parameters) can learn to solve Euclidean geometry problems.

Hypothesis 2: With the support of accompanying software (e.g., verifiers or numerical embeddings), such LLMs can solve Euclidean geometry problems.

The level of Euclidean Geometry problems we are aiming at is roughly that of e.g. Akopyan's book "Geometry in Figures". We acknowledge the support of MSR for this project during its initial phase.

Google bucket link:
https://console.cloud.google.com/storage/browser/euclid_2d?inv=1&invt=Ab4r5g&project=versatile-bolt-330819

## <span id="syntax"> Geometry Syntax </span>
### <span id="syntax-object-types"> Object Types </span>
### <span id="syntax-constructions"> Constructions </span>
### <span id="syntax-predicates"> Predicates </span>

## <span id="configuration"> Geometry Configuration Rules </span>
### <span id="configuration-constructions"> Constructions </span>
### <span id="configuration-predicates"> Predicates </span>
### <span id="configuration-theorems"> Theorems </span>

## <span id="syntax-structure"> Geometry Document </span>
### <span id="syntax-assumptions"> Assumptions </span>
### <span id="syntax-embedding"> Embedding </span>
### <span id="syntax-need-to-prove"> Need to prove </span>
### <span id="syntax-proof"> Proof </span>

## <span id="problem-generator"> Generating Problems </span>
### <span id="problem-generator-introduction"> Introduction </span>
### <span id="problem-generator-capabilities"> Capabilities </span>
### <span id="problem-generator-introduction"> Usage </span>

## <span id="solver"> Solving Problems </span>
### <span id="solver-embedding"> Embedding a question </span>
### <span id="solver-proof-generation"> Generating a proof </span>
### <span id="solver-trimming"> Trimming proofs </span>
### <span id="solver-checking"> Checking + Validating a proof </span>
### <span id="solver-interacting"> Running an interactive terminal </span>
### <span id="solver-prettifying"> Prettifying </span>