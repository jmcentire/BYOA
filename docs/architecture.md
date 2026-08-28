# BYOA Architecture

Inspired by the component modularity of `apprentice` and the strict tenant/policy containment of `Reeve`, the BYOA architecture is divided into three primary domains: the **Enterprise Surface** (what the company exposes), the **CABP Gateway** (the security and telemetry boundary), and the **Synthetic Harness** (for simulating BYOA behavior).

## 1. Enterprise Surface
The declarative configuration defining what a BYOA can do. Similar to `apprentice.yaml` skill packages, companies define their interfaces here.

- `Schema Registry`: OpenAPI 3.1 definitions for executable APIs (the tools).
- `Resource Provider`: RAG integration and structured policy provision. Exposes versioned facts and procedures.
- `Stigmergic Optimizer`: The automated loop that consumes DP (Differential Privacy) telemetry and iteratively rewrites MCP Prompts and tool schemas to reduce SERF errors.

## 2. CABP (Context-Aware Broker Protocol) Gateway
The operational boundary. This acts similarly to the `apprentice` router and PII middleware, but focused on neutralizing the Lethal Trifecta for inbound untrusted agents.

- `cabp_auth`: Extracts JWT, validates claims, and resolves strict ACLs (tenant isolation similar to Reeve).
- `cabp_context_injector`: Hardcodes user identity into payloads to prevent confused deputy attacks.
- `cabp_sanitizer`: Output filtering to strip leaked PII and prompt-injection patterns before returning to the BYOA.
- `serf_formatter`: Translates raw backend errors into the Structured Error Recovery Framework taxonomy (e.g., `SCHEMA.INVALID_SEGMENT`, `AUTH.USER_PRESENCE_REQUIRED`).
- `otel_emitter`: Emits distributed traces and aggregates SERF metrics with Differential Privacy noise.

## 3. Synthetic Harness
The testing framework to prove the architecture.

- `synthetic_users`: Generates 1,000 diverse, multi-turn intents (e.g., complex booking modifications, policy disputes).
- `byoa_clients`: Heterogeneous LLM agents (simulating different models/frameworks) that act on behalf of the synthetic users.
- `evaluation_engine`: Measures Task Resolution Rate, Decision Path Depth, and Out-of-Distribution Success.

## The Stigmergic Loop (Execution Flow)
1. **Request**: BYOA connects via MCP to the CABP Gateway.
2. **Execute**: BYOA attempts to resolve a user intent using the available schemas and RAG resources.
3. **Failure/Success**: The enterprise backend succeeds or fails. The `serf_formatter` standardizes the outcome.
4. **Telemetry**: `otel_emitter` captures the outcome.
5. **Optimization**: The `Stigmergic Optimizer` detects an elevated `SCHEMA.INVALID_INPUT` rate on a specific endpoint. It automatically rewrites the OpenAPI parameter description (the environment) to be more machine-readable.
6. **Convergence**: Future BYOAs succeed on the first attempt without the company ever reading a conversation transcript.
