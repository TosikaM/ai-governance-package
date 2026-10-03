# AI System Retirement & Decommissioning Checklist

**Checklist Identifier:** `ORG-RET-[YEAR]-[PROJECT_ID]`  
**Status:** DRAFT  
**System Name:** [System Name]  
**Project ID:** [project_id matching ai-project-manifest.yaml]  
**Permanent SYS-ID:** [SYS-ID from central inventory]  
**Target Decommissioning Date:** [YYYY-MM-DD]  
**Governed Controls:** [`ORG-CTL-RET-001`](file:///c:/ai-governance-package/baseline/controls/retirement/CTL-RET-001.yaml) through [`ORG-CTL-RET-004`](file:///c:/ai-governance-package/baseline/controls/retirement/CTL-RET-004.yaml)

---

## 1. Decommissioning Intake & Stakeholder Notification

- [ ] **1.1 Formal Retirement Intake Registered (`ORG-CTL-RET-001`):**
  - Project Lead submitted formal decommissioning ticket in enterprise IT Service Management portal.
  - Verification Ticket ID: `[ITSM-TICKET-ID]`
- [ ] **1.2 90-Day Advance Deprecation Notice Published (`ORG-CTL-RET-004`):**
  - Deprecation notice sent to all downstream API consumers and internal tenants.
  - Notice Publication Date: `[YYYY-MM-DD]` (Must be $\ge$ 90 days before final endpoint teardown).
  - Migration Guide Link: `[URL to replacement system or alternate API endpoint]`
- [ ] **1.3 Business Owner Approval:**
  - Written confirmation from Business Product Owner that replacement capabilities or phase-out plans are operational.

---

## 2. Ingress & Traffic Deprecation

- [ ] **2.1 Production Traffic Rerouted or Terminated:**
  - All active user sessions gracefully drained.
  - Upstream DNS and load balancer traffic shifted to replacement service or maintenance tombstone.
- [ ] **2.2 HTTP 410 Gone Tombstone Configured:**
  - Public and internal endpoints configured to return `HTTP 410 Gone` with structured JSON redirection metadata.
  - Tombstone TTL window configured (default: 60 days).

---

## 3. Credential & Identity Teardown (`ORG-CTL-RET-003`)

- [ ] **3.1 Agent Machine Credentials Revoked:**
  - Non-human SPIFFE IDs, OAuth2 service principals, and API bearer keys revoked in enterprise IAM directory.
  - Revocation confirmation logged: `[IAM Revocation Audit Reference]`
- [ ] **3.2 Database & Storage Access Keys Deleted:**
  - All database user accounts, S3 bucket IAM policies, and secret manager secrets assigned to this service destroyed.

---

## 4. Vector Database & Cache Data Purging (`ORG-CTL-RET-003`)

- [ ] **4.1 Vector Embeddings Collection Dropped:**
  - Vector database indices, collections, and partitions associated with the system permanently dropped.
  - Collection Name: `[vector_collection_name]`
- [ ] **4.2 Semantic Cache Flushed:**
  - Redis / Memcached semantic query caches purged to prevent stale responses.
- [ ] **4.3 Temporary Training Buffers Purged:**
  - Scratch disks, temporary staging buckets, and uncurated prompt logs securely erased adhering to NIST SP 800-88 sanitization standards.

---

## 5. Model Weight Cold Archival (`ORG-CTL-RET-002`)

- [ ] **5.1 Immutable Cold Weight Storage Lock:**
  - Candidate model weights transferred to long-term immutable WORM cold storage vault for statutory retention period (e.g. 7 years).
  - Vault Storage URI: `s3://compliance-vault.internal.net/archives/models/[project_id]/`
- [ ] **5.2 SHA-256 Digest Verification:**
  - Archived model weight file SHA-256 digest computed and recorded:
  - SHA-256 Digest: `[64-character hexadecimal hash]`
  - Matches final production release attestation: [YES / NO]

---

## 6. Central Inventory Status Transition (`ORG-CTL-RET-001`)

- [ ] **6.1 Inventory Status Updated to DECOMMISSIONED:**
  - Central enterprise AI inventory status updated from `ACTIVE` / `MAINTENANCE` to `DECOMMISSIONED`.
  - Date of Transition: `[YYYY-MM-DD]`
- [ ] **6.2 Manifest Lifecycle Stage Pinned:**
  - `ai-project-manifest.yaml` updated with `lifecycle_stage: "decommissioned"`.

---

## 7. Accountable Decommissioning Sign-Offs

| Decommissioning Gate | Approver Role Placeholder | Name | Decision | Date |
|---|---|---|:---:|:---:|
| **Technical Teardown Gate** | `[ROLE: Lead AI Engineer]` | [Name] | [VERIFIED] | [YYYY-MM-DD] |
| **Data Protection & Purge Gate** | `[ROLE: Enterprise Data Protection Officer]` | [Name] | [VERIFIED] | [YYYY-MM-DD] |
| **Security & IAM Revocation Gate** | `[ROLE: Enterprise CISO / IAM Lead]` | [Name] | [VERIFIED] | [YYYY-MM-DD] |
| **Final Lifecycle Closure** | `[ROLE: Enterprise AI Review Board Chair]` | [Name] | [DECOMMISSIONED] | [YYYY-MM-DD] |
