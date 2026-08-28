# BYOA Agent-Experience Parity: Research Program and Experimental Design

## 1. The Thesis (Falsifiable Form)
**Claim B (Strong):** The improvements a company derives from *aggregate structured telemetry* (no transcripts) are (i) comparable in magnitude to those derivable from transcripts, and (ii) **transfer to agent implementations that generated none of the telemetry.**

> For a fixed task distribution, environment improvements derived only from privacy-bounded aggregate telemetry produce task-completion and policy-compliance gains on a *held-out agent implementation* that are within $\epsilon$ of the gains a transcript-fed company-owned agent achieves on itself, over the same number of improvement rounds.

## 2. Theoretical Framing
*   **Company -> Agent (The AX Contract):** This is **Information Design / Bayesian Persuasion** (Kamenica & Gentzkow 2011). The company commits ex ante to a published information structure consumed by heterogeneous receivers.
*   **Agent -> Company (Telemetry/Outcome):** This is **Strategic Communication** (Crawford-Sobel 1982). The agent's self-reported outcome is cheap talk with misaligned incentives, predicting a partition-equilibrium coarsening that justifies enum task classes over free-text.
*   **The Residual:** The BYOA architecture compresses telemetry for the company but allows the champion agent to retain the uncompressed context. The edge-case evaluation tests whether this retained residual produces better outcomes on high-variance tasks (Rate-Distortion-Perception; Blau & Michaeli 2019).

## 3. Experimental Design (Forking tau-bench)
We will fork **tau-bench** (Sierra Research, Yao et al. 2024) to provide the domains, policies, API tools, database, and LLM user simulator. 

**The 2x2 Matrix + Transfer Arm:**

| | Improve the agent (prompt/adapter) | Improve the environment (schemas, errors) |
|---|---|---|
| **Sees transcripts** | A1 (Today's owned agent) | A2 |
| **Sees structured telemetry only**| B1 | B2 (The BYOA thesis) |

*   **Arm C (The Transfer Test):** Take B2's optimized environment, freeze it, and evaluate on a **held-out agent family** that contributed no telemetry. *This is the measurement that matters.*

### Metrics
*   **Primary:** Task success (database-state match), `pass^k` for reliability, policy-violation rate.
*   **Secondary:** Effort (tool calls, retries), dead-end rate, escalation rate.
*   **Instrumentation:** Reason-code distribution, detection latency.

### Ablation Ladder
Identify which environment layer carries the gain:
1. Structured error semantics only (SERF codes)
2. + Versioned resources with stable rule IDs
3. + Machine-readable procedures and confirmation boundaries
4. + Authoritative receipts

## 4. Falsification Conditions
*   **Transfer fails:** B2's improvements don't generalize to Arm C. (Built an adapter, not a substrate).
*   **Transcript advantage persists:** A1 retains a durable edge on standard tasks.
*   **Loop cannot close under privacy:** No $\epsilon$ compatible with a defensible privacy claim yields sufficient signal at realistic volumes due to sequential composition (continual release DP).
*   **Environment optimization saturates:** Explicit structure cannot replace experiential learning.
