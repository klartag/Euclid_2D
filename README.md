# Euclid 2D

### Table of Contents

| Section | Description |
|-|-|
| [Introduction](#introduction)             | What is this repository about?                                            |
| [Geometry Syntax](#syntax)                | How to formulate a geometry problem or proof                              |
| [Generating Problems](#problem-generator) | How to generate geometry problems (just their statements, without proof)  |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Introduction](#problem-generator-introduction)         |   |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Capabilities](#problem-generator-capabilities)         |   |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Usage](#problem-generator-introduction)                |   |
| [Solving Problems](#solver)               | How to solve geometry problems                                            |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Embedding a question](#solver-embedding)               | How to take a geometry problem and embed it in 2D space |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Generating a proof](#solver-proof-generation)          | How to take a geometry problem and generate a proof |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Trimming proofs](#solver-trimming)                     | How to shorten a proof until its length is locally optimal |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Checking + Validating a proof](#solver-checking)       | How to make sure a written proof is correct |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Running an interactive terminal](#solver-interacting)  | How to evaluate expressions and predicates in a geometry problem (possibly with a partially-written proof) |
| &nbsp;&nbsp;&nbsp;&nbsp;  [Prettifying](#solver-prettifying)                      | How to make a proof easier to read by humans |

<a name="introduction"><a />
## Introduction

This is an open-source research project focused on using AI to solve, invent, and analyze problems in 2D Euclidean geometry.

The subject has a rich history, including Tarski's work on the decidability of Euclidean geometry in the 1920s and the practical contributions of Chou, Gao, and Zhang in the 1990s, which came close to achieving IMO-level problem-solving. Recent interest in the field was reignited by Google DeepMind's press release in July 2024, suggesting that Alpha Geometry 2 has mastered IMO-level geometry questions. However, as of January 2025, Google has not disclosed Alpha Geometry 2. We believe that open-source projects like this can increase the likelihood of AI becoming a useful tool for advancing mathematics and benefiting the mathematical community.

We focus on Large Language Models (LLMs), hoping to integrate an LLM proficient in geometry with those knowledgeable in other domains. We hope this integration will create a synergistic effect, enhancing the capabilities of LLMs across a broad spectrum of logical and geometrical applications.

We are testing the following hypotheses.

Hypothesis 1: LLMs of moderate size (< 70B parameters) can learn to solve Euclidean geometry problems.

Hypothesis 2: With the support of accompanying software (e.g., verifiers or numerical embeddings), such LLMs can solve Euclidean geometry problems.

The level of Euclidean Geometry problems we are aiming at is roughly that of e.g. Akopyan's book "Geometry in Figures". We acknowledge the support of MSR for this project during its initial phase.

Google bucket link:
https://console.cloud.google.com/storage/browser/euclid_2d?inv=1&invt=Ab4r5g&project=versatile-bolt-330819

<a name="syntax">
## Geometry Syntax

<a name="problem-generator">
## Generating Problems

<a name="problem-generator-introduction">
### Introduction

<a name="problem-generator-capabilities">
### Capabilities

<a name="problem-generator-introduction">
### Usage

<a name="solver">
## Solving Problems

<a name="solver-embedding">
### Embedding a question

<a name="solver-proof-generation">
### Generating a proof

<a name="solver-trimming">
### Trimming proofs

<a name="solver-checking">
### Checking + Validating a proof

<a name="solver-interacting">
### Running an interactive terminal

<a name="solver-prettifying">
### Prettifying