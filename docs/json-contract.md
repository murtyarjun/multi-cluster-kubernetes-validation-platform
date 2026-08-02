# JSON Contract

## Purpose

The JSON contract defines the standardized data format used throughout the platform.

Every collector produces JSON that conforms to this contract.

Every downstream component—including the Comparison Engine, Report Generator, Unified Dashboard, and Historical Repository—consumes this standardized structure.

The JSON contract is considered the **single source of truth** for the platform.

---

# Design Principles

The JSON contract follows several engineering principles:

- Human readable
- Machine readable
- Versioned
- Extensible
- Backward compatible
- Collector independent
- Report independent

The JSON structure should remain stable even as new collectors or reporting formats are introduced.

---

# High Level Structure

```text
Change
│
├── Metadata
├── Clusters
│
├── Collectors
│      ├── Nodes
│      ├── Pods
│      ├── Deployments
│      ├── Namespaces
│      ├── Certificates
│      ├── Traffic
│      └── Platform Components
│
├── Summary
│
├── Warnings
│
└── Errors
```

---

# Root Object

```json
{
  "schemaVersion": "1.0",
  "changeNumber": "CHG000123",
  "mode": "PRE",
  "generatedAt": "2026-08-02T12:30:00Z",
  "platformVersion": "0.2.0",
  "clusters": []
}
```

---

# Change Metadata

| Field | Description |
|--------|-------------|
| schemaVersion | JSON schema version |
| changeNumber | Maintenance change identifier |
| mode | PRE or POST |
| generatedAt | Report generation timestamp |
| platformVersion | Application version |

---

# Cluster Object

Each cluster contains its own validation results.

```json
{
  "clusterName": "eks-prod-01",
  "context": "eks-prod-01",
  "cloud": "AWS",
  "environment": "Production",
  "status": "SUCCESS",
  "executionTime": 8.42,
  "collectors": []
}
```

---

# Collector Object

Every collector returns exactly the same structure.

```json
{
  "collector": "pods",
  "status": "SUCCESS",
  "startedAt": "...",
  "completedAt": "...",
  "executionTime": 1.23,

  "summary": {},

  "data": {},

  "warnings": [],

  "errors": []
}
```

---

# Collector Status

Supported values

- SUCCESS
- WARNING
- FAILED
- SKIPPED

These values are standardized across every collector.

---

# Summary Object

Every collector should provide a concise summary.

Example

```json
{
  "healthy": 112,
  "warning": 2,
  "failed": 1
}
```

---

# Data Object

The `data` section is collector specific.

Example

Node Collector

```json
{
  "nodes": [
    {
      "name": "node-01",
      "ready": true,
      "version": "1.33.1",
      "roles": [
        "worker"
      ]
    }
  ]
}
```

Pod Collector

```json
{
  "pods": [
    {
      "namespace": "payments",
      "name": "payment-api",
      "status": "Running"
    }
  ]
}
```

The platform never assumes the structure of the `data` section.

Only the corresponding collector understands it.

---

# Warnings

Warnings represent non-critical observations.

Example

```json
[
  "2 Pods restarting",
  "Certificate expires in 12 days"
]
```

---

# Errors

Errors represent collector execution failures.

Example

```json
[
  "Unable to connect to cluster",
  "kubectl command timed out"
]
```

---

# Processing Pipeline

```
Collector

↓

Collector JSON

↓

Comparison Engine

↓

Comparison Model

↓

Report Generator

↓

HTML

↓

Unified Dashboard
```

JSON remains the source of truth throughout the pipeline.

---

# Versioning

Every JSON document includes a schema version.

Future schema changes must maintain backward compatibility whenever possible.

Current version

```
1.0
```

---

# Extensibility

Future collectors should be added without changing the root contract.

Examples

- Istio Collector
- Velero Collector
- OPA Collector
- Gatekeeper Collector
- FluxCD Collector

Each new collector only needs to produce a valid Collector Object.

---

# Engineering Decisions

## JSON is the source of truth

Reports, dashboards, and comparisons are generated from JSON instead of directly from Kubernetes or HTML.

---

## HTML is a presentation layer

HTML reports are generated from structured JSON.

The platform never compares HTML reports.

---

## Comparison uses structured data

The Comparison Engine compares PRE and POST JSON documents.

This ensures deterministic comparisons and avoids parsing presentation artifacts.

---

## Loose Coupling

Collectors never communicate with the dashboard.

Collectors never generate HTML.

Collectors only collect facts.

Presentation layers consume structured JSON.

---

# Future Enhancements

Future schema extensions may include:

- Execution metrics
- Historical trend data
- Performance metrics
- Change approvals
- AI-generated summaries
- Collector versioning
- Plugin metadata

These enhancements should not require changes to existing collectors.