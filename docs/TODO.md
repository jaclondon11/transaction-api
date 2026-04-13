TODO ideas

Usar Pydantic para validaciones
Implementar dependency injection
Agregar Docker
Simular SQS con cola interna
Agregar pytest con coverage
Logging estructurado

TODO Structure
app/
 ├── main.py
 ├── api/
 │    ├── routes.py
 ├── domain/
 │    ├── models.py
 │    ├── rules.py
 ├── services/
 │    ├── transaction_service.py
 │    ├── rule_engine.py
 ├── infrastructure/
 │    ├── repository.py
 │    ├── queue.py
 └── tests/