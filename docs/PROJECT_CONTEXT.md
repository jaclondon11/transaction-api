# 🧠 Project Context — Transaction Monitoring API

## 🎯 Goal

Build a backend system using FastAPI that:

* Processes transactions
* Applies configurable rules (rule engine)
* Returns APPROVED / REJECTED
* Emits events (future phase)

---

## 🏗️ Current Architecture

Layers:

* API (FastAPI)
* Services (business logic)
* Domain (models + rules)
* Infrastructure (repository, future queue)

---

## ✅ Current Implementation

* FastAPI project initialized
* Transaction model (Pydantic)
* Basic rule: amount limit
* TransactionService (orchestration)
* In-memory repository

---

## 🚀 Next Tasks

### 1. Fix Dependency Injection

* Create dependency providers
* Use `Depends` in routes
* Ensure services are not coupled to infrastructure

---

### 2. Improve API Design

* Replace query params with request body (Pydantic)
* Add proper validation

---

### 3. Rule Engine v2

* Support multiple rules
* Make rules configurable (not hardcoded)

---

### 4. Event-Driven (next phase)

* Emit event when transaction is rejected
* Simulate queue (in-memory first)

---

## 🧠 Coding Guidelines

* Use clean architecture principles
* Keep services framework-agnostic
* Use dependency injection everywhere
* Write readable and testable code

---

## 🧪 Testing (future)

* Unit test for Rule Engine
* Unit test for TransactionService
* Use dependency injection to mock repository

---

## 💡 Important

This is a learning project but should be implemented as if it were production-ready.

Focus on:

* Clean design
* Scalability
* Maintainability
